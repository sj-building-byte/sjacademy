#!/usr/bin/env python3
"""Builds the Elementor widget for /a-level-subject-combinations-tool/ (plain ASCII).
Run: python3 build.py [out.html]. Needs node. Reads ROUTES and SUBJ from source.html, so the tool and the
crawlable 'by degree' sections come from one data set. Faq html and FAQ JSON-LD come from one list too."""
import html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "a-level-subject-combinations-tool-elementor-widget.html")
src = open(os.path.join(HERE, "source.html"), encoding="utf-8").read()
std = ("<script>\n/* Standard page script, copied unchanged from 02 Website/Scripts/sj-page-script.js */\n"
       + open(os.path.join(HERE, "..", "sj-page-script.js"), encoding="utf-8").read().strip() + "\n</script>")

META = ("Free A Level subjects combination tool for Pakistan. Get three ranked picks for medicine, engineering, business, "
        "law and more, with IBCC rules.")
assert 140 <= len(META) <= 155, len(META)

# ---- data from the page script ----
def grab(name):
    m = re.search(r"var %s=(.*?);\n" % name, src, re.S)
    return m.group(1)
js = "var SUBJ=%s;var ROUTES=%s;console.log(JSON.stringify({s:SUBJ,r:ROUTES}))" % (grab("SUBJ"), grab("ROUTES"))
data = json.loads(subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True).stdout)
SUBJ = data["s"]; ROUTES = {r["id"]: r for r in data["r"]}
SUBJ["psychology"] = SUBJ.get("psychology", "Psychology")

def a(s):  # ascii-safe html text
    return s.encode("ascii", "xmlcharrefreplace").decode("ascii")

def join(items, word="and"):
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " " + word + " " + items[-1]

def subjects_line(r):
    core = [SUBJ[k] for k in r["core"]]
    ch = r.get("choose")
    if ch:
        opts = join([SUBJ[k] for k in ch["from"]], "or")
        num = {1: "one", 2: "two", 3: "three"}[ch["n"]]
        extra = ("any %s of %s" if not core else "%s of %s")
        extra = ("any three of " + opts) if not core else ("plus %s of %s" % (num if ch["n"] > 1 else "one", opts))
        return (join(core) + " " + extra) if core else extra[0].upper() + extra[1:]
    return join(core)

GOALS = [
    ("medicine", "medicine", "Medicine and dentistry in Pakistan need the full science set. Abroad, Biology and Chemistry are the core.", ["med_pk", "med_abroad"]),
    ("engineering", "engineering", "Mathematics and Physics sit at the centre of every engineering route. Chemistry matters for IBCC equivalence.", ["eng_pk", "eng_abroad"]),
    ("computer science", "computer science", "Mathematics comes first. Physics or Computer Science completes the combination IBCC accepts.", ["cs_ics", "data_ai"]),
    ("business and finance", "business and finance", "Business routes are flexible. Finance and actuarial routes lean on Mathematics.", ["finance", "business", "econ_policy"]),
    ("law", "law", "Law programmes rarely fix A Level subjects. Essay subjects build the skills they test.", ["law"]),
    ("architecture and design", "architecture and design", "Art and Design anchors the portfolio. Mathematics or Physics helps for architecture.", ["arch", "design"]),
]
cards = []
for gid, label, intro, ids in GOALS:
    rs = []
    for i in ids:
        r = ROUTES[i]
        rs.append('<div class="sj-stack"><h4 class="sj-h4">%s</h4><p class="sj-small"><b>Subjects:</b> %s.</p>'
                  '<p class="sj-small"><b>Degrees:</b> %s.</p><p class="sj-small sj-muted"><b>Equivalence:</b> %s</p></div>'
                  % (r["title"], subjects_line(r), r["degrees"], r["ibcc"]))
    cards.append('<article class="sj-card sjc-goal"><div class="sj-stack"><h3 class="sj-h3">A Level subject combination for %s</h3><p class="sj-small sj-measure">%s</p></div>%s</article>'
                 % (label, intro, "".join(rs)))
GOALS_HTML = ('''  <!-- 3b. BY DEGREE (written into the HTML from the same data as the tool, so search engines and readers see it without JavaScript) -->
  <section class="sj-section sj-bg-canvas" id="sjc-goals">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-stack">
        <div class="sj-eyebrow">By degree</div>
        <h2 class="sj-h2">A Level subject combinations for <span class="sj-hl">every degree</span></h2>
        <p class="sj-measure">The tool above ranks these routes for you. Here they are in full, for medicine, engineering, computer science, business and finance, law, and architecture and design.</p>
      </div>
      <div class="sj-grid sj-grid-2">%s</div>
    </div>
  </section>''' % "".join(cards))

