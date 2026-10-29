#!/usr/bin/env python3
"""Builds the SJ Academy university admission criteria tool (Elementor HTML widget).

Usage:  python3 generate-university-admissions-page.py
Reads:  uni_data.py (same folder). Edit the data there, never in the HTML.
Writes: university-admission-criteria-tool-elementor-widget.html

The static tables, tabs, calendar and FAQ are written into the HTML so Google can read them.
The interactive checker reads the same data from an embedded JSON block.
"""
import html
import json
import os
import re
from datetime import date

import uni_data as D

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "university-admission-criteria-tool-elementor-widget.html")
SUBN = dict(D.SUBJECTS)
AREAN = dict(D.AREAS)
WA = "https://wa.me/923362144454?text="
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTHS_L = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def e(s):
    """Escape for HTML and force plain ASCII."""
    s = html.escape(str(s), quote=True)
    s = s.replace("&#x27;", "&rsquo;").replace("'", "&rsquo;")
    return s.encode("ascii", "xmlcharrefreplace").decode("ascii")


def nice_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return "%d %s %d" % (d, MONTHS_L[m - 1], y)


def names(ids, joiner="and"):
    n = [SUBN[i] for i in ids]
    if len(n) == 1:
        return n[0]
    return ", ".join(n[:-1]) + " " + joiner + " " + n[-1]


def describe(rules, prog):
    """Plain-English summary of a programme's extra rules (beyond the university's common rules)."""
    out = []
    if "minSorted" in rules:
        ms = rules["minSorted"]
        if ms == ["B", "B", "C"]:
            out.append("At least 2 Bs and 1 C")
        elif ms == ["B", "C", "C"]:
            out.append("At least 1 B and 2 Cs")
        elif ms == ["D", "D"]:
            out.append("At least D in two principal subjects")
        else:
            out.append("At least " + ", ".join(ms))
    if "need" in rules:
        out.append(names(rules["need"]) + " required")
    if "sets" in rules:
        out.append(prog.get("setLabel") or " or ".join(names(s) for s in rules["sets"]))
    if "minEach" in rules:
        out.append("; ".join("%s at %s or better" % (SUBN[k], v) for k, v in rules["minEach"].items()))
    if "oneOfMin" in rules:
        o = rules["oneOfMin"]
        out.append("%s at %s or better" % (names(o["subs"], "or"), o["g"]))
    if "hssc" in rules:
        out.append("%d%% HSSC equivalence" % rules["hssc"])
    if "monashScore" in rules:
        out.insert(0, "Monash A Level score of %d or more from your best three" % rules["monashScore"])
    if not out:
        out.append("Any A Level subjects")
    return ". ".join(out)


CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg>'


# ---------------------------------------------------------------- data for the script
def js_data():
    unis = []
    for u in D.UNIS:
        keep = {k: u[k] for k in ("id", "short", "name", "city", "cities", "url", "test", "merit", "fee", "notes",
                                  "dates", "expected", "common") if k in u}
        for k in ("merit_w", "merit_formula", "test_name", "min_test"):
            if k in u:
                keep[k] = u[k]
        for k in ("glance_grades", "glance_subjects"):
            keep[k] = u[k]
        keep["progs"] = [dict(p, desc=describe(p["rules"], p)) for p in u["progs"]]
        unis.append(keep)
    data = {"subjects": D.SUBJECTS, "areas": D.AREAS, "unis": unis, "verified": D.VERIFIED}
    s = json.dumps(data, ensure_ascii=True, separators=(",", ":"))
    return s.replace("</", "<\\/")


# ---------------------------------------------------------------- static sections
def glance_table():
    rows = []
    for u in D.UNIS:
        rows.append(
            '<tr><td data-label="University"><b>%s</b><br><span class="sj-caption">%s</span></td>'
            '<td data-label="A Level minimum">%s</td>'
            '<td data-label="Admission test">%s</td><td data-label="How seats are decided">%s</td></tr>'
            % (e(u["short"]), e(u["city"]), e(u["glance_grades"]), e(u["test"]), e(u["merit"])))
    return "\n".join(rows)


