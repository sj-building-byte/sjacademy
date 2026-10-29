#!/usr/bin/env python3
"""Builds the Elementor HTML widget for /ibcc-equivalence-calculator/ (plain ASCII output).
Run: python3 build.py [out.html]. Needs node (reads the A* tables from engine.js)."""
import html, json, os, re, subprocess, sys, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "ibcc-calculator-elementor-widget.html")
SITE = "https://www.sjacademy.pk"
URL = SITE + "/ibcc-equivalence-calculator/"
POPUP = "#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D"
UPDATED = "20 October 2026"
VERSION = "2.1"

engine = open(os.path.join(HERE, "engine.js")).read().replace("if (typeof module !== 'undefined') { module.exports = SJI; }", "").strip()
app = open(os.path.join(HERE, "app.js")).read().strip()
std = open(os.path.join(HERE, "sj-page-script.js")).read().strip()
data = json.loads(subprocess.run(["node", "-e", "const S=require('%s/engine.js');console.log(JSON.stringify({a:S.ASTAR,s:S.SUBJ}))" % HERE],
                                 capture_output=True, text=True, check=True).stdout)
AST = data["a"]


def a(s):
    return html.escape(s, quote=True).encode("ascii", "xmlcharrefreplace").decode("ascii")


def wa(ref, level=""):
    msg = "\n".join(["Hi SJ Academy, I used your IBCC calculator and I'd like a free demo class.", "Level: " + level, "Subject: ",
                     "Mode (in class or online): ", "(Ref: %s)" % ref, "My name is "])
    return "https://wa.me/923362144454?text=" + urllib.parse.quote(msg, safe="")


TICK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.2 4.2L19 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# ---------- A* tables (from the engine, which ref_check.py compares with IBCC's PDFs) ----------
TROWS = [("phy", "Physics"), ("chem", "Chemistry"), ("bio", "Biology"), ("cs", "Computer Science"), ("math", "Mathematics"),
         ("eng", "English"), ("urdu", "Urdu"), ("pst", "Pakistan Studies"), ("isl", "Islamiyat"), ("_", "Other subjects")]
A_NA = {"eng", "urdu", "pst", "isl"}
tabs, panels = [], []
for i, y in enumerate(["2026", "2025", "2024", "2023", "2022", "2021"]):
    o, al = AST["O"][y], AST["A"][y]
    body = "".join('<tr><td>%s</td><td class="sj-num">%s</td><td class="sj-num">%s</td></tr>' % (
        n, o.get(k, o["_"]), "&ndash;" if k in A_NA else al.get(k, al["_"])) for k, n in TROWS)
    tabs.append('<button type="button" role="tab" id="sji-t%s" aria-controls="sji-p%s" aria-selected="%s" tabindex="%s">%s</button>' % (
        y, y, "true" if i == 0 else "false", "0" if i == 0 else "-1", y))
    panels.append('<div role="tabpanel" id="sji-p%s" aria-labelledby="sji-t%s"%s><div class="sj-table-wrap"><table class="sj-table">'
                  '<caption class="sj-vh">IBCC A* marks, %s session</caption><thead><tr><th scope="col">Subject</th><th scope="col" class="sj-num">O Level</th>'
                  '<th scope="col" class="sj-num">A Level</th></tr></thead><tbody>%s</tbody></table></div></div>' % (y, y, "" if i == 0 else " hidden", y, body))
ASTAR_TABLES = '<div class="sj-tabs" role="tablist" aria-label="Exam session">%s</div><div class="sji-tabbox">%s</div>' % ("".join(tabs), "".join(panels))

