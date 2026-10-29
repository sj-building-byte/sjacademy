import re,json,html
U="/mnt/user-data/uploads/Website Pages + Design/"
OUT="/mnt/user-data/outputs/a-level-business-past-papers-elementor-widget.html"
B="https://sjacademy.pk/file/Past-papers-storage/A+Level/Business+%289609%29"
YEARS=[2025,2024,2023,2022,2021,2020]
T={1:["qp","ms"],2:["qp","ms"],3:["qp","ms","in"],4:["qp","ms"]}
PN={1:"Business Concepts 1",2:"Business Concepts 2",3:"Business Decision-Making",4:"Business Strategy"}
LBL={"qp":"QP","ms":"MS","in":"IN"}
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
            links=' '.join(f'<a href="{B}/{folder}/9609_{s}{str(y)[2:]}_{t}_{p}{v}.pdf">{LBL[t]} {p}{v}</a>' for t in ts)
            tds.append(f'<td data-label="Variant {v}"><span>{links}</span></td>')
        rows.append(f'<tr data-paper="{p}"><td data-label="Paper"><span><b>Paper {p}</b> <span class="sj-muted">{PN[p]}</span></span></td>{"".join(tds)}</tr>')
    return f'''<h3 class="sj-h3">{name} {y}</h3>
<div class="sj-table-wrap"><table class="sj-table sj-table-stack"><thead><tr><th scope="col">Paper</th><th scope="col">Variant 1</th><th scope="col">Variant 2</th><th scope="col">Variant 3</th></tr></thead><tbody>
{chr(10).join(rows)}
</tbody></table></div>'''
tabs='\n'.join(f'<button role="tab" id="sjp-t{y}" aria-controls="sjp-y{y}" aria-selected="{"true" if i==0 else "false"}"{"" if i==0 else " tabindex=\"-1\""}>{y}</button>' for i,y in enumerate(YEARS))
panels='\n'.join(f'<div class="sj-tabpanel sj-stack sjp-year" role="tabpanel" id="sjp-y{y}" aria-labelledby="sjp-t{y}">\n<h3 class="sj-h4 sjp-yh">A Level Business past papers {y}</h3>\n{table(y,"s")}\n{table(y,"w")}\n</div>' for y in YEARS)
TICK='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg>'
FAQ=[
("Are these A Level Business past papers free?","Yes. Every question paper, mark scheme and insert on this page is free to open and download. You do not need to sign up."),
("Which years of 9609 past papers are on this page?","This page has Cambridge AS and A Level Business (9609) past papers from 2020 to 2025, for the May/June and Oct/Nov series, Papers 1 to 4, in all three variants."),
("Are Business and Business Studies past papers the same?","Yes. Cambridge calls the subject Business, with the syllabus code 9609. Many students and schools still call it Business Studies. The papers on this page are the ones you need for either name."),
("How do I read a 9609 past paper file name?","Every file follows the Cambridge pattern 9609_s25_qp_12. The letter is the session (s = May/June, w = Oct/Nov), the two digits are the year, qp is the question paper and ms is the mark scheme. The last two digits are the paper number followed by the variant, so 12 means Paper 1, Variant 2."),
("Which variant should I practise?","Cambridge sets different variants of the same paper for different time zones. They test the same syllabus to the same standard, so practise every variant from a session. It gives you three papers to practise from each series."),
("How should I use the mark schemes?",f'Attempt the paper under timed conditions first, then mark it yourself against the mark scheme. Note where you lost marks for missing application or structure, not only for wrong answers. Our guide on <a class="sj-link" href="{SITE}/blog/how-to-use-mark-scheme/">how to use a Cambridge mark scheme</a> walks through the method, and our <a class="sj-link" href="{SITE}/blog/a-level-thresholds-guide/">A Level grade thresholds guide</a> explains how raw marks convert to grades.'),
("Do you have A Level Business topical past papers?",f'Not on this page. Papers here are listed by year and series. For practice by topic, use the free <a class="sj-link" href="{SITE}/a-level-business-quiz/">chapter-wise Business quizzes</a> and the <a class="sj-link" href="{SITE}/a-level-business-9609-definitions/">9609 definitions</a>.'),
]
faq_html='\n'.join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><div class="sj-faq-a"><p>{a}</p></div></details>' for i,(q,a) in enumerate(FAQ))
strip=lambda t: html.unescape(re.sub(r'<[^>]+>','',t)).strip()
ld_faq={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in FAQ]}
ld_crumbs={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},{"@type":"ListItem","position":2,"name":"A Level past papers","item":SITE+"/a-level-past-papers/"},{"@type":"ListItem","position":3,"name":"Business (9609)","item":SITE+"/a-level-past-papers/business-9609/"}]}
ld_col={"@context":"https://schema.org","@type":"CollectionPage","name":"A Level Business (9609) past papers and mark schemes, 2020 to 2025","url":SITE+"/a-level-past-papers/business-9609/","inLanguage":"en","about":"Cambridge International AS and A Level Business (9609)","publisher":{"@type":"EducationalOrganization","name":"SJ Academy","url":SITE+"/"}}
OTHER=[("accounts-9706","Accounts (9706)"),("biology-9700","Biology (9700)"),("chemistry-9701","Chemistry (9701)"),("computer-science-9618","Computer Science (9618)"),("economics-9708","Economics (9708)"),("english-9695","English (9695)"),("law-9084","Law (9084)"),("mathematics-9709","Mathematics (9709)"),("physics-9702","Physics (9702)"),("psychology-9990","Psychology (9990)"),("sociology-9699","Sociology (9699)"),("urdu-9686","Urdu (9686)")]
other=' '.join(f'<a class="sj-chip" href="{SITE}/a-level-past-papers/{s}/">{n}</a>' for s,n in OTHER)
jump=''.join(f'<a class="sj-btn sj-btn-ghost" href="#sjp-y{y}" data-sjp-year="{y}" data-loc="hero">{y}</a>' for y in YEARS)
demo=wa("Hi SJ Academy, I saw the A Level Business past papers page and would like to book a free demo class for A Level Business. My name is ")
share=wa("A Level Business (9609) past papers and mark schemes, 2020 to 2025: "+SITE+"/a-level-past-papers/business-9609/")
js=open(U+"07-Code & Scripts/sj-page-script.js").read().strip()
P="#sj.sj-p-pp-business "
page=f'''<!-- SJ Academy A Level Business (9609) past papers, Elementor HTML widget. Version 1.0, October 2026.
     Built on the shared stylesheet sj-brand.css 3.1.1 (already in Additional CSS). Family: Resource, on the dotted surface (owner decision, 7 October 2026).
     Paste this whole file into one HTML widget on /a-level-past-papers/business-9609/, replacing the old tool.
     Section: full width, zero padding, no entrance animation. Page layout: Elementor Full Width. Hide Title: Yes.
     Every paper link is in the HTML, so search engines can read the full list. Files stay in the same storage folder.
     This file is plain ASCII on purpose: symbols are written as codes so they cannot be garbled. -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>

<div id="sj" class="sj-p-pp-business" data-family="resource">

  <!-- 1. HERO -->
  <section class="sj-section sj-bg-dots" data-sj-hero>
    <div class="sj-wrap">
      <nav class="sj-crumbs" aria-label="Breadcrumb"><ol><li><a href="{SITE}/">Home</a></li><li><a href="{SITE}/a-level-past-papers/">A Level past papers</a></li><li aria-current="page">Business (9609)</li></ol></nav>
    </div>
    <div class="sj-wrap sj-grid sj-grid-hero">
      <div class="sj-stack">
        <h1 class="sj-h1"><span class="sj-pill"><span>Cambridge AS &amp; A Level &middot; 9609</span></span>A Level Business past papers and <span class="sj-hl">mark schemes</span></h1>
        <p class="sj-lead sj-measure">Free Cambridge AS and A Level Business (9609) past papers, mark schemes and inserts from 2020 to 2025, for Papers 1 to 4. Still call it Business Studies? Same subject, same papers.</p>
        <div class="sj-row"><span class="sj-chip sj-chip-yellow">Free, no sign-up</span><span class="sj-chip">Papers 1 to 4</span><span class="sj-updated">Updated October 2026</span></div>
      </div>
      <div class="sj-offset sj-stack">
        <h2 class="sj-h3">Jump to a year</h2>
        <div class="sjp-years">{jump}</div>
        <p class="sj-small sj-muted">May/June and Oct/Nov, all three variants, 324 files.</p>
        <p><a class="sj-link" href="{share}" target="_blank" rel="noopener" data-event="resource_share" data-loc="hero">Share this page on WhatsApp</a></p>
      </div>
    </div>
  </section>

  <!-- 2. PAPERS -->
  <section class="sj-section sj-bg-white" id="sjp-papers">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <h2 class="sj-h2">Business (9609) past papers <span class="sj-hl">by year</span></h2>
        <p class="sjp-top">QP is the question paper, MS is the mark scheme and IN is the insert with the Paper 3 case study. The two digits are the paper and the variant, so QP 12 is Paper 1, Variant 2.</p>
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
          <li><b>Sit it under exam timing</b><span>Paper 1 and Paper 4 are 1 hour 15 minutes. Paper 2 is 1 hour 30 minutes. Paper 3 is 1 hour 45 minutes.</span></li>
          <li><b>Mark it against the mark scheme</b><span>Go line by line. Give yourself the mark only if the mark scheme would.</span></li>
          <li><b>Find the pattern in the lost marks</b><span>Missing application, a chain that stops early, or evaluation that says "it depends". That is what to fix next.</span></li>
          <li><b>Redo the weak question type</b><span>Pick the same question size from another variant and try again.</span></li>
        </ol>
      </div>
      <div class="sj-stack sjp-side">
        <div class="sj-paper">
          <div class="sj-paper-q"><small>How to read a file name</small>9609_s25_qp_12</div>
          <div class="sj-paper-a"><div>9609 <span class="sj-mark">Business</span></div><div>s25 <span class="sj-mark">May/June 2025</span></div><div>qp <span class="sj-mark">question paper</span></div><div>12 <span class="sj-mark">Paper 1, Variant 2</span></div></div>
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
        <div class="sj-eyebrow">More for 9609</div>
        <h2 class="sj-h2">More A Level <span class="sj-hl">Business resources</span></h2>
      </div>
      <div class="sj-grid sj-grid-4">
        <a class="sj-tile" href="{SITE}/a-level-business-9609-solved-past-papers-2025/"><b>Solved Business past papers, 2025</b><p>24 papers and 199 questions, solved for Papers 1 to 4. Paid PDF.</p><span class="sj-link sj-link-go">See the solved papers</span></a>
        <a class="sj-tile" href="{SITE}/a-level-business-9609-definitions/"><b>A Level Business definitions</b><p>AS and A2 definitions for Papers 1 to 4. Free.</p><span class="sj-link sj-link-go">Get the definitions</span></a>
        <a class="sj-tile" href="{SITE}/a-level-business-quiz/"><b>Business quizzes</b><p>Short chapter-wise quizzes with instant marking. Free.</p><span class="sj-link sj-link-go">Take a quiz</span></a>
        <a class="sj-tile" href="{SITE}/blog/how-to-answer-20-mark-business-question-a-level/"><b>The 20-mark question</b><p>How to plan and write the Paper 4 strategy essay.</p><span class="sj-link sj-link-go">Read the guide</span></a>
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
        <h2 class="sj-h2">Questions about <span class="sj-hl">9609 past papers</span></h2>
      </div>
      <div class="sj-faq">
{faq_html}
      </div>
    </div>
  </section>

  <!-- 6. CLASS OFFER -->
  <section class="sj-section sj-bg-yellow">
    <div class="sj-wrap sj-stack sjp-final">
      <h2 class="sj-h2">Stuck on the same question type every paper?</h2>
      <p class="sj-measure">That is usually technique, not knowledge. Sir Sunyyan Junaid teaches A Level Business in DHA Phase 7, Karachi, and live online, and marks your answers the way Cambridge does.</p>
      <div class="sj-row"><a class="sj-btn sj-btn-primary" href="{demo}" target="_blank" rel="noopener" data-loc="final_band">Book a free demo</a><a class="sj-btn sj-btn-ghost" href="{SITE}/a-level-business-tuition/" data-loc="final_band">A Level Business tuition</a></div>
    </div>
  </section>
</div>

<style>
/* Page-only layout for the Business past papers page. Every rule is scoped to this page. */
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
/* Page script for the Business past papers page: year tabs start state, paper filter, new-tab downloads. */
(function(){{
  var root=document.getElementById('sj'); if(!root||!root.classList.contains('sj-p-pp-business')) return;
  var each=function(list,fn){{Array.prototype.forEach.call(list,fn)}};
  /* all years are in the page; with scripts on, show one year at a time */
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
