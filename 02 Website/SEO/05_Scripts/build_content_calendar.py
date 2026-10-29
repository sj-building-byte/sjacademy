"""Build the SJ Academy content calendar workbook (.xlsx) for upload to Google Sheets.

Reads the blog and Instagram calendar CSVs in 03_Plans_and_Content/ and writes
03_Plans_and_Content/SJ_Academy_Content_Calendar_2026-27.xlsx

Run from the workspace root:  python3 05_Scripts/build_content_calendar.py
"""
import csv
import datetime as dt
import re

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

BLOG_CSV = "03_Plans_and_Content/Blog_Content_Plan_2026-27/Blog_Calendar_Oct-Dec_2026.csv"
IG_CSV = "03_Plans_and_Content/Instagram_Plan_2026-27/Instagram_Calendar_Oct2026-Jan2027.csv"
PIPE_CSV = "03_Plans_and_Content/Blog_Content_Plan_2026-27/Instagram_to_Blog_Plan.csv"
OUT = "03_Plans_and_Content/SJ_Academy_Content_Calendar_2026-27.xlsx"

FONT = "Arial"
BROWN, YELLOW, ORANGE, CREAM, GREY = "453516", "FCE004", "FE6100", "FFF9CC", "F4F4F4"
HEAD_FILL = PatternFill("solid", fgColor=BROWN)
HEAD_FONT = Font(name=FONT, bold=True, color="FFFFFF", size=10)
BODY_FONT = Font(name=FONT, size=10)
INPUT_FILL = PatternFill("solid", fgColor=CREAM)
THIN = Side(style="thin", color="D9D9D9")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP_TOP = Alignment(wrap_text=True, vertical="top")
TOP = Alignment(vertical="top")
DATE_FMT = "ddd dd mmm yyyy"

STATUSES = ["Idea", "Planned", "In progress", "In review", "Scheduled", "Published", "Postponed", "Dropped"]
STATUS_COLORS = {"Idea": "EDEDED", "Planned": "DDEBF7", "In progress": "FFF2CC", "In review": "FCE4D6",
                 "Scheduled": "E2D9F3", "Published": "C6EFCE", "Postponed": "F8CBAD", "Dropped": "BFBFBF"}
PILLARS = ["Exam Resources", "Subject Advice", "Student Tech", "Websites and Apps", "Study Spots",
           "Future and Careers", "Parents' Guides", "Shareable", "Community and News"]
TRACKS = ["Tuition", "Audience/Affiliate", "Brand/Share"]
POST_TYPES = ["New", "Refresh", "Merge"]
INTENTS = ["Informational", "Commercial", "Navigational", "Social (not search)"]
SERIES = ["Examiner Mode (carousel)", "Sir Says (teacher reel)", "Tool Drop (carousel)", "POV (5-8s reel)",
          "Parent Guide (carousel)", "Comment-to-Get", "Sunday Special"]
FORMATS = ["Carousel", "Reel 5-8s", "Reel 8-15s", "Reel 30-45s", "Story", "Image", "Varies"]
PEOPLE = ["Sir Sunyyan Junaid", "Sir Salman", "Sir Umair", "Sir Kashan", "Sir Muhammad Riza", "Zaman",
          "Writer", "Designer", "Video editor", "Social media manager", "Editor"]
YES_NO = ["Done", "Not done"]