def uni_tabs():
    tabs, panels = [], []
    for i, u in enumerate(D.UNIS):
        sel = i == 0
        tabs.append('<button type="button" role="tab" id="sju-tab-%s" aria-controls="sju-uni-%s" aria-selected="%s"%s>%s</button>'
                    % (u["id"], u["id"], "true" if sel else "false", "" if sel else ' tabindex="-1"', e(u["short"])))
        prow = "\n".join('<tr><td data-label="Programme">%s</td><td data-label="Extra requirement">%s</td></tr>'
                         % (e(p["name"]), e(describe(p["rules"], p))) for p in u["progs"])
        notes = "".join("<li>%s<span>%s</span></li>" % (CHECK, e(n)) for n in u["notes"])
        dates = "".join('<li><b class="sj-num">%s</b> %s</li>' % (e(nice_date(d["d"])), e(d["t"])) for d in u["dates"])
        if u["expected"]:
            dates += "<li>%s</li>" % e(u["expected"])
        srcs = " &middot; ".join('<a class="sj-link" href="%s" target="_blank" rel="noopener">%s</a>'
                                 % (e(s), e(re.sub(r"^https?://(www\.)?", "", s).split("/")[0])) for s in u["sources"])
        panels.append("""<div class="sj-tabpanel sj-stack" role="tabpanel" id="sju-uni-%(id)s" aria-labelledby="sju-tab-%(id)s"%(hid)s>
  <h3 class="sj-h3">%(name)s admission criteria for A Level students</h3>
  <div class="sj-row"><span class="sj-chip">%(city)s</span><span class="sj-chip">%(sector)s</span><span class="sj-updated">Checked %(ver)s</span></div>
  <div class="sju-facts">
    <div><h4 class="sj-h4">%(gh)s</h4><p>%(grades)s. %(subjects)s.</p></div>
    <div><h4 class="sj-h4">%(th)s</h4><p>%(test)s.</p></div>
    <div><h4 class="sj-h4">How %(short)s decides admission</h4><p>%(merit)s.</p></div>
    <div><h4 class="sj-h4">%(short)s fees</h4><p>%(fee)s.</p></div>
  </div>
  <div class="sj-table-wrap"><table class="sj-table sj-table-stack"><thead><tr><th scope="col">Programme</th><th scope="col">Extra requirement</th></tr></thead><tbody>
%(prow)s
  </tbody></table></div>
  <h4 class="sj-h4">%(dh)s</h4>
  <ul class="sju-dates">%(dates)s</ul>
  <h4 class="sj-h4">Worth knowing</h4>
  <ul class="sj-ticks">%(notes)s</ul>
  <p class="sj-small">Sources: %(srcs)s</p>
</div>""" % {"id": u["id"], "hid": "" if i == 0 else " hidden", "name": e(u["name"]), "city": e(u["city"]),
             "sector": e(u["sector"]), "ver": D.VERIFIED, "grades": e(u["glance_grades"]), "subjects": e(u["glance_subjects"]),
             "test": e(u["test"]), "merit": e(u["merit"]), "fee": e(u["fee"]), "prow": prow, "cycle": D.CYCLE,
             "dates": dates, "notes": notes, "srcs": srcs, "short": e(u["short"]),
             "gh": e(u.get("grades_heading") or u["short"] + " eligibility criteria for A Level students"),
             "th": e(u.get("test_heading") or u["short"] + " admission test"),
             "dh": e(u.get("dates_heading") or u["short"] + " deadlines and key dates, " + D.CYCLE)})
    return "\n".join(tabs), "\n".join(panels)


def calendar():
    items = []
    for u in D.UNIS:
        for d in u["dates"]:
            items.append((d["d"], u["short"], d["t"], d["k"]))
    items.sort()
    out = []
    for iso, short, label, kind in items:
        y, m, dd = (int(x) for x in iso.split("-"))
        out.append('<li class="sj-ticket" data-date="%s"><div class="sj-ticket-stub"><b>%d</b>%s %d</div>'
                   '<div class="sj-ticket-body"><b>%s</b><span>%s</span><span class="sju-left" aria-live="off"></span></div></li>'
                   % (iso, dd, MONTHS[m - 1], y, e(short), e(label)))
    expected = "\n".join('<tr><td data-label="University"><b>%s</b></td><td data-label="What to expect">%s</td></tr>'
                         % (e(u["short"]), e(u["expected"])) for u in D.UNIS if u["expected"] and not u["dates"])
    return "\n".join(out), expected


def faq():
    det = []
    for i, (q, a) in enumerate(D.FAQ):
        det.append('<details%s><summary>%s</summary><div class="sj-faq-a"><p>%s</p></div></details>'
                   % (" open" if i == 0 else "", e(q), e(a)))
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in D.FAQ]}
    return "\n".join(det), json.dumps(ld, ensure_ascii=True).replace("</", "<\\/")


def options(pairs, placeholder):
    return '<option value="">%s</option>' % e(placeholder) + "".join(
        '<option value="%s">%s</option>' % (e(k), e(v)) for k, v in pairs)


def area_choices():
    return "".join('<label class="sj-choice"><input type="checkbox" name="sju-area" value="%s"><span>%s</span></label>'
                   % (k, e(v)) for k, v in D.AREAS) + \
        '<label class="sj-choice"><input type="checkbox" name="sju-area" value="all"><span>Show me everything</span></label>'