# ---------- FAQ ----------
FAQ = [
    ("How does IBCC calculate O Level equivalence?", "sji-faq-o",
     "IBCC turns each grade into marks out of 100: A is 85, B 75, C 65, D 55 and E 45, and A* gets a subject value set for each exam session (93 or 94 in 2026). "
     "If you took O Levels in Pakistan, your 8 subjects (English, Maths, Urdu, Islamiyat, Pakistan Studies and 3 electives) give a total out of 800, which is scaled to 900. "
     "If you took them abroad, or you are a foreign or dual national, 5 subjects (English, Maths and 3 electives) give a total out of 500, also scaled to 900."),
    ("How does IBCC calculate A Level equivalence for FSc?", "sji-faq-a",
     "For most students your 8 O Levels and 3 A Levels are added together, giving marks out of 1100 with no scaling. If you are exempt from Urdu, Islamiyat and Pakistan Studies, "
     "5 O Levels and 3 A Levels give a total out of 800, which is scaled to 1100. For Pre-Medical, Pre-Engineering and Computer Science students who finish O Levels in 2026 or later, "
     "the February 2026 rule applies instead (see below)."),
    ("What is an A* worth in IBCC equivalence in 2026?", "sji-faq-astar",
     "For the 2026 session, an O Level A* is worth 93 in English and Urdu and 94 in every other subject. An A Level A* is worth 95 in Physics, 93 in Computer Science and 94 in "
     "Chemistry, Biology, Maths and other subjects. The values change every year, so the calculator uses the table for the session in which you sat each subject. "
     "Before 2021, A* counted as a flat 90."),
    ("Does the February 2026 IBCC rule apply to me?", "sji-faq-2026",
     "Only if you are in a science group (Pre-Medical, Pre-Engineering or Computer Science) and finish your O Levels in 2026 or later. For you, IBCC counts only the 5 compulsory O Levels "
     "plus your 3 A Levels, and your O Level electives no longer count towards the marks, though you still need to pass them. If your O Levels finished in 2025 or earlier, "
     "the old rule still applies and all 8 O Levels count. Humanities is not covered by the new rule. The calculator picks the right rule from the O Level years you enter."),
    ("Is O Level equivalence out of 900 or 1100?", "sji-faq-900",
     "We show it out of 900. IBCC's worked example gives 750 out of 800 as 844, which is 750 / 800 x 900. Its older example, Cambridge's guide for Pakistan and other calculators "
     "also use 900. IBCC's newest copy of that page, uploaded in April 2026, labels the formula 1100 but still shows 844, so we have kept 900 until IBCC corrects it. "
     "Your percentage is the same either way."),
    ("Who is exempt from Urdu, Islamiyat and Pakistan Studies?", "sji-faq-exempt",
     "Foreign nationals and dual nationals are exempt. For O Level (SSC) equivalence, so are students who took their O Levels abroad. For A Level (HSSC) equivalence, Pakistani students "
     "are exempt only if they took both their O Levels and A Levels abroad. If you took one in Pakistan and one abroad, you still need to pass all three."),
    ("Can I use IGCSE 9 to 1 grades?", "sji-faq-91",
     "Yes. IBCC converts 8 to 87, 7 to 82, 6 to 77, 5 to 70, 4 to 60, 3 to 50 and 2 to 40. Grade 9 is listed with A* as above 90, so the calculator uses the subject's A* value for it. "
     "Grade 1 is not accepted. In the calculator, open \"More options\" and tick the 9 to 1 box."),
    ("Which grades does IBCC not accept?", "sji-faq-fail",
     "IBCC only accepts grades A* to E (or 9 to 2). A U, or an F or G at IGCSE, does not count, and you need at least an E in every subject IBCC requires for your group."),
    ("What if I sat my subjects in different years?", "sji-faq-years",
     "IBCC works out each subject using the A* table for the session you sat it in, so the same grade can be worth slightly different marks. Open \"More options\" in the calculator, tick \"different years\" "
     "and set the year for each subject. The calculator handles every session from 2006 onwards, with 2027 and 2028 as forecasts until IBCC publishes them."),
    ("Is this my official IBCC equivalence?", "sji-faq-official",
     "No. This is an estimate using IBCC's published rules. Your official equivalence certificate comes from IBCC when you apply with your original results, "
     "and universities use that certificate. SJ Academy is not part of IBCC."),
]
faq_html = "\n".join('<details id="%s"><summary>%s</summary><div class="sj-faq-a"><p>%s</p></div></details>' % (i, a(q), a(ans)) for q, i, ans in FAQ)
ld_faq = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, i, ans in FAQ]}
ld_app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "IBCC Equivalence Calculator", "url": URL,
          "applicationCategory": "EducationalApplication", "operatingSystem": "Any", "isAccessibleForFree": True,
          "offers": {"@type": "Offer", "price": "0", "priceCurrency": "PKR"},
          "description": "Calculates O Level (SSC, Matric) and A Level (HSSC, FSc) equivalence marks using IBCC's published A* marks for 2021 to 2026 and the February 2026 rule.",
          "provider": {"@type": "EducationalOrganization", "name": "SJ Academy", "url": SITE + "/"}, "dateModified": "2026-10-20"}


def opt(name, value, title, sub):
    return ('<label class="sji-opt"><input type="radio" name="%s" value="%s"><span><b>%s</b><small>%s</small></span></label>'
            % (name, value, title, sub))