# Blog enrichment: id -> (secondary keywords, search intent, target URL)
BLOG_EXTRA = {
    1: ("best laptop for students in pakistan; student laptop price in pakistan; which laptop is best for students", "Commercial", "/blog/best-laptop-for-students/"),
    2: ("what to bring to cambridge exam; caie exam day rules; zone 4 exam timings", "Informational", "/blog/caie-exam-day-guide/"),
    3: ("o level memes; o level student life", "Social (not search)", "/blog/things-o-level-students-say/"),
    4: ("9609 paper 3 case study; a level business case study tips; level 4 answers business", "Informational", "/blog/9609-paper-3-case-study/"),
    5: ("ipad for students pakistan; best tablet for note taking; tablet vs laptop for students", "Commercial", "/blog/best-tablets-for-students/"),
    6: ("4024 revision plan; o level maths last week tips; o level maths past papers", "Informational", "/blog/o-level-maths-4024-revision-plan/"),
    7: ("english learning app for urdu speakers; best free english learning app; asan english app", "Commercial", "/blog/the-best-free-english-learning-apps/"),
    8: ("scientific calculator tricks; casio fx-991 functions; calculator allowed in o level exam", "Commercial", "/blog/best-calculators-o-a-level/"),
    9: ("a level subject combination quiz; which a level subjects should i take", "Social (not search)", "/blog/a-level-subject-combination-quiz/"),
    10: ("best cafes in karachi for studying; libraries in karachi; quiet places to study karachi", "Informational", "/blog/best-cafes-in-karachi-for-students/"),
    11: ("5054 common mistakes; o level physics exam tips; o level physics paper 2", "Informational", "/blog/o-level-physics-5054-mistakes/"),
    12: ("marking scheme; what is mark scheme; how to use past papers", "Informational", "/blog/how-to-use-mark-scheme/"),
    13: ("study apps for students; apps for o level students; focus apps", "Commercial", "/blog/best-study-apps/"),
    14: ("libraries in lahore; cafes in lahore for studying; co-working lahore students", "Informational", "/blog/best-places-to-study-in-lahore/"),
    15: ("o level starter pack; o level student life pakistan", "Social (not search)", "/blog/o-level-starter-pack/"),
    16: ("11.11 laptop deals pakistan; laptop under 150k; daraz 11.11 laptops", "Commercial", "/blog/11-11-student-laptop-deals/"),
    17: ("5070 organic chemistry; o level chemistry tips; organic reactions list", "Informational", "/blog/o-level-chemistry-organic-reactions/"),
    18: ("libraries in islamabad; cafes in islamabad for studying; quiet places islamabad", "Informational", "/blog/best-places-to-study-in-islamabad/"),
    19: ("o level or matric which is better; o level equivalent to matric; o level cost pakistan", "Informational", "/blog/o-level-vs-matric/"),
    20: ("youtube channels for o level; best a level youtube channels; free o level lectures", "Informational", "/blog/best-education-youtube-channels/"),
    21: ("winter break study plan; revision timetable template; may june 2027 preparation", "Informational", "/blog/winter-break-revision-timetable/"),
    22: ("laptop for programming students; laptop specs for computer science", "Commercial", "/blog/laptops-for-a-level-computer-science/"),
    23: ("9708 diagrams; a level economics essay tips; economics diagrams list", "Informational", "/blog/a-level-economics-diagrams/"),
    24: ("caie exam memes; exam hall moments", "Social (not search)", "/blog/caie-exam-hall-moments/"),
    25: ("free educational websites; best websites for o level students; top 10 educational websites", "Informational", "/blog/top-10-free-educational-websites-for-students/"),
    26: ("computer science scope in pakistan; bs cs salary pakistan; best universities for cs pakistan", "Informational", "/blog/computer-science-scope-pakistan/"),
    27: ("acca vs ca pakistan; bba scope pakistan; accounting careers after a levels", "Informational", "/blog/ca-vs-acca-vs-bba-pakistan/"),
    28: ("edexcel vs cambridge; cambridge or edexcel which is better; edexcel a levels pakistan", "Informational", "/blog/cambridge-caie-vs-pearson-edexcel/"),
    29: ("7081 syllabus; o level business studies 7115 changes; business 7081 june 2027", "Informational", "/blog/o-level-business-7115-to-7081/"),
    30: ("ai for studying; chatgpt for students; free ai tools pakistan students", "Commercial", "/blog/understanding-ai-for-studies/"),
    31: ("caie leak 2026; caie retake 2026; cambridge 2026 news pakistan", "Informational", "/blog/caie-2026-year-in-review/"),
    32: ("gift ideas for students pakistan; study gifts", "Commercial", "/blog/gifts-for-o-a-level-students/"),
    33: ("5090 diagrams; o level biology tips; biology diagrams list", "Informational", "/blog/o-level-biology-5090-diagrams/"),
    34: ("a level subjects in pakistan; a level combination for medical; a level combination for engineering", "Informational", "/blog/best-a-level-subjects-combinations/"),
    35: ("cambridge results date; how to check caie results pakistan; oct nov results january", "Informational", "/blog/caie-oct-nov-2026-results/"),
    36: ("o level student survey; how pakistani students study", "Social (not search)", "/blog/student-survey-2026/"),
}

SERIES_PILLAR = {
    "Examiner Mode (carousel)": "Subject Advice", "Sir Says (teacher reel)": "Subject Advice",
    "Tool Drop (carousel)": "Student Tech", "POV (5-8s reel)": "Shareable", "Parent Guide (carousel)": "Parents' Guides",
    "Comment-to-Get": "Exam Resources", "Sunday Special": "Community and News",
}
HASHTAGS = {
    "POV (5-8s reel)": "#caiememes #olevel #alevel #sjacademy",
    "Parent Guide (carousel)": "#olevelspakistan #alevelspakistan #parenting #sjacademy",
}
DEFAULT_TAGS = "#olevel #alevel #caie #olevelspakistan #sjacademy"
QUIZ_ROTATION = ["O Level Maths 4024", "A Level Physics 9702", "O Level Chemistry 5070", "A Level Business 9609",
                 "O Level Pakistan Studies 2059", "O Level Biology 5090", "A Level Economics 9708"]

BACKLOG_2027 = [
    ("Jan 2027", "Exam Resources", "Oct/Nov 2026 results: grade meanings, remarks and retake options", "caie results remarks", "Strategy"),
    ("Jan 2027", "Exam Resources", "Oct/Nov 2026 grade thresholds (update O Level page, A Level page)", "o level grade thresholds", "Strategy"),
    ("Jan 2027", "Parents' Guides", "Annual fee refresh: all top schools and college posts", "school fees karachi 2027", "Strategy"),
    ("Jan 2027", "Exam Resources", "How to Study for O and A Level Exams (consolidates 2025 study-tip posts, 301 redirects)", "how to study for o level exams", "Strategy + Instagram"),
    ("Jan 2027", "Future and Careers", "University application calendar for A Level students in Pakistan", "university admissions 2027 pakistan", "Strategy"),
    ("Jan 2027", "Future and Careers", "Careers With the Best Future in Pakistan (and Which A Levels Lead to Each)", "best career options in pakistan", "Instagram"),
    ("Jan 2027", "Subject Advice", "A Level Business Evaluation (AO4): the 5-Step Formula (refresh 20-mark post)", "a level business evaluation", "Instagram"),
    ("Jan 2027", "Shareable", "New Year resolutions every A Level student breaks by February", "(social)", "Strategy"),
    ("Feb 2027", "Exam Resources", "May/June 2027 private candidate registration explained", "private candidate registration caie", "Strategy"),
    ("Feb 2027", "Exam Resources", "Ramzan Study Timetable for O and A Level Students", "ramadan study timetable", "Strategy + Instagram"),
    ("Feb 2027", "Future and Careers", "MBBS vs BDS vs Pharm-D in Pakistan", "mbbs vs bds pakistan", "Strategy"),
    ("Feb 2027", "Student Tech", "Best budget laptops refresh (post-holiday prices)", "best budget laptop in pakistan", "Strategy"),
    ("Mar 2027", "Exam Resources", "From C to A in 60 Days: a Subject-by-Subject Plan", "how to improve grades in 2 months", "Instagram"),
    ("Mar 2027", "Subject Advice", "A Level Economics 9708: How to Draw Diagrams That Earn Full Marks (moved)", "a level economics diagrams", "Calendar swap (proposed)"),
    ("Mar 2027", "Subject Advice", "O Level Biology 5090: The Diagrams You Must Be Able to Draw (moved)", "o level biology diagrams", "Calendar swap (proposed)"),
    ("Mar 2027", "Future and Careers", "Scholarships for Pakistani students after A Levels", "scholarships after a levels", "Strategy"),
    ("Apr 2027", "Exam Resources", "Started Late? A 4-Week Rescue Plan for CAIE Exams", "started studying late for exams", "Instagram"),
    ("Apr 2027", "Exam Resources", "May/June 2027 Zone 4 timetable guide", "zone 4 timetable may june 2027", "Strategy"),
    ("Apr 2027", "Community and News", "What Happens If a CAIE Paper Leaks? (refresh /blog/caie-paper-leak/)", "caie paper leak", "Instagram"),
    ("May 2027", "Exam Resources", "Stress, sleep and nutrition during exams (professional reviewer)", "exam stress tips", "Strategy"),
    ("Jun 2027", "Exam Resources", "What to Do This Summer: a Productive Break Plan", "what to do in summer vacation for students", "Instagram"),
    ("Jul 2027", "Student Tech", "Back-to-school tech guide: laptops, tablets, gear", "best laptops for students", "Strategy"),
    ("Jul 2027", "Student Tech", "Best Tablets for Students in Pakistan (moved from Oct 2026)", "best tablet for students in pakistan", "Calendar swap (proposed)"),
    ("Jul 2027", "Future and Careers", "How to Make Your CV Stand Out Before University (refresh)", "cv for university students pakistan", "Instagram"),
    ("Aug 2027", "Exam Resources", "May/June 2027 grade thresholds (O Level update + A Level page on results day)", "a level grade thresholds 2027", "Strategy"),
    ("Aug 2027", "Exam Resources", "Results day guide: checking results, remarks, retakes", "caie results august 2027", "Strategy"),
    ("Sep 2027", "Exam Resources", "Starting A Levels: what changes from O Level", "starting a levels tips", "Strategy"),
]


