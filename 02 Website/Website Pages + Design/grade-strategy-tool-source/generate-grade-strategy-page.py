#!/usr/bin/env python3
"""
SJ Academy: A Level grade strategy tool page builder (/a-level-grade-strategy-tool/).

Inputs (same folder):
  gt_data.py    Cambridge grade thresholds (edit this after each results day)
  build_data.py checks the data against Cambridge's own A Level rows and refuses to build on a mismatch
  engine.js     the calculation engine (pure functions)
  ui.js         the tool's page behaviour
  page-script.html the standard sj-page-script.js, copied unchanged

Output:
  a-level-grade-strategy-tool-elementor-widget.html   paste into the Elementor HTML widget
  a-level-grade-strategy-tool-PREVIEW.html            same page with the shared stylesheet inlined, for checking in a browser

Run: python3 generate-grade-strategy-page.py [--css path/to/sj-brand.min.css]
Plain ASCII output. Python 3.8 or newer, no other packages.
"""
import argparse, html, json, os, re, sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gt_data as D
from build_data import build

WA = "https://wa.me/923362144454?text="
POPUP = "#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D"
TICK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg>'
NEWEST = D.SESSIONS[0][1]


def read(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return f.read()


def ascii_js(s):
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in s)


# ---------------------------------------------------------------- data
def data_payload():
    rows, problems = build()
    if problems:
        sys.exit("Threshold check failed for: %s" % ", ".join(problems))
    subs = []
    for code in D.ORDER:
        rs = [r for r in rows if r["code"] == code]
        subs.append({"code": code, "name": rs[0]["name"],
                     "routes": [{k: v for k, v in r.items() if k not in ("code", "name")} for r in rs]})
    return {"sessions": [{"k": k, "label": l, "y": y, "m": m} for k, l, y, m in D.SESSIONS], "subjects": subs}


def threshold_tables():
    """Official Cambridge rows for the newest series, Pakistan (variant 2) papers."""
    k = D.SESSIONS[0][0]
    by = {s["code"]: s for s in D.SUBJECTS}
    al, asl = [], []
    for code in D.ORDER:
        s = by[code]
        if code == "9709":
            r1, r3 = s["routes"][0], s["routes"][2]
            al.append(("Mathematics", code, "P1, P3, M1, S1", 250, r1["check"][k]))
            al.append(("Mathematics", code, "P1, P3, S1, S2", 250, r3["check"][k]))
            asl.append(("Mathematics", code, "P1 + M1", 125, s["as_rows_all"]["P1+M1"][k][0]))
            asl.append(("Mathematics", code, "P1 + S1", 125, s["as_rows_all"]["P1+S1"][k][0]))
            continue
        r = s["routes"][0]
        P = s["papers"]
        asmax = round(sum(P[p][1] * P[p][2] for p in r["as"]))
        tot = asmax + round(sum(P[p][1] * P[p][2] for p in r["a2"]))
        chk, asr = r["check"][k], r["as_rows"][k]
        if len(chk) == 2:
            for i, v in enumerate(("33", "34")):
                al.append((s["name"], code, "practical " + v, tot, chk[i]))
                asl.append((s["name"], code, "practical " + v, asmax, asr[i]))
        else:
            al.append((s["name"], code, "", tot, chk[0]))
            asl.append((s["name"], code, "", asmax, asr[0]))

    def table(rows, heads, cap):
        h = "".join('<th scope="col"%s>%s</th>' % (' class="sj-num"' if i else "", x) for i, x in enumerate(heads))
        body = []
        for name, code, note, mx, vals in rows:
            label = "%s (%s)%s" % (name, code, ('<span class="sj-muted sj-small"> %s</span>' % note) if note else "")
            cells = "".join('<td data-label="%s" class="sj-num">%s</td>' % (heads[i + 2], v) for i, v in enumerate(vals))
            body.append('<tr><td data-label="Subject">%s</td><td data-label="Max" class="sj-num">%s</td>%s</tr>' % (label, mx, cells))
        return ('<div class="sj-table-wrap"><table class="sj-table sj-table-stack"><caption class="sj-vh">%s</caption><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
                % (cap, h, "".join(body)))

    t_al = table(al, ["Subject", "Max", "A*", "A", "B", "C", "D", "E"], "A Level thresholds, " + NEWEST)
    t_as = table(asl, ["Subject", "Max", "a", "b", "c", "d", "e"], "AS Level thresholds, " + NEWEST)
    return t_al, t_as


