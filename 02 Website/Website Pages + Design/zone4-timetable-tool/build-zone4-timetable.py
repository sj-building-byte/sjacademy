#!/usr/bin/env python3
"""
SJ Academy: CAIE Zone 4 timetable page builder.

Builds the Elementor HTML widget for /caie-zone-4-timetable/ in one of two states:

  waiting   Cambridge has not published the series yet. Status card, WhatsApp alert,
            how the tool works, the running series as a working tool, syllabus codes, FAQ.
  live      The final timetable is out. The full timetable is written into the HTML
            (so search engines read it), with search, a "your papers" list, calendar
            download, WhatsApp share and print.

Data is a CSV with the header:  date,session,level,code,duration,subject
  date      2027-04-23
  session   AM, PM or EV
  level     IG (IGCSE), OL (O Level), AS (AS Level), AL (A Level, the A2 papers)
  code      9609/12
  duration  1h 15m
  subject   Business

Examples
  python3 build-zone4-timetable.py --state waiting --archive data/nov-2026.csv --out page.html
  python3 build-zone4-timetable.py --state live --current data/may-june-2027.csv \
      --series "May/June 2027" --version "Version 1, October 2026" --out page.html

Output is plain ASCII. Python 3.8 or newer, no other packages.
"""
import argparse
import csv
import datetime as dt
import html
import json
import re
import sys

SITE = "https://www.sjacademy.pk"
PAGE_URL = SITE + "/caie-zone-4-timetable/"
WA_NUMBER = "923362144454"
POPUP = "#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D"
PAGE_CODE = "RS-ZONE4"
CAL_URL = "https://www.cambridgeinternational.org/Images/746010-monthly-calendar-2026-international-.pdf"
HELP_URL = "https://help.cambridgeinternational.org/hc/en-gb/articles/29505585906194-When-will-exam-timetables-be-released"
KEYTIME_URL = "https://www.cambridgeinternational.org/keytime"
CAMBRIDGE_URL = "https://www.cambridgeinternational.org/"

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
LEVELS = {"IG": ("IGCSE", "IGCSE"), "OL": ("O Level", "O Level"),
          "AS": ("AS Level", "AS"), "AL": ("A Level (A2)", "A2")}
LV_ORDER = {"IG": 0, "OL": 1, "AS": 2, "AL": 3}
SESS_ORDER = {"AM": 0, "PM": 1, "EV": 2}

A_LEVEL_CODES = [
    ("Business", "9609"), ("Economics", "9708"), ("Mathematics", "9709"),
    ("Accounting", "9706"), ("Physics", "9702"), ("Chemistry", "9701"),
    ("Biology", "9700"), ("Computer Science", "9618"), ("Further Mathematics", "9231"),
    ("Psychology", "9990"), ("Sociology", "9699"), ("Law", "9084"),
    ("English General Paper", "8021"), ("Geography", "9696"), ("History", "9489"),
    ("Literature in English", "9695"), ("English Language", "9093"),
    ("Information Technology", "9626"), ("Urdu", "9686"),
]
O_LEVEL_CODES = [
    ("Mathematics Syllabus D", "4024"), ("Physics", "5054"), ("Chemistry", "5070"),
    ("Biology", "5090"), ("Accounting", "7707"), ("Business", "7081"),
    ("Economics", "2281"), ("Commerce", "7100"), ("Computer Science", "2210"),
    ("Pakistan Studies", "2059"), ("Islamiyat", "2058"), ("English Language", "1123"),
    ("Urdu Second Language", "3248"), ("Additional Mathematics", "4037"),
    ("Geography", "2217"), ("History", "2147"), ("Sociology", "2251"),
    ("Statistics", "4040"), ("Literature in English", "2010"),
]


# ---------------------------------------------------------------- helpers
def esc(s):
    """Escape text for HTML and keep the file plain ASCII."""
    s = html.escape(str(s), quote=True).replace("&#x27;", "&rsquo;")
    return s.encode("ascii", "xmlcharrefreplace").decode("ascii")


def long_day(d):
    return "%s %d %s %d" % (DAYS[d.weekday()], d.day, MONTHS[d.month - 1], d.year)


def day_month(d):
    return "%d %s" % (d.day, MONTHS[d.month - 1])


def day_month_year(d):
    return "%d %s %d" % (d.day, MONTHS[d.month - 1], d.year)


def wa(message):
    return "https://wa.me/%s?text=%s" % (WA_NUMBER, urlquote(message))


def urlquote(s):
    from urllib.parse import quote
    return quote(s, safe="")


def md(s):
    """[text](url) to (html, plain text)."""
    plain = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s).replace("'", "\u2019")
    out = []
    pos = 0
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", s):
        out.append(esc(s[pos:m.start()]))
        out.append('<a class="sj-link" href="%s" target="_blank" rel="noopener">%s</a>' % (m.group(2), esc(m.group(1))))
        pos = m.end()
    out.append(esc(s[pos:]))
    return "".join(out), plain


def sort_key(r):
    return (r["date"], SESS_ORDER[r["session"]], LV_ORDER[r["level"]], r["subject"].lower(), r["code"])


# ---------------------------------------------------------------- data
def load_csv(path):
    rows, problems = [], []
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        need = ["date", "session", "level", "code", "duration", "subject"]
        if [h.strip().lower() for h in (reader.fieldnames or [])] != need:
            sys.exit("CSV header must be exactly: " + ",".join(need) + "  (found: %s)" % reader.fieldnames)
        for i, raw in enumerate(reader, start=2):
            r = {k.strip().lower(): (v or "").strip() for k, v in raw.items()}
            try:
                r["date"] = dt.date.fromisoformat(r["date"])
            except ValueError:
                problems.append("line %d: bad date %r" % (i, r["date"]))
                continue
            r["session"] = r["session"].upper()
            r["level"] = r["level"].upper()
            if r["session"] not in SESS_ORDER:
                problems.append("line %d: session %r is not AM, PM or EV" % (i, r["session"]))
            if r["level"] not in LEVELS:
                problems.append("line %d: level %r is not IG, OL, AS or AL" % (i, r["level"]))
            if not re.fullmatch(r"\d{4}/\d{2}", r["code"]):
                problems.append("line %d: code %r does not look like 9609/12" % (i, r["code"]))
            if not re.fullmatch(r"(\d+h)?( ?\d+m)?", r["duration"]) or not r["duration"]:
                problems.append("line %d: duration %r does not look like 1h 15m" % (i, r["duration"]))
            if not r["subject"]:
                problems.append("line %d: subject is empty" % i)
            rows.append(r)
    seen = {}
    for r in rows:
        key = (r["date"], r["code"])
        if key in seen:
            problems.append("duplicate paper: %s on %s" % (r["code"], r["date"]))
        seen[key] = 1
    codes = {}
    for r in rows:
        codes.setdefault(r["code"], set()).add(r["date"])
    for c, ds in codes.items():
        if len(ds) > 1:
            problems.append("code %s appears on %d different dates" % (c, len(ds)))
    weekend = sorted({r["date"] for r in rows if r["date"].weekday() >= 5})
    notes = []
    if weekend:
        notes.append("papers on a weekend (check they are real): " + ", ".join(str(d) for d in weekend))
    if problems:
        print("\nDATA PROBLEMS (fix the CSV, then run again):", file=sys.stderr)
        for p in problems:
            print("  - " + p, file=sys.stderr)
        sys.exit(1)
    rows.sort(key=sort_key)
    return rows, notes


def summarise(rows):
    ds = sorted({r["date"] for r in rows})
    by_level = {k: sum(1 for r in rows if r["level"] == k) for k in LEVELS}
    return {"n": len(rows), "first": ds[0], "last": ds[-1], "days": len(ds), "by_level": by_level}


# ---------------------------------------------------------------- markup pieces
CIRCLE = ('<svg class="sj-circle" viewBox="0 0 120 70" preserveAspectRatio="none" aria-hidden="true">'
          '<path d="M14 38C10 18 40 6 68 7c27 1 44 13 42 30-2 16-30 24-56 23C28 59 8 50 13 30" '
          'fill="none" stroke="#FE6100" stroke-width="2.6" stroke-linecap="round"/></svg>')
SEARCH_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/>'
              '<path d="M20 20l-4-4"/></svg>')


def row_html(r):
    lv = LEVELS[r["level"]][1]
    name = esc(r["subject"])
    return (
        '<tr class="zt-r" data-l="%s" data-s="%s" data-c="%s">'
        '<td class="zt-pk"><label class="zt-lab"><input type="checkbox" value="%s" '
        'aria-label="Add %s %s, %s"></label></td>'
        '<td class="zt-sb"><b>%s</b><small class="zt-mt">%s &middot; %s &middot; %s</small></td>'
        '<td class="zt-cd sj-num">%s</td><td class="zt-lv">%s</td><td class="zt-du sj-num">%s</td>'
        '<td class="zt-se"><span class="zt-ses zt-%s">%s</span></td></tr>'
    ) % (r["level"], r["session"], r["code"], r["code"], name, r["code"], long_day(r["date"]),
         name, r["code"], lv, esc(r["duration"]), r["code"], lv, esc(r["duration"]),
         r["session"], r["session"])


