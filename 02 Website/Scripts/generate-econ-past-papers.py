import re,json,html
U="/mnt/user-data/uploads/Website Pages + Design/"
OUT="/mnt/user-data/outputs/a-level-economics-past-papers-elementor-widget.html"
B="https://sjacademy.pk/file/Past-papers-storage/A+Level/Economics+%289708%29"
YEARS=[2025,2024,2023,2022,2021,2020]
T={1:["qp","ms"],2:["qp","ms"],3:["qp","ms"],4:["qp","ms"]}
PN={1:"Multiple Choice (AS)",2:"Data Response &amp; Essays (AS)",3:"Multiple Choice (A2)",4:"Data Response &amp; Essays (A2)"}
LBL={"qp":"QP","ms":"MS"}
SITE="https://www.sjacademy.pk"
WA="https://wa.me/923362144454?text="
def wa(t):
    from urllib.parse import quote
    return WA+quote(t,safe='')
def table(y,s):
    name={"s":"May/June","w":"Oct/Nov"}[s]; folder={"s":"May+June","w":"October+November"}[s]+"+"+str(y)
    rows=[]
    for p,ts in T.items():
        tds=[]
        for v in (1,2,3):
            links=' '.join(f'<a href="{B}/{folder}/9708_{s}{str(y)[2:]}_{t}_{p}{v}.pdf">{LBL[t]} {p}{v}</a>' for t in ts)
            tds.append(f'<td data-label="Variant {v}"><span>{links}</span></td>')
        rows.append(f'<tr data-paper="{p}"><td data-label="Paper"><span><b>Paper {p}</b> <span class="sj-muted">{PN[p]}</span></span></td>{"".join(tds)}</tr>')
    return f'''<h3 class="sj-h3">{name} {y}</h3>
<div class="sj-table-wrap"><table class="sj-table sj-table-stack"><thead><tr><th scope="col">Paper</th><th scope="col">Variant 1</th><th scope="col">Variant 2</th><th scope="col">Variant 3</th></tr></thead><tbody>
{chr(10).join(rows)}
</tbody></table></div>'''
def _tab(i,y):
    sel="true" if i==0 else "false"
    tidx='' if i==0 else ' tabindex="-1"'
    return f'<button role="tab" id="sjp-t{y}" aria-controls="sjp-y{y}" aria-selected="{sel}"{tidx}>{y}</button>'