SOURCES = """Sources (checked 20 October 2026):
     IBCC grade conversion and A* tables 2021-2026: https://ibcc.edu.pk/conversion-for-equivalence/
     IBCC British system requirements: https://ibcc.edu.pk/equivalence-intro/british-system/
     IBCC E2 form (exemption for mixed Pakistan/abroad): https://ibcc.edu.pk/wp-content/uploads/2024/08/E2-British.pdf
     IBCC notification IBCC/EC-176/Imp-05/7-2/2026, 17 Feb 2026: https://ibcc.edu.pk/notification-for-calculation-of-a-level-equivalent-qualification-based-on-compulsory-subjects-of-o-level/
     IBCC O Level example (x900): https://ibcc.edu.pk/equivalence/Example-for-Calculating-O-Level-Marks-1.pdf (April 2026 copy labels 1100 with the same 844 result)
     IBCC A Level example: https://ibcc.edu.pk/equivalence/Example-for-Calculating-A-Levels-Marks-1.pdf
     IBCC FAQs: https://ibcc.edu.pk/faqs/equivalence-faqs/
     Cambridge Destination Pakistan brochure: https://www.cambridgeinternational.org/Images/505904-destination-pakistan-brochure.pdf
     Accuracy check: ref_check.py (120 A* values vs IBCC text, 5,000 random cases vs a separate Python version, 8 worked examples) - all pass."""