def tbody_html(rows):
    out = []
    days = []
    for r in rows:
        if not days or days[-1][0] != r["date"]:
            days.append((r["date"], []))
        days[-1][1].append(r)
    for d, rs in days:
        out.append('<tbody class="zt-d" data-d="%s"><tr class="zt-dr"><th colspan="6" scope="colgroup">%s'
                   '<span> &middot; %d paper%s</span></th></tr>%s</tbody>'
                   % (d.isoformat(), long_day(d), len(rs), "" if len(rs) == 1 else "s",
                      "".join(row_html(r) for r in rs)))
    return "\n".join(out)


THEAD = ('<thead><tr><th scope="col"><span class="sj-vh">Add</span></th><th scope="col">Subject</th>'
         '<th scope="col">Code</th><th scope="col">Level</th><th scope="col">Duration</th>'
         '<th scope="col">Session</th></tr></thead>')


def filter_card(sid, search_label="Search by subject, code or day", with_offset=True, hint=True):
    levels = "".join(
        '<label class="sj-choice"><input type="radio" name="zt-lv-%s" value="%s"%s><span>%s</span></label>'
        % (sid, v, " checked" if v == "" else "", lab)
        for v, lab in [("", "All"), ("IG", "IGCSE"), ("OL", "O Level"), ("AS", "AS"), ("AL", "A2")])
    inner = (
        '<div class="sj-field"><label class="sj-label" for="zt-q-%s">%s</label>'
        '<div class="sj-search">%s<input class="sj-input" id="zt-q-%s" type="search" '
        'placeholder="For example 9609 or Business" autocomplete="off" autocapitalize="off" spellcheck="false" '
        'data-zt-for="%s" data-part="search"></div>%s</div>'
        '<div class="sj-field"><span class="sj-label" id="zt-lvl-%s">Level</span>'
        '<div class="sj-choices" role="radiogroup" aria-labelledby="zt-lvl-%s" data-zt-for="%s" data-part="levels">%s</div></div>'
        '<label class="sj-check" data-zt-for="%s" data-part="past-wrap" hidden><input type="checkbox" '
        'data-zt-for="%s" data-part="past"><span>Hide papers already sat</span></label>'
        '<div class="zt-meta"><p class="zt-count" role="status" aria-live="polite" data-zt-for="%s" data-part="count"></p>'
        '<div class="sj-row"><button class="sj-btn sj-btn-ghost sj-btn-sm" type="button" data-zt-for="%s" data-part="addall" hidden>Add all shown</button>'
        '<button class="sj-btn sj-btn-ghost sj-btn-sm" type="button" data-zt-for="%s" data-part="clear" hidden>Clear filters</button></div></div>'
    ) % (sid, esc(search_label), SEARCH_SVG, sid, sid,
         '<p class="sj-help">Tick the papers you sit. Your list builds below.</p>' if hint else "",
         sid, sid, sid, levels, sid, sid, sid, sid, sid)
    if with_offset:
        return '<div class="sj-offset sj-stack" id="zt-tool-%s">%s</div>' % (sid, inner)
    return '<div class="sj-stack">%s</div>' % inner


def mine_panel(sid):
    return (
        '<div class="sj-card sj-tagged zt-mine" id="zt-mine-%s" data-zt-for="%s" data-part="mine" hidden>'
        '<span class="sj-tag">your list</span>'
        '<h3 class="sj-h3">Your papers (<span data-zt-for="%s" data-part="mine-n">0</span>)</h3>'
        '<ul class="zt-ml" data-zt-for="%s" data-part="mine-list"></ul>'
        '<p class="sj-small zt-clash" data-zt-for="%s" data-part="mine-clash" hidden>Two of your papers share a session. '
        'Tell your exams officer early, so your centre can arrange it.</p>'
        '<div class="sj-row">'
        '<button class="sj-btn sj-btn-primary sj-btn-sm" type="button" data-zt-for="%s" data-part="ical" data-event="resource_download" data-loc="calendar">Add to calendar</button>'
        '<a class="sj-btn sj-btn-wa sj-btn-sm" href="#" target="_blank" rel="noopener" data-zt-for="%s" data-part="share" data-loc="share">Send on WhatsApp</a>'
        '<button class="sj-btn sj-btn-ghost sj-btn-sm" type="button" data-zt-for="%s" data-part="print">Print</button>'
        '<button class="sj-btn sj-btn-ghost sj-btn-sm" type="button" data-zt-for="%s" data-part="wipe">Clear list</button>'
        '</div>'
        '<p class="sj-caption">The calendar file adds each paper as an all-day event with a reminder the day before. '
        'Check your Statement of Entry for start times.</p>'
        '</div>'
    ) % (sid, sid, sid, sid, sid, sid, sid, sid, sid)


def results_block(sid, body_html, js_render, caption="Cambridge Zone 4 timetable by date"):
    skel = ""
    if js_render:
        skel = ('<div class="sj-stack" data-zt-for="%s" data-part="skel" aria-hidden="true">'
                '<span class="sj-skel"></span><span class="sj-skel"></span><span class="sj-skel"></span></div>'
                '<noscript><p class="sj-small">Turn on JavaScript to search this timetable, or read the official PDF on the '
                '<a class="sj-link" href="%s" target="_blank" rel="noopener">Cambridge International website</a>.</p></noscript>'
                '<div class="sj-alert sj-alert-err" role="alert" data-zt-for="%s" data-part="fail" hidden><b>Timetable did not load</b>'
                '<p>Refresh the page, or <a class="sj-link" href="%s" target="_blank" rel="noopener" data-loc="timetable_error">WhatsApp us</a> and we will send the dates.</p></div>'
                % (sid, CAMBRIDGE_URL, sid, wa("Hi SJ Academy, the Zone 4 timetable on your site did not load for me.\n(Ref: %s)\nMy name is " % PAGE_CODE)))
        skel = skel.replace("%s", "") if False else skel
    return (
        '%s<div class="sj-table-wrap" data-zt-for="%s" data-part="wrap"><table class="sj-table zt-table" data-zt-for="%s" data-part="table">'
        '<caption class="sj-vh">%s</caption>%s%s</table></div>'
        '<div class="sj-empty" data-zt-for="%s" data-part="empty" hidden><b>No papers found</b>'
        '<p>Try a subject name or a code such as 9609, or clear the filters.</p>'
        '<button class="sj-btn sj-btn-sm" type="button" data-zt-for="%s" data-part="clear2">Clear filters</button></div>'
    ) % (skel, sid, sid, esc(caption), THEAD, body_html, sid, sid)


def faq_html(items, open_first=True):
    parts, ld = [], []
    for i, (q, a) in enumerate(items):
        a_html, a_text = md(a)
        parts.append('<details%s><summary>%s</summary><div class="sj-faq-a"><p>%s</p></div></details>'
                     % (" open" if (i == 0 and open_first) else "", esc(q), a_html))
        ld.append({"@type": "Question", "name": q.replace("'", "\u2019"),
                   "acceptedAnswer": {"@type": "Answer", "text": a_text}})
    return "\n".join(parts), ld


def crumbs():
    return ('<nav class="sj-crumbs" aria-label="Breadcrumb"><ol><li><a href="%s/">Home</a></li>'
            '<li><a href="%s/free-caie-resources/">Free CAIE resources</a></li>'
            '<li aria-current="page">CAIE Zone 4 timetable</li></ol></nav>' % (SITE, SITE))


def codes_section(codes_live, bg):
    def lst(items):
        out = []
        for name, code in items:
            if codes_live:
                out.append('<li><button type="button" class="zt-codebtn" data-zt-code="%s"><b>%s</b><span>%s</span></button></li>'
                           % (code, esc(name), code))
            else:
                out.append('<li><b>%s</b><span>%s</span></li>' % (esc(name), code))
        return "\n".join(out)
    return (
        '<section class="sj-section %s" id="codes"><div class="sj-wrap sj-stack-lg">'
        '<div class="sj-stack"><div class="sj-eyebrow">Syllabus codes</div>'
        '<h2 class="sj-h2">Find your <span class="sj-hl">subject code</span></h2>'
        '<p class="sj-measure">Search the timetable by name or by code. These are common Cambridge syllabus codes for Pakistani candidates.</p></div>'
        '<div class="sj-grid sj-grid-2">'
        '<div class="sj-card"><h3 class="sj-h3">AS and A Level</h3><ul class="zt-codes">%s</ul></div>'
        '<div class="sj-card"><h3 class="sj-h3">O Level</h3><ul class="zt-codes">%s</ul>'
        '<p class="sj-small sj-muted">IGCSE codes start with 0, for example Mathematics 0580 and Physics 0625.</p></div>'
        '</div></div></section>'
    ) % (bg, lst(A_LEVEL_CODES), lst(O_LEVEL_CODES))


