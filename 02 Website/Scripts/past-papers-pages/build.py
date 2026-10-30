#!/usr/bin/env python3
"""Builds the subject past papers pages (one Elementor HTML widget each) from two sources:
  - the file list in the past paper viewer widget (written by check-files.py from Backblaze), so every link exists
  - subjects.py, the page copy and checked facts for each subject

Run:  python3 build.py                      (every subject in subjects.py)
      python3 build.py "O Level/Pakistan Studies"
Output goes to 02 Website/Pages/. Every paper link is written into the HTML so search engines can read it.
"""
import html
import json
import os
import re
import sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.normpath(os.path.join(HERE, "..", ".."))
VIEWER = os.path.join(WEB, "Tools", "Past Paper Viewer", "past-paper-viewer-elementor-widget.html")
PAGE_JS = os.path.join(WEB, "Scripts", "sj-page-script.js")
OUT_DIR = os.path.join(WEB, "Pages")
sys.path.insert(0, HERE)
from subjects import SUBJECTS, O_LEVEL_PAGES  # noqa: E402

SITE = "https://www.sjacademy.pk"
STORE = "https://sjacademy.pk/file/Past-papers-storage"
SESSIONS = [("s", "May/June", "May+June", "mj"), ("w", "Oct/Nov", "October+November", "on")]
LBL = {"qp": "QP", "ms": "MS", "in": "IN", "ci": "CI"}
TYPE_ORDER = ["qp", "ms", "in", "ci"]
LEVEL_FOLDER = {"O Level": "O+Level", "A Level": "A+Level"}
LEVEL_HUB = {"O Level": "/o-level-past-papers/", "A Level": "/a-level-past-papers/"}


def viewer_files():
    s = open(VIEWER, encoding="ascii").read()
    return json.loads(re.search(r"var FILES = (.*);\n", s).group(1))


def enc(folder):
    return folder.replace(" ", "+").replace("(", "%28").replace(")", "%29")


def series_data(entry):
    """{year: {session code: {paper: {variant or '': {type: token}}}}}"""
    out = {}
    for key, tokens in entry["s"].items():
        se, y = key[0], 2000 + int(key[1:])
        for tok in tokens.split():
            t, c = tok.split("_")
            c = c[1:] if len(c) == 2 and c[0] == "0" else c
            paper, var = (int(c), "") if len(c) == 1 else (int(c[0]), c[1:])
            out.setdefault(y, {}).setdefault(se, {}).setdefault(paper, {}).setdefault(var, {})[t] = tok
    return out