# ---------------------------------------------------------------- FAQ
FAQ = [
    ("How do I work out the marks I need in A2 for an A?",
     "Turn your AS PUM back into the weighted AS mark Cambridge holds for you, then add the A2 thresholds of the series you will sit. The calculator above does both steps with Cambridge&rsquo;s own thresholds. For example, an AS b in Business (PUM 75, May/June 2026) needs about 65 to 71 out of 100 in A2 for an overall A, depending on the series."),
    ("What is PUM on my Cambridge statement of results?",
     "PUM stands for percentage uniform mark. It is a score out of 100 that shows where you sit inside your grade: a grade a starts at 80, b at 70, c at 60, d at 50 and e at 40. It is not the percentage of marks you scored. A PUM of 75 means you were halfway between the b and a thresholds."),
    ("How long can I carry forward my AS result?",
     "13 months. If you sat AS in May/June 2026, you can use it in Oct/Nov 2026 or May/June 2027, but not in Oct/Nov 2027. If you sat AS in Oct/Nov, you can use it in the next May/June or Oct/Nov series."),
    ("If I retake AS, which result does Cambridge use?",
     "It depends on your entry. If you re-sit AS in the same series as A2 and your entry includes your previous AS, Cambridge works out both and uses the AS result that gives the better A Level grade. Each AS sitting counts as one package, so papers from different series are never mixed. With a carry-forward-only entry, only the AS result named on the entry counts."),
    ("Do I need 90% in A2 for an A* in Cambridge A Level?",
     "No. That rule belongs to an old UK exam board system. Cambridge awards A* on your total weighted mark across AS and A2, like every other grade. There is no separate A2 requirement."),
    ("Should I retake AS or carry it forward?",
     "Compare the standard you need in A2 with the standard you showed at AS. If the A2 marks you need are at or below your AS grade standard, carrying forward is realistic. If they are two or more grades above it, re-sitting AS usually costs fewer marks overall. The calculator shows both side by side."),
    ("Why does the calculator show a range instead of one number?",
     "Cambridge sets grade thresholds after each series is marked, so they move. The A2 thresholds for your exam are not known yet, so the tool tests your result against the last three series and shows the spread. Plan for the top of the range."),
    ("Can I carry forward AS Maths with Paper 2?",
     "No. Cambridge does not let an AS made of Pure Mathematics 1 and Pure Mathematics 2 count towards the full A Level. Only AS Maths taken as P1 with Mechanics or P1 with Statistics 1 can be carried forward. With P1 and P2, you sit all four A Level papers."),
    ("Which subjects does the calculator cover?",
     "Mathematics, Physics, Chemistry, Biology, Business, Economics, Accounting, Computer Science, Psychology, Sociology, English Literature and Law, using the papers sat in Pakistan. Urdu is not included because Cambridge sets its AS grades separately from its paper thresholds, so this method cannot predict it reliably."),
]


def faq_html():
    items = []
    for i, (q, a) in enumerate(FAQ):
        items.append('<details%s><summary>%s</summary><div class="sj-faq-a"><p>%s</p></div></details>' % (" open" if i == 0 else "", q, a))
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": html.unescape(q),
                          "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)}} for q, a in FAQ]}
    return "\n".join(items), json.dumps(ld, ensure_ascii=True)