# ---------------------------------------------------------------- page
CSS = r"""
#sj.sj-p-uni-criteria [hidden]{display:none!important}
#sj.sj-p-uni-criteria .sju-prog{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;margin-top:10px}
#sj.sj-p-uni-criteria .sju-prog li{height:6px;border-radius:3px;background:var(--sj-line)}#sj.sj-p-uni-criteria .sju-prog li.is-on{background:var(--sj-cta)}
#sj.sj-p-uni-criteria .sju-nav,#sj.sj-p-uni-criteria .sju-top{display:flex;flex-wrap:wrap;gap:var(--sj-s3);align-items:center;justify-content:space-between}
#sj.sj-p-uni-criteria .sju-top{align-items:flex-start;flex-wrap:nowrap}
#sj.sj-p-uni-criteria .sju-arow{display:grid;grid-template-columns:minmax(0,1fr) 104px auto;gap:8px;align-items:center}#sj.sj-p-uni-criteria .sju-arow .sj-select{padding-left:12px;padding-right:34px;background-position:right 10px center}
#sj.sj-p-uni-criteria .sju-x{display:grid;place-items:center;width:44px;height:44px;border-radius:50%;font-size:22px;color:var(--sj-muted)}
#sj.sj-p-uni-criteria .sju-counts{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:10px}
#sj.sj-p-uni-criteria .sju-cnt{display:grid;justify-items:center;gap:6px;padding:10px 6px;border:1.5px solid var(--sj-ink);border-radius:var(--sj-r-md);background:#fff}
#sj.sj-p-uni-criteria .sju-cnt>b{font-weight:500;font-size:18px;color:var(--sj-ink)}
#sj.sj-p-uni-criteria .sju-step{display:flex;align-items:center;gap:6px}#sj.sj-p-uni-criteria .sju-step output{min-width:24px;text-align:center;font-weight:500;font-size:18px}
#sj.sj-p-uni-criteria .sju-step button{display:grid;place-items:center;width:44px;height:44px;border:1.5px solid var(--sj-ink);border-radius:50%;font-size:20px;line-height:1;background:var(--sj-canvas)}
#sj.sj-p-uni-criteria .sju-step button:active{background:var(--sj-yellow)}
#sj.sj-p-uni-criteria .sju-checks li.is-no svg{stroke:var(--sj-pen)}#sj.sj-p-uni-criteria .sju-checks li.is-no{color:var(--sj-pen-text)}
#sj.sj-p-uni-criteria .sju-dl{display:grid;gap:var(--sj-s3);margin:0}#sj.sj-p-uni-criteria .sju-dl dt{font-size:12px;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--sj-muted)}
#sj.sj-p-uni-criteria .sju-dl dd{margin:2px 0 0;font-size:15px;color:var(--sj-ink)}
#sj.sj-p-uni-criteria .sju-list{display:grid;gap:var(--sj-s4);grid-template-columns:minmax(0,1fr)}
#sj.sj-p-uni-criteria .sju-card{display:grid;gap:var(--sj-s4);align-content:start}
#sj.sj-p-uni-criteria .sju-star{display:inline-flex;align-items:center;gap:6px;flex:none;min-height:44px;padding:6px 14px;border:1.5px solid var(--sj-ink);border-radius:var(--sj-r-pill);font-size:14px;font-weight:500;background:#fff}
#sj.sj-p-uni-criteria .sju-star[aria-pressed="true"]{background:var(--sj-yellow)}
#sj.sj-p-uni-criteria .sju-merit{display:grid;gap:8px;padding:14px 16px;border-radius:var(--sj-r-md);background:var(--sj-canvas)}
#sj.sj-p-uni-criteria .sju-merit label{display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-size:15px}#sj.sj-p-uni-criteria .sju-merit .sj-input{width:96px;min-height:44px}
#sj.sj-p-uni-criteria .sju-more summary{min-height:44px;display:flex;align-items:center;font-size:15px;font-weight:500;color:var(--sj-ink);text-decoration:underline;text-underline-offset:3px}
#sj.sj-p-uni-criteria .sju-more>div{display:grid;gap:8px;font-size:15px;padding-top:4px}
#sj.sj-p-uni-criteria .sju-tickets{display:grid;gap:var(--sj-s3);grid-template-columns:minmax(0,1fr)}#sj.sj-p-uni-criteria .sju-tickets .sj-ticket{max-width:none}
#sj.sj-p-uni-criteria .sju-tickets .sj-ticket-body span{display:block}#sj.sj-p-uni-criteria .sju-left{font-weight:500;color:var(--sj-cta-dark)!important}
#sj.sj-p-uni-criteria .sju-dates{display:grid;gap:6px;font-size:15px}#sj.sj-p-uni-criteria .sju-two{display:grid;gap:var(--sj-s6);grid-template-columns:minmax(0,1fr)}
#sj.sj-p-uni-criteria .sju-final{text-align:center;display:grid;justify-items:center}#sj.sj-p-uni-criteria .sju-final .sj-row{justify-content:center}
#sj.sj-p-uni-criteria #sju-tool,#sj.sj-p-uni-criteria #sju-rh{scroll-margin-top:110px}#sj.sj-p-uni-criteria .sj-stamp{flex:none}
#sj.sj-p-uni-criteria .sju-tag{display:inline-block;font-size:12px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;padding:2px 8px;border-radius:var(--sj-r-sm);background:var(--sj-ok-bg);color:var(--sj-ok)}
#sj.sj-p-uni-criteria .sju-hero{display:grid;justify-items:center;gap:var(--sj-s6)}#sj.sj-p-uni-criteria .sju-intro{text-align:center;justify-items:center;max-width:860px}
#sj.sj-p-uni-criteria .sju-intro .sj-pill{margin-left:auto;margin-right:auto}#sj.sj-p-uni-criteria .sju-intro .sj-row{justify-content:center}#sj.sj-p-uni-criteria #sju-tool{width:calc(100% - 9px);max-width:760px}
#sj.sj-p-uni-criteria .sju-mode{display:grid;grid-template-columns:1fr 1fr;padding:4px;gap:4px;border:1.5px solid var(--sj-ink);border-radius:var(--sj-r-pill);background:var(--sj-canvas)}
#sj.sj-p-uni-criteria .sju-mode button{min-height:44px;padding:6px 10px;border-radius:var(--sj-r-pill);text-align:center;font-size:15px;font-weight:500;color:var(--sj-ink)}#sj.sj-p-uni-criteria .sju-mode button[aria-pressed="true"]{background:var(--sj-yellow);box-shadow:inset 0 0 0 1.5px var(--sj-ink)}
#sj.sj-p-uni-criteria .sju-pick,#sj.sj-p-uni-criteria .sju-facts{display:grid;gap:var(--sj-s4);grid-template-columns:minmax(0,1fr)}#sj.sj-p-uni-criteria .sju-facts p{margin-top:4px;font-size:15px}
@media (min-width:600px){#sj.sj-p-uni-criteria .sju-pick,#sj.sj-p-uni-criteria .sju-facts{grid-template-columns:repeat(2,minmax(0,1fr))}#sj.sj-p-uni-criteria .sju-tickets{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:900px){#sj.sj-p-uni-criteria .sju-list{grid-template-columns:repeat(2,minmax(0,1fr))}#sj.sj-p-uni-criteria .sju-tickets{grid-template-columns:repeat(3,minmax(0,1fr))}
#sj.sj-p-uni-criteria .sju-two{grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:var(--sj-s7);align-items:start}#sj.sj-p-uni-criteria .sju-dl{grid-template-columns:repeat(2,minmax(0,1fr))}}
"""