# ---- subjects list ----
LIST = [
    ("Mathematics", "9709", "Engineering, computer science, finance, architecture"),
    ("Further Mathematics", "9231", "Engineering and mathematics at top universities"),
    ("Physics", "9702", "Engineering, computer science, medicine in Pakistan"),
    ("Chemistry", "9701", "Medicine, engineering, biosciences"),
    ("Biology", "9700", "Medicine, biosciences, psychology"),
    ("Computer Science", "9618", "Computer science, data science, AI"),
    ("Economics", "9708", "Finance, economics, policy, business"),
    ("Business", "9609", "Business, management, marketing"),
    ("Accounting", "9706", "Accounting, finance, ACCA and CA routes"),
    ("English Language", "9093", "Law, media, humanities"),
    ("Literature in English", "9695", "Law, humanities, communication"),
    ("History", "9489", "Law, international relations, humanities"),
    ("Sociology", "9699", "Social sciences, policy, law"),
    ("Psychology", "9990", "Psychology, health sciences, neuroscience"),
    ("Law", "9084", "Law and legal studies"),
    ("Geography", "9696", "Architecture, planning, environmental studies"),
    ("Art and Design", "9479", "Architecture, design, media"),
    ("Urdu", "9686", "A second language option for any route"),
]
rows = "".join('<tr><td data-label="Subject">%s</td><td data-label="Code" class="sj-num">%s</td><td data-label="Often chosen for">%s</td></tr>' % (n, c, f) for n, c, f in LIST)
LIST_HTML = ('''  <!-- 3c. SUBJECTS LIST -->
  <section class="sj-section sj-bg-white" id="sjc-list">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-stack">
        <div class="sj-eyebrow">Subjects list</div>
        <h2 class="sj-h2">A Level subjects list for <span class="sj-hl">Pakistan</span></h2>
        <p class="sj-measure">Cambridge International AS and A Level has more than 50 subjects. These are the ones Pakistani students choose most, with their syllabus codes. Cambridge sets no compulsory subjects, so the subjects you need depend on your degree.</p>
      </div>
      <div class="sj-table-wrap">
        <table class="sj-table sj-table-stack">
          <caption class="sj-vh">Cambridge A Level subjects and syllabus codes</caption>
          <thead><tr><th scope="col">Subject</th><th scope="col" class="sj-num">Syllabus code</th><th scope="col">Often chosen for</th></tr></thead>
          <tbody>%s</tbody>
        </table>
      </div>
      <p class="sj-small sj-muted sj-measure">Codes are Cambridge syllabus numbers. Check the current syllabus and the subjects your school or centre offers before you decide.</p>
    </div>
  </section>''' % rows)

# ---- FAQ (one list feeds the page and the JSON-LD) ----
FAQ = [
    ("What is the best A Level subject combination?",
     "There is no single best combination. It depends on the degree you want. Physics, Chemistry and Biology suit medicine in Pakistan. Mathematics, Physics and Chemistry suit engineering. Mathematics with Economics suits finance. Pick the degree first, then the subjects it asks for."),
    ("How many A Level subjects should I take?",
     "Cambridge says students typically take four subjects at AS and three at A Level. IBCC equivalence is built on three A Level subjects, so three is the usual load. Take a fourth only if a degree you want asks for it."),
    ("Are any A Level subjects compulsory?",
     "No. Cambridge does not make any A Level subject compulsory. Your degree, university and IBCC equivalence decide which subjects you need. IBCC fixes the subjects for the science groups, and Humanities accepts any three."),
    ("Which A Level subject combination do I need for medicine in Pakistan?",
     "For IBCC Pre-Medical equivalence you need Physics, Chemistry and Biology at A Level, plus SSC Science with Biology. Biology and Chemistry without Physics suits medicine abroad, but it does not earn Pre-Medical equivalence in Pakistan."),
    ("Which A Levels do I need for engineering?",
     "Mathematics, Physics and Chemistry give you IBCC Pre-Engineering equivalence. Many UK engineering courses ask for Mathematics and Physics, and some prefer Further Mathematics. Check the course page for your target university."),
    ("Which A Level subjects do I need for computer science?",
     "Mathematics is the subject computer science courses most often ask for. IBCC accepts Physics, Computer Science and Mathematics for its Computer Science group. Check each course, because requirements differ by university."),
    ("Can I study business or law with science subjects?",
     "Often yes. Many business and law programmes do not fix A Level subjects, though finance and economics programmes usually prefer Mathematics. Check each programme before you decide."),
    ("Which A Level subjects are the easiest or the hardest?",
     "There is no official ranking, and difficulty depends on you. Choose subjects you can score well in and that your degree needs. Question 2 of the tool asks how you score best, so the ranking reflects your strengths."),
    ("How accurate are the results?",
     "The tool compares your answers with common degree routes and IBCC's equivalence rules. It is guidance, not an admissions rule. Confirm requirements with each university and with IBCC before you finalise your subjects."),
]
assert 5 <= len(FAQ) <= 9
faq_html = "\n".join('<details%s><summary>%s</summary><div class="sj-faq-a"><p>%s</p></div></details>'
                     % (" open" if i == 0 else "", a(html.escape(q)), a(html.escape(t, quote=False))) for i, (q, t) in enumerate(FAQ))
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": t}} for q, t in FAQ]}
FAQ_LD = '<script type="application/ld+json">%s</script>' % json.dumps(faq_ld, ensure_ascii=True)

out = (src.replace("@@META@@", META).replace("<!--SJ_GOALS-->", GOALS_HTML).replace("<!--SJ_LIST-->", LIST_HTML)
       .replace("<!--SJ_FAQ-->", faq_html).replace("<!--SJ_FAQ_LD-->", FAQ_LD).replace("<!--SJ_PAGE_SCRIPT-->", std))
assert "<!--SJ_" not in out and "@@" not in out
assert all(ord(c) < 128 for c in out), [c for c in out if ord(c) > 127][:5]
assert "—" not in out and "&mdash;" not in out
open(OUT, "w", encoding="utf-8").write(out)
print("built", len(out), "bytes; meta", len(META), "chars; faq", len(FAQ))