tabs='\n'.join(_tab(i,y) for i,y in enumerate(YEARS))
panels='\n'.join(f'<div class="sj-tabpanel sj-stack sjp-year" role="tabpanel" id="sjp-y{y}" aria-labelledby="sjp-t{y}">\n<h3 class="sj-h4 sjp-yh">A Level Economics past papers {y}</h3>\n{table(y,"s")}\n{table(y,"w")}\n</div>' for y in YEARS)
FAQ=[
("Are these A Level Economics past papers free?","Yes. Every question paper and mark scheme on this page is free to open and download. You do not need to sign up."),
("Which years of 9708 past papers are on this page?","This page has Cambridge AS and A Level Economics (9708) past papers from 2020 to 2025, for the May/June and Oct/Nov series, Papers 1 to 4, in all three variants."),
("What is on each Economics paper?","Paper 1 and Paper 3 are multiple choice. Paper 2 and Paper 4 are data response and essay papers, where you work from extracts, tables and charts to answer structured questions and write essays."),
("How do I read a 9708 past paper file name?","Every file follows the Cambridge pattern 9708_s25_qp_12. The letter is the session (s = May/June, w = Oct/Nov), the two digits are the year, qp is the question paper and ms is the mark scheme. The last two digits are the paper number followed by the variant, so 12 means Paper 1, Variant 2."),
("Which variant should I practise?","Cambridge sets different variants of the same paper for different time zones. They test the same syllabus to the same standard, so practise every variant from a session. It gives you three papers to practise from each series."),
("How should I use the mark schemes?",f'Attempt the paper under timed conditions first, then mark it yourself against the mark scheme. On Paper 2 and Paper 4, check where you lost marks for not using the data given, not only for missing economics content. Our guide on <a class="sj-link" href="{SITE}/blog/how-to-use-mark-scheme/">how to use a Cambridge mark scheme</a> walks through the method, and our <a class="sj-link" href="{SITE}/blog/a-level-thresholds-guide/">A Level grade thresholds guide</a> explains how raw marks convert to grades.'),
("Is this the same as IGCSE or O Level Economics past papers?","No. This page is for Cambridge International AS and A Level Economics, syllabus 9708. IGCSE and O Level Economics is a separate syllabus, 2281, with its own past papers."),
]
faq_html='\n'.join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><div class="sj-faq-a"><p>{a}</p></div></details>' for i,(q,a) in enumerate(FAQ))
strip=lambda t: html.unescape(re.sub(r'<[^>]+>','',t)).strip()
ld_faq={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in FAQ]}
ld_crumbs={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},{"@type":"ListItem","position":2,"name":"A Level past papers","item":SITE+"/a-level-past-papers/"},{"@type":"ListItem","position":3,"name":"Economics (9708)","item":SITE+"/a-level-past-papers/economics-9708/"}]}
ld_col={"@context":"https://schema.org","@type":"CollectionPage","name":"A Level Economics (9708) past papers and mark schemes, 2020 to 2025","url":SITE+"/a-level-past-papers/economics-9708/","inLanguage":"en","about":"Cambridge International AS and A Level Economics (9708)","publisher":{"@type":"EducationalOrganization","name":"SJ Academy","url":SITE+"/"}}
OTHER=[("accounts-9706","Accounts (9706)"),("biology-9700","Biology (9700)"),("business-9609","Business (9609)"),("chemistry-9701","Chemistry (9701)"),("computer-science-9618","Computer Science (9618)"),("english-9695","English (9695)"),("law-9084","Law (9084)"),("mathematics-9709","Mathematics (9709)"),("physics-9702","Physics (9702)"),("psychology-9990","Psychology (9990)"),("sociology-9699","Sociology (9699)"),("urdu-9686","Urdu (9686)")]
other=' '.join(f'<a class="sj-chip" href="{SITE}/a-level-past-papers/{s}/">{n}</a>' for s,n in OTHER)
jump=''.join(f'<a class="sj-btn sj-btn-ghost" href="#sjp-y{y}" data-sjp-year="{y}" data-loc="hero">{y}</a>' for y in YEARS)
demo=wa("Hi SJ Academy, I saw the A Level Economics past papers page and would like to book a free demo class for A Level Economics. My name is ")
share=wa("A Level Economics (9708) past papers and mark schemes, 2020 to 2025: "+SITE+"/a-level-past-papers/economics-9708/")
total_files=sum(len(ts) for ts in T.values())*3*2*len(YEARS)
js=open(U+"07-Code & Scripts/sj-page-script.js").read().strip()
P="#sj.sj-p-pp-economics "
page=f'''<!-- SJ Academy A Level Economics (9708) past papers, Elementor HTML widget. Version 1.0, October 2026.
     Built on the shared stylesheet sj-brand.css 3.1.1 (already in Additional CSS). Family: Resource, on the dotted surface.
     Paste this whole file into one HTML widget on /a-level-past-papers/economics-9708/, replacing the old client-side tool.
     Section: full width, zero padding, no entrance animation. Page layout: Elementor Full Width. Hide Title: Yes.
     Every paper link is in the HTML, so search engines can read the full list. Files stay in the same storage folder.
     NOTE: the live page's old tool listed an Insert (IN) file for Paper 3 (Multiple Choice, A2), copied wholesale from
     the Business (9609) template's paperTypes object. Paper 3 is multiple choice; I could not confirm Cambridge issues
     a separate insert for ANY 9708 Economics paper, so this build has no IN links at all (qp + ms only, every paper).
     If 9708 does issue an insert for Paper 2 or Paper 4 (the data response papers), tell me and I will add it.
     This file is plain ASCII on purpose: symbols are written as codes so they cannot be garbled. -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>

<div id="sj" class="sj-p-pp-economics" data-family="resource">

  <!-- 1. HERO -->
  <section class="sj-section sj-bg-dots" data-sj-hero>
    <div class="sj-wrap">
      <nav class="sj-crumbs" aria-label="Breadcrumb"><ol><li><a href="{SITE}/">Home</a></li><li><a href="{SITE}/a-level-past-papers/">A Level past papers</a></li><li aria-current="page">Economics (9708)</li></ol></nav>
    </div>
    <div class="sj-wrap sj-grid sj-grid-hero">
      <div class="sj-stack">
        <h1 class="sj-h1"><span class="sj-pill"><span>Cambridge AS &amp; A Level &middot; 9708</span></span>A Level Economics past papers and <span class="sj-hl">mark schemes</span></h1>
        <p class="sj-lead sj-measure">Free Cambridge AS and A Level Economics (9708) past papers and mark schemes from 2020 to 2025, for Papers 1 to 4, multiple choice and data response.</p>
        <div class="sj-row"><span class="sj-chip sj-chip-yellow">Free, no sign-up</span><span class="sj-chip">Papers 1 to 4</span><span class="sj-updated">Updated October 2026</span></div>
      </div>
      <div class="sj-offset sj-stack">
        <h2 class="sj-h3">Jump to a year</h2>
        <div class="sjp-years">{jump}</div>
        <p class="sj-small sj-muted">May/June and Oct/Nov, all three variants, {total_files} files.</p>
        <p><a class="sj-link" href="{share}" target="_blank" rel="noopener" data-event="resource_share" data-loc="hero">Share this page on WhatsApp</a></p>
      </div>
    </div>
  </section>

  <!-- 2. PAPERS -->
  <section class="sj-section sj-bg-white" id="sjp-papers">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <h2 class="sj-h2">Economics (9708) past papers <span class="sj-hl">by year</span></h2>
        <p class="sjp-top">QP is the question paper and MS is the mark scheme. The two digits are the paper and the variant, so QP 12 is Paper 1, Variant 2.</p>
      </div>
      <div class="sj-stack" id="sjp-filter" hidden>
        <span class="sj-label" id="sjp-fl">Show</span>
        <div class="sj-choices" role="group" aria-labelledby="sjp-fl">
          <label class="sj-choice"><input type="radio" name="sjp-p" value="" checked><span>All papers</span></label>
          <label class="sj-choice"><input type="radio" name="sjp-p" value="1"><span>Paper 1</span></label>
          <label class="sj-choice"><input type="radio" name="sjp-p" value="2"><span>Paper 2</span></label>
          <label class="sj-choice"><input type="radio" name="sjp-p" value="3"><span>Paper 3</span></label>
          <label class="sj-choice"><input type="radio" name="sjp-p" value="4"><span>Paper 4</span></label>
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

  <!-- 3. HOW TO USE THEM -->
  <section class="sj-section sj-bg-dots">
    <div class="sj-wrap sjp-two">
      <div class="sj-stack">
        <div class="sj-eyebrow">How to use them</div>
        <h2 class="sj-h2">Past papers only work <span class="sj-hl">with marking</span></h2>
        <p class="sj-measure">Doing ten papers without marking them is ten rehearsals of the same mistakes. One paper, marked properly, teaches more.</p>
        <ol class="sj-steps">
          <li><b>Sit it under exam timing</b><span>Papers 1 and 3 are shorter multiple choice papers. Papers 2 and 4 are longer, with data response and essay questions.</span></li>
          <li><b>Mark it against the mark scheme</b><span>On Paper 2 and 4, check whether you used the data given, not only whether the economics was correct.</span></li>
          <li><b>Find the pattern in the lost marks</b><span>A missed evaluation point, a diagram not explained in words, or an answer that ignored the extract. That is what to fix next.</span></li>
          <li><b>Redo the same question type</b><span>Pick the same question from another variant and try again.</span></li>
        </ol>
      </div>
      <div class="sj-stack sjp-side">
        <div class="sj-paper">
          <div class="sj-paper-q"><small>How to read a file name</small>9708_s25_qp_12</div>
          <div class="sj-paper-a"><div>9708 <span class="sj-mark">Economics</span></div><div>s25 <span class="sj-mark">May/June 2025</span></div><div>qp <span class="sj-mark">question paper</span></div><div>12 <span class="sj-mark">Paper 1, Variant 2</span></div></div>
          <div class="sj-paper-note">w = Oct/Nov, ms = mark scheme</div>
        </div>
        <span class="sj-hand sj-tilt-r">mark it before you move on</span>
      </div>
    </div>
  </section>

  <!-- 4. RELATED RESOURCES -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">More for 9708</div>
        <h2 class="sj-h2">More A Level <span class="sj-hl">Economics resources</span></h2>
      </div>
      <div class="sj-grid sj-grid-4">
        <a class="sj-tile" href="{SITE}/a-level-economics-tuition/"><b>A Level Economics tuition</b><p>AS and A2 Economics classes at DHA Phase 7 and online.</p><span class="sj-link sj-link-go">See the class</span></a>
        <a class="sj-tile" href="{SITE}/blog/a-level-thresholds-guide/"><b>A Level grade thresholds</b><p>How raw marks convert to an A*, A or B grade.</p><span class="sj-link sj-link-go">Read the guide</span></a>
        <a class="sj-tile" href="{SITE}/blog/how-to-use-mark-scheme/"><b>How to use a mark scheme</b><p>The method for marking your own paper properly.</p><span class="sj-link sj-link-go">Read the guide</span></a>
        <a class="sj-tile" href="{SITE}/o-level-past-papers/economics-2281/"><b>O Level Economics past papers</b><p>Papers and mark schemes for the 2281 syllabus.</p><span class="sj-link sj-link-go">See O Level papers</span></a>
      </div>
      <div class="sj-stack">
        <h3 class="sj-h4">Past papers for other A Level subjects</h3>
        <div class="sj-row">{other}</div>
      </div>
    </div>
  </section>

  <!-- 5. FAQ -->
  <section class="sj-section sj-bg-canvas">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">FAQ</div>
        <h2 class="sj-h2">Questions about <span class="sj-hl">9708 past papers</span></h2>
      </div>
      <div class="sj-faq">
{faq_html}
      </div>
    </div>
  </section>

  <!-- 6. CLASS OFFER -->
  <section class="sj-section sj-bg-yellow">
    <div class="sj-wrap sj-stack sjp-final">
      <h2 class="sj-h2">Losing marks on the data response questions?</h2>
      <p class="sj-measure">That is usually technique, not knowledge. SJ Academy teaches A Level Economics in DHA Phase 7, Karachi, and live online, and marks your answers the way Cambridge does.</p>
      <div class="sj-row"><a class="sj-btn sj-btn-primary" href="{demo}" target="_blank" rel="noopener" data-loc="final_band">Book a free demo</a><a class="sj-btn sj-btn-ghost" href="{SITE}/a-level-economics-tuition/" data-loc="final_band">A Level Economics tuition</a></div>
    </div>
  </section>
</div>

<style>
/* Page-only layout for the Economics past papers page. Every rule is scoped to this page. */
{P}.sjp-top{{margin-top:var(--sj-s3)}}
{P}.sjp-year td a{{display:inline-flex;align-items:center;min-height:44px;padding:0 10px;margin:2px 4px 2px 0;border:1.5px solid var(--sj-ink);border-radius:var(--sj-r-md);background:#fff;font-size:15px;font-weight:500;color:var(--sj-ink);white-space:nowrap}}
{P}.sjp-year td a:hover{{background:var(--sj-yellow-light)}}
{P}.sjp-year>h3{{margin-top:var(--sj-s5)}}
{P}.sjp-year>.sjp-yh{{margin-top:0;color:var(--sj-muted)}}
{P}.sjp-year tr[hidden]{{display:none}}
{P}.sjp-two{{display:grid;gap:var(--sj-s6);grid-template-columns:minmax(0,1fr)}}
{P}.sj-paper-a .sj-mark{{float:right}}
{P}.sjp-final{{text-align:center;display:grid;justify-items:center}}
{P}.sjp-final .sj-row{{justify-content:center}}
{P}#sjp-papers,{P}.sjp-year{{scroll-margin-top:110px}}
{P}.sjp-years{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--sj-s3)}}
{P}.sjp-side{{display:grid;justify-items:center}}
{P}.sjp-side .sj-paper{{width:100%}}
@media (min-width:900px){{
  {P}.sjp-two{{grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:var(--sj-s7);align-items:center}}
}}
</style>

<script>
/* Page script for the Economics past papers page: year tabs start state, paper filter, new-tab downloads. */
(function(){{
  var root=document.getElementById('sj'); if(!root||!root.classList.contains('sj-p-pp-economics')) return;
  var each=function(list,fn){{Array.prototype.forEach.call(list,fn)}};
  var panels=root.querySelectorAll('.sjp-year');
  each(panels,function(p,i){{p.hidden=i>0}});
  document.getElementById('sjp-tabs').hidden=false;
  document.getElementById('sjp-filter').hidden=false;
  each(root.querySelectorAll('[data-sjp-year]'),function(a){{a.addEventListener('click',function(e){{
    var t=document.getElementById('sjp-t'+a.getAttribute('data-sjp-year')); if(!t) return;
    e.preventDefault();t.click();document.getElementById('sjp-papers').scrollIntoView({{behavior:'smooth'}});
  }})}});
  each(root.querySelectorAll('input[name="sjp-p"]'),function(i){{
    i.addEventListener('change',function(){{
      if(!i.checked) return;
      each(root.querySelectorAll('.sjp-year tr[data-paper]'),function(r){{r.hidden=!!i.value&&r.getAttribute('data-paper')!==i.value}});
    }});
  }});
  each(root.querySelectorAll('.sjp-year td a'),function(a){{a.target='_blank';a.setAttribute('download','');a.rel='noopener';a.setAttribute('data-loc','papers')}});
}})();
</script>

<script>
/* Standard page script, copied unchanged from 07-Code & Scripts/sj-page-script.js */
{js}
</script>

<script type="application/ld+json">{json.dumps(ld_col,ensure_ascii=True)}</script>
<script type="application/ld+json">{json.dumps(ld_crumbs,ensure_ascii=True)}</script>
<script type="application/ld+json">{json.dumps(ld_faq,ensure_ascii=True)}</script>
'''
assert all(ord(c)<128 for c in page)
open(OUT,'w').write(page)
print(len(page),page.count('.pdf">'),'gtag' in page,page.count('<h1'))