def related_section(bg, heading_hl, intro):
    tiles = [
        ("A Level past papers", "Question papers and mark schemes, by subject.", "/a-level-past-papers/", "Open A Level papers"),
        ("O Level past papers", "Question papers and mark schemes, by subject.", "/o-level-past-papers/", "Open O Level papers"),
        ("CAIE 2027 timeline", "Entries, exams and results dates for the 2027 series.", "/caie-2027-pakistan-timeline/", "See the timeline"),
        ("Private candidate registration", "How private candidates in Pakistan enter the exams.", "/caie-private-candidate-registration/", "See how to enter"),
        ("Exam day guide", "What to bring and what to expect on the day.", "/blog/caie-exam-day-guide/", "Read the guide"),
        ("O Level grade thresholds", "Grade thresholds by series.", "/o-level-grade-thresholds/", "See thresholds"),
    ]
    t = "".join('<a class="sj-tile" href="%s%s"><b>%s</b><p>%s</p><span class="sj-link sj-link-go">%s</span></a>'
                % (SITE, u, esc(a), esc(b), esc(c)) for a, b, u, c in tiles)
    return (
        '<section class="sj-section %s"><div class="sj-wrap sj-stack-lg">'
        '<div class="sj-stack"><div class="sj-eyebrow">Related</div>'
        '<h2 class="sj-h2">%s</h2><p class="sj-measure">%s</p></div>'
        '<div class="sj-grid sj-grid-3">%s</div></div></section>'
    ) % (bg, heading_hl, esc(intro), t)


def final_band(series_label):
    msg = ("Hi SJ Academy, I'd like to book a free demo class.\nLevel: \nSubject: \nSession: %s\n"
           "Mode (in class or online): \n(Ref: %s)\nMy name is " % (series_label, PAGE_CODE))
    return (
        '<section class="sj-section sj-bg-yellow"><div class="sj-wrap sj-stack zt-final">'
        '<h2 class="sj-h2">Dates sorted. Now the marks.</h2>'
        '<p class="sj-measure">SJ Academy teaches Cambridge O Level and A Level in DHA Phase 7, Karachi, and live online. '
        'May/June 2027 classes are running, and every class except lab practicals starts with a free demo.</p>'
        '<div class="sj-row"><a class="sj-btn sj-btn-primary" href="%s" target="_blank" rel="noopener" data-loc="final_band">Book a free demo on WhatsApp</a></div>'
        '<p><a class="sj-link" href="%s" data-loc="final_band">or register for a class</a></p>'
        '<p class="sj-small"><a class="sj-link" href="%s/a-level-tuition-center-karachi/">A Level classes</a> &nbsp; '
        '<a class="sj-link" href="%s/o-level-tuition-center-karachi/">O Level classes</a></p>'
        '<p class="sj-small">SJ Academy is an independent tuition centre and is not affiliated with or endorsed by Cambridge.</p>'
        '</div></section>'
    ) % (wa(msg), POPUP, SITE, SITE)


def bar_html(sid):
    return (
        '<div class="sj-bar" data-zt-for="%s" data-part="bar">'
        '<button class="sj-btn sj-btn-primary" type="button" data-zt-for="%s" data-part="bar-ical" data-event="resource_download" data-loc="bar">Add to calendar</button>'
        '<a class="sj-btn sj-btn-wa" href="#" target="_blank" rel="noopener" data-zt-for="%s" data-part="bar-share" data-loc="bar">Send on WhatsApp</a>'
        '</div>' % (sid, sid, sid)
    )


# ---------------------------------------------------------------- page CSS and JS
PAGE_CSS = r"""
/* Page-only layout for the Zone 4 timetable. Every rule is scoped to this page. */
#sj.sj-p-zone-4-timetable .zt-dl{display:grid;gap:var(--sj-s3);margin:var(--sj-s4) 0 var(--sj-s5)}
#sj.sj-p-zone-4-timetable .zt-dl dt{font-size:12px;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--sj-muted)}
#sj.sj-p-zone-4-timetable .zt-dl dd{margin:2px 0 0;font-size:16px;color:var(--sj-ink)}
#sj.sj-p-zone-4-timetable .zt-two{display:grid;gap:var(--sj-s6);grid-template-columns:minmax(0,1fr);align-items:start}
#sj.sj-p-zone-4-timetable .zt-final{text-align:center;display:grid;justify-items:center}
#sj.sj-p-zone-4-timetable .zt-meta{display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;justify-content:space-between}
#sj.sj-p-zone-4-timetable .zt-count{font-size:14px;color:var(--sj-muted)}
#sj.sj-p-zone-4-timetable .zt-codes{display:grid;gap:0 24px;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));margin:var(--sj-s3) 0}
#sj.sj-p-zone-4-timetable .zt-codes li,#sj.sj-p-zone-4-timetable .zt-codebtn{display:flex;justify-content:space-between;gap:12px;width:100%;padding:10px 0;border-top:1px solid var(--sj-line);color:var(--sj-ink);font-size:15px}
#sj.sj-p-zone-4-timetable .zt-codes li:has(.zt-codebtn){padding:0}
#sj.sj-p-zone-4-timetable .zt-codebtn{min-height:var(--sj-tap);align-items:center;text-align:left}
#sj.sj-p-zone-4-timetable .zt-codes b{font-weight:400}
#sj.sj-p-zone-4-timetable .zt-codes span{font-variant-numeric:tabular-nums;color:var(--sj-muted)}
@media (hover:hover){#sj.sj-p-zone-4-timetable .zt-codebtn:hover{background:var(--sj-yellow-light)}}
#sj.sj-p-zone-4-timetable .zt-table{table-layout:auto}
#sj.sj-p-zone-4-timetable .zt-dr th{padding:10px 16px;border-top:1.5px solid var(--sj-ink);border-bottom:0;background:var(--sj-yellow-light);font-size:15px;font-weight:500;letter-spacing:0;text-transform:none;color:var(--sj-ink);white-space:normal}
#sj.sj-p-zone-4-timetable .zt-dr th span{font-weight:400;color:var(--sj-muted)}
#sj.sj-p-zone-4-timetable .zt-d:first-of-type .zt-dr th{border-top:0}
#sj.sj-p-zone-4-timetable .zt-r td{padding:8px 16px;vertical-align:middle}
#sj.sj-p-zone-4-timetable .zt-r.is-on td{background:var(--sj-yellow-light)}
#sj.sj-p-zone-4-timetable .zt-r.is-past td{color:var(--sj-muted)}
#sj.sj-p-zone-4-timetable .zt-pk{width:56px;padding:0!important}
#sj.sj-p-zone-4-timetable .zt-lab{display:grid;place-items:center;min-width:56px;min-height:var(--sj-tap);cursor:pointer}
#sj.sj-p-zone-4-timetable .zt-lab input{width:22px;height:22px;margin:0;accent-color:var(--sj-ink);cursor:pointer}
#sj.sj-p-zone-4-timetable .zt-sb b{font-weight:500}
#sj.sj-p-zone-4-timetable .zt-mt{display:block;font-size:14px;color:var(--sj-muted)}
#sj.sj-p-zone-4-timetable .zt-ses{display:inline-block;min-width:44px;padding:2px 8px;border:1.5px solid var(--sj-ink);border-radius:var(--sj-r-sm);background:#fff;font-size:13px;font-weight:500;text-align:center;color:var(--sj-ink)}
#sj.sj-p-zone-4-timetable .zt-PM{background:var(--sj-kraft)}
#sj.sj-p-zone-4-timetable .zt-EV{background:var(--sj-ink);color:var(--sj-yellow)}
#sj.sj-p-zone-4-timetable .zt-ml li{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:2px 12px;align-items:center;padding:8px 0;border-top:1px solid var(--sj-line)}
#sj.sj-p-zone-4-timetable .zt-ml{margin:var(--sj-s3) 0}
#sj.sj-p-zone-4-timetable .zt-ml .zt-w{grid-column:2;font-size:14px;color:var(--sj-muted)}
#sj.sj-p-zone-4-timetable .zt-x{display:grid;place-items:center;width:var(--sj-tap);height:var(--sj-tap);font-size:22px;line-height:1;color:var(--sj-ink)}
#sj.sj-p-zone-4-timetable .zt-mine>*+*{margin-top:var(--sj-s3)}
#sj.sj-p-zone-4-timetable .zt-mine{margin-bottom:var(--sj-s5)}
#sj.sj-p-zone-4-timetable .zt-clash{padding:8px 12px;background:var(--sj-yellow-light);border-radius:var(--sj-r-sm);color:var(--sj-ink)}
#sj.sj-p-zone-4-timetable [id^="zt-"]{scroll-margin-top:110px}
@media (max-width:899px){
#sj.sj-p-zone-4-timetable .zt-table thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
#sj.sj-p-zone-4-timetable .zt-table,#sj.sj-p-zone-4-timetable .zt-table tbody,#sj.sj-p-zone-4-timetable .zt-table tr,#sj.sj-p-zone-4-timetable .zt-table th,#sj.sj-p-zone-4-timetable .zt-table td{display:block;width:100%}
#sj.sj-p-zone-4-timetable .zt-table tr.zt-r{display:grid;grid-template-columns:56px minmax(0,1fr) auto;align-items:center;padding-right:12px;border-top:1px solid var(--sj-line)}
#sj.sj-p-zone-4-timetable .zt-table .zt-r td{padding:6px 0;border:0}
#sj.sj-p-zone-4-timetable .zt-table tr.zt-r.is-on{background:var(--sj-yellow-light)}
#sj.sj-p-zone-4-timetable .zt-table td.zt-cd,#sj.sj-p-zone-4-timetable .zt-table td.zt-lv,#sj.sj-p-zone-4-timetable .zt-table td.zt-du{display:none}
#sj.sj-p-zone-4-timetable .zt-table td.zt-pk{width:auto;padding:0}
}
@media (min-width:900px){
#sj.sj-p-zone-4-timetable .zt-two{grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:var(--sj-s7)}
#sj.sj-p-zone-4-timetable .zt-mt{display:none}
}
@media print{
#sj.sj-p-zone-4-timetable.zt-print-mine .sj-section{display:none}
#sj.sj-p-zone-4-timetable.zt-print-mine .sj-section.zt-keep{display:block}
#sj.sj-p-zone-4-timetable.zt-print-mine .zt-keep .sj-wrap>*:not(.zt-mine){display:none}
}
"""