PAGE_SCRIPT = r"""(function(){
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

TOOL_JS = open(os.path.join(HERE, "tool.js")).read()


def build():
    tabs, panels = uni_tabs()
    cal, expected = calendar()
    faq_html, faq_ld = faq()
    subj_opts = options(D.SUBJECTS, "Subject")
    uni_opts = options([(u["id"], u["short"]) for u in D.UNIS], "Choose a university")
    grade_opts = options([(g, g) for g in ["A*", "A", "B", "C", "D", "E"]], "Grade")
    demo = WA + "Hi%20SJ%20Academy%2C%20I%27d%20like%20to%20book%20a%20free%20demo%20class.%0ALevel%3A%20A%20Level%0ASubject%3A%20%0AMode%20%28in%20class%20or%20online%29%3A%20%0A%28Ref%3A%20TL-UNI%29%0AMy%20name%20is%20"
    err_wa = WA + "Hi%20SJ%20Academy%2C%20the%20university%20admissions%20tool%20did%20not%20work%20for%20me.%0A%28Ref%3A%20TL-UNI%29%0AMy%20name%20is%20"
    counters = "".join(
        '<div class="sju-cnt"><b>%s</b><div class="sju-step"><button type="button" data-o="%s" data-d="-1" aria-label="One less %s">&minus;</button>'
        '<output id="sju-o-%s" aria-live="polite">0</output><button type="button" data-o="%s" data-d="1" aria-label="One more %s">+</button></div></div>'
        % (g, g, g, g.replace("*", "s"), g, g) for g in ["A*", "A", "B", "C", "D", "E"])

    page = f"""<!-- SJ Academy university admission criteria tool, Elementor HTML widget. Version 2.2, built {date.today().isoformat()}.
     Page: /university-admission-criteria-tool/ (address unchanged). Family: Tool, on the graph-paper surface.
     Needs the shared stylesheet sj-brand.css 3.1.1 in Additional CSS.
     Build: Elementor Full Width, Hide Title = Yes. One HTML widget in a full-width section, zero padding, no entrance animation.
     Replaces the old widget in full. The old Google Sheet (4 published CSV tabs) is no longer read by this page.
     DO NOT EDIT THIS FILE BY HAND. Edit uni_data.py and run generate-university-admissions-page.py.
     Set in Yoast: Title  LUMS, NUST & IBA Admission Criteria 2027 | Eligibility Checker
                   Meta   LUMS, NUST, IBA, GIKI and FAST admission and eligibility criteria for Fall 2027: A Level grades, SAT requirements, merit formulas and deadlines, plus a free checker for your grades.
                   Focus keyphrase: lums admission criteria
     Not used on purpose: phone bottom bar (it would cover results), registration form (popup 6023 is the only one).
     The page script block near the end is the standard sj-page-script.js, copied unchanged.
     Saved answers stay in the visitor's own browser (localStorage key sju-v1). Nothing is sent anywhere.
     This file is plain ASCII: symbols are written as codes so they cannot be garbled. -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>