def style_header(ws, headers, row=1, input_cols=()):
    for c, h in enumerate(headers, 1):
        cell = ws.cell(row=row, column=c, value=h)
        cell.font = HEAD_FONT
        cell.fill = PatternFill("solid", fgColor=ORANGE) if c in input_cols else HEAD_FILL
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        cell.border = BORDER
    ws.row_dimensions[row].height = 32


def style_body(ws, first_row, last_row, ncols, wrap_cols=(), date_cols=(), input_cols=()):
    for r in range(first_row, last_row + 1):
        for c in range(1, ncols + 1):
            cell = ws.cell(row=r, column=c)
            cell.font = BODY_FONT
            cell.border = BORDER
            cell.alignment = WRAP_TOP if c in wrap_cols else TOP
            if c in date_cols:
                cell.number_format = DATE_FMT
            if c in input_cols:
                cell.fill = INPUT_FILL


def add_list_validation(ws, col, first_row, last_row, list_range):
    dv = DataValidation(type="list", formula1=list_range, allow_blank=True, showDropDown=False)
    dv.error = "Pick a value from the list (edit the list on the Lists tab)."
    dv.errorStyle = "warning"
    ws.add_data_validation(dv)
    col_letter = get_column_letter(col)
    dv.add(f"{col_letter}{first_row}:{col_letter}{last_row}")


def add_status_colors(ws, status_col, first_row, last_row):
    col = get_column_letter(status_col)
    rng = f"{col}{first_row}:{col}{last_row}"
    for status, color in STATUS_COLORS.items():
        ws.conditional_formatting.add(
            rng, FormulaRule(formula=[f'${col}{first_row}="{status}"'], fill=PatternFill("solid", fgColor=color), stopIfTrue=True))


def add_overdue_rule(ws, date_col, status_col, first_row, last_row):
    d, s = get_column_letter(date_col), get_column_letter(status_col)
    ws.conditional_formatting.add(
        f"{d}{first_row}:{d}{last_row}",
        FormulaRule(formula=[f'AND(${d}{first_row}<>"",${d}{first_row}<TODAY(),${s}{first_row}<>"Published",${s}{first_row}<>"Scheduled",${s}{first_row}<>"Dropped")'],
                    font=Font(name=FONT, color="C00000", bold=True), fill=PatternFill("solid", fgColor="FFE5E5")))


def add_week_band(ws, week_col, first_row, last_row, ncols):
    w = get_column_letter(week_col)
    ws.conditional_formatting.add(
        f"A{first_row}:{get_column_letter(ncols)}{last_row}",
        FormulaRule(formula=[f"MOD(${w}{first_row},2)=0"], fill=PatternFill("solid", fgColor=GREY)))


def set_widths(ws, widths):
    for col, w in widths.items():
        ws.column_dimensions[col].width = w


def slug_id(prefix, n):
    return f"{prefix}-{n:03d}"