page = """<!-- SJ Academy IBCC Equivalence Calculator. Elementor HTML widget. Version __VERSION__, built __UPDATED__.
     Address stays /ibcc-equivalence-calculator/. Replaces the current calculator HTML widget completely (it has the H1).
     Family: Tool. Uses the shared stylesheet sj-brand.css 3.1.1 (already in Additional CSS). Plain ASCII on purpose.
     Yoast SEO title: IBCC Equivalence Calculator 2026 (O/A Level) | SJ Academy
     Yoast meta description: Work out your O Level (Matric) and A Level (FSc) IBCC equivalence with the official A* marks for every session and the February 2026 rule. Free and instant.
     GA4: fires calculation_complete (calc_level, calc_rule; no grades or marks) once per visit, plus whatsapp_click and register_open via the page script.
     __SOURCES__ -->
<style>
#sj.sj-p-ibcc .sji-sec{padding:28px 0}#sj.sj-p-ibcc .sji-sec:first-child{padding-bottom:8px}#sj.sj-p-ibcc .sji-head{margin-bottom:20px}
#sj.sj-p-ibcc .sji-grid{display:grid;gap:20px;align-items:start}
@media (min-width:960px){#sj.sj-p-ibcc .sji-grid{grid-template-columns:minmax(0,1fr) 360px}#sj.sj-p-ibcc .sji-aside{position:sticky;top:96px;max-height:calc(100vh - 112px);overflow:auto;padding:0 10px 10px 0}#sj.sj-p-ibcc .sji-bar{display:none!important}}
@media (max-width:959px){#sj.sj-p-ibcc .is-empty .sji-aside{display:none}}
#sj.sj-p-ibcc .sji-form{border:1.5px solid var(--sj-ink);border-radius:var(--sj-r-lg);background:#fff;padding:18px 16px;min-width:0}
#sj.sj-p-ibcc .sji-form{counter-reset:sji}
#sj.sj-p-ibcc .sji-q{border:0;margin:0 0 20px;padding:0;min-width:0}
#sj.sj-p-ibcc .sji-qt{display:flex;align-items:center;gap:10px;float:left;width:100%;margin:0 0 10px;padding:0;font-size:18px;line-height:1.3;font-weight:500;color:var(--sj-ink);counter-increment:sji}
#sj.sj-p-ibcc .sji-qt::before{content:counter(sji);flex:none;display:grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--sj-yellow);font-size:15px}
#sj.sj-p-ibcc .sji-q>.sji-qt+*{clear:both}
#sj.sj-p-ibcc .sji-seg{display:grid;grid-template-columns:1fr 1fr;gap:10px}
#sj.sj-p-ibcc .sji-seg label{position:relative;cursor:pointer;display:block}
#sj.sj-p-ibcc .sji-seg input{position:absolute;opacity:0;width:1px;height:1px}
#sj.sj-p-ibcc .sji-seg span{display:flex;flex-direction:column;justify-content:center;min-height:68px;height:100%;padding:10px 14px 10px 44px;border:1.5px solid var(--sj-ink);border-radius:var(--sj-r-md);background:#fff;line-height:1.3;color:var(--sj-ink);position:relative}
#sj.sj-p-ibcc .sji-seg span::before{content:"";position:absolute;left:14px;top:50%;width:18px;height:18px;margin-top:-9px;border:2px solid var(--sj-ink);border-radius:50%;background:#fff}
#sj.sj-p-ibcc .sji-seg b{font-weight:500}
#sj.sj-p-ibcc .sji-seg small{display:block;font-size:13px;color:var(--sj-muted)}
#sj.sj-p-ibcc .sji-seg input:checked+span{background:var(--sj-yellow-light);box-shadow:inset 5px 0 0 var(--sj-yellow),3px 3px 0 var(--sj-ink)}
#sj.sj-p-ibcc .sji-seg input:checked+span::before{background:radial-gradient(circle,var(--sj-ink) 0 4px,#fff 4.5px)}
#sj.sj-p-ibcc .sji-seg input:focus-visible+span{outline:3px solid var(--sj-ink);outline-offset:2px}
#sj.sj-p-ibcc .sji-seg-s{grid-template-columns:1fr}
@media (min-width:480px){#sj.sj-p-ibcc .sji-seg-s{grid-template-columns:1fr 1fr}}
#sj.sj-p-ibcc .sji-q .sj-help{margin-top:10px}#sj.sj-p-ibcc .sji-form>.sji-q:last-child{margin-bottom:0}
@media (max-width:959px){#sj.sj-p-ibcc .sji-grid:not(.is-empty){padding-bottom:64px}}
#sj.sj-p-ibcc .sji-set{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:0 0 20px}
#sj.sj-p-ibcc .sji-set .sj-field:only-child,#sj.sj-p-ibcc .sji-set .sj-field[hidden]+.sj-field{grid-column:auto}
#sj.sj-p-ibcc [data-block]{margin-top:4px}#sj.sj-p-ibcc .sji-sub{margin:14px 0 2px;font-size:13px;font-weight:500;letter-spacing:.06em;text-transform:uppercase;color:var(--sj-muted)}
#sj.sj-p-ibcc .sji-r{display:grid;grid-template-columns:minmax(0,1fr) 96px;gap:8px;align-items:center;padding:6px 0;border-top:1px solid var(--sj-line)}
#sj.sj-p-ibcc .sji-r.sji-r3{grid-template-columns:minmax(0,1fr) 86px 86px}
#sj.sj-p-ibcc .sji-r .sj-select{min-height:48px;padding:8px 30px 8px 12px;background-position:right 8px center}
#sj.sj-p-ibcc .sji-r .sji-g{font-weight:500}
#sj.sj-p-ibcc .sji-r.is-done .sji-g{background-color:var(--sj-yellow-light)}
#sj.sj-p-ibcc .sji-r.is-error{background:var(--sj-err-bg)}
#sj.sj-p-ibcc .sji-name{font-weight:500;color:var(--sj-ink)}
#sj.sj-p-ibcc .sji-more{margin-top:16px;border-top:1px solid var(--sj-line);padding-top:4px}
#sj.sj-p-ibcc .sji-more summary,#sj.sj-p-ibcc .sji-work summary{display:flex;align-items:center;min-height:44px;font-weight:500;cursor:pointer;color:var(--sj-ink)}
#sj.sj-p-ibcc .sji-more summary::after,#sj.sj-p-ibcc .sji-work summary::after{content:"+";margin-left:8px;color:var(--sj-cta)}#sj.sj-p-ibcc .sji-more[open] summary::after,#sj.sj-p-ibcc .sji-work[open] summary::after{content:"\\2212"}
#sj.sj-p-ibcc .sji-card{border:1.5px solid var(--sj-ink);border-radius:var(--sj-r-lg);background:#fff;padding:20px 18px;box-shadow:var(--sj-sh-offset);scroll-margin-top:96px}
#sj.sj-p-ibcc .sji-big{margin:4px 0;font-size:52px;line-height:1.05;font-weight:500;color:var(--sj-ink)}#sj.sj-p-ibcc .sji-big span{font-size:22px;color:var(--sj-muted)}#sj.sj-p-ibcc .sji-dim{color:var(--sj-line)}
#sj.sj-p-ibcc .sji-prog{height:8px;margin:12px 0 0;border-radius:8px;background:var(--sj-line);overflow:hidden}#sj.sj-p-ibcc .sji-prog i{display:block;height:100%;background:var(--sj-orange)}
#sj.sj-p-ibcc .sji-also,#sj.sj-p-ibcc .sji-warn{margin-top:10px}#sj.sj-p-ibcc .sji-warn{font-size:14px;color:var(--sj-pen-text)}
#sj.sj-p-ibcc .sji-work{margin-top:8px}#sj.sj-p-ibcc .sji-off td{color:var(--sj-muted)}
#sj.sj-p-ibcc .sji-notes{margin:10px 0 0;padding:0 0 0 18px;font-size:14px}#sj.sj-p-ibcc .sji-notes li+li{margin-top:6px}
#sj.sj-p-ibcc .sji-tip{margin-top:14px;padding:16px;border-radius:var(--sj-r-md);background:var(--sj-yellow-light);border:1.5px solid var(--sj-ink)}#sj.sj-p-ibcc .sji-tip>*+*{margin-top:10px}
#sj.sj-p-ibcc .sji-acts{margin-top:12px;color:var(--sj-muted)}#sj.sj-p-ibcc .sji-lnk{border:0;background:none;padding:8px 0;font:inherit;color:var(--sj-ink);text-decoration:underline;cursor:pointer}
#sj.sj-p-ibcc .sji-bar{position:fixed;left:0;right:0;bottom:0;z-index:var(--sj-z-bar);display:flex;justify-content:space-between;gap:10px;width:100%;min-height:56px;padding:10px 16px calc(10px + env(safe-area-inset-bottom,0px));border:0;border-top:1.5px solid var(--sj-ink);background:var(--sj-yellow);color:var(--sj-ink);font:inherit;font-size:15px;text-align:left;cursor:pointer}#sj.sj-p-ibcc .sji-bar b{font-weight:500;white-space:nowrap}#sj.sj-p-ibcc .sji-bar.is-ready{background:var(--sj-cta);color:#fff;border-top-color:var(--sj-ink)}
#sj.sj-p-ibcc .sji-tabbox .sj-table td:first-child{font-weight:500;color:var(--sj-ink)}
</style>

<div id="sj" class="sj-p-ibcc" data-family="tool">

  <!-- 1. CALCULATOR -->
  <div class="sji-sec"><div class="sj-wrap">
    <div class="sj-stack sji-head">
      <div class="sj-pill"><span>Free tool &middot; Updated __UPDATED__</span></div>
      <h1 class="sj-h1">IBCC Equivalence <span class="sj-hl">Calculator 2026</span></h1>
      <p class="sj-lead sj-measure">Enter your grades and see your Matric (SSC) or FSc (HSSC) marks straight away. It uses IBCC&rsquo;s official 2026 rules.</p>
    </div>

    <div class="sji-grid" data-sji>
      <div class="sji-form">
        <noscript><div class="sj-alert"><b>Turn on JavaScript</b><p>The calculator needs JavaScript. The rules and A* tables are below.</p></div></noscript>
        <fieldset class="sji-q" data-flow><legend class="sji-qt">What do you want to calculate?</legend>
          <div class="sji-seg">
            <label><input type="radio" name="sji-target" value="ssc"><span><b>O Level</b><small>Get my Matric (SSC) marks</small></span></label>
            <label><input type="radio" name="sji-target" value="hssc"><span><b>A Level</b><small>Get my FSc (HSSC) marks</small></span></label>
          </div>
          <p class="sj-help" data-start>Tap one to start. It takes about a minute, and your grades stay on your device.</p>
        </fieldset>

        <div data-setup hidden>
          <fieldset class="sji-q" data-flow><legend class="sji-qt">Where did you take your exams?</legend>
            <div class="sji-seg">
              <label><input type="radio" name="sji-route" value="pk"><span><b>In Pakistan</b></span></label>
              <label><input type="radio" name="sji-route" value="abroad"><span><b>Abroad</b><small>or foreign national</small></span></label>
            </div>
            <p class="sj-help" data-hssc>&ldquo;Abroad&rdquo; means both your O and A Levels. If only one was abroad, choose Pakistan.</p>
          </fieldset>

          <fieldset class="sji-q" data-flow data-hssc><legend class="sji-qt">Which FSc group?</legend>
            <div class="sji-seg sji-seg-s">
              <label><input type="radio" name="sji-group" value="pm"><span><b>Pre-Medical</b><small>Physics, Chemistry, Biology</small></span></label>
              <label><input type="radio" name="sji-group" value="pe"><span><b>Pre-Engineering</b><small>Physics, Chemistry, Maths</small></span></label>
              <label><input type="radio" name="sji-group" value="cs"><span><b>Computer Science</b><small>Physics, Maths, Computer Science</small></span></label>
              <label><input type="radio" name="sji-group" value="hum"><span><b>Humanities</b><small>Any 3 A Level subjects</small></span></label>
            </div>
          </fieldset>

          <div class="sji-set" data-flow>
            <div class="sj-field"><label class="sj-label" for="sji-oy">O Level year</label>__OY__</div>
            <div class="sj-field" data-hssc><label class="sj-label" for="sji-ay">A Level year</label>__AY__</div>
          </div>

          <div data-block="O" data-flow hidden><p class="sji-qt" id="sji-oh">Your O Level grades</p><p class="sj-help" data-count="O"></p><div data-rows="O" role="group" aria-labelledby="sji-oh"></div></div>
          <div data-block="A" data-flow hidden><p class="sji-qt" id="sji-ah">Your A Level grades</p><p class="sj-help" data-count="A"></p><div data-rows="A" role="group" aria-labelledby="sji-ah"></div></div>

          <details class="sji-more"><summary>Different years, 9 to 1 grades or Ethics?</summary>
            <label class="sj-check"><input type="checkbox" id="sji-multi"><span>My subjects are from different years</span></label>
            <label class="sj-check"><input type="checkbox" id="sji-nums"><span>My O Level grades are numbers (9 to 1)</span></label>
            <label class="sj-check" data-eth><input type="checkbox" id="sji-eth"><span>I took Ethics instead of Islamiyat</span></label>
          </details>
        </div>
      </div>

      <aside class="sji-aside" aria-label="Your result">
        <div class="sji-card" data-result tabindex="-1"></div>
        <p class="sj-caption" style="margin-top:12px">An estimate from IBCC&rsquo;s published rules. Your official equivalence comes from IBCC. SJ Academy is not part of IBCC.</p>
        <p class="sj-vh" aria-live="polite" data-live></p>
      </aside>
      <button type="button" class="sji-bar" data-bar hidden></button>
    </div>
  </div></div>

  <!-- 2. HOW IT WORKS -->
  <div class="sji-sec"><div class="sj-wrap"><div class="sj-prose">
    <h2>How IBCC works out your equivalence</h2>
    <p>IBCC (the Inter Boards Coordination Commission) converts Cambridge and Edexcel grades into Pakistani board marks so you can apply to universities and colleges in Pakistan. There are three steps.</p>
    <h3>1. Each grade becomes marks out of 100</h3>
    <div class="sj-grid sj-grid-2">
      <div class="sj-table-wrap"><table class="sj-table"><caption class="sj-vh">IBCC marks for letter grades</caption><thead><tr><th scope="col">Letter grade</th><th scope="col" class="sj-num">Marks</th></tr></thead><tbody>
        <tr><td>A*</td><td class="sj-num">90+ (table below)</td></tr><tr><td>A</td><td class="sj-num">85</td></tr><tr><td>B</td><td class="sj-num">75</td></tr>
        <tr><td>C</td><td class="sj-num">65</td></tr><tr><td>D</td><td class="sj-num">55</td></tr><tr><td>E</td><td class="sj-num">45</td></tr><tr><td>U, F, G</td><td class="sj-num">Not accepted</td></tr></tbody></table></div>
      <div class="sj-table-wrap"><table class="sj-table"><caption class="sj-vh">IBCC marks for IGCSE 9 to 1 grades</caption><thead><tr><th scope="col">IGCSE grade</th><th scope="col" class="sj-num">Marks</th></tr></thead><tbody>
        <tr><td>9</td><td class="sj-num">Same as A*</td></tr><tr><td>8</td><td class="sj-num">87</td></tr><tr><td>7</td><td class="sj-num">82</td></tr><tr><td>6</td><td class="sj-num">77</td></tr>
        <tr><td>5</td><td class="sj-num">70</td></tr><tr><td>4</td><td class="sj-num">60</td></tr><tr><td>3</td><td class="sj-num">50</td></tr><tr><td>2</td><td class="sj-num">40</td></tr><tr><td>1</td><td class="sj-num">Not accepted</td></tr></tbody></table></div>
    </div>
    <h3>2. A* depends on the subject and the year</h3>
    <p>Since 2021, IBCC publishes a separate A* value for each subject and exam session. Before 2021, A* counted as 90. Here are the official values:</p>
    __ASTAR__
    <h3>3. The right subjects are added up</h3>
    <ul>
      <li><b>O Level (Matric, SSC), taken in Pakistan:</b> English, Maths, Urdu, Islamiyat, Pakistan Studies and 3 electives. The total out of 800 is scaled to 900. Physics, Chemistry and Biology or Computer Science put you in the Science group.</li>
      <li><b>O Level, taken abroad or foreign/dual national:</b> English, Maths and 3 electives. The total out of 500 is scaled to 900.</li>
      <li><b>A Level (FSc, HSSC):</b> your 8 O Levels plus 3 A Levels for your group, out of 1100. Pre-Medical needs Physics, Chemistry and Biology; Pre-Engineering needs Physics, Chemistry and Maths; Computer Science needs Physics, Maths and Computer Science; Humanities takes any 3 subjects.</li>
      <li><b>A Level, exempt students:</b> 5 O Levels plus 3 A Levels, out of 800, scaled to 1100.</li>
      <li><b>The February 2026 rule:</b> for science-group students who finish O Levels in 2026 or later, only the 5 compulsory O Levels and the 3 A Levels count (English, Maths and the A Levels if you are exempt). Your O Level electives still need a pass.</li>
    </ul>
    <div class="sj-answer"><p><b>Worked example from IBCC:</b> eight O Level A*s from 2021 add up to 750 out of 800. 750 / 800 &times; 900 = 843.75, so the SSC equivalence is 844 out of 900 (93.78%). Add three A Level A*s (93, 93 and 94) and the HSSC equivalence is 1030 out of 1100 (93.64%).</p></div>
  </div></div></div>

  <!-- 3. CLASS OFFER -->
  <div class="sji-sec"><div class="sj-wrap">
    <div class="sj-bg-brown sj-stack" style="border-radius:var(--sj-r-lg);padding:28px 20px">
      <div class="sj-eyebrow">For O and A Level students</div>
      <h2 class="sj-h2">Want a better number? <span class="sj-hl">Raise the grades behind it.</span></h2>
      <p class="sj-measure">SJ Academy is a Cambridge O Level and A Level tuition academy. Join in person at DHA Phase 7, Karachi, or live online from anywhere in Pakistan. 4,500+ students taught so far.</p>
      <ul class="sj-ticks sj-measure">
        <li>__TICK__<span>Past-paper practice marked to the mark scheme</span></li>
        <li>__TICK__<span>Feedback on the marks you lost</span></li>
        <li>__TICK__<span>Teachers from LUMS, IBA and ex-KGS</span></li>
        <li>__TICK__<span>226+ five-star Google reviews</span></li>
        <li>__TICK__<span>Your first class is free</span></li>
      </ul>
      <div class="sj-row"><a class="sj-btn sj-btn-primary" href="__WA_END__" target="_blank" rel="noopener" data-loc="offer_end">Book a free demo class on WhatsApp</a></div>
      <p>or <a class="sj-link" href="__POPUP__" data-loc="offer_end">register for a class</a></p>
      <p class="sj-small"><a class="sj-link" href="__SITE__/a-level-grade-strategy-tool/">A Level grade strategy tool</a> &middot; <a class="sj-link" href="__SITE__/o-level-grade-thresholds/">O Level grade thresholds</a> &middot; <a class="sj-link" href="__SITE__/classes-schedule/">Class timetable</a> &middot; <a class="sj-link" href="__SITE__/fee-structure/">Fees</a></p>
    </div>
  </div></div>

  <!-- 4. FAQ -->
  <div class="sji-sec"><div class="sj-wrap sj-stack-lg">
    <div><div class="sj-eyebrow">FAQ</div><h2 class="sj-h2">IBCC equivalence <span class="sj-hl">questions</span></h2></div>
    <div class="sj-faq">
__FAQ__
    </div>
  </div></div>

  <!-- 5. SOURCES -->
  <div class="sji-sec"><div class="sj-wrap"><div class="sj-prose">
    <h2 class="sj-h3">Sources and how we checked</h2>
    <p class="sj-small">Every A* value above is taken from IBCC&rsquo;s own tables and checked by a script against IBCC&rsquo;s documents. The calculator also reproduces IBCC&rsquo;s and Cambridge&rsquo;s worked examples exactly. Last checked __UPDATED__.</p>
    <ul class="sj-small">
      <li><a class="sj-link" href="https://ibcc.edu.pk/conversion-for-equivalence/" rel="noopener" target="_blank">IBCC: grade conversion and yearly A* tables</a></li>
      <li><a class="sj-link" href="https://ibcc.edu.pk/equivalence-intro/british-system/" rel="noopener" target="_blank">IBCC: O Level and A Level requirements</a></li>
      <li><a class="sj-link" href="https://ibcc.edu.pk/notification-for-calculation-of-a-level-equivalent-qualification-based-on-compulsory-subjects-of-o-level/" rel="noopener" target="_blank">IBCC: February 2026 notification on compulsory subjects</a></li>
      <li><a class="sj-link" href="https://ibcc.edu.pk/equivalence/Example-for-Calculating-A-Levels-Marks-1.pdf" rel="noopener" target="_blank">IBCC: worked A Level example</a></li>
      <li><a class="sj-link" href="https://ibcc.edu.pk/faqs/equivalence-faqs/" rel="noopener" target="_blank">IBCC: equivalence FAQs</a></li>
    </ul>
  </div></div></div>
</div>

<script>
__ENGINE__
__APP__
</script>
<script>
__STD__
</script>

<script type="application/ld+json">__LD_APP__</script>
<script type="application/ld+json">__LD_FAQ__</script>
"""