STD_JS = r"""(function(){
  var root=document.getElementById('sj');
  if(!root){return;}
  var each=function(list,fn){Array.prototype.forEach.call(list,fn);};

  /* Tabs: role="tablist" > role="tab" aria-controls="panel-id" */
  each(root.querySelectorAll('[role="tablist"]'),function(list){
    var tabs=Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    var pick=function(tab,focus){
      tabs.forEach(function(t){
        var on=t===tab;
        t.setAttribute('aria-selected',on?'true':'false');
        t.tabIndex=on?0:-1;
        var panel=document.getElementById(t.getAttribute('aria-controls'));
        if(panel){panel.hidden=!on;}
      });
      if(focus){tab.focus();}
    };
    tabs.forEach(function(tab,i){
      tab.addEventListener('click',function(){pick(tab,false);});
      tab.addEventListener('keydown',function(e){
        var step=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;
        if(!step){return;}
        e.preventDefault();
        pick(tabs[(i+step+tabs.length)%tabs.length],true);
      });
    });
  });

  /* Phone bottom bar: shows once the element marked data-sj-hero has scrolled away */
  var bar=root.querySelector('.sj-bar');
  var hero=root.querySelector('[data-sj-hero]');
  if(bar&&hero&&'IntersectionObserver' in window){
    root.classList.add('sj-has-bar');
    new IntersectionObserver(function(entries){
      bar.classList.toggle('is-on',!entries[0].isIntersecting);
    }).observe(hero);
  }

  /* Video: loads the player only after a tap */
  each(root.querySelectorAll('.sj-video[data-src]'),function(v){
    v.addEventListener('click',function(e){
      e.preventDefault();
      var f=document.createElement('iframe');
      f.src=v.getAttribute('data-src');
      f.title=v.getAttribute('data-title')||'Video';
      f.allow='autoplay; encrypted-media; picture-in-picture';
      f.allowFullscreen=true;
      f.style.cssText='position:absolute;inset:0;width:100%;height:100%;border:0';
      v.innerHTML='';
      v.appendChild(f);
    });
  });

  /* Measurement: one event name per action, location read from data-loc */
  var send=function(name,loc){
    var g=window['gt'+'ag'];
    if(typeof g==='function'){g('event',name,{link_location:loc||'unknown',page_family:root.getAttribute('data-family')||''});}
  };
  root.addEventListener('click',function(e){
    var a=e.target.closest?e.target.closest('a,button'):null;
    if(!a){return;}
    var href=a.getAttribute('href')||'';
    var loc=a.getAttribute('data-loc');
    if(href.indexOf('wa.me')>-1){send('whatsapp_click',loc);}
    else if(href.indexOf('popup%3Aopen')>-1){send('register_open',loc);}
    else if(a.hasAttribute('download')){send('resource_download',loc);}
    else if(a.hasAttribute('data-event')){send(a.getAttribute('data-event'),loc);}
  });
})();"""