def main():
    blog = list(csv.DictReader(open(BLOG_CSV)))
    ig = list(csv.DictReader(open(IG_CSV)))
    pipe = list(csv.DictReader(open(PIPE_CSV)))
    start = dt.date(2026, 10, 5)

    wb = Workbook()

    # ---------------- Dashboard ----------------
    ds = wb.active
    ds.title = "Dashboard"

    # ---------------- Blog Calendar ----------------
    wsb = wb.create_sheet("Blog Calendar")
    bh = ["ID", "Publish date", "Day", "Week", "Month", "Pillar", "Track", "New / Refresh", "Topic / working title",
          "Primary keyword", "Secondary keywords", "Search intent", "Target URL", "Demand evidence",
          "Internal links and CTA", "Author / reviewer", "Instagram tie-in", "Status", "Assigned to", "Draft due",
          "Draft link", "Live URL", "Published on", "GSC clicks (28d)", "GSC impressions (28d)", "Avg position",
          "CTR", "Notes"]
    b_input = {18, 19, 20, 21, 22, 23, 24, 25, 26, 28}
    style_header(wsb, bh, input_cols=b_input)
    blog_by_date = {dt.date.fromisoformat(r["publish_date"]): int(r["#"]) for r in blog}

    def tie_blog_id(tie):
        m = re.search(r"\((\d{1,2}) (Oct|Nov|Dec)\)", tie or "")
        if not m:
            return None
        month = {"Oct": 10, "Nov": 11, "Dec": 12}[m.group(2)]
        return blog_by_date.get(dt.date(2026, month, int(m.group(1))))

    ig_by_blog = {}
    for i, r in enumerate(ig, 1):
        bid = tie_blog_id(r["blog_tie_in"])
        if bid:
            ig_by_blog.setdefault(bid, []).append(slug_id("IG", i))
    for i, r in enumerate(blog, 1):
        rr = i + 1
        n = int(r["#"])
        d = dt.date.fromisoformat(r["publish_date"])
        sec, intent, url = BLOG_EXTRA[n]
        title = r["working_title"]
        ties = ig_by_blog.get(n, [])
        vals = [slug_id("BLOG", n), d, f"=TEXT(B{rr},\"ddd\")", f"=INT((B{rr}-Dashboard!$C$4)/7)+1",
                f"=TEXT(B{rr},\"mmm yyyy\")", r["pillar"], r["track"], r["new_or_refresh"], title,
                r["primary_keyword"], sec, intent, url, r["demand_evidence"], r["internal_links_and_cta"],
                r["author_or_reviewer"], ", ".join(ties), "Planned", None, d - dt.timedelta(days=5), None, None, None,
                None, None, None, f"=IF(Y{rr}=\"\",\"\",IF(Y{rr}=0,0,X{rr}/Y{rr}))", None]
        for c, v in enumerate(vals, 1):
            wsb.cell(row=rr, column=c, value=v)
    last_b = len(blog) + 1
    style_body(wsb, 2, last_b + 20, len(bh), wrap_cols={9, 11, 14, 15, 17, 28}, date_cols={2, 20, 23},
               input_cols=b_input)
    for r in range(2, last_b + 21):
        wsb.cell(row=r, column=27).number_format = "0.0%"
        wsb.cell(row=r, column=26).number_format = "0.0"
    set_widths(wsb, {"A": 11, "B": 16, "C": 6, "D": 6, "E": 10, "F": 17, "G": 16, "H": 11, "I": 46, "J": 26,
                     "K": 34, "L": 15, "M": 30, "N": 34, "O": 34, "P": 20, "Q": 14, "R": 13, "S": 16, "T": 16,
                     "U": 18, "V": 22, "W": 16, "X": 11, "Y": 12, "Z": 10, "AA": 8, "AB": 30})
    wsb.freeze_panes = "J2"
    wsb.auto_filter.ref = f"A1:{get_column_letter(len(bh))}{last_b}"
    add_list_validation(wsb, 6, 2, last_b + 20, "=Lists!$B$2:$B$10")
    add_list_validation(wsb, 7, 2, last_b + 20, "=Lists!$C$2:$C$4")
    add_list_validation(wsb, 8, 2, last_b + 20, "=Lists!$D$2:$D$4")
    add_list_validation(wsb, 12, 2, last_b + 20, "=Lists!$E$2:$E$5")
    add_list_validation(wsb, 16, 2, last_b + 20, "=Lists!$H$2:$H$20")
    add_list_validation(wsb, 18, 2, last_b + 20, "=Lists!$A$2:$A$9")
    add_list_validation(wsb, 19, 2, last_b + 20, "=Lists!$H$2:$H$20")
    add_status_colors(wsb, 18, 2, last_b + 20)
    add_overdue_rule(wsb, 2, 18, 2, last_b + 20)
    add_week_band(wsb, 4, 2, last_b, len(bh))
    wsb["I1"].comment = Comment("Working title. Change freely; the ID stays the same.", "SJ Academy")
    wsb["J1"].comment = Comment("The one search term this post is built to rank for. Check it in Google Keyword Planner before writing if the evidence says 'estimated'.", "SJ Academy")
    wsb["N1"].comment = Comment("Source: Google Search Console, sjacademy.pk, 1 Jun to 28 Sep 2026, pulled 30 Sep 2026, unless the cell says otherwise.", "SJ Academy")

    # ---------------- Instagram Calendar ----------------
    wsi = wb.create_sheet("Instagram Calendar")
    ih = ["ID", "Date", "Day", "Week", "Week theme", "Series", "Format", "Pillar", "Topic / hook (on screen)",
          "Concept / brief", "Caption CTA", "Hashtags", "Teacher", "Blog tie-in", "Goal", "Boost or collab",
          "Status", "Assigned to", "Asset link", "Post link", "Views", "Reach", "Likes", "Comments", "Shares",
          "Saves", "Follows", "Saves per 1k reach", "Follows per 1k reach", "Notes"]
    i_input = {17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30}
    style_header(wsi, ih, input_cols=i_input)
    fmt_map = {"Reel 30-45s": "Reel 30-45s", "Reel 5-8s": "Reel 5-8s", "Reel 8-15s or carousel": "Reel 8-15s"}
    for i, r in enumerate(ig, 1):
        rr = i + 1
        d = dt.date.fromisoformat(r["date"])
        fmt = fmt_map.get(r["format"], r["format"])
        low = r["concept"].lower()
        if fmt == "Carousel" and (low.startswith("reel") or "montage" in low or "timelapse" in low):
            fmt = "Reel 30-45s"
        if fmt == "Varies":
            fmt = "Carousel" if "carousel" in low else ("Reel 30-45s" if "reel" in low else "Varies")
        vals = [slug_id("IG", i), d, f"=TEXT(B{rr},\"ddd\")", int(r["week"]), r["week_theme"], r["series"],
                fmt, SERIES_PILLAR[r["series"]], r["hook_on_screen"], r["concept"],
                r["caption_cta"], HASHTAGS.get(r["series"], DEFAULT_TAGS), r["teacher"],
                (f"{slug_id('BLOG', tie_blog_id(r['blog_tie_in']))}: " if tie_blog_id(r["blog_tie_in"]) else "") + r["blog_tie_in"], r["goal"],
                r["boost_or_collab"], "Planned", None, None, None, None, None, None, None, None, None, None,
                f"=IF(V{rr}=\"\",\"\",IF(V{rr}=0,0,Z{rr}/V{rr}*1000))",
                f"=IF(V{rr}=\"\",\"\",IF(V{rr}=0,0,AA{rr}/V{rr}*1000))", None]
        for c, v in enumerate(vals, 1):
            wsi.cell(row=rr, column=c, value=v)
    last_i = len(ig) + 1
    style_body(wsi, 2, last_i + 20, len(ih), wrap_cols={5, 9, 10, 11, 14, 16, 30}, date_cols={2}, input_cols=i_input)
    for r in range(2, last_i + 21):
        for c in (21, 22, 23, 24, 25, 26, 27):
            wsi.cell(row=r, column=c).number_format = "#,##0"
        for c in (28, 29):
            wsi.cell(row=r, column=c).number_format = "0.0"
    set_widths(wsi, {"A": 9, "B": 16, "C": 6, "D": 6, "E": 22, "F": 22, "G": 12, "H": 16, "I": 40, "J": 50,
                     "K": 26, "L": 28, "M": 20, "N": 26, "O": 22, "P": 26, "Q": 13, "R": 16, "S": 18, "T": 18,
                     "U": 10, "V": 10, "W": 9, "X": 10, "Y": 9, "Z": 9, "AA": 9, "AB": 10, "AC": 10, "AD": 30})
    wsi.freeze_panes = "J2"
    wsi.auto_filter.ref = f"A1:{get_column_letter(len(ih))}{last_i}"
    add_list_validation(wsi, 6, 2, last_i + 20, "=Lists!$F$2:$F$8")
    add_list_validation(wsi, 7, 2, last_i + 20, "=Lists!$G$2:$G$8")
    add_list_validation(wsi, 8, 2, last_i + 20, "=Lists!$B$2:$B$10")
    add_list_validation(wsi, 13, 2, last_i + 20, "=Lists!$H$2:$H$20")
    add_list_validation(wsi, 17, 2, last_i + 20, "=Lists!$A$2:$A$9")
    add_list_validation(wsi, 18, 2, last_i + 20, "=Lists!$H$2:$H$20")
    add_status_colors(wsi, 17, 2, last_i + 20)
    add_overdue_rule(wsi, 2, 17, 2, last_i + 20)
    add_week_band(wsi, 4, 2, last_i, len(ih))
    wsi["U1"].comment = Comment("Fill in from Instagram Insights about 7 days after posting.", "SJ Academy")
    wsi["AB1"].comment = Comment("Account averages Jan to Sep 2026 (organic): carousels 22.6 saves per 1k reach, reels 4.1. Source: Instagram post export, 30 Sep 2026.", "SJ Academy")
    wsi["AC1"].comment = Comment("Account averages Jan to Sep 2026 (organic): carousels 1.83 follows per 1k reach, reels 0.83. Target: 2.0+. Source: Instagram post export, 30 Sep 2026.", "SJ Academy")

    # ---------------- Stories Plan ----------------
    wss = wb.create_sheet("Stories Plan")
    sh = ["Date", "Day", "Week", "1. Link sticker (UTM)", "UTM campaign", "2. Past Paper Question of the Day",
          "Quiz subject", "3. Reshare", "4. Poll or question box", "5. Behind the scenes", "Frames posted",
          "Link clicks", "Done", "Notes"]
    s_input = {6, 9, 10, 11, 12, 13, 14}
    style_header(wss, sh, input_cols=s_input)
    for i, r in enumerate(ig, 1):
        rr = i + 1
        d = dt.date.fromisoformat(r["date"])
        tie = r["blog_tie_in"]
        link = f"Blog: {tie.split(' (')[0]}" if tie else "Today's feed post / tool / enrol page"
        camp = re.sub(r"[^a-z0-9]+", "_", (tie.split(" (")[0] if tie else r["hook_on_screen"]).lower())[:40].strip("_")
        poll = "Ask a teacher anything (question box)" if d.weekday() == 2 else ""
        vals = [d, f"=TEXT(A{rr},\"ddd\")", int(r["week"]), link, camp, None, QUIZ_ROTATION[d.weekday()],
                f"=\"Reshare \"&'Instagram Calendar'!A{rr}", poll, None, None, None, "Not done", None]
        for c, v in enumerate(vals, 1):
            wss.cell(row=rr, column=c, value=v)
    last_s = len(ig) + 1
    style_body(wss, 2, last_s, len(sh), wrap_cols={4, 6, 9, 10, 14}, date_cols={1}, input_cols=s_input)
    set_widths(wss, {"A": 16, "B": 6, "C": 6, "D": 36, "E": 28, "F": 36, "G": 22, "H": 14, "I": 30, "J": 24,
                     "K": 9, "L": 9, "M": 10, "N": 28})
    wss.freeze_panes = "D2"
    wss.auto_filter.ref = f"A1:N{last_s}"
    add_list_validation(wss, 13, 2, last_s, "=Lists!$I$2:$I$3")
    wss.conditional_formatting.add(f"M2:M{last_s}", FormulaRule(formula=['$M2="Done"'], fill=PatternFill("solid", fgColor="C6EFCE")))
    add_week_band(wss, 3, 2, last_s, len(sh))
    wss["E1"].comment = Comment("Use as utm_campaign. Full link format: https://www.sjacademy.pk/<page>?utm_source=instagram&utm_medium=story&utm_campaign=<this value>", "SJ Academy")

    # ---------------- Insta to Blog Ideas ----------------
    wsp = wb.create_sheet("Insta to Blog Ideas")
    ph = ["Rank", "Action", "Blog title", "Primary keyword", "Suggested date", "Calendar change", "Source Instagram post",
          "Source stats", "Why it will work", "Accuracy and production notes", "Status", "Notes"]
    style_header(wsp, ph, input_cols={11, 12})
    for i, r in enumerate(pipe, 1):
        rr = i + 1
        vals = [int(r["rank"]), r["action"], r["blog_title"], r["primary_keyword"],
                dt.date.fromisoformat(r["suggested_date"]), r["calendar_change"], r["source_instagram_post"],
                r["source_stats"], r["why_it_will_work"], r["accuracy_and_production_notes"], "Idea", None]
        for c, v in enumerate(vals, 1):
            wsp.cell(row=rr, column=c, value=v)
    last_p = len(pipe) + 1
    style_body(wsp, 2, last_p, len(ph), wrap_cols={2, 3, 6, 7, 8, 9, 10, 12}, date_cols={5}, input_cols={11, 12})
    set_widths(wsp, {"A": 6, "B": 14, "C": 42, "D": 26, "E": 16, "F": 34, "G": 34, "H": 26, "I": 34, "J": 34,
                     "K": 12, "L": 24})
    wsp.freeze_panes = "D2"
    wsp.auto_filter.ref = f"A1:L{last_p}"
    add_list_validation(wsp, 11, 2, last_p, "=Lists!$A$2:$A$9")
    add_status_colors(wsp, 11, 2, last_p)

    # ---------------- Blog Ideas 2027 ----------------
    wsk = wb.create_sheet("Blog Ideas 2027")
    kh = ["Month", "Pillar", "Topic / working title", "Primary keyword", "Source", "Status", "Planned date", "Notes"]
    style_header(wsk, kh, input_cols={6, 7, 8})
    for i, row in enumerate(BACKLOG_2027, 2):
        for c, v in enumerate(list(row) + ["Idea", None, None], 1):
            wsk.cell(row=i, column=c, value=v)
    last_k = len(BACKLOG_2027) + 1
    style_body(wsk, 2, last_k + 15, len(kh), wrap_cols={3, 8}, date_cols={7}, input_cols={6, 7, 8})
    set_widths(wsk, {"A": 10, "B": 18, "C": 60, "D": 32, "E": 22, "F": 12, "G": 16, "H": 30})
    wsk.freeze_panes = "C2"
    wsk.auto_filter.ref = f"A1:H{last_k}"
    add_list_validation(wsk, 2, 2, last_k + 15, "=Lists!$B$2:$B$10")
    add_list_validation(wsk, 6, 2, last_k + 15, "=Lists!$A$2:$A$9")
    add_status_colors(wsk, 6, 2, last_k + 15)

    # ---------------- Keywords ----------------
    wkw = wb.create_sheet("Keywords")
    kwh = ["Keyword", "Type", "Blog post ID", "Post title", "Publish date", "Status", "Pillar", "Search intent",
           "Current position", "Target position", "Notes"]
    style_header(wkw, kwh, input_cols={9, 10, 11})
    rr = 2
    for i, r in enumerate(blog, 1):
        n = int(r["#"])
        if r["primary_keyword"].startswith("("):
            continue
        kws = [(r["primary_keyword"], "Primary")] + [(k.strip(), "Secondary") for k in BLOG_EXTRA[n][0].split(";")]
        for kw, typ in kws:
            row_ref = n + 1
            vals = [kw, typ, slug_id("BLOG", n),
                    f"=INDEX('Blog Calendar'!$I:$I,MATCH($C{rr},'Blog Calendar'!$A:$A,0))",
                    f"=INDEX('Blog Calendar'!$B:$B,MATCH($C{rr},'Blog Calendar'!$A:$A,0))",
                    f"=INDEX('Blog Calendar'!$R:$R,MATCH($C{rr},'Blog Calendar'!$A:$A,0))",
                    f"=INDEX('Blog Calendar'!$F:$F,MATCH($C{rr},'Blog Calendar'!$A:$A,0))",
                    f"=INDEX('Blog Calendar'!$L:$L,MATCH($C{rr},'Blog Calendar'!$A:$A,0))",
                    None, 3 if typ == "Primary" else 10, None]
            for c, v in enumerate(vals, 1):
                wkw.cell(row=rr, column=c, value=v)
            rr += 1
    last_kw = rr - 1
    style_body(wkw, 2, last_kw + 15, len(kwh), wrap_cols={4, 11}, date_cols={5}, input_cols={9, 10, 11})
    set_widths(wkw, {"A": 40, "B": 11, "C": 11, "D": 46, "E": 16, "F": 12, "G": 17, "H": 15, "I": 10, "J": 10, "K": 30})
    wkw.freeze_panes = "B2"
    wkw.auto_filter.ref = f"A1:K{last_kw}"
    wkw["J1"].comment = Comment("Target Google position. Primary keywords: top 3. Secondary: top 10. Change as needed.", "SJ Academy")

    # ---------------- Lists ----------------
    wl = wb.create_sheet("Lists")
    lh = ["Status", "Pillar", "Track", "New / Refresh", "Search intent", "Instagram series", "Format", "People", "Done"]
    style_header(wl, lh)
    for c, items in enumerate([STATUSES, PILLARS, TRACKS, POST_TYPES, INTENTS, SERIES, FORMATS, PEOPLE, YES_NO], 1):
        for r, v in enumerate(items, 2):
            wl.cell(row=r, column=c, value=v)
    style_body(wl, 2, 20, len(lh), input_cols=set(range(1, 10)))
    set_widths(wl, {get_column_letter(c): 24 for c in range(1, 10)})
    for s, color in STATUS_COLORS.items():
        wl.cell(row=STATUSES.index(s) + 2, column=1).fill = PatternFill("solid", fgColor=color)

    # ---------------- Data Sources ----------------
    wd = wb.create_sheet("Data Sources")
    dh = ["Written to", "Source", "Object", "Obtained via", "Query or request", "Parameters", "Run at",
          "Requested by", "Row count", "Changes after retrieval", "Notes"]
    style_header(wd, dh)
    rows = [
        [f"'Blog Calendar'!A1:AB{last_b}", "SJ Academy blog plan (Claude Code)", BLOG_CSV, "Local file, built by Claude",
         "Blog calendar for Oct to Dec 2026 based on Search Console demand", "5 Oct to 25 Dec 2026, 3 posts a week",
         "30 Sep 2026", "Sunyyan Junaid", len(blog), "Added secondary keywords, search intent, target URL, tracking columns", "Demand evidence from Google Search Console, sjacademy.pk, 1 Jun to 28 Sep 2026"],
        [f"'Instagram Calendar'!A1:AD{last_i}", "SJ Academy Instagram plan (Claude Code)", IG_CSV, "Local file, built by Claude",
         "Instagram calendar based on the 30 Sep 2026 account analysis", "5 Oct 2026 to 3 Jan 2027, 1 post a day",
         "30 Sep 2026", "Sunyyan Junaid", len(ig), "Added pillar, hashtags, tracking and metric columns", "Benchmarks from Meta Business Suite exports (posts, stories, audience), 1 Jan to 29 Sep 2026"],
        [f"'Insta to Blog Ideas'!A1:L{last_p}", "SJ Academy Instagram-to-blog plan (Claude Code)", PIPE_CSV, "Local file, built by Claude",
         "Turn the most viral Instagram posts into blog posts", "18 ideas", "30 Sep 2026", "Sunyyan Junaid", len(pipe),
         "None", "Calendar swaps in the 'Calendar change' column are proposals, not yet applied to the Blog Calendar"],
        [f"'Blog Ideas 2027'!A1:H{last_k}", "SJ Academy blog strategy (Claude Code)",
         "03_Plans_and_Content/Blog_Content_Plan_2026-27/Blog_Strategy_2026-27.md", "Local file, built by Claude",
         "January to September 2027 themes", "Jan to Sep 2027", "30 Sep 2026", "Sunyyan Junaid", len(BACKLOG_2027),
         "Condensed to one row per idea", ""],
    ]
    for r, row in enumerate(rows, 2):
        for c, v in enumerate(row, 1):
            wd.cell(row=r, column=c, value=v)
    style_body(wd, 2, len(rows) + 1, len(dh), wrap_cols=set(range(1, 12)))
    set_widths(wd, {get_column_letter(c): 24 for c in range(1, 12)})

    # ---------------- Dashboard content ----------------
    ds["A1"] = "SJ Academy Content Calendar 2026-27"
    ds["A1"].font = Font(name=FONT, bold=True, size=16, color=BROWN)
    ds["A2"] = "One place for every blog post and Instagram post: plan it, assign it, track it, measure it."
    ds["A2"].font = Font(name=FONT, italic=True, size=10, color="595959")
    ds["A4"] = "Calendar start date (Week 1 Monday)"
    ds["C4"] = start
    ds["C4"].number_format = DATE_FMT
    ds["C4"].fill = INPUT_FILL
    ds["C4"].comment = Comment("Input: Week numbers on every tab count from this date.", "SJ Academy")
    ds["A5"] = "Today"
    ds["C5"] = "=TODAY()"
    ds["C5"].number_format = DATE_FMT
    ds["A6"] = "Current week"
    ds["C6"] = "=IF(C5<C4,0,INT((C5-C4)/7)+1)"
    for r in (4, 5, 6):
        ds[f"A{r}"].font = Font(name=FONT, bold=True, size=10)
        ds[f"C{r}"].font = BODY_FONT

    ds["A8"] = "Status"
    ds["B8"] = "Blog"
    ds["C8"] = "Instagram"
    ds["D8"] = "Insta to Blog ideas"
    for c in "ABCD":
        ds[f"{c}8"].font = HEAD_FONT
        ds[f"{c}8"].fill = HEAD_FILL
        ds[f"{c}8"].alignment = Alignment(horizontal="center")
    for i, s in enumerate(STATUSES):
        r = 9 + i
        ds[f"A{r}"] = f"=Lists!A{i + 2}"
        ds[f"B{r}"] = f"=COUNTIF('Blog Calendar'!$R:$R,$A{r})"
        ds[f"C{r}"] = f"=COUNTIF('Instagram Calendar'!$Q:$Q,$A{r})"
        ds[f"D{r}"] = f"=COUNTIF('Insta to Blog Ideas'!$K:$K,$A{r})"
        ds[f"A{r}"].fill = PatternFill("solid", fgColor=STATUS_COLORS[s])
    tr = 9 + len(STATUSES)
    ds[f"A{tr}"] = "Total"
    for c in "BCD":
        ds[f"{c}{tr}"] = f"=SUM({c}9:{c}{tr - 1})"
    ds[f"A{tr}"].font = Font(name=FONT, bold=True, size=10)

    r0 = tr + 2
    ds[f"A{r0}"] = "This week"
    ds[f"B{r0}"] = "Blog"
    ds[f"C{r0}"] = "Instagram"
    for c in "ABC":
        ds[f"{c}{r0}"].font = HEAD_FONT
        ds[f"{c}{r0}"].fill = HEAD_FILL
        ds[f"{c}{r0}"].alignment = Alignment(horizontal="center")
    ds[f"A{r0 + 1}"] = "Planned this week"
    ds[f"B{r0 + 1}"] = f"=COUNTIF('Blog Calendar'!$D:$D,$C$6)"
    ds[f"C{r0 + 1}"] = f"=COUNTIF('Instagram Calendar'!$D:$D,$C$6)"
    ds[f"A{r0 + 2}"] = "Published this week"
    ds[f"B{r0 + 2}"] = f"=COUNTIFS('Blog Calendar'!$D:$D,$C$6,'Blog Calendar'!$R:$R,\"Published\")"
    ds[f"C{r0 + 2}"] = f"=COUNTIFS('Instagram Calendar'!$D:$D,$C$6,'Instagram Calendar'!$Q:$Q,\"Published\")"
    ds[f"A{r0 + 3}"] = "Overdue (date passed, not published)"
    ds[f"B{r0 + 3}"] = "=COUNTIFS('Blog Calendar'!$B:$B,\"<\"&$C$5,'Blog Calendar'!$R:$R,\"<>Published\",'Blog Calendar'!$R:$R,\"<>Scheduled\",'Blog Calendar'!$R:$R,\"<>Dropped\",'Blog Calendar'!$R:$R,\"<>\")"
    ds[f"C{r0 + 3}"] = "=COUNTIFS('Instagram Calendar'!$B:$B,\"<\"&$C$5,'Instagram Calendar'!$Q:$Q,\"<>Published\",'Instagram Calendar'!$Q:$Q,\"<>Scheduled\",'Instagram Calendar'!$Q:$Q,\"<>Dropped\",'Instagram Calendar'!$Q:$Q,\"<>\")"
    ds[f"A{r0 + 4}"] = "Stories done this week"
    ds[f"C{r0 + 4}"] = f"=COUNTIFS('Stories Plan'!$C:$C,$C$6,'Stories Plan'!$M:$M,\"Done\")"

    r1 = r0 + 6
    ds[f"A{r1}"] = "Blog posts by pillar"
    ds[f"B{r1}"] = "Planned"
    ds[f"C{r1}"] = "Published"
    ds[f"E{r1}"] = "Instagram by series"
    ds[f"F{r1}"] = "Planned"
    ds[f"G{r1}"] = "Published"
    ds[f"H{r1}"] = "Avg saves per 1k reach"
    ds[f"I{r1}"] = "Avg follows per 1k reach"
    for c in "ABCEFGHI":
        ds[f"{c}{r1}"].font = HEAD_FONT
        ds[f"{c}{r1}"].fill = HEAD_FILL
        ds[f"{c}{r1}"].alignment = Alignment(horizontal="center", wrap_text=True)
    for i in range(len(PILLARS)):
        r = r1 + 1 + i
        ds[f"A{r}"] = f"=Lists!B{i + 2}"
        ds[f"B{r}"] = f"=COUNTIF('Blog Calendar'!$F:$F,$A{r})"
        ds[f"C{r}"] = f"=COUNTIFS('Blog Calendar'!$F:$F,$A{r},'Blog Calendar'!$R:$R,\"Published\")"
    for i in range(len(SERIES)):
        r = r1 + 1 + i
        ds[f"E{r}"] = f"=Lists!F{i + 2}"
        ds[f"F{r}"] = f"=COUNTIF('Instagram Calendar'!$F:$F,$E{r})"
        ds[f"G{r}"] = f"=COUNTIFS('Instagram Calendar'!$F:$F,$E{r},'Instagram Calendar'!$Q:$Q,\"Published\")"
        ds[f"H{r}"] = f"=IFERROR(AVERAGEIFS('Instagram Calendar'!$AB:$AB,'Instagram Calendar'!$F:$F,$E{r},'Instagram Calendar'!$AB:$AB,\"<>\"),\"\")"
        ds[f"I{r}"] = f"=IFERROR(AVERAGEIFS('Instagram Calendar'!$AC:$AC,'Instagram Calendar'!$F:$F,$E{r},'Instagram Calendar'!$AC:$AC,\"<>\"),\"\")"
        ds[f"H{r}"].number_format = "0.0"
        ds[f"I{r}"].number_format = "0.0"

    r2 = r1 + len(PILLARS) + 3
    legend = [
        ("How to use this calendar", None),
        ("Orange header = columns your team fills in (status, owner, links, results). Brown header = the plan.", None),
        ("Cream cells = input cells. Everything else is either the plan or a formula.", None),
        ("Status: pick from the dropdown. Colours update automatically; a red date means it is overdue.", None),
        ("Grey bands mark alternate weeks. Filter any column with the filter buttons in row 1.", None),
        ("Add a row: copy the last row, give it the next ID (BLOG-037, IG-092) and a date. Formulas and dropdowns carry on.", None),
        ("Instagram results: fill Views, Reach, Saves, Follows about 7 days after posting. Saves and follows per 1k reach calculate themselves.", None),
        ("Blog results: fill GSC clicks, impressions and position 4 weeks after publishing (Search Console > Performance > Pages).", None),
        ("Change dropdown options (people, pillars, statuses) on the Lists tab.", None),
        ("Stories: tick 'Done' each day. Build story links as https://www.sjacademy.pk/<page>?utm_source=instagram&utm_medium=story&utm_campaign=<UTM campaign>.", None),
    ]
    for i, (text, _) in enumerate(legend):
        c = ds.cell(row=r2 + i, column=1, value=text)
        c.font = Font(name=FONT, bold=(i == 0), size=11 if i == 0 else 10, color=BROWN if i == 0 else "000000")
    for row in ds.iter_rows(min_row=8, max_row=r1 + len(PILLARS), max_col=9):
        for cell in row:
            if cell.value is not None and cell.font != HEAD_FONT and cell.row not in (8, r0, r1):
                cell.font = BODY_FONT
                cell.border = BORDER
    set_widths(ds, {"A": 38, "B": 12, "C": 18, "D": 18, "E": 26, "F": 10, "G": 11, "H": 13, "I": 13})
    ds.sheet_view.showGridLines = False

    wb.save(OUT)
    print(f"Saved {OUT}: blog {len(blog)}, instagram {len(ig)}, stories {len(ig)}, ideas {len(pipe)}, 2027 {len(BACKLOG_2027)}, keywords {last_kw - 1}")


if __name__ == "__main__":
    main()