OPT_TARGET = (opt("sji-target", "ssc", "O Level &rarr; Matric (SSC)", "O Level equivalence, out of 900") +
              opt("sji-target", "hssc", "A Level &rarr; FSc / Inter (HSSC)", "O and A Levels together, out of 1100"))
OPT_ROUTE_SSC = (opt("sji-route-ssc", "pk", "In Pakistan", "8 subjects, including Urdu, Islamiyat and Pakistan Studies") +
                 opt("sji-route-ssc", "abroad", "Abroad", "5 subjects: English, Maths and 3 electives") +
                 opt("sji-route-ssc", "foreign", "I&rsquo;m a foreign or dual national", "5 subjects: English, Maths and 3 electives"))
OPT_ROUTE_HSSC = (opt("sji-route-hssc", "pk", "Both in Pakistan", "8 O Levels + 3 A Levels") +
                  opt("sji-route-hssc", "mixed", "One in Pakistan, one abroad", "You still need Urdu, Islamiyat and Pakistan Studies") +
                  opt("sji-route-hssc", "abroad", "Both O and A Levels abroad", "Exempt from Urdu, Islamiyat and Pakistan Studies") +
                  opt("sji-route-hssc", "foreign", "I&rsquo;m a foreign or dual national", "Exempt from Urdu, Islamiyat and Pakistan Studies"))