PAGE_JS = r"""(function(){
  'use strict';
  var root=document.getElementById('sj');
  if(!root||root.className.indexOf('sj-p-zone-4-timetable')<0){return;}
  var DAYS=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  var MON=['January','February','March','April','May','June','July','August','September','October','November','December'];
  var LV={IG:['IGCSE','IGCSE'],OL:['O Level','O Level'],AS:['AS Level','AS'],AL:['A Level (A2)','A2']};
  var LVO={IG:0,OL:1,AS:2,AL:3},SO={AM:0,PM:1,EV:2};
  function pad(n){return (n<10?'0':'')+n;}
  var now=new Date();
  var TODAY=now.getFullYear()+'-'+pad(now.getMonth()+1)+'-'+pad(now.getDate());
  function utc(iso){var p=iso.split('-');return Date.UTC(+p[0],+p[1]-1,+p[2]);}
  function longDay(iso){var d=new Date(utc(iso));return DAYS[d.getUTCDay()]+' '+d.getUTCDate()+' '+MON[d.getUTCMonth()]+' '+d.getUTCFullYear();}
  function shortDay(iso){var d=new Date(utc(iso));return DAYS[d.getUTCDay()].slice(0,3)+' '+d.getUTCDate()+' '+MON[d.getUTCMonth()].slice(0,3);}
  function until(iso){var n=Math.round((utc(iso)-utc(TODAY))/864e5);return n<0?'done':n===0?'today':n===1?'tomorrow':'in '+n+' days';}
  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
  function part(id,name){return root.querySelector('[data-zt-for="'+id+'"][data-part="'+name+'"]');}
  var mem={};
  function load(k){try{var v=window.localStorage.getItem(k);return v?JSON.parse(v):[];}catch(e){return mem[k]||[];}}
  function save(k,v){try{window.localStorage.setItem(k,JSON.stringify(v));}catch(e){mem[k]=v;}}

  function rowHTML(r){
    var lv=LV[r[2]][1],n=esc(r[5]),du=esc(r[4]);
    return '<tr class="zt-r" data-l="'+r[2]+'" data-s="'+r[1]+'" data-c="'+r[3]+'"><td class="zt-pk"><label class="zt-lab"><input type="checkbox" value="'+r[3]+'" aria-label="Add '+n+' '+r[3]+', '+longDay(r[0])+'"></label></td><td class="zt-sb"><b>'+n+'</b><small class="zt-mt">'+r[3]+' &middot; '+lv+' &middot; '+du+'</small></td><td class="zt-cd sj-num">'+r[3]+'</td><td class="zt-lv">'+lv+'</td><td class="zt-du sj-num">'+du+'</td><td class="zt-se"><span class="zt-ses zt-'+r[1]+'">'+r[1]+'</span></td></tr>';
  }
  function bodyHTML(data){
    var by={},order=[];
    data.forEach(function(r){if(!by[r[0]]){by[r[0]]=[];order.push(r[0]);}by[r[0]].push(r);});
    order.sort();
    return order.map(function(d){
      by[d].sort(function(a,b){return SO[a[1]]-SO[b[1]]||LVO[a[2]]-LVO[b[2]]||a[5].toLowerCase().localeCompare(b[5].toLowerCase())||a[3].localeCompare(b[3]);});
      return '<tbody class="zt-d" data-d="'+d+'"><tr class="zt-dr"><th colspan="6" scope="colgroup">'+longDay(d)+'<span> &middot; '+by[d].length+' paper'+(by[d].length===1?'':'s')+'</span></th></tr>'+by[d].map(rowHTML).join('')+'</tbody>';
    }).join('');
  }

  function fold(line){var out=[],s=line;while(s.length>74){out.push(s.slice(0,74));s=' '+s.slice(74);}out.push(s);return out;}
  function tx(s){return String(s).replace(/\\/g,'\\\\').replace(/;/g,'\\;').replace(/,/g,'\\,').replace(/\n/g,'\\n');}
  function nextDay(iso){var d=new Date(utc(iso)+864e5);return d.getUTCFullYear()+pad(d.getUTCMonth()+1)+pad(d.getUTCDate());}
  function makeICS(list,label){
    var st=now.getUTCFullYear()+pad(now.getUTCMonth()+1)+pad(now.getUTCDate())+'T'+pad(now.getUTCHours())+pad(now.getUTCMinutes())+pad(now.getUTCSeconds())+'Z';
    var L=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//SJ Academy//Zone 4 timetable//EN','CALSCALE:GREGORIAN','METHOD:PUBLISH','X-WR-CALNAME:'+tx('CAIE '+label+' papers')];
    list.forEach(function(r){
      var d=r.d.replace(/-/g,'');
      var what=r.name+' '+r.c;
      L.push('BEGIN:VEVENT','UID:'+r.c.replace('/','-')+'-'+d+'@sjacademy.pk','DTSTAMP:'+st,'DTSTART;VALUE=DATE:'+d,'DTEND;VALUE=DATE:'+nextDay(r.d),
        'SUMMARY:'+tx(what+' ('+r.s+' session)'),
        'DESCRIPTION:'+tx('CAIE '+label+', '+LV[r.l][0]+', '+r.du+'. '+r.s+' session. Check your Statement of Entry for your start time. Dates from the Cambridge Zone 4 timetable, copied by SJ Academy (sjacademy.pk).'),
        'TRANSP:TRANSPARENT',
        'BEGIN:VALARM','TRIGGER:-P6DT15H','ACTION:DISPLAY','DESCRIPTION:'+tx('In a week: '+what),'END:VALARM',
        'BEGIN:VALARM','TRIGGER:-PT15H','ACTION:DISPLAY','DESCRIPTION:'+tx('Tomorrow: '+what+' ('+r.s+')'),'END:VALARM',
        'END:VEVENT');
    });
    L.push('END:VCALENDAR');
    var out=[];L.forEach(function(l){out=out.concat(fold(l));});
    return out.join('\r\n')+'\r\n';
  }
  function download(name,text){
    var blob=new Blob([text],{type:'text/calendar;charset=utf-8'});
    var url=URL.createObjectURL(blob);
    var a=document.createElement('a');a.href=url;a.download=name;a.style.display='none';
    document.body.appendChild(a);a.click();
    setTimeout(function(){document.body.removeChild(a);URL.revokeObjectURL(url);},800);
  }

  function init(box){
    var id=box.getAttribute('data-zt'),label=box.getAttribute('data-label')||'';
    var primary=box.getAttribute('data-primary')==='1';
    var table=part(id,'table'),search=part(id,'search'),count=part(id,'count'),empty=part(id,'empty'),wrap=part(id,'wrap');
    var clear=part(id,'clear'),clear2=part(id,'clear2'),addAll=part(id,'addall'),pastCb=part(id,'past'),pastWrap=part(id,'past-wrap'),levels=part(id,'levels');
    var mine=part(id,'mine'),mineList=part(id,'mine-list'),mineN=part(id,'mine-n'),clash=part(id,'mine-clash');
    var ical=part(id,'ical'),share=part(id,'share'),prt=part(id,'print'),wipe=part(id,'wipe');
    var bar=part(id,'bar'),barIcal=part(id,'bar-ical'),barShare=part(id,'bar-share');
    if(!table||!search){return;}

    if(box.getAttribute('data-render')==='js'){
      var skel=part(id,'skel'),src=document.querySelector('script[data-zt-data="'+id+'"]'),data=null;
      try{data=JSON.parse(src.textContent);}catch(e){}
      if(skel){skel.hidden=true;}
      if(!data){var f=part(id,'fail');if(f){f.hidden=false;}if(wrap){wrap.hidden=true;}return;}
      table.insertAdjacentHTML('beforeend',bodyHTML(data));
    }

    var groups=[],rows=[],map={};
    Array.prototype.forEach.call(table.querySelectorAll('tbody.zt-d'),function(tb){
      var g={tb:tb,rows:[]};groups.push(g);
      var d=tb.getAttribute('data-d');
      Array.prototype.forEach.call(tb.querySelectorAll('tr.zt-r'),function(tr){
        var l=tr.getAttribute('data-l'),c=tr.getAttribute('data-c');
        var r={tr:tr,tb:tb,d:d,s:tr.getAttribute('data-s'),l:l,c:c,name:tr.querySelector('b').textContent,du:tr.querySelector('.zt-du').textContent,cb:tr.querySelector('input'),
          blob:(tr.textContent+' '+longDay(d)+' '+LV[l][0]+' '+LV[l][1]).toLowerCase()};
        rows.push(r);g.rows.push(r);map[c]=r;
        tr.classList.toggle('is-past',d<TODAY);
      });
    });
    var anyPast=rows.some(function(r){return r.d<TODAY;});
    var anyFuture=rows.some(function(r){return r.d>=TODAY;});
    if(pastWrap&&anyPast){pastWrap.hidden=false;}
    if(pastCb&&anyPast&&anyFuture&&box.getAttribute('data-hidepast')==='1'){pastCb.checked=true;}

    function level(){var c=levels&&levels.querySelector('input:checked');return c?c.value:'';}
    function tokens(){return search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);}
    function apply(){
      var t=tokens(),lv=level(),hp=!!(pastCb&&pastCb.checked),shown=0;
      rows.forEach(function(r){
        var ok=(!lv||r.l===lv)&&(!hp||r.d>=TODAY)&&t.every(function(x){return r.blob.indexOf(x)>-1;});
        r.tr.hidden=!ok;if(ok){shown++;}
      });
      groups.forEach(function(g){g.tb.hidden=!g.rows.some(function(r){return !r.tr.hidden;});});
      var filtered=!!(t.length||lv||hp);
      count.textContent=filtered?'Showing '+shown+' of '+rows.length+' papers':rows.length+' papers';
      empty.hidden=shown>0;if(wrap){wrap.hidden=shown===0;}
      if(clear){clear.hidden=!filtered;}
      if(addAll){addAll.hidden=!(shown>0&&shown<=40&&(t.length||lv));}
    }
    function reset(){
      search.value='';if(pastCb){pastCb.checked=false;}
      var all=levels&&levels.querySelector('input[value=""]');if(all){all.checked=true;}
      apply();
    }

    var key='sjzt:'+id;
    var picks=load(key).filter(function(c){return map[c];});
    if(primary){
      var m=/[#&]p=([^&]+)/.exec(window.location.hash||'');
      if(m){
        var fromHash=decodeURIComponent(m[1]).split(',').filter(function(c){return map[c];});
        if(fromHash.length){picks=fromHash;}
      }
    }
    function selected(){
      return picks.map(function(c){return map[c];}).sort(function(a,b){return a.d<b.d?-1:a.d>b.d?1:SO[a.s]-SO[b.s]||(a.c<b.c?-1:1);});
    }
    function shareHref(sel){
      var lines=['My CAIE '+label+' papers (Zone 4):'];
      sel.slice(0,25).forEach(function(r){lines.push(shortDay(r.d)+', '+r.s+': '+r.name+' '+r.c);});
      if(sel.length>25){lines.push('and '+(sel.length-25)+' more');}
      lines.push('Find yours: '+window.location.origin+window.location.pathname+'#p='+encodeURIComponent(picks.join(',')));
      return 'https://wa.me/?text='+encodeURIComponent(lines.join('\n'));
    }
    function renderMine(){
      rows.forEach(function(r){var on=picks.indexOf(r.c)>-1;r.cb.checked=on;r.tr.classList.toggle('is-on',on);});
      if(!mine){return;}
      var sel=selected();
      mine.hidden=sel.length===0;
      if(bar){bar.classList.toggle('is-on',sel.length>0&&!mineVisible);root.classList.toggle('sj-has-bar',sel.length>0);}
      if(!sel.length){return;}
      mineN.textContent=sel.length;
      var seen={},dupe=false;
      sel.forEach(function(r){var k=r.d+r.s;if(seen[k]){dupe=true;}seen[k]=1;});
      clash.hidden=!dupe;
      mineList.innerHTML=sel.map(function(r){
        return '<li><span class="zt-ses zt-'+r.s+'">'+r.s+'</span><span><b>'+esc(r.name)+'</b> '+r.c+'<br><span class="zt-w">'+shortDay(r.d)+' &middot; '+until(r.d)+'</span></span><button type="button" class="zt-x" data-rm="'+r.c+'" aria-label="Remove '+esc(r.name)+' '+r.c+'">&times;</button></li>';
      }).join('');
      var h=shareHref(sel);
      if(share){share.setAttribute('href',h);}
      if(barShare){barShare.setAttribute('href',h);}
    }
    var mineVisible=false;
    if(mine&&bar&&'IntersectionObserver' in window){
      new IntersectionObserver(function(en){mineVisible=en[0].isIntersecting;bar.classList.toggle('is-on',picks.length>0&&!mineVisible);}).observe(mine);
    }
    function setPicks(next){picks=next;save(key,picks);renderMine();}
    function toggle(c,on){
      var i=picks.indexOf(c);
      if(on&&i<0){setPicks(picks.concat([c]));}
      else if(!on&&i>-1){setPicks(picks.filter(function(x){return x!==c;}));}
    }
    function downloadNow(){
      var sel=selected();if(!sel.length){return;}
      download('caie-zone-4-'+id+'-my-papers.ics',makeICS(sel,label));
    }

    search.addEventListener('input',apply);
    if(levels){levels.addEventListener('change',apply);}
    if(pastCb){pastCb.addEventListener('change',apply);}
    if(clear){clear.addEventListener('click',reset);}
    if(clear2){clear2.addEventListener('click',reset);}
    if(addAll){addAll.addEventListener('click',function(){
      var add=rows.filter(function(r){return !r.tr.hidden&&picks.indexOf(r.c)<0;}).map(function(r){return r.c;});
      if(add.length){setPicks(picks.concat(add));}
    });}
    table.addEventListener('change',function(e){var t=e.target;if(t&&t.type==='checkbox'){toggle(t.value,t.checked);}});
    if(mineList){mineList.addEventListener('click',function(e){var b=e.target.closest?e.target.closest('[data-rm]'):null;if(b){toggle(b.getAttribute('data-rm'),false);}});}
    if(wipe){wipe.addEventListener('click',function(){setPicks([]);});}
    if(ical){ical.addEventListener('click',downloadNow);}
    if(barIcal){barIcal.addEventListener('click',downloadNow);}
    if(prt){prt.addEventListener('click',function(){
      root.classList.add('zt-print-mine');
      var done=function(){root.classList.remove('zt-print-mine');window.removeEventListener('afterprint',done);};
      window.addEventListener('afterprint',done);
      window.print();
    });}
    apply();renderMine();
    if(primary&&picks.length&&/[#&]p=/.test(window.location.hash||'')&&mine){
      setTimeout(function(){try{mine.scrollIntoView({behavior:'smooth',block:'start'});}catch(e){}},150);
    }
    box.zt={search:search,apply:apply};
  }

  Array.prototype.forEach.call(root.querySelectorAll('[data-zt]'),init);

  /* Syllabus code buttons: fill the search box of the main timetable */
  Array.prototype.forEach.call(root.querySelectorAll('[data-zt-code]'),function(b){
    b.addEventListener('click',function(){
      var box=root.querySelector('[data-zt][data-primary="1"]');if(!box||!box.zt){return;}
      var s=box.zt.search;s.value=b.getAttribute('data-zt-code');box.zt.apply();
      try{s.scrollIntoView({behavior:'smooth',block:'center'});}catch(e){}
      s.focus({preventScroll:true});
    });
  });
})();"""