def build(key):
    S = SUBJECTS[key]
    F = viewer_files()[key]
    data = series_data(F)
    years = sorted(data, reverse=True)
    first, last = years[-1], years[0]
    fmt = dict(first=first, last=last, site=SITE)
    code, name, lv = S["code"], S["name"], S["level"]
    P = "#sj.%s " % S["wrapper"]
    base = "%s/%s/%s" % (STORE, LEVEL_FOLDER[lv], enc(F["f"]))
    page_url = SITE + LEVEL_HUB[lv] + S["slug"] + "/"
    lvslug = lv.lower().replace(" ", "-")
    nfiles = 0

    def file_url(y, se, tok):
        sess = [x for x in SESSIONS if x[0] == se][0]
        return "%s/%s+%d/%s_%s%02d_%s.pdf" % (base, sess[2], y, code, se, y % 100, tok)

    def viewer_url(y, se, paper, var):
        sess = [x for x in SESSIONS if x[0] == se][0]
        return "%s/past-paper-viewer/?level=%s&amp;subject=%s&amp;series=%d-%s&amp;paper=%d%s" % (SITE, lvslug, S["viewer_subject"], y, sess[3], paper, var)

    def table(y, se):
        nonlocal nfiles
        sess = [x for x in SESSIONS if x[0] == se][0]
        papers = data[y][se]
        variants = sorted({v for p in papers.values() for v in p})
        single = variants == [""]
        head = '<th scope="col">Files</th>' if single else "".join('<th scope="col">Variant %s</th>' % v for v in variants)
        rows = []
        for p in sorted(papers):
            pname = S["papers"].get(p, ("", "", ""))[0]
            tds = []
            for v in variants:
                cell = papers[p].get(v)
                label = "Files" if single else "Variant " + v
                if not cell or "qp" not in cell:
                    tds.append('<td data-label="%s"><span class="sj-muted">Not set</span></td>' % label)
                    continue
                links = []
                for t in TYPE_ORDER:
                    if t in cell:
                        nfiles += 1
                        links.append('<a href="%s">%s%s</a>' % (file_url(y, se, cell[t]), LBL[t], "" if single else " " + str(p) + v))
                side = '<a class="sjp-side" href="%s" data-event="viewer_click" data-loc="papers">Side by side</a>' % viewer_url(y, se, p, v) if "ms" in cell else ""
                tds.append('<td data-label="%s"><span>%s %s</span></td>' % (label, " ".join(links), side))
            rows.append('<tr data-paper="%d"><td data-label="Paper"><span><b>Paper %d</b> <span class="sj-muted">%s</span></span></td>%s</tr>' % (p, p, pname, "".join(tds)))
        return ('<h3 class="sj-h3">%s %d</h3>\n<div class="sj-table-wrap"><table class="sj-table sj-table-stack"><thead><tr><th scope="col">Paper</th>%s</tr></thead><tbody>\n%s\n</tbody></table></div>'
                % (sess[1], y, head, "\n".join(rows)))

    tabs = "\n".join('<button role="tab" id="sjp-t%d" aria-controls="sjp-y%d" aria-selected="%s"%s>%d</button>'
                     % (y, y, "true" if i == 0 else "false", "" if i == 0 else ' tabindex="-1"', y) for i, y in enumerate(years))
    panels = "\n".join('<div class="sj-tabpanel sj-stack sjp-year" role="tabpanel" id="sjp-y%d" aria-labelledby="sjp-t%d">\n<h3 class="sj-h4 sjp-yh">%s %s past papers %d</h3>\n%s\n</div>'
                       % (y, y, lv, name, y, "\n".join(table(y, se) for se in ("s", "w") if se in data[y])) for y in years)
    jump = "".join('<a class="sj-btn sj-btn-ghost" href="#sjp-y%d" data-sjp-year="%d" data-loc="hero">%d</a>' % (y, y, y) for y in years)
    pfilter = "\n".join('          <label class="sj-choice"><input type="radio" name="sjp-p" value="%d"><span>%s</span></label>' % (p, S["papers"][p][2]) for p in sorted(S["papers"]))
    structure = "\n".join('<tr><td data-label="Paper"><span><b>%s</b> <span class="sj-muted">%s</span></span></td><td data-label="Time"><span>%s</span></td><td data-label="Marks"><span>%s</span></td><td data-label="What you do"><span>%s</span></td></tr>' % r for r in S["structure"])
    steps = "\n".join("          <li><b>%s</b><span>%s</span></li>" % st for st in S["steps"])
    faq = [(q, a.format(**fmt)) for q, a in S["faq"]]
    faq_html = "\n".join('<details%s><summary>%s</summary><div class="sj-faq-a"><p>%s</p></div></details>' % (" open" if i == 0 else "", q, a) for i, (q, a) in enumerate(faq))
    others = " ".join('<a class="sj-chip" href="%s/o-level-past-papers/%s/">%s</a>' % (SITE, s, n) for s, n in O_LEVEL_PAGES if s != S["slug"])
    demo = "https://wa.me/923362144454?text=" + quote("Hi SJ Academy, I saw the %s %s past papers page and would like to book a free demo class for %s %s.\nMode (in class or online): \n(Ref: %s)\nMy name is " % (lv, name, lv, name, S["ref"]), safe="")
    share = "https://wa.me/?text=" + quote("%s %s (%s) past papers and mark schemes, %d to %d: %s" % (lv, name, code, first, last, page_url), safe="")
    viewer_first = viewer_url(last, "s" if "s" in data[last] else "w", min(data[last]["s" if "s" in data[last] else "w"]), "")
    strip = lambda t: html.unescape(re.sub(r"<[^>]+>", "", t)).strip()
    ld = [
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": "%s %s (%s) past papers and mark schemes, %d to %d" % (lv, name, code, first, last),
         "url": page_url, "inLanguage": "en", "about": "Cambridge %s %s (%s)" % (lv, name, code),
         "publisher": {"@type": "EducationalOrganization", "name": "SJ Academy", "url": SITE + "/"}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "%s past papers" % lv, "item": SITE + LEVEL_HUB[lv]},
            {"@type": "ListItem", "position": 3, "name": "%s (%s)" % (name, code), "item": page_url}]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faq]},
    ]
    js = open(PAGE_JS, encoding="utf-8").read().strip()
    meta = S["meta"].format(**fmt)
    body = f'''<!-- SJ Academy {lv} {name} ({code}) past papers, Elementor HTML widget. Built {BUILT} by Scripts/past-papers-pages/build.py.
     Page: {LEVEL_HUB[lv]}{S["slug"]}/  (keep the address). Family: Resource. Shared stylesheet sj-brand.css 3.1.1 (already in Additional CSS).
     Paste this whole file into one HTML widget, replacing the old tool. Section: full width, zero padding, no entrance animation. Layout: Elementor Full Width. Hide Title: Yes.
     Set in Yoast: Title  {S["title"]}
                   Meta   {meta}
                   Focus keyphrase  {S["keyphrase"]}
                   Canonical  leave as the page address
     Every link was checked against Backblaze ({{nfiles_placeholder}} files). The "Side by side" links need /past-paper-viewer/ to be live first.
     WhatsApp Ref code: {S["ref"]}. Do not edit by hand: change subjects.py or the file list and rebuild. -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>
<div id="sj" class="{S["wrapper"]}" data-family="resource">
  <!-- 1. HERO -->
  <section class="sj-section sj-bg-dots" data-sj-hero>
    <div class="sj-wrap">
      <nav class="sj-crumbs" aria-label="Breadcrumb"><ol><li><a href="{SITE}/">Home</a></li><li><a href="{SITE}{LEVEL_HUB[lv]}">{lv} past papers</a></li><li aria-current="page">{name} ({code})</li></ol></nav>
    </div>
    <div class="sj-wrap sj-grid sj-grid-hero">
      <div class="sj-stack">
        <h1 class="sj-h1"><span class="sj-pill"><span>Cambridge {lv} &middot; {code}</span></span>{lv} {name} past papers and <span class="sj-hl">mark schemes</span></h1>
        <p class="sj-lead sj-measure">{S["lead"].format(**fmt)}</p>
        <div class="sj-row"><span class="sj-chip sj-chip-yellow">Free, no sign-up</span><span class="sj-chip">{len(S["papers"])} papers, {first} to {last}</span><span class="sj-updated">Updated {UPDATED}</span></div>
      </div>
      <div class="sj-offset sj-stack">
        <h2 class="sj-h3">Jump to a year</h2>
        <div class="sjp-years">{jump}</div>
        <p class="sj-small sj-muted">May/June and Oct/Nov, {{nfiles}} files, every link checked.</p>
        <p><a class="sj-link" href="{viewer_first}" data-event="viewer_click" data-loc="hero">Open the latest paper side by side with its mark scheme</a></p>
        <p><a class="sj-link" href="{share}" target="_blank" rel="noopener" data-event="resource_share" data-loc="hero">Share this page on WhatsApp</a></p>
      </div>
    </div>
  </section>
  <!-- 2. PAPERS -->
  <section class="sj-section sj-bg-white" id="sjp-papers">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <h2 class="sj-h2">{name} past papers <span class="sj-hl">by year</span></h2>
        <p class="sjp-top">{S["files_note"]} "Side by side" opens the paper next to its mark scheme.</p>
      </div>
      <div class="sj-stack" id="sjp-filter" hidden>
        <span class="sj-label" id="sjp-fl">Show</span>
        <div class="sj-choices" role="group" aria-labelledby="sjp-fl">
          <label class="sj-choice"><input type="radio" name="sjp-p" value="" checked><span>All papers</span></label>
{pfilter}
        </div>
      </div>
      <div>
        <div class="sj-tabs" role="tablist" aria-label="Year" id="sjp-tabs" hidden>
{tabs}
        </div>
{panels}
      </div>
      <p class="sj-small sj-muted sj-measure">Past papers and mark schemes are the copyright of Cambridge University Press &amp; Assessment. SJ Academy is an independent tuition centre and is not affiliated with or endorsed by Cambridge.</p>
    </div>
  </section>
  <!-- 3. WHAT IS ON EACH PAPER -->
  <section class="sj-section sj-bg-canvas">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <div class="sj-eyebrow">The exam</div>
        <h2 class="sj-h2">What is on each <span class="sj-hl">{name} paper</span></h2>
        <p class="sjp-top">As set in the October/November 2025 papers. Check the current syllabus on the Cambridge website before your exam.</p>
      </div>
      <div class="sj-table-wrap"><table class="sj-table sj-table-stack"><thead><tr><th scope="col">Paper</th><th scope="col">Time</th><th scope="col">Marks</th><th scope="col">What you do</th></tr></thead><tbody>
{structure}
      </tbody></table></div>
    </div>
  </section>
  <!-- 4. HOW TO USE THEM -->
  <section class="sj-section sj-bg-dots">
    <div class="sj-wrap sjp-two">
      <div class="sj-stack">
        <div class="sj-eyebrow">How to use them</div>
        <h2 class="sj-h2">Past papers only work <span class="sj-hl">with marking</span></h2>
        <p class="sj-measure">Doing ten papers without marking them is ten rehearsals of the same mistakes. One paper, marked properly, teaches more.</p>
        <ol class="sj-steps">
{steps}
        </ol>
      </div>
      <div class="sj-stack sjp-side-col">
        <div class="sj-paper">
          <div class="sj-paper-q"><small>How to read a file name</small>{code}_w25_qp_01</div>
          <div class="sj-paper-a"><div>{code} <span class="sj-mark">{name}</span></div><div>w25 <span class="sj-mark">Oct/Nov 2025</span></div><div>qp <span class="sj-mark">question paper</span></div><div>01 <span class="sj-mark">Paper 1</span></div></div>
          <div class="sj-paper-note">s = May/June, ms = mark scheme, in = insert</div>
        </div>
        <span class="sj-hand sj-tilt-r">{S["hand"]}</span>
      </div>
    </div>
  </section>
  <!-- 5. RELATED RESOURCES -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">More for {code}</div>
        <h2 class="sj-h2">More {lv} <span class="sj-hl">{name} help</span></h2>
      </div>
      <div class="sj-grid sj-grid-4">
        <a class="sj-tile" href="{SITE}/past-paper-viewer/"><b>Past paper viewer</b><p>Paper on the left, mark scheme on the right. Free.</p><span class="sj-link sj-link-go">Open the viewer</span></a>
        <a class="sj-tile" href="{SITE}{S["tuition"]}"><b>{lv} {name} tuition</b><p>Classes at DHA Phase 7, Karachi, and live online.</p><span class="sj-link sj-link-go">See the class</span></a>
        <a class="sj-tile" href="{SITE}/o-level-grade-thresholds/"><b>{lv} grade thresholds</b><p>How raw marks turn into an A*, A or B.</p><span class="sj-link sj-link-go">See the thresholds</span></a>
        <a class="sj-tile" href="{SITE}/blog/how-to-use-mark-scheme/"><b>How to use a mark scheme</b><p>The method for marking your own paper properly.</p><span class="sj-link sj-link-go">Read the guide</span></a>
      </div>
      <div class="sj-stack">
        <h3 class="sj-h4">Past papers for other {lv} subjects</h3>
        <div class="sj-row">{others}</div>
      </div>
    </div>
  </section>
  <!-- 6. FAQ -->
  <section class="sj-section sj-bg-canvas">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">FAQ</div>
        <h2 class="sj-h2">Questions about <span class="sj-hl">{code} past papers</span></h2>
      </div>
      <div class="sj-faq">
{faq_html}
      </div>
    </div>
  </section>
  <!-- 7. CLASS OFFER -->
  <section class="sj-section sj-bg-yellow">
    <div class="sj-wrap sj-stack sjp-final">
      <h2 class="sj-h2">{S["band_title"]}</h2>
      <p class="sj-measure">{S["band_text"]}</p>
      <div class="sj-row"><a class="sj-btn sj-btn-primary" href="{demo}" target="_blank" rel="noopener" data-loc="final_band">Book a free demo class</a><a class="sj-btn sj-btn-ghost" href="{SITE}{S["tuition"]}" data-loc="final_band">{lv} {name} tuition</a></div>
    </div>
  </section>
</div>
<style>
/* Page-only layout for this past papers page. Every rule is scoped to this page. */
{P}.sjp-top{{margin-top:var(--sj-s3)}}
{P}.sjp-year td a{{display:inline-flex;align-items:center;min-height:44px;padding:0 10px;margin:2px 4px 2px 0;border:1.5px solid var(--sj-ink);border-radius:var(--sj-r-md);background:#fff;font-size:15px;font-weight:500;color:var(--sj-ink);white-space:nowrap}}
{P}.sjp-year td a:hover{{background:var(--sj-yellow-light)}}
{P}.sjp-year td a.sjp-side{{border-style:dashed;font-weight:400}}
{P}.sjp-year>h3{{margin-top:var(--sj-s5)}}
{P}.sjp-year>.sjp-yh{{margin-top:0;color:var(--sj-muted)}}
{P}.sjp-year tr[hidden]{{display:none}}
{P}.sjp-two{{display:grid;gap:var(--sj-s6);grid-template-columns:minmax(0,1fr)}}
{P}.sj-paper-a .sj-mark{{float:right}}
{P}.sjp-final{{text-align:center;display:grid;justify-items:center}}
{P}.sjp-final .sj-row{{justify-content:center}}
{P}#sjp-papers,{P}.sjp-year{{scroll-margin-top:110px}}
{P}.sjp-years{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--sj-s2)}}
{P}.sjp-years .sj-btn{{min-width:0;padding-left:0;padding-right:0}}
{P}.sjp-side-col{{display:grid;justify-items:center}}
{P}.sjp-side-col .sj-paper{{width:100%}}
@media (min-width:900px){{
  {P}.sjp-two{{grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:var(--sj-s7);align-items:center}}
}}
</style>
<script>
/* Page script: year tabs start state, paper filter, papers open in a new tab. */
(function(){{
  var root=document.getElementById('sj'); if(!root||!root.classList.contains('{S["wrapper"]}')) return;
  var each=function(list,fn){{Array.prototype.forEach.call(list,fn)}};
  var panels=root.querySelectorAll('.sjp-year');
  each(panels,function(p,i){{p.hidden=i>0}});
  document.getElementById('sjp-tabs').hidden=false;
  document.getElementById('sjp-filter').hidden=false;
  each(root.querySelectorAll('[data-sjp-year]'),function(a){{a.addEventListener('click',function(e){{
    var t=document.getElementById('sjp-t'+a.getAttribute('data-sjp-year')); if(!t) return;
    e.preventDefault();t.click();t.scrollIntoView({{block:'nearest',inline:'center'}});document.getElementById('sjp-papers').scrollIntoView({{behavior:'smooth'}});
  }})}});
  each(root.querySelectorAll('input[name="sjp-p"]'),function(i){{
    i.addEventListener('change',function(){{
      if(!i.checked) return;
      each(root.querySelectorAll('.sjp-year tr[data-paper]'),function(r){{r.hidden=!!i.value&&r.getAttribute('data-paper')!==i.value}});
    }});
  }});
  each(root.querySelectorAll('.sjp-year td a:not(.sjp-side)'),function(a){{a.target='_blank';a.rel='noopener';a.setAttribute('download','');a.setAttribute('data-loc','papers')}});
}})();
</script>
<script>
/* Standard page script, copied unchanged from Scripts/sj-page-script.js */
{js}
</script>
''' + "\n".join('<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=True) for x in ld) + "\n"
    body = body.replace("{nfiles}", str(nfiles)).replace("{nfiles_placeholder}", str(nfiles))
    body = "\n".join(l for l in body.split("\n") if l.strip()) + "\n"
    body.encode("ascii")
    out = os.path.join(OUT_DIR, S["page_file"])
    open(out, "w", encoding="ascii", newline="\n").write(body)
    print("%s: %d years (%d to %d), %d files, %d KB -> %s" % (key, len(years), first, last, nfiles, len(body) // 1024, out))
    return out


BUILT = "30 October 2026"
UPDATED = "October 2026"

if __name__ == "__main__":
    for k in (sys.argv[1:] or list(SUBJECTS)):
        build(k)