# ---------------------------------------------------------------- page
CSS = r"""
<style>
/* Page-only layout for the grade strategy tool. Every rule is scoped to this page. */
#sj.sj-p-grade-strategy [hidden]{display:none!important}
#sj.sj-p-grade-strategy fieldset{border:0;margin:0;padding:0;min-width:0}#sj.sj-p-grade-strategy legend{padding:0;margin-bottom:6px}
#sj.sj-p-grade-strategy .sjg-hero{display:grid;justify-items:center;gap:var(--sj-s6)}#sj.sj-p-grade-strategy .sjg-intro{text-align:center;justify-items:center;max-width:860px}
#sj.sj-p-grade-strategy .sjg-intro .sj-pill{margin-left:auto;margin-right:auto}#sj.sj-p-grade-strategy .sjg-intro .sj-row{justify-content:center}
#sj.sj-p-grade-strategy #sjg-tool{width:calc(100% - 9px);max-width:760px;scroll-margin-top:110px}#sj.sj-p-grade-strategy #sjg-rh{scroll-margin-top:110px}
#sj.sj-p-grade-strategy .sjg-pick{display:grid;gap:var(--sj-s4);grid-template-columns:minmax(0,1fr)}
#sj.sj-p-grade-strategy .sjg-mode{display:grid;grid-template-columns:1fr 1fr;padding:4px;gap:4px;border:1.5px solid var(--sj-ink);border-radius:var(--sj-r-pill);background:var(--sj-canvas)}
#sj.sj-p-grade-strategy .sjg-mode button{min-height:44px;padding:6px 10px;border-radius:var(--sj-r-pill);text-align:center;font-size:15px;font-weight:500;color:var(--sj-ink)}#sj.sj-p-grade-strategy .sjg-mode button[aria-pressed="true"]{background:var(--sj-yellow);box-shadow:inset 0 0 0 1.5px var(--sj-ink)}
#sj.sj-p-grade-strategy .sjg-pum{display:grid;grid-template-columns:96px minmax(0,1fr);gap:var(--sj-s4);align-items:center}
#sj.sj-p-grade-strategy input[type=range]{width:100%;height:44px;accent-color:var(--sj-cta);cursor:pointer;margin:0}
#sj.sj-p-grade-strategy .sjg-choices{display:flex;flex-wrap:wrap;gap:8px}#sj.sj-p-grade-strategy .sjg-choices .sj-choice span{min-width:52px;justify-content:center}
#sj.sj-p-grade-strategy .sjg-quick{display:grid;grid-template-columns:auto minmax(0,1fr);gap:var(--sj-s4);align-items:center;padding:var(--sj-s4);border-radius:var(--sj-r-md);background:var(--sj-yellow-light)}
#sj.sj-p-grade-strategy .sjg-quick p+p{margin-top:6px}#sj.sj-p-grade-strategy .sj-stamp{flex:none;background:#fff}
#sj.sj-p-grade-strategy .sjg-cards{display:grid;gap:var(--sj-s6);grid-template-columns:minmax(0,1fr)}#sj.sj-p-grade-strategy .sjg-cards .sj-card{display:grid;gap:var(--sj-s3);align-content:start}
#sj.sj-p-grade-strategy .sjg-cards .sj-tagged{border:1.5px solid var(--sj-ink)}#sj.sj-p-grade-strategy .sjg-body>*+*{margin-top:var(--sj-s3)}
#sj.sj-p-grade-strategy .sjg-big{font-size:clamp(36px,calc(28px + 1.6vw),48px);font-weight:600;line-height:1;letter-spacing:-.03em;color:var(--sj-ink)}#sj.sj-p-grade-strategy .sjg-of{font-size:15px;color:var(--sj-muted)}
#sj.sj-p-grade-strategy .sjg-wi{padding:var(--sj-s4);border-radius:var(--sj-r-md);background:var(--sj-canvas)}
#sj.sj-p-grade-strategy .sjg-two{display:grid;gap:var(--sj-s6);grid-template-columns:minmax(0,1fr)}#sj.sj-p-grade-strategy .sjg-side{display:grid;gap:var(--sj-s5);justify-items:start}
#sj.sj-p-grade-strategy .sjg-pum-t td,#sj.sj-p-grade-strategy .sjg-pum-t th{padding:10px 14px}
#sj.sj-p-grade-strategy .sjg-final{text-align:center;display:grid;justify-items:center}#sj.sj-p-grade-strategy .sjg-final .sj-row{justify-content:center}
@media (min-width:600px){#sj.sj-p-grade-strategy .sjg-pick{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:1000px){#sj.sj-p-grade-strategy .sjg-cards{grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--sj-s5)}
#sj.sj-p-grade-strategy .sjg-two{grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:var(--sj-s7);align-items:start}}
</style>
"""