# ---------------------------------------------------------------- pages
def build(args):
    state = args.state
    checked = args.checked
    built = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    alert_on = not args.no_alert

    arch_rows = arch_sum = None
    if args.archive:
        arch_rows, notes_a = load_csv(args.archive)
        arch_sum = summarise(arch_rows)
        for n in notes_a:
            print("note (archive): " + n)

    cur_rows = cur_sum = None
    if state == "live":
        if not args.current:
            sys.exit("--state live needs --current data.csv")
        cur_rows, notes_c = load_csv(args.current)
        cur_sum = summarise(cur_rows)
        for n in notes_c:
            print("note (current): " + n)

    arch_running = bool(arch_sum) and arch_sum["last"] >= built
    series = args.series
    series_id = args.series_id
    arch_label = args.archive_label
    arch_id = args.archive_id

    # ---- titles and descriptions
    both = arch_running and arch_label
    if state == "waiting":
        if both:
            seo_title = "Zone 4 Timetable %s & %s | SJ Academy" % (arch_label, series)
            seo_meta = ("Cambridge Zone 4 date sheet: %s timetable with all %d papers, searchable by subject or code. "
                        "%s not out yet: get a WhatsApp alert." % (arch_label, arch_sum["n"], series))
        else:
            seo_title = "CAIE Zone 4 Timetable %s: Date Sheet | SJ Academy" % series
            seo_meta = ("CAIE date sheet for %s (Zone 4 timetable): not published yet. Get an alert on WhatsApp "
                        "and search the %s dates meanwhile." % (series, arch_label))
    else:
        if both:
            seo_title = "Zone 4 Timetable %s & %s | SJ Academy" % (series, arch_label)
            seo_meta = ("Cambridge Zone 4 date sheet for %s (%d papers) and %s. Search by subject or code, "
                        "tick yours and save them to your calendar." % (series, cur_sum["n"], arch_label))
        else:
            seo_title = "CAIE Zone 4 Timetable %s: Date Sheet | SJ Academy" % series
            seo_meta = ("CAIE %s date sheet, Zone 4: all %d papers. Search by subject or code, "
                        "tick yours and save them to your calendar." % (series, cur_sum["n"]))
    seo_title_len, seo_meta_len = len(seo_title), len(seo_meta)

    # ---- FAQ
    zone_q = "Is Pakistan in Zone 4?"
    zone_a = ("Cambridge publishes one timetable for each administrative zone, and centres in Pakistan are in Zone 4. "
              "Papers can fall on different dates in different zones, so check your centre's zone with your exams officer "
              "before you trust any date sheet, including this one.")
    sessions_q = "What do AM, PM and EV mean?"
    sessions_a = ("They are Cambridge's three exam sessions: morning, afternoon and evening. Your centre sets the start time under "
                  "Cambridge's [key time rules](%s), so ask your exams officer for the exact time. Every candidate in a session must "
                  "be under full centre supervision at the key time." % KEYTIME_URL)
    private_q = "Can private candidates use this timetable?"
    private_a = ("Yes. Private candidates sit the same papers on the same dates as everyone else in their zone. You must be entered "
                 "through a centre first, and your Statement of Entry confirms your venue. See our "
                 "[private candidate registration page](%s/caie-private-candidate-registration/)." % SITE)
    if state == "waiting":
        faq = [
            ("When will the May/June 2027 date sheet be released?",
             "Cambridge publishes the final June series timetable in October of the year before, so October 2026 for May/June 2027. "
             "[Cambridge's 2026 calendar](%s) lists it under October. As of %s it is not published yet, and this page is updated "
             "as soon as it is." % (CAL_URL, checked)),
            ("Where do I find the official Cambridge timetable?",
             "Cambridge International Education, which students also write as CAIE or CIE, posts each zone's timetable as a PDF on the [Cambridge International website](%s). "
             "Exams officers also receive it through Cambridge Direct. Private candidates should check with the centre they entered through."
             % CAMBRIDGE_URL),
            (zone_q, zone_a),
            (sessions_q, sessions_a),
            ("What is the difference between the provisional and final timetable?",
             "The provisional timetable goes to exams officers in May, and centres have four weeks to comment on it. The final one follows "
             "in October. Cambridge marks changes from the provisional version in red on the final timetable. "
             "See [when Cambridge releases timetables](%s)." % HELP_URL),
            ("Will the timetable change after it is published?",
             "Sometimes. Cambridge can reissue a timetable: the June 2026 Zone 2 timetable, for example, carries a Version 2 dated "
             "January 2026. We note the version on this page and update it when a new one appears."),
            ("Are AS and A2 papers on the same timetable?",
             "Yes. Cambridge lists IGCSE, O Level, AS Level and A Level papers together for each zone. A2 papers are labelled "
             "A Level (AL) in Cambridge's timetable."),
            (private_q, private_a),
        ]
    else:
        n, first, last = cur_sum["n"], cur_sum["first"], cur_sum["last"]
        ver = args.version
        faq = [
            ("When do the %s exams start and finish?" % series,
             "In Zone 4, papers run from %s to %s. That is %d papers across %d exam days." % (long_day(first), long_day(last), n, cur_sum["days"])),
            ("How do I find my paper dates?",
             "Type your subject name or syllabus code, such as 9609, into the search box and tick each paper you sit. Your list sorts "
             "by date, flags papers that share a session, and saves to your calendar as one file."),
            ("What does a code like 9609/12 mean?",
             "The four digits before the slash are the syllabus, so 9609 is A Level Business. The first digit after the slash is the "
             "paper number and the second is the variant, so 9609/12 is Paper 1, variant 2."),
            (sessions_q, sessions_a),
            ("What if two of my papers are in the same session?",
             "Tell your exams officer as soon as you see it, so your centre can arrange it under Cambridge's rules. "
             "Your list on this page flags every pair that shares a session."),
            ("Is this the official timetable?",
             "The dates are copied from Cambridge's Zone 4 final timetable (%s) and checked against the PDF on %s. Cambridge can reissue a "
             "timetable, so check the official PDF on the [Cambridge International website](%s) before you plan anything final."
             % (ver, checked, CAMBRIDGE_URL)),
            (zone_q, zone_a),
            (private_q, private_a),
        ]
    if state == "waiting" and arch_running:
        faq.insert(0, ("What are the %s exam dates in Zone 4?" % arch_label,
                       "Papers run from %s to %s: %d papers across %d exam days. Search the timetable on this page by subject name or code."
                       % (long_day(arch_sum["first"]), long_day(arch_sum["last"]), arch_sum["n"], arch_sum["days"])))
    faq_items_html, faq_ld = faq_html(faq)

    # ---- hero and sections
    def onnow_section(bg, rows_n, a_first, a_last):
        if arch_running:
            eyebrow = "On now"
            intro = ("Cambridge&rsquo;s Zone 4 final timetable for the %s series: %d papers from %s to %s. Search it, tick your "
                     "remaining papers and save them to your calendar." % (esc(arch_label), rows_n, day_month(a_first), day_month_year(a_last)))
        else:
            eyebrow = "Series finished"
            intro = ("This series ended on %s. The full Zone 4 timetable stays here for reference: %d papers from %s to %s."
                     % (day_month_year(a_last), rows_n, day_month(a_first), day_month_year(a_last)))
        return (
            '<section class="sj-section %s zt-keep" id="on-now"><div class="sj-wrap sj-stack-lg">'
            '<div class="sj-stack"><div class="sj-eyebrow">%s</div>'
            '<h2 class="sj-h2">%s <span class="sj-hl">date sheet</span> for Zone 4</h2>'
            '<p class="sj-measure">%s</p></div>'
            '<div class="zt" data-zt="%s" data-label="%s" data-render="js" data-primary="1" data-hidepast="1">%s%s%s'
            '<p class="sj-caption">AM, PM and EV are Cambridge sessions. Start times follow your centre&rsquo;s <a class="sj-link" href="%s" target="_blank" rel="noopener">key time</a>. '
            'Source: Cambridge International, Zone 4 final timetable, %s series.</p></div>'
            '</div></section>'
        ) % (bg, eyebrow, esc(arch_label), intro, arch_id, esc(arch_label), filter_card(arch_id, hint=True), mine_panel(arch_id),
             results_block(arch_id, "", True, "Cambridge Zone 4 timetable, %s, by date" % arch_label), KEYTIME_URL, esc(arch_label))

    if state == "waiting":
        alert_msg = ("Hi SJ Academy, please message me when the %s date sheet is out.\nLevel: \nSubjects: \n(Ref: %s-ALERT)\nMy name is "
                     % (series, PAGE_CODE))
        alert_btn = ('<a class="sj-btn sj-btn-primary sj-btn-block" href="%s" target="_blank" rel="noopener" data-loc="status_card">Alert me on WhatsApp</a>'
                     '<p class="sj-help">We send one message when the timetable is out.</p>' % wa(alert_msg)) if alert_on else ""
        if arch_running:
            h1 = ('<span class="sj-pill"><span>Cambridge date sheet</span></span>Zone 4 timetable: <span class="sj-hl">%s</span> and %s'
                  % (esc(arch_label), esc(series)))
            lead = ("The %s date sheet is below, searchable by subject or code. The %s timetable is not out yet: Cambridge publishes it in October, "
                    "and every paper will appear on this page." % (esc(arch_label), esc(series)))
            oct_row = ('<div><dt>%s</dt><dd>On now: %d papers, %s to %s</dd>'
                       '<p><a class="sj-link sj-link-go" href="#on-now" data-loc="status_card">Open the %s timetable</a></p></div>'
                       % (esc(arch_label), arch_sum["n"], day_month(arch_sum["first"]), day_month(arch_sum["last"]), esc(arch_label)))
        else:
            h1 = ('<span class="sj-pill"><span>CAIE date sheet %s</span></span>Not out yet. Your <span class="sj-hl">exam dates</span> will appear here.'
                  % esc(series))
            lead = ("Cambridge publishes the Zone 4 final timetable for the June series in October. When it goes up, every paper appears here, "
                    "searchable by subject name or code.")
            oct_row = ('<div><dt>%s</dt><dd>Finished on %s</dd>'
                       '<p><a class="sj-link sj-link-go" href="#on-now" data-loc="status_card">See the %s timetable</a></p></div>'
                       % (esc(arch_label), day_month_year(arch_sum["last"]), esc(arch_label)))
        hero = (
            '<section class="sj-section sj-bg-dots"><div class="sj-wrap sj-grid sj-grid-hero">'
            '<div class="sj-stack">%s'
            '<h1 class="sj-h1">%s</h1>'
            '<p class="sj-lead sj-measure">%s</p>'
            '<div class="sj-row"><span class="sj-chip sj-chip-yellow">Free</span><span class="sj-chip">Zone 4</span><span class="sj-updated">Updated %s</span></div>'
            '<p><span class="sj-hand sj-tilt-l">bookmark this page</span></p>'
            '</div>'
            '<div class="sj-offset sj-tagged"><span class="sj-tag">status</span>'
            '<p class="sj-eyebrow">Zone 4 final timetable</p>'
            '<dl class="zt-dl">%s'
            '<div><dt>%s</dt><dd>Not published yet. Cambridge publishes it in <span class="sj-circled">%s<b>October</b></span> 2026.</dd></div>'
            '<div><dt>Last checked</dt><dd>%s</dd></div></dl>%s</div>'
            '</div></section>'
        ) % (crumbs(), h1, lead, checked, oct_row, esc(series), CIRCLE, checked, alert_btn)

        how = (
            '<section class="sj-section sj-bg-canvas"><div class="sj-wrap zt-two">'
            '<div class="sj-stack"><div class="sj-eyebrow">How it works</div>'
            '<h2 class="sj-h2">Find your papers in <span class="sj-hl">four steps</span></h2>'
            '<ol class="sj-steps">'
            '<li><b>Search your subject</b><span>Type a name or a code such as 9609. Filter by IGCSE, O Level, AS or A2.</span></li>'
            '<li><b>Tick your papers</b><span>Add every paper you sit. Two papers in one session get flagged.</span></li>'
            '<li><b>Save it to your calendar</b><span>One file puts every paper on its date, with a reminder the day before.</span></li>'
            '<li><b>Send it or print it</b><span>Share your list on WhatsApp, or print it for the wall.</span></li>'
            '</ol></div>'
            '<div class="sj-stack"><div class="sj-sticky"><span class="sj-hand">check your zone</span>'
            '<p>Cambridge publishes one timetable per zone. Centres in Pakistan are in Zone 4. Not sure about yours? Ask your exams officer first.</p></div>'
            '<p class="sj-measure">When the %s timetable is out, it works exactly like the %s timetable.</p></div>'
            '</div></section>'
        ) % (esc(series), esc(arch_label))

        on_now = onnow_section("sj-bg-white", arch_sum["n"], arch_sum["first"], arch_sum["last"])
        body = (hero + on_now + how + codes_section(False, "sj-bg-white")
                + related_section("sj-bg-canvas", 'While you wait, <span class="sj-hl">keep revising</span>',
                                  "Past papers, the 2027 timeline and registration help, all in one place.")
                + '<section class="sj-section sj-bg-white"><div class="sj-wrap sj-stack-lg"><div class="sj-stack"><div class="sj-eyebrow">FAQ</div>'
                  '<h2 class="sj-h2">Questions about the <span class="sj-hl">date sheet</span></h2></div>'
                  '<div class="sj-faq">%s</div></div></section>' % faq_items_html
                + final_band(series))
        json_blob = ('<script type="application/json" data-zt-data="%s">%s</script>'
                     % (arch_id, json.dumps([[r["date"].isoformat(), r["session"], r["level"], r["code"], r["duration"], r["subject"]]
                                              for r in arch_rows], separators=(",", ":"), ensure_ascii=True)))
        bar_for = arch_id
        status_word = "WAITING"
    else:
        n, first, last = cur_sum["n"], cur_sum["first"], cur_sum["last"]
        hero = (
            '<section class="sj-section sj-bg-dots"><div class="sj-wrap sj-grid sj-grid-hero">'
            '<div class="sj-stack">%s'
            '<h1 class="sj-h1"><span class="sj-pill"><span>Final timetable</span></span>Zone 4 timetable <span class="sj-hl">%s</span>: find your papers</h1>'
            '<p class="sj-lead sj-measure">The Zone 4 final timetable for %s: %d papers from %s to %s. Search by subject or code, tick what you sit and save it to your calendar.</p>'
            '<div class="sj-row"><span class="sj-chip sj-chip-yellow">Final timetable</span><span class="sj-chip">%s</span><span class="sj-updated">Checked %s</span></div>'
            '<p><span class="sj-hand sj-tilt-l">tick once, save for good</span></p>%s'
            '</div>%s</div></section>'
        ) % (crumbs(), esc(series), series, n, day_month(first), day_month_year(last), esc(args.version), checked,
             ('<p><a class="sj-link sj-link-go" href="#on-now">Sitting %s papers? Jump to that timetable</a></p>' % esc(arch_label)) if (arch_rows and arch_running) else "",
             filter_card(series_id))
        results = (
            '<section class="sj-section sj-bg-white zt-keep" id="timetable"><div class="sj-wrap sj-stack">'
            '<div class="zt" data-zt="%s" data-label="%s" data-primary="1">%s'
            '<div class="sj-stack"><div class="sj-eyebrow">The timetable</div>'
            '<h2 class="sj-h2">Every paper, <span class="sj-hl">day by day</span></h2></div>%s'
            '<p class="sj-caption">AM, PM and EV are Cambridge sessions. Start times follow your centre&rsquo;s <a class="sj-link" href="%s" target="_blank" rel="noopener">key time</a>. '
            'Source: Cambridge International, Zone 4 final timetable, %s. Checked against the PDF on %s.</p></div>'
            '</div></section>'
        ) % (series_id, esc(series), mine_panel(series_id), results_block(series_id, tbody_html(cur_rows), False),
             KEYTIME_URL, esc(args.version), checked)
        # the mine panel must come before the heading in print; keep it as a direct child of the wrap
        results = results.replace('<div class="zt" data-zt="%s" data-label="%s" data-primary="1">' % (series_id, esc(series)),
                                  '<div class="zt" data-zt="%s" data-label="%s" data-primary="1" style="display:contents">' % (series_id, esc(series)))
        archive = ""
        json_blob = ""
        if arch_rows:
            if arch_running:
                archive = onnow_section("sj-bg-canvas", arch_sum["n"], arch_sum["first"], arch_sum["last"])
            else:
                a_first, a_last = arch_sum["first"], arch_sum["last"]
                archive = (
                    '<section class="sj-section sj-bg-canvas" id="on-now"><div class="sj-wrap sj-stack">'
                    '<details class="zt-arch"><summary class="sj-link">Looking for the %s timetable? Open it</summary>'
                    '<div class="sj-stack" style="margin-top:16px"><p class="sj-measure">The %s Zone 4 timetable ran from %s to %s, with %d papers.</p>'
                    '<div class="zt" data-zt="%s" data-label="%s" data-render="js" data-hidepast="1">%s%s%s</div></div></details>'
                    '</div></section>'
                ) % (esc(arch_label), esc(arch_label), day_month(a_first), day_month_year(a_last), arch_sum["n"],
                     arch_id, esc(arch_label), filter_card(arch_id, hint=False), mine_panel(arch_id),
                     results_block(arch_id, "", True, "Cambridge Zone 4 timetable, %s, by date" % arch_label))
            json_blob = ('<script type="application/json" data-zt-data="%s">%s</script>'
                         % (arch_id, json.dumps([[r["date"].isoformat(), r["session"], r["level"], r["code"], r["duration"], r["subject"]]
                                                  for r in arch_rows], separators=(",", ":"), ensure_ascii=True)))
        how = (
            '<section class="sj-section sj-bg-canvas"><div class="sj-wrap zt-two">'
            '<div class="sj-stack"><div class="sj-eyebrow">How to use it</div>'
            '<h2 class="sj-h2">Four steps, <span class="sj-hl">one calendar</span></h2>'
            '<ol class="sj-steps">'
            '<li><b>Search your subject</b><span>Type a name or a code such as 9609. Filter by IGCSE, O Level, AS or A2.</span></li>'
            '<li><b>Tick your papers</b><span>Add every paper you sit, or use Add all shown for one subject.</span></li>'
            '<li><b>Check for clashes</b><span>Two papers in one session get flagged, so you can tell your exams officer early.</span></li>'
            '<li><b>Save and share</b><span>Download one calendar file, send the list on WhatsApp, or print it.</span></li>'
            '</ol></div>'
            '<div class="sj-stack"><div class="sj-sticky"><span class="sj-hand">check your zone</span>'
            '<p>Cambridge publishes one timetable per zone. Centres in Pakistan are in Zone 4. Not sure about yours? Ask your exams officer first.</p></div></div>'
            '</div></section>'
        )
        body = (hero + results + how + codes_section(True, "sj-bg-white") + archive
                + related_section("sj-bg-canvas", 'Next up, <span class="sj-hl">past papers</span>',
                                  "Practise on real papers now that you know your dates.")
                + '<section class="sj-section sj-bg-white"><div class="sj-wrap sj-stack-lg"><div class="sj-stack"><div class="sj-eyebrow">FAQ</div>'
                  '<h2 class="sj-h2">Questions about the <span class="sj-hl">date sheet</span></h2></div>'
                  '<div class="sj-faq">%s</div></div></section>' % faq_items_html
                + final_band(series))
        bar_for = series_id
        status_word = "LIVE"

    # ---- structured data
    crumb_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Free CAIE resources", "item": SITE + "/free-caie-resources/"},
        {"@type": "ListItem", "position": 3, "name": "CAIE Zone 4 timetable", "item": PAGE_URL}]}
    faq_ld_full = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_ld}

    comment = (
        "<!-- SJ Academy CAIE Zone 4 timetable, Elementor HTML widget. Version 2.0, built %s.\n"
        "     Page: /caie-zone-4-timetable/ (address unchanged). Family: Resource, on the dotted surface.\n"
        "     State of this build: %s for %s.\n"
        "     Needs the shared stylesheet sj-brand.css 3.1.1 in Additional CSS.\n"
        "     Build: Elementor Full Width, Hide Title = Yes. One HTML widget in a full-width section, zero padding, no entrance animation.\n"
        "     This replaces the old widget in full (old CSS, old script, old data list).\n"
        "     Set in Yoast: Title  %s\n"
        "                   Meta   %s\n"
        "                   Social title: same as the title.\n"
        "     WhatsApp page code: %s (alert message uses %s-ALERT).\n"
        "     Rebuild with build-zone4-timetable.py. The timetable is written into the HTML so search engines read it.\n"
        "     The page script block is the standard sj-page-script.js, copied unchanged, followed by the timetable script.\n"
        "     This file is plain ASCII. -->\n"
    ) % (built.isoformat(), status_word, series, seo_title, seo_meta, PAGE_CODE, PAGE_CODE)

    fonts = (
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media=\'all\'">\n'
        '<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>\n'
    )

    out = (
        comment + fonts + "\n"
        + '<div id="sj" class="sj-p-zone-4-timetable" data-family="resource">\n'
        + body + "\n" + bar_html(bar_for) + "\n</div>\n\n"
        + "<style>" + PAGE_CSS + "</style>\n\n"
        + json_blob + "\n"
        + "<script>\n" + STD_JS + "\n</script>\n"
        + "<script>\n" + PAGE_JS + "\n</script>\n"
        + '<script type="application/ld+json">' + json.dumps(faq_ld_full, ensure_ascii=True) + "</script>\n"
        + '<script type="application/ld+json">' + json.dumps(crumb_ld, ensure_ascii=True) + "</script>\n"
    )
    bad = [c for c in out if ord(c) > 127]
    if bad:
        sys.exit("Output has non-ASCII characters: %r" % bad[:10])
    for word in ("\u2014", "gtag"):
        if word in out:
            sys.exit("Output contains forbidden text: %r" % word)

    with open(args.out, "w", encoding="ascii", newline="\n") as fh:
        fh.write(out)

    print("\nBuilt %s (%d bytes, %s state)" % (args.out, len(out.encode("ascii")), state))
    print("SEO title (%d chars): %s" % (seo_title_len, seo_title))
    print("Meta (%d chars):       %s" % (seo_meta_len, seo_meta))
    if seo_title_len > 60:
        print("WARNING: title is over 60 characters")
    if not 120 <= seo_meta_len <= 160:
        print("WARNING: meta description should be about 140 to 155 characters")
    for label, s in (("archive", arch_sum), ("current", cur_sum)):
        if s:
            lv = ", ".join("%s %d" % (k, v) for k, v in s["by_level"].items())
            print("%s: %d papers, %s to %s, %d exam days (%s)" % (label, s["n"], s["first"], s["last"], s["days"], lv))
            if s["n"] < 150:
                print("WARNING: %s has only %d papers. A Zone 4 series normally has more than 200. Check the CSV is complete." % (label, s["n"]))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--state", choices=["waiting", "live"], required=True)
    p.add_argument("--current", help="CSV for the series on this page (live state)")
    p.add_argument("--series", default="May/June 2027", help="series name shown on the page")
    p.add_argument("--series-id", default="mj27", help="short id, used for saved lists")
    p.add_argument("--version", default="Version 1, October 2026", help="version line printed on Cambridge's PDF")
    p.add_argument("--archive", help="CSV for the series that is still running (shown as its own tool)")
    p.add_argument("--archive-label", default="Oct/Nov 2026")
    p.add_argument("--archive-id", default="on26")
    p.add_argument("--checked", default=None, help='date you last checked Cambridge, for example "28 October 2026"')
    p.add_argument("--today", default=None, help="override today (YYYY-MM-DD), for testing")
    p.add_argument("--no-alert", action="store_true", help="leave out the WhatsApp alert button (waiting state)")
    p.add_argument("--out", required=True)
    args = p.parse_args()
    if not args.checked:
        t = dt.date.today()
        args.checked = day_month_year(t)
    build(args)


if __name__ == "__main__":
    main()