<div id="sj" class="sj-p-uni-criteria" data-family="tool">

  <!-- 1. HERO: centred. The tool is the offset card, lookup first -->
  <section class="sj-section sj-bg-grid">
    <div class="sj-wrap sju-hero">
      <div class="sj-stack sju-intro">
        <h1 class="sj-h1"><span class="sj-pill"><span>LUMS, NUST &amp; IBA admission criteria 2027</span></span>Eligibility criteria for every top <span class="sj-hl">university</span></h1>
        <p class="sj-lead">Pick a university to see its {D.CYCLE} admission criteria: grades, subjects, tests, merit and deadlines. Or enter your grades and see every programme you qualify for.</p>
        <div class="sj-row"><span class="sj-chip sj-chip-yellow">Free</span><span class="sj-chip">{len(D.UNIS)} universities, Pakistan and abroad</span><span class="sj-updated">Checked against official pages, {D.VERIFIED}</span></div>
      </div>

      <div class="sj-offset sj-stack" id="sju-tool">
        <div class="sju-mode" role="group" aria-label="Choose what to do">
          <button type="button" id="sju-m-look" aria-pressed="true">University criteria</button>
          <button type="button" id="sju-m-grades" aria-pressed="false">Check my grades</button>
        </div>

        <div id="sju-look" class="sj-stack">
          <div class="sju-pick">
            <div class="sj-field"><label class="sj-label" for="sju-uni">University</label><select class="sj-select" id="sju-uni">{uni_opts}</select></div>
            <div class="sj-field"><label class="sj-label" for="sju-prog">Programme</label><select class="sj-select" id="sju-prog" disabled><option value="">All programmes</option></select></div>
          </div>
          <div id="sju-look-out" aria-live="polite"><p class="sj-help">Choose a university to see its criteria here.</p></div>
        </div>

        <div id="sju-grades" class="sj-stack" hidden>
        <span class="sj-hand sj-tilt-l">predicted grades work too</span>
        <div id="sju-quiz" class="sj-stack">
          <div>
            <p class="sj-eyebrow" id="sju-count" aria-live="polite">Step 1 of 4</p>
            <ol class="sju-prog" aria-hidden="true"><li class="is-on"></li><li></li><li></li><li></li></ol>
          </div>

          <fieldset class="sj-stack" data-step="1" style="border:0;padding:0;margin:0">
            <legend class="sj-h3">Your A Levels</legend>
            <p class="sj-help">Three or four full A Levels. Use predicted grades if results are not out yet.</p>
            <div id="sju-arows" class="sj-stack"></div>
            <template id="sju-arow-t"><div class="sju-arow"><select class="sj-select" aria-label="A Level subject">{subj_opts}</select><select class="sj-select" aria-label="Grade">{grade_opts}</select><button type="button" class="sju-x" aria-label="Remove this subject">&times;</button></div></template>
            <button type="button" class="sj-btn sj-btn-ghost sj-btn-sm" id="sju-add">Add a fourth subject</button>
          </fieldset>

          <fieldset class="sj-stack" data-step="2" hidden style="border:0;padding:0;margin:0">
            <legend class="sj-h3">Your O Levels</legend>
            <p class="sj-help">Count your grades in the 8 subjects IBCC uses: English, Maths, Urdu, Islamiyat, Pakistan Studies and three electives.</p>
            <div class="sju-counts">{counters}</div>
            <p class="sj-small" id="sju-otot" aria-live="polite">0 of 8 entered</p>
          </fieldset>

          <fieldset class="sj-stack" data-step="3" hidden style="border:0;padding:0;margin:0">
            <legend class="sj-h3">What do you want to study?</legend>
            <p class="sj-help">Pick up to three.</p>
            <div class="sj-choices" id="sju-areas">{area_choices()}</div>
          </fieldset>

          <fieldset class="sj-stack" data-step="4" hidden style="border:0;padding:0;margin:0">
            <legend class="sj-h3">Last details (optional)</legend>
            <div class="sj-field"><span class="sj-label" id="sju-tl">When are your final A Level exams?</span>
              <div class="sj-choices" role="radiogroup" aria-labelledby="sju-tl">
                <label class="sj-choice"><input type="radio" name="sju-time" value="jun27"><span>May/June 2027</span></label>
                <label class="sj-choice"><input type="radio" name="sju-time" value="nov26"><span>Oct/Nov 2026</span></label>
                <label class="sj-choice"><input type="radio" name="sju-time" value="done"><span>Already done</span></label>
              </div></div>
            <div class="sj-field"><span class="sj-label" id="sju-cl">Where would you study?</span>
              <div class="sj-choices" role="radiogroup" aria-labelledby="sju-cl">
                <label class="sj-choice"><input type="radio" name="sju-city" value="any" checked><span>Anywhere</span></label>
                <label class="sj-choice"><input type="radio" name="sju-city" value="karachi"><span>Karachi</span></label>
                <label class="sj-choice"><input type="radio" name="sju-city" value="lahore"><span>Lahore</span></label>
                <label class="sj-choice"><input type="radio" name="sju-city" value="islamabad"><span>Islamabad area</span></label>
                <label class="sj-choice"><input type="radio" name="sju-city" value="abroad"><span>Abroad</span></label>
              </div></div>
            <div class="sj-field"><label class="sj-label" for="sju-sat">SAT score, if you have one</label>
              <input class="sj-input" id="sju-sat" type="number" inputmode="numeric" min="400" max="1600" step="10" placeholder="For example 1350" style="max-width:220px"></div>
          </fieldset>

          <p class="sj-help" id="sju-hint" aria-live="polite"></p>
          <div class="sju-nav">
            <button class="sj-btn sj-btn-ghost" type="button" id="sju-back" hidden>Back</button>
            <button class="sj-btn sj-btn-primary" type="button" id="sju-next" data-loc="tool">Continue</button>
          </div>
        </div>

        <div id="sju-done" class="sj-stack" hidden>
          <h2 class="sj-h3">Your answers</h2>
          <dl class="sju-dl" id="sju-sum"></dl>
          <div class="sj-row">
            <button class="sj-btn sj-btn-ghost sj-btn-sm" type="button" id="sju-edit">Edit answers</button>
            <button class="sj-btn sj-btn-ghost sj-btn-sm" type="button" id="sju-reset">Start again</button>
          </div>
        </div>
        <div id="sju-err" class="sj-alert sj-alert-err" role="alert" hidden><b>Something went wrong</b><p>The checker could not build your result. Try again, or <a class="sj-link" href="{err_wa}" target="_blank" rel="noopener" data-loc="tool_error">WhatsApp us</a>.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. RESULT (filled by the script) -->
  <section class="sj-section sj-bg-canvas" id="sju-result" hidden>
    <div class="sj-wrap sj-stack-lg">
      <div class="sju-top">
        <div class="sj-stack">
          <div class="sj-eyebrow">Your result</div>
          <h2 class="sj-h2" id="sju-rh" tabindex="-1">Your {D.CYCLE} <span class="sj-hl">university map</span></h2>
          <p class="sj-measure" id="sju-lede"></p>
        </div>
        <span class="sj-stamp" id="sju-stamp" aria-hidden="true">0</span>
      </div>
      <div class="sj-proof" id="sju-nums"></div>
      <div id="sju-unlock"></div>
      <div>
        <div class="sj-tabs" role="tablist" aria-label="Programmes by result">
          <button type="button" role="tab" id="sju-t1" aria-controls="sju-p1" aria-selected="true">Qualify<span id="sju-n1"></span></button>
          <button type="button" role="tab" id="sju-t2" aria-controls="sju-p2" aria-selected="false" tabindex="-1">Raise grades<span id="sju-n2"></span></button>
          <button type="button" role="tab" id="sju-t3" aria-controls="sju-p3" aria-selected="false" tabindex="-1">Change subjects<span id="sju-n3"></span></button>
        </div>
        <div class="sj-tabpanel" role="tabpanel" id="sju-p1" aria-labelledby="sju-t1"></div>
        <div class="sj-tabpanel" role="tabpanel" id="sju-p2" aria-labelledby="sju-t2" hidden></div>
        <div class="sj-tabpanel" role="tabpanel" id="sju-p3" aria-labelledby="sju-t3" hidden></div>
      </div>

      <div class="sj-stack" id="sju-short">
        <div>
          <div class="sj-eyebrow">Your shortlist</div>
          <h2 class="sj-h2">Deadlines for your shortlist</h2>
        </div>
        <div id="sju-short-body"></div>
      </div>

      <div class="sj-card sj-stack">
        <h3 class="sj-h3">Want a second pair of eyes on your plan?</h3>
        <p class="sj-measure">Send us your grades and shortlist on WhatsApp. If a grade is holding you back, ask about a free demo class in that subject.</p>
        <div class="sj-row"><a class="sj-btn sj-btn-wa" id="sju-wa" href="{demo}" target="_blank" rel="noopener" data-loc="result">Talk to us on WhatsApp</a>
        <a class="sj-link" id="sju-share" href="https://wa.me/" target="_blank" rel="noopener" data-event="resource_share" data-loc="result">Share my shortlist</a></div>
      </div>
      <p class="sj-small sj-muted sj-measure">Results compare your grades with each university&rsquo;s published minimums. Equivalence figures are estimates from IBCC&rsquo;s conversion. Meeting a minimum lets you apply; it does not promise a seat. Confirm every rule on the official site before you apply.</p>
    </div>
  </section>

  <!-- 3. HOW IT WORKS -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sju-two">
      <div class="sj-stack">
        <div class="sj-eyebrow">How it works</div>
        <h2 class="sj-h2">Two ways to <span class="sj-hl">use it</span></h2>
        <ol class="sj-steps">
          <li><b>Look up a university</b><span>Pick a university and programme for its grades, subjects, test, merit formula, fees and next deadline, with an aggregate calculator.</span></li>
          <li><b>Or check your grades</b><span>Enter your A Levels, count your O Level grades and pick up to three areas to study.</span></li>
          <li><b>Read your map</b><span>Every programme sorted into qualify, raise grades or change subjects, with your merit aggregate and the one grade worth raising.</span></li>
          <li><b>Shortlist and track</b><span>Star the programmes you want. Their deadlines land in one list with calendar reminders.</span></li>
        </ol>
      </div>
      <div class="sj-card sj-stack">
        <h3 class="sj-h3">What the checker tests</h3>
        <ul class="sj-ticks">
          <li>{CHECK}<span>Grade minimums, such as LUMS&rsquo;s BBB average or IBA&rsquo;s 2 Bs and 1 C</span></li>
          <li>{CHECK}<span>Required subjects, such as Maths for computing or Physics, Chemistry and Biology for MBBS</span></li>
          <li>{CHECK}<span>IBCC equivalence floors, such as 60% for NUST and 65% for MDCAT</span></li>
          <li>{CHECK}<span>The single grade improvement that opens the most programmes for you</span></li>
        </ul>
      </div>
    </div>
  </section>

  <!-- 4. AT A GLANCE (static, for readers and search) -->
  <section class="sj-section sj-bg-grid" id="sju-glance">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-stack">
        <div class="sj-eyebrow">University admission criteria in Pakistan</div>
        <h2 class="sj-h2">Admission and eligibility criteria at a <span class="sj-hl">glance</span></h2>
        <p class="sj-measure">The minimum each university asks of A Level students for {D.CYCLE}, side by side.</p>
      </div>
      <div class="sj-table-wrap">
        <table class="sj-table sj-table-stack">
          <thead><tr><th scope="col">University</th><th scope="col">A Level minimum</th><th scope="col">Admission test</th><th scope="col">How seats are decided</th></tr></thead>
          <tbody>
{glance_table()}
          </tbody>
        </table>
      </div>
      <p class="sj-table-cue">Scroll sideways to see the full table.</p>
    </div>
  </section>

  <!-- 5. BY UNIVERSITY (static index tabs) -->
  <section class="sj-section sj-bg-white" id="sju-unis">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-stack">
        <div class="sj-eyebrow">By university</div>
        <h2 class="sj-h2">Every programme, every <span class="sj-hl">rule</span></h2>
        <p class="sj-measure">Pick a university for its programmes, tests, fees and {D.CYCLE} dates, with links to the official pages.</p>
      </div>
      <div>
        <div class="sj-tabs" role="tablist" aria-label="Universities">
{tabs}
        </div>
{panels}
      </div>
    </div>
  </section>

  <!-- 6. CALENDAR -->
  <section class="sj-section sj-bg-grid" id="sju-calendar">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-stack">
        <div class="sj-eyebrow">Calendar</div>
        <h2 class="sj-h2">{D.CYCLE} admissions <span class="sj-hl">calendar</span></h2>
        <p class="sj-measure">Confirmed dates, soonest first. Past dates drop off by themselves.</p>
      </div>
      <ol class="sju-tickets" id="sju-cal">
{cal}
      </ol>
      <p><button type="button" class="sj-btn sj-btn-ghost sj-btn-sm" id="sju-cal-more" hidden>Show all dates</button></p>
      <div class="sj-empty" id="sju-cal-empty" hidden><b>Every confirmed date has passed</b><p>Check each university&rsquo;s site for the next cycle.</p></div>
      <div class="sj-stack">
        <h3 class="sj-h3">Not announced yet</h3>
        <div class="sj-table-wrap"><table class="sj-table sj-table-stack"><thead><tr><th scope="col">University</th><th scope="col">What to expect</th></tr></thead><tbody>
{expected}
        </tbody></table></div>
      </div>
    </div>
  </section>

  <!-- 7. CAVEATS -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sju-two">
      <div class="sj-stack">
        <div class="sj-eyebrow">Before you apply</div>
        <h2 class="sj-h2">The minimum is the <span class="sj-hl">start line</span></h2>
        <p class="sj-measure">Grades get you through the door. The admission test usually decides the seat. At NUST, NET is <span class="sj-circled"><svg class="sj-circle" viewBox="0 0 120 70" preserveAspectRatio="none" aria-hidden="true"><path d="M14 38C10 18 40 6 68 7c27 1 44 13 42 30-2 16-30 24-56 23C28 59 8 50 13 30" fill="none" stroke="#FE6100" stroke-width="2.6" stroke-linecap="round"/></svg><b>75%</b></span> of your merit; at GIKI the test is 85%.</p>
        <ul class="sj-ticks">
          <li>{CHECK}<span>Book your tests early. NET-1 and IBA Round 1 both close before the end of 2026.</span></li>
          <li>{CHECK}<span>Apply for IBCC equivalence as soon as your results allow. Almost every university asks for it.</span></li>
          <li>{CHECK}<span>Apply to more than one university. Deadlines do not care about load-shedding, or about which university replied first.</span></li>
        </ul>
      </div>
      <div class="sj-stack" style="justify-items:start">
        <div class="sj-sticky sj-tilt-r"><span class="sj-hand">fine print</span><p>Rules change every cycle. Each university section links to its source, so check it again before you pay an application fee.</p></div>
        <div class="sj-card sj-stack">
          <h3 class="sj-h3">Not in the checker yet</h3>
          <p class="sj-small">Universities whose {D.CYCLE} rules we could not confirm on an official page. We would rather leave a university out than guess. Want one added? Tell us on WhatsApp.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 8. RELATED TOOLS -->
  <section class="sj-section sj-bg-grid">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">Next</div>
        <h2 class="sj-h2">More tools for <span class="sj-hl">your plan</span></h2>
      </div>
      <div class="sj-grid sj-grid-3">
        <a class="sj-tile" href="https://www.sjacademy.pk/ibcc-equivalence-calculator/"><b>IBCC equivalence calculator</b><p>Get the exact equivalence figure universities will use.</p><span class="sj-link sj-link-go">Open the calculator</span></a>
        <a class="sj-tile" href="https://www.sjacademy.pk/a-level-subject-combinations-tool/"><b>A Level subject combinations</b><p>Still choosing subjects? Match them to the degree first.</p><span class="sj-link sj-link-go">Open the tool</span></a>
        <a class="sj-tile" href="https://www.sjacademy.pk/a-level-grade-strategy-tool/"><b>A Level grade strategy tool</b><p>Plan the marks you need for the grade you are after.</p><span class="sj-link sj-link-go">Open the tool</span></a>
      </div>
      <p class="sj-small sj-muted sj-measure">SJ Academy is an independent tuition centre. It is not affiliated with, or endorsed by, any university listed here or by Cambridge.</p>
    </div>
  </section>

  <!-- 9. CLASS OFFER -->
  <section class="sj-section sj-bg-yellow">
    <div class="sj-wrap sj-stack sju-final">
      <h2 class="sj-h2">One grade short? Fix it with us</h2>
      <p class="sj-measure">SJ Academy teaches Cambridge A Level Maths, Physics, Chemistry, Biology, Computer Science, Economics, Business and Accounting in DHA Phase 7, Karachi, and live online. Every class except lab practicals starts with a free demo.</p>
      <div class="sj-row"><a class="sj-btn sj-btn-primary" href="{demo}" target="_blank" rel="noopener" data-loc="final_band">Book a free demo</a></div>
      <p><a class="sj-link" href="#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D" data-loc="final_band">or register for a class</a></p>
    </div>
  </section>

  <!-- 10. FAQ -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">FAQ</div>
        <h2 class="sj-h2">University admission <span class="sj-hl">questions</span></h2>
      </div>
      <div class="sj-faq">
{faq_html}
      </div>
    </div>
  </section>
</div>

<script type="application/ld+json">{faq_ld}</script>
<script type="application/json" id="sju-data">{js_data()}</script>

<style>
/* Page-only layout for the university admission criteria tool. Every rule is scoped to this page. */{CSS}</style>

<script>
{TOOL_JS}
</script>

<script>
/* Standard SJ Academy page script (sj-page-script.js), copied unchanged */
{PAGE_SCRIPT}
</script>
"""
    with open(OUT, "w", encoding="ascii") as f:
        f.write(page)
    print("wrote", OUT, len(page), "bytes")


if __name__ == "__main__":
    build()