def page():
    data = data_payload()
    t_al, t_as = threshold_tables()
    faq_items, faq_ld = faq_html()
    engine = read("engine.js")
    ui = read("ui.js")
    pscript = read("page-script.html")
    grades = "".join('<label class="sj-choice"><input type="radio" name="sjg-grade" value="%s"><span>%s</span></label>' % (g, g) for g in "abcdeu")
    pos = "".join('<label class="sj-choice"><input type="radio" name="sjg-pos" value="%d"><span>%s</span></label>' % (i, t)
                  for i, t in enumerate(["Just made it", "Middle", "Nearly the next grade"]))
    tgs = "".join('<label class="sj-choice"><input type="radio" name="sjg-tg" value="%d"><span>%s</span></label>' % (i, g)
                  for i, g in enumerate(["A*", "A", "B", "C", "D", "E"]))
    demo = WA + "Hi%20SJ%20Academy%2C%20I%27d%20like%20to%20book%20a%20free%20demo%20class.%0ALevel%3A%20A%20Level%0ASubject%3A%20%0AMode%20%28in%20class%20or%20online%29%3A%20%0A%28Ref%3A%20TL-GRADE%29%0AMy%20name%20is%20"
    err_wa = WA + "Hi%20SJ%20Academy%2C%20the%20A%20Level%20grade%20calculator%20did%20not%20work%20for%20me.%0A%28Ref%3A%20TL-GRADE%29%0AMy%20name%20is%20"
    sessions_txt = ", ".join(s[1] for s in D.SESSIONS)

    return f"""<!-- SJ Academy A Level grade strategy tool, Elementor HTML widget. Version 2.0, built {date.today().isoformat()}.
     Page: /a-level-grade-strategy-tool/ (address unchanged). Family: Tool, on the graph-paper surface.
     Needs the shared stylesheet sj-brand.css 3.1.1 in Additional CSS.
     Build: Elementor Full Width, Hide Title = Yes. One HTML widget in a full-width section, zero padding, no entrance animation.
     Replaces the old "Grade Comeback Calculator" widget in full (old CSS, old script and the PUM modal are gone).
     DO NOT EDIT THIS FILE BY HAND. Edit gt_data.py (thresholds), engine.js or ui.js and run generate-grade-strategy-page.py.
     Thresholds: Cambridge grade threshold tables, Pakistan papers (variant 2, practicals 33 and 34), {sessions_txt}.
     Set in Yoast: Title  A Level Grade Calculator: Marks You Need in A2 | CAIE
                   Meta   Free Cambridge A Level grade calculator. Enter your AS PUM and target grade to see the A2 marks you need, whether to retake AS, and which series you can still use.
                   Focus keyphrase: a level grade calculator
     Not used on purpose: phone bottom bar (it would cover results), registration form (popup 6023 is the only one).
     The page script block near the end is the standard sj-page-script.js, copied unchanged.
     Saved answers stay in the visitor's own browser (localStorage key sjg-v1). Nothing is sent anywhere.
     This file is plain ASCII: symbols are written as codes so they cannot be garbled. -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>

<div id="sj" class="sj-p-grade-strategy" data-family="tool">

  <!-- 1. HERO: centred. The tool is the offset card -->
  <section class="sj-section sj-bg-grid">
    <div class="sj-wrap sjg-hero">
      <div class="sj-stack sjg-intro">
        <h1 class="sj-h1"><span class="sj-pill"><span>A Level grade calculator &middot; CAIE</span></span>How many marks do you need in <span class="sj-hl">A2</span>?</h1>
        <p class="sj-lead">Put in your AS result and the grade you want. The calculator runs it through Cambridge&rsquo;s own grade thresholds and shows what you need in A2, whether re-sitting AS is worth it, and which exam series you can still use.</p>
        <div class="sj-row"><span class="sj-chip sj-chip-yellow">Free</span><span class="sj-chip">12 subjects</span><span class="sj-updated">Cambridge thresholds to {NEWEST}</span></div>
      </div>

      <div class="sj-offset sj-stack" id="sjg-tool">
        <div class="sjg-pick">
          <div class="sj-field"><label class="sj-label" for="sjg-subj">Subject</label><select class="sj-select" id="sjg-subj"></select></div>
          <div class="sj-field"><label class="sj-label" for="sjg-sat">When did you sit AS?</label><select class="sj-select" id="sjg-sat"></select></div>
        </div>
        <div class="sj-field" id="sjg-route-f" hidden><label class="sj-label" for="sjg-route">Your Maths papers</label><select class="sj-select" id="sjg-route"></select>
          <p class="sj-help">Took P1 and P2 at AS? That AS can&rsquo;t count towards the full A Level, so you sit all four A Level papers.</p></div>

        <div class="sj-stack">
          <div class="sjg-mode" role="group" aria-label="How do you know your AS result?">
            <button type="button" id="sjg-m-pum" aria-pressed="true">I know my PUM</button>
            <button type="button" id="sjg-m-grade" aria-pressed="false">I only know my grade</button>
          </div>
          <div id="sjg-pum-box" class="sj-field">
            <div class="sj-field" id="sjg-pum-f">
              <label class="sj-label" for="sjg-pum">AS PUM (0 to 100)</label>
              <div class="sjg-pum"><input class="sj-input sj-num" id="sjg-pum" type="number" inputmode="numeric" min="0" max="100" step="1" aria-describedby="sjg-pum-h"><input type="range" id="sjg-pum-r" min="0" max="100" step="1" aria-label="AS PUM slider"></div>
              <p class="sj-error">Enter a number from 0 to 100.</p>
              <p class="sj-help" id="sjg-pum-h">The number next to your grade on the statement of results. <b id="sjg-pum-g"></b></p>
            </div>
          </div>
          <div id="sjg-grade-box" class="sj-stack" hidden>
            <div><fieldset><legend class="sj-label">AS grade</legend><div class="sjg-choices">{grades}</div></fieldset></div>
            <div><fieldset><legend class="sj-label">Where in that grade?</legend><div class="sjg-choices">{pos}</div></fieldset></div>
          </div>
        </div>

        <div><fieldset><legend class="sj-label">Overall A Level grade you want</legend><div class="sjg-choices">{tgs}</div></fieldset></div>

        <div class="sjg-quick" aria-live="polite">
          <span class="sj-stamp" id="sjg-stamp" aria-hidden="true">A</span>
          <div><p id="sjg-head"></p><p class="sj-small"><b id="sjg-verdict"></b> <a class="sj-link sj-link-go" href="#sjg-rh" data-event="tool_result_jump" data-loc="tool">See all three routes</a></p></div>
        </div>
        <div class="sj-row"><span class="sj-hand sj-tilt-l">updates as you type</span><button class="sj-btn sj-btn-ghost sj-btn-sm" type="button" id="sjg-reset">Start again</button></div>
        <div id="sjg-err" class="sj-alert sj-alert-err" role="alert" hidden><b>Something went wrong</b><p>The calculator could not load. Refresh the page, or <a class="sj-link" href="{err_wa}" target="_blank" rel="noopener" data-loc="tool_error">WhatsApp us</a> your subject, PUM and target grade.</p></div>
      </div>
    </div>
  </section>

  <!-- 2. RESULT -->
  <section class="sj-section sj-bg-canvas" id="sjg-result">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-stack">
        <div class="sj-eyebrow">Your result</div>
        <h2 class="sj-h2" id="sjg-rh" tabindex="-1">Your three <span class="sj-hl">routes</span></h2>
        <p class="sj-measure" id="sjg-sum" aria-live="polite"></p>
        <div class="sj-alert" id="sjg-rec" aria-live="polite"></div>
      </div>

      <div class="sjg-cards">
        <div class="sj-card" id="sjg-c1">
          <div class="sj-eyebrow">Route 1</div>
          <h3 class="sj-h3">Keep your AS, sit A2 only</h3>
          <p class="sj-small sj-muted">A2 marks you need (weighted)</p>
          <div class="sjg-body"></div>
          <div class="sjg-wi sj-stack">
            <label class="sj-label" for="sjg-wi">Try it: if you score <span id="sjg-wi-v" class="sj-num"></span> in A2</label>
            <input type="range" id="sjg-wi" min="0" max="100" step="1">
            <p class="sj-small" id="sjg-wi-out" aria-live="polite"></p>
          </div>
        </div>

        <div class="sj-card" id="sjg-c2">
          <span class="sj-tag" id="sjg-c2-tag" hidden>best fit</span>
          <div class="sj-eyebrow">Route 2</div>
          <h3 class="sj-h3">Re-sit AS as well</h3>
          <p class="sj-small">Sit the AS papers again, with A2 or a series before. If your entry includes your old AS, Cambridge keeps whichever AS gives the better grade.</p>
          <div class="sj-table-wrap"><table class="sj-table sj-table-stack"><caption class="sj-vh">A2 marks needed after an AS re-sit</caption>
            <thead><tr><th scope="col">AS re-sit result</th><th scope="col" class="sj-num">A2 needed (of <span id="sjg-resit-max"></span>)</th></tr></thead>
            <tbody id="sjg-resit"></tbody></table></div>
          <p class="sj-small sj-muted">More papers in one series, but each grade you add at AS takes marks off what A2 has to do.</p>
        </div>

        <div class="sj-card" id="sjg-c3">
          <span class="sj-tag" id="sjg-c3-tag" hidden>your route</span>
          <div class="sj-eyebrow">Route 3</div>
          <h3 class="sj-h3">Start again: all papers in one series</h3>
          <p class="sj-small sj-muted">Total weighted marks you need</p>
          <div id="sjg-fresh"></div>
          <p class="sj-small">Your old AS doesn&rsquo;t count. This is the route when your AS is more than 13 months old by the time you sit A2, or when you took AS Maths as P1 and P2.</p>
        </div>
      </div>

      <div class="sj-stack">
        <h3 class="sj-h3">Every grade at a glance</h3>
        <p class="sj-small sj-muted" id="sjg-ladder-cap"></p>
        <div class="sj-table-wrap"><table class="sj-table sj-table-stack"><caption class="sj-vh">A2 marks needed for each overall grade</caption>
          <thead><tr><th scope="col">Overall grade</th><th scope="col" class="sj-num">A2 marks needed</th><th scope="col" class="sj-num">Last three series</th><th scope="col">Standard on A2</th></tr></thead>
          <tbody id="sjg-ladder"></tbody></table></div>
      </div>

      <div class="sj-stack">
        <div class="sj-row">
          <a class="sj-btn sj-btn-wa" id="sjg-wa" href="{WA}" target="_blank" rel="noopener" data-loc="result">Talk it through on WhatsApp</a>
          <a class="sj-link" id="sjg-share" href="https://wa.me/" target="_blank" rel="noopener" data-event="resource_share" data-loc="result">Send this result to a parent or friend</a>
        </div>
        <p class="sj-small sj-muted sj-measure">Estimates from Cambridge&rsquo;s published thresholds for the papers sat in Pakistan. The thresholds for your own exam are set after it is marked, so treat the top of each range as your target.</p>
      </div>
    </div>
  </section>

  <!-- 3. HOW IT WORKS -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sjg-two">
      <div class="sj-stack">
        <div class="sj-eyebrow">How it works</div>
        <h2 class="sj-h2">The same maths <span class="sj-hl">Cambridge does</span></h2>
        <ol class="sj-steps">
          <li><b>Your PUM becomes marks</b><span>PUM is a straight line between grade thresholds, so it converts back into the weighted AS mark Cambridge holds for you, using the thresholds of the series you sat.</span></li>
          <li><b>AS and A2 thresholds add up</b><span>When you carry AS forward, your A Level threshold is your AS series&rsquo; thresholds plus the A2 thresholds of the series you sit A2 in. The tool checks this against Cambridge&rsquo;s published rows.</span></li>
          <li><b>Three recent series, one range</b><span>Your A2 thresholds aren&rsquo;t set yet, so the tool tests your result against {sessions_txt} and shows the spread.</span></li>
          <li><b>Routes compared on standard</b><span>The A2 marks you need are matched to a grade standard on the A2 papers, then compared with the grade you got at AS.</span></li>
        </ol>
      </div>
      <div class="sj-card sj-stack">
        <h3 class="sj-h3">Why a range, not one number</h3>
        <p>Cambridge sets thresholds after every series is marked. For the same AS result, the A2 marks needed for a grade can move by more than 10 between series in Maths and Sociology.</p>
        <p>One neat number would look confident and be wrong half the time. Plan for the top of the range and enjoy the surprise in August.</p>
      </div>
    </div>
  </section>

  <!-- 4. RULES (caveats) -->
  <section class="sj-section sj-bg-grid">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-stack">
        <div class="sj-eyebrow">Before you decide</div>
        <h2 class="sj-h2">Five rules that <span class="sj-hl">change the plan</span></h2>
      </div>
      <div class="sjg-two">
        <div class="sj-stack">
          <div class="sj-card sj-stack"><h3 class="sj-h3">Your AS lasts 13 months</h3><p>An AS result counts towards the full A Level only if you finish within 13 months. Sat AS in May/June 2026? You can use it in Oct/Nov 2026 or May/June 2027, not later.</p></div>
          <div class="sj-card sj-stack"><h3 class="sj-h3">Re-sitting AS comes with a safety net</h3><p>Re-sit AS in the same series as A2 with an entry that includes your old AS, and Cambridge uses whichever AS gives the better A Level grade. Each sitting counts as one package: papers from different series are never mixed.</p></div>
          <div class="sj-card sj-stack"><h3 class="sj-h3">A* has no separate A2 rule</h3><p>Cambridge awards A* on your total weighted mark, like every other grade. The &ldquo;90% in A2&rdquo; rule you may have heard about belongs to an old UK system, not Cambridge.</p></div>
          <div class="sj-card sj-stack"><h3 class="sj-h3">AS Maths with Paper 2 can&rsquo;t be carried</h3><p>Only AS Maths taken as P1 with Mechanics, or P1 with Statistics 1, counts towards A Level. P1 with P2 means all four A Level papers.</p></div>
          <div class="sj-card sj-stack"><h3 class="sj-h3">Entries close early</h3><p>School candidates enter through their school. Private candidates in Pakistan enter through the British Council. Ask for an entry that carries forward your AS, and book it months before the exams.</p></div>
        </div>
        <div class="sjg-side">
          <div class="sj-sticky sj-tilt-r"><span class="sj-hand">remember</span><p>Thresholds move every series. Plan for the tougher one.</p></div>
          <div class="sj-card sj-stack">
            <h3 class="sj-h3">What PUM means</h3>
            <p class="sj-small">PUM is not your percentage. It shows where you sit inside a grade.</p>
            <div class="sj-table-wrap"><table class="sj-table sjg-pum-t"><caption class="sj-vh">PUM ranges for each AS grade</caption>
              <thead><tr><th scope="col">AS grade</th><th scope="col" class="sj-num">PUM</th></tr></thead>
              <tbody><tr><td>a</td><td class="sj-num">80&ndash;100</td></tr><tr><td>b</td><td class="sj-num">70&ndash;79</td></tr><tr><td>c</td><td class="sj-num">60&ndash;69</td></tr><tr><td>d</td><td class="sj-num">50&ndash;59</td></tr><tr><td>e</td><td class="sj-num">40&ndash;49</td></tr><tr><td>u</td><td class="sj-num">0&ndash;39</td></tr></tbody></table></div>
            <p class="sj-small sj-muted">A PUM of 75 means halfway between the b and a thresholds, whatever the raw marks were.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 5. THRESHOLDS (static, for readers and search) -->
  <section class="sj-section sj-bg-white" id="sjg-thresholds">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-stack">
        <div class="sj-eyebrow">Reference</div>
        <h2 class="sj-h2">A Level grade thresholds, <span class="sj-hl">{NEWEST}</span></h2>
        <p class="sj-measure">Weighted marks for the papers sat in Pakistan: variant 2 (12, 22, 32, 42) and practical 33 or 34. The calculator uses these plus Oct/Nov 2025 and May/June 2025.</p>
      </div>
      <div>
        <div class="sj-tabs" role="tablist" aria-label="Threshold tables">
          <button type="button" role="tab" id="sjg-t1" aria-controls="sjg-p1" aria-selected="true">A Level</button>
          <button type="button" role="tab" id="sjg-t2" aria-controls="sjg-p2" aria-selected="false" tabindex="-1">AS Level</button>
        </div>
        <div class="sj-tabpanel" role="tabpanel" id="sjg-p1" aria-labelledby="sjg-t1">{t_al}</div>
        <div class="sj-tabpanel" role="tabpanel" id="sjg-p2" aria-labelledby="sjg-t2" hidden>{t_as}</div>
      </div>
      <p class="sj-small sj-muted sj-measure">Source: Cambridge International grade threshold tables, {NEWEST}. Thresholds are for the whole syllabus after weighting, not raw paper marks.</p>
    </div>
  </section>

  <!-- 6. RELATED TOOLS -->
  <section class="sj-section sj-bg-grid">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">Next</div>
        <h2 class="sj-h2">More tools for <span class="sj-hl">your plan</span></h2>
      </div>
      <div class="sj-grid sj-grid-3">
        <a class="sj-tile" href="https://www.sjacademy.pk/university-admission-criteria-tool/"><b>University admission criteria</b><p>See which universities your target grades open.</p><span class="sj-link sj-link-go">Open the tool</span></a>
        <a class="sj-tile" href="https://www.sjacademy.pk/ibcc-equivalence-calculator/"><b>IBCC equivalence calculator</b><p>Get the equivalence figure Pakistani universities use.</p><span class="sj-link sj-link-go">Open the calculator</span></a>
        <a class="sj-tile" href="https://www.sjacademy.pk/a-level-subject-combinations-tool/"><b>A Level subject combinations</b><p>Match your subjects to the degree you want.</p><span class="sj-link sj-link-go">Open the tool</span></a>
      </div>
      <p class="sj-small sj-muted sj-measure">SJ Academy is an independent tuition centre. It is not affiliated with, or endorsed by, Cambridge.</p>
    </div>
  </section>

  <!-- 7. CLASS OFFER -->
  <section class="sj-section sj-bg-yellow">
    <div class="sj-wrap sj-stack sjg-final">
      <h2 class="sj-h2">Need those A2 marks? Let&rsquo;s get them</h2>
      <p class="sj-measure">SJ Academy teaches Cambridge A Level in DHA Phase 7, Karachi, and live online, with past-paper practice marked to the mark scheme and feedback on every lost mark. Every class except lab practicals starts with a free demo.</p>
      <div class="sj-row"><a class="sj-btn sj-btn-primary" href="{demo}" target="_blank" rel="noopener" data-loc="final_band">Book a free demo</a></div>
      <p><a class="sj-link" href="{POPUP}" data-loc="final_band">or register for a class</a></p>
    </div>
  </section>

  <!-- 8. FAQ -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">FAQ</div>
        <h2 class="sj-h2">Questions about <span class="sj-hl">A2 and retakes</span></h2>
      </div>
      <div class="sj-faq">
{faq_items}
      </div>
    </div>
  </section>
</div>
<script type="application/ld+json">{faq_ld}</script>
{CSS.strip()}
<script>
window.SJG_DATA={json.dumps(data, separators=(",", ":"))};
{ascii_js(engine)}
</script>
<script>
{ascii_js(ui)}
</script>
{pscript.strip()}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--css", default=os.path.join(HERE, "sj-brand.min.css"))
    ap.add_argument("--out", default=os.path.join(HERE, "a-level-grade-strategy-tool-elementor-widget.html"))
    ap.add_argument("--preview", default=os.path.join(HERE, "a-level-grade-strategy-tool-PREVIEW.html"))
    a = ap.parse_args()
    widget = page()
    bad = [(i, c) for i, c in enumerate(widget) if ord(c) > 127]
    if bad:
        sys.exit("Non-ASCII characters at %s" % bad[:5])
    if "gtag" in re.sub(r"window\['gt'\+'ag'\]", "", widget.split("-->", 1)[1]):
        sys.exit("Literal gtag found in the widget body")
    with open(a.out, "w", encoding="ascii") as f:
        f.write(widget)
    if os.path.exists(a.css):
        css = read(a.css) if os.path.dirname(a.css) == HERE else open(a.css, encoding="utf-8").read()
        prev = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                '<title>A Level grade calculator (preview)</title><style>body{margin:0}</style><style>' + css + '</style></head><body>' + widget + '</body></html>')
        with open(a.preview, "w", encoding="utf-8") as f:
            f.write(prev)
    print("Wrote", a.out, len(widget), "bytes")


if __name__ == "__main__":
    main()