OPT_GROUP = (opt("sji-group", "pm", "Pre-Medical", "A Level Physics, Chemistry, Biology") +
             opt("sji-group", "pe", "Pre-Engineering", "A Level Physics, Chemistry, Maths") +
             opt("sji-group", "cs", "Computer Science", "A Level Physics, Maths, Computer Science") +
             opt("sji-group", "hum", "Humanities", "Any 3 A Levels, e.g. Business, Economics, Accounting"))


def ysel(i, v):
    return '<select class="sj-select" id="%s">%s</select>' % (i, "".join(
        '<option value="%d"%s>%s</option>' % (y, " selected" if y == v else "", l) for y, l in
        [(2028, "2028 (forecast)"), (2027, "2027 (forecast)"), (2026, "2026"), (2025, "2025"), (2024, "2024"), (2023, "2023"), (2022, "2022"), (2021, "2021"), (2020, "2006 to 2020")]))


app_js = app.replace("'__WA__'", json.dumps("https://wa.me/923362144454?text=")).replace("'__URL__'", json.dumps(URL))
js = (engine + "\n" + app_js)
js = js.encode("ascii", "backslashreplace").decode("ascii")
rep = {"__VERSION__": VERSION, "__UPDATED__": UPDATED, "__SOURCES__": SOURCES, "__OPT_TARGET__": OPT_TARGET,
       "__OPT_ROUTE_SSC__": OPT_ROUTE_SSC, "__OPT_ROUTE_HSSC__": OPT_ROUTE_HSSC, "__OPT_GROUP__": OPT_GROUP,
       "__OY__": ysel("sji-oy", 2026), "__AY__": ysel("sji-ay", 2026), "__ASTAR__": ASTAR_TABLES, "__TICK__": TICK,
       "__WA_END__": a(wa("IBCC-END")), "__POPUP__": POPUP, "__SITE__": SITE, "__FAQ__": faq_html,
       "__ENGINE__": "", "__APP__": "", "__STD__": std,
       "__LD_APP__": json.dumps(ld_app, ensure_ascii=True), "__LD_FAQ__": json.dumps(ld_faq, ensure_ascii=True)}
for k, v in rep.items():
    page = page.replace(k, v)
page = page.replace("<script>\n\n\n</script>", "<script>\n" + js + "\n</script>", 1)
left = re.findall(r"__[A-Z0-9_]+__", page)
assert not left, left
bad = sorted({c for c in page if ord(c) > 127})
assert not bad, bad
assert "<title" not in page and "<html" not in page and "<body" not in page
assert page.count("<h1") == 1
open(OUT, "w", encoding="ascii").write(page)
print("wrote", OUT, len(page), "bytes")
