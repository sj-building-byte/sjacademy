#!/usr/bin/env python3
"""Assembles the WooCommerce-driven /ebooks/ library widget. Run once; the page then updates itself from WooCommerce."""
import json
from urllib.parse import quote

SITE = "https://www.sjacademy.pk"
WA = "https://wa.me/923362144454?text="
here = __file__.rsplit("/", 1)[0]


def wa(t):
    return WA + quote(t, safe="")


DEMO = wa("Hi SJ Academy, I'd like to book a free demo class.\nLevel: \nSubject: \nSession: \nMode (in class or online): \n(Ref: EBOOKS)\nMy name is ")
REQUEST = wa("Hi SJ Academy, I'd like notes or an ebook for this subject and topic: \n(Ref: EB-REQUEST)\nMy name is ")
QUESTION = wa("Hi SJ Academy, I have a question about your ebooks and notes.\n(Ref: EBOOKS)\nMy name is ")
POPUP = "#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D"
TICK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg>'

FAQ = [
    ("Are SJ Academy ebooks and notes free?",
     "Most are. Free items say Free on the card; some ask for your details in a short form first, others download straight away. Paid items show their price on the card before you click anything.", None),
    ("What is the difference between ebooks, notes and other resources?",
     "Ebooks are complete books: a full topic guide or a full set of solved past papers. Notes are chapter-by-chapter summaries for revision. Other resources are the quick tools: formula sheets, worksheets and answer planners.", None),
    ("How do I pay for paid ebooks or notes?",
     "Tap the button on the card, read what is inside, then tap Buy now and you go straight to checkout on sjacademy.pk. Pay once, in Pakistani rupees, with a credit or debit card, SadaPay, JazzCash, Easypaisa and more, through SmartPay, the secure payment gateway on our site.", None),
    ("When do I get the PDF after paying?",
     "Straight away. The download link shows on the order confirmation page and is also sent to the email address you enter at checkout.", None),
    ("Can I print them?",
     "Yes. Print them, annotate them, highlight them until the pages are more yellow than white. They are for your own study, so please send friends to this page instead of forwarding the file.", None),
    ("Are these official Cambridge materials?",
     "No. SJ Academy is an independent tuition centre in Karachi and is not affiliated with or endorsed by Cambridge. Our teachers write these for the Cambridge O Level and A Level syllabuses they teach.", None),
    ("Can you make notes for my subject?",
     "Tell us on WhatsApp which subject and topic you want. Requests decide what we write next.", None),
    ("What if a paid download does not work?",
     'Message us on WhatsApp with your order number and we will sort it out. Refunds follow our <a class="sj-link" href="%s/refund-policy/">refund policy</a>.' % SITE,
     "Message us on WhatsApp with your order number and we will sort it out. Refunds follow our refund policy."),
]
faq_html = "\n".join('<details%s><summary>%s</summary><div class="sj-faq-a"><p>%s</p></div></details>'
                     % (" open" if n == 0 else "", q, a) for n, (q, a, _) in enumerate(FAQ))
ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": pl or a}} for q, a, pl in FAQ]}
ld_crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
    {"@type": "ListItem", "position": 2, "name": "Ebooks and notes", "item": SITE + "/ebooks/"}]}

skel = "".join('<div class="sjk-skel" aria-hidden="true"><span class="sj-skel"></span><span class="sj-skel" style="width:70%"></span><span class="sj-skel"></span><span class="sj-skel" style="width:40%"></span><span class="sj-skel"></span></div>' for _ in range(4))

HTML = """<!-- SJ Academy ebooks and notes library, Elementor HTML widget. Version 2.0, October 2026.
     Page: /ebooks/ (address unchanged). Family: Resource. Needs the shared stylesheet sj-brand.css 3.1.1.
     Build: Elementor Full Width, Hide Title = Yes. One HTML widget in a full-width section, zero padding, no entrance animation.

     THE SHELF FILLS ITSELF FROM WOOCOMMERCE. Do not edit this widget to add a book. Add a product instead:
       Category  SJ Library  (slug sj-library). Only products in this category appear.
       Tags      one level:   A Level, O Level, IGCSE or SAT
                 one subject: Business, Maths, Physics, Chemistry, Economics ... (any other tag is read as the subject; its name shows in the Subject filter)
                 type:        Notes or Resource (no type tag = ebook)
                 Coming soon  shows the card as Coming soon with a WhatsApp notify button
       Free item   External/Affiliate product. Product URL = its landing page (with the form) or a PDF. No price.
       Paid item   Simple, Virtual, Downloadable product with a price. Tick Sold individually.
                   Custom attribute "Landing page" = full URL of its landing page (else the card goes straight to checkout).
       Optional custom attributes (Visible on product page ticked): "Syllabus code" (9609), "Details" (88 pages / Papers 1 to 4).
       Short description = the one or two lines on the card. Product image = the cover. Order = Products > Sorting (menu order).
     Filters accept URL parameters: /ebooks/?type=notes, ?subject=maths, ?level=o-level, ?status=free.
     This file is plain ASCII on purpose. -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>

<div id="sj" class="sj-p-ebooks" data-family="resource">

  <!-- 1. HERO -->
  <section class="sj-section sj-bg-dots" data-sj-hero>
    <div class="sj-wrap">
      <nav class="sj-crumbs" aria-label="Breadcrumb"><ol><li><a href="SITE/">Home</a></li><li aria-current="page">Ebooks and notes</li></ol></nav>
    </div>
    <div class="sj-wrap sjk-hero">
      <div class="sj-stack">
        <h1 class="sj-h1"><span class="sj-pill"><span>O &amp; A Level ebooks and notes &middot; PDF</span></span>Study material that shows you <span class="sj-hl">where marks</span> come from</h1>
        <p class="sj-lead sj-measure">Solved past papers, topic guides and revision notes, written by the teachers who mark answers at SJ Academy every week. Most of it is free. Download, print, scribble all over it.</p>
        <div class="sj-row"><a class="sj-btn sj-btn-primary" href="#sjk-shelf" data-loc="hero">Browse the library</a></div>
        <p class="sj-small"><a class="sj-link sj-link-go" href="SITE/a-level-business-9609-solved-past-papers-2025/" data-loc="hero">Start with the free Business solved papers</a></p>
      </div>
      <div class="sjk-pile" id="sjk-pile" aria-hidden="true"></div>
    </div>
  </section>

  <!-- 2. THE LIBRARY (filled from WooCommerce) -->
  <section class="sj-section sj-bg-white" id="sjk-shelf">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">The library</div>
        <h2 class="sj-h2">Pick what you need, <span class="sj-hl">skip the rest</span></h2>
      </div>

      <div>
        <div id="sjk-tabs"></div>
        <div class="sj-tabpanel sj-stack">
          <div class="sj-filterbar sjk-filters">
            <div class="sj-field"><label class="sj-label" for="sjk-q">Search</label><div class="sj-search"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg><input class="sj-input" id="sjk-q" type="search" placeholder="Try 9609, quadratics, Paper 5" autocomplete="off"></div></div>
            <div class="sj-field"><label class="sj-label" for="sjk-level">Level</label><select class="sj-select" id="sjk-level"><option value="all">All levels</option></select></div>
            <div class="sj-field"><label class="sj-label" for="sjk-subject">Subject</label><select class="sj-select" id="sjk-subject"><option value="all">All subjects</option></select></div>
          </div>
          <fieldset class="sjk-status"><legend class="sj-vh">Show</legend><div class="sj-choices">
            <label class="sj-choice"><input type="radio" name="sjk-status" value="all" checked><span>All</span></label>
            <label class="sj-choice"><input type="radio" name="sjk-status" value="free"><span>Free</span></label>
            <label class="sj-choice"><input type="radio" name="sjk-status" value="paid"><span>Paid</span></label>
            <label class="sj-choice"><input type="radio" name="sjk-status" value="soon"><span>Coming soon</span></label>
          </div></fieldset>
        </div>
        <p class="sj-small sj-muted sjk-count" id="sjk-count" aria-live="polite">Loading the library&hellip;</p>
      </div>

      <div class="sjk-grid" id="sjk-grid" aria-busy="true">SKEL</div>

      <div class="sjk-more-wrap" id="sjk-more-wrap" hidden><button type="button" class="sj-btn sj-btn-ghost" id="sjk-more">Show all</button></div>

      <div class="sj-empty" id="sjk-empty" hidden>
        <b>Nothing on this shelf yet</b>
        <p>Nothing matches those filters. Clear them, or tell us what you want us to make next.</p>
        <div class="sj-row" style="justify-content:center"><button type="button" class="sj-btn sj-btn-ghost sj-btn-sm" id="sjk-reset">Clear filters</button><a class="sj-btn sj-btn-wa sj-btn-sm" href="REQUEST" target="_blank" rel="noopener" data-loc="shelf_empty">Request it on WhatsApp</a></div>
      </div>

      <div class="sj-empty" id="sjk-error" hidden>
        <b>The library did not load</b>
        <p>That is on us, not your Wi-Fi. Refresh the page, or message us and we will send you what you need.</p>
        <div class="sj-row" style="justify-content:center"><button type="button" class="sj-btn sj-btn-ghost sj-btn-sm" onclick="location.reload()">Refresh</button><a class="sj-btn sj-btn-wa sj-btn-sm" href="QUESTION" target="_blank" rel="noopener" data-loc="shelf_error">WhatsApp us</a></div>
      </div>
    </div>
  </section>

  <!-- 3. HOW GETTING ONE WORKS -->
  <section class="sj-section sj-bg-brown">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">How it works</div>
        <h2 class="sj-h2">From this page to your <span class="sj-hl">phone in a minute</span></h2>
      </div>
      <div class="sj-grid sj-grid-2">
        <div class="sj-stack">
          <h3 class="sj-h3">Free</h3>
          <ol class="sj-steps">
            <li><b>Tap the button on a free card</b><span>Get it free or Download PDF.</span></li>
            <li><b>Fill a short form, if it asks</b><span>Some items ask for your details first. Others download straight away.</span></li>
            <li><b>Open the PDF</b><span>On your phone, your laptop, or printed and stapled.</span></li>
          </ol>
        </div>
        <div class="sj-stack">
          <h3 class="sj-h3">Paid</h3>
          <ol class="sj-steps">
            <li><b>See what is inside</b><span>The price is on the card before you click. No surprises at checkout.</span></li>
            <li><b>Pay your way</b><span>Credit or debit card, SadaPay, JazzCash, Easypaisa and more, through SmartPay's secure checkout. In rupees, paid once.</span></li>
            <li><b>Download straight after paying</b><span>The link shows on the confirmation page and lands in your email.</span></li>
          </ol>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. WHO WRITES THEM + REQUEST -->
  <section class="sj-section sj-bg-dots">
    <div class="sj-wrap sjk-two">
      <div class="sj-stack">
        <div class="sj-eyebrow">Who writes them</div>
        <h2 class="sj-h2">Written by teachers, <span class="sj-hl">not textbooks</span></h2>
        <p class="sj-measure">Our teachers teach these subjects every week, in DHA Phase 7, Karachi, and live online. What they write holds what they keep explaining in class: how an answer is structured, the step students skip, the definition that drops a mark because one word is missing.</p>
        <ul class="sj-ticks sj-measure">
          <li>TICK<span>Written for the Cambridge syllabus code on the cover</span></li>
          <li>TICK<span>Answers in full, not bullet points copied from a mark scheme</span></li>
          <li>TICK<span>PDFs that work on a phone and print cleanly</span></li>
        </ul>
      </div>
      <div class="sj-stack sjk-side">
        <div class="sj-offset sj-stack">
          <h3 class="sj-h3">Missing your subject?</h3>
          <p>Tell us the subject and the topic that is giving you trouble. Requests decide what we write next.</p>
          <p><a class="sj-btn sj-btn-wa sj-btn-block" href="REQUEST" target="_blank" rel="noopener" data-loc="request">Request notes on WhatsApp</a></p>
        </div>
        <span class="sj-hand sj-tilt-r">the more of you ask, the faster it gets written</span>
      </div>
    </div>
  </section>

  <!-- 5. FAQ -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">FAQ</div>
        <h2 class="sj-h2">Questions about the <span class="sj-hl">library</span></h2>
      </div>
      <div class="sj-faq">
FAQ
      </div>
    </div>
  </section>

  <!-- 6. MORE FREE RESOURCES -->
  <section class="sj-section sj-bg-canvas">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">More free stuff</div>
        <h2 class="sj-h2">Free tools, <span class="sj-hl">no form</span></h2>
      </div>
      <div class="sj-grid sj-grid-4">
        <a class="sj-tile" href="SITE/a-level-past-papers/"><b>A Level past papers</b><p>Question papers and mark schemes by subject.</p><span class="sj-link sj-link-go">Open A Level papers</span></a>
        <a class="sj-tile" href="SITE/o-level-past-papers/"><b>O Level past papers</b><p>Question papers and mark schemes by subject.</p><span class="sj-link sj-link-go">Open O Level papers</span></a>
        <a class="sj-tile" href="SITE/university-admission-criteria-tool/"><b>University admission criteria</b><p>See what your target university asks for.</p><span class="sj-link sj-link-go">Check the criteria</span></a>
        <a class="sj-tile" href="SITE/a-level-business-quiz/"><b>Business quizzes</b><p>Chapter-wise A Level Business quizzes with instant marking.</p><span class="sj-link sj-link-go">Take a quiz</span></a>
      </div>
      <p class="sj-small sj-muted sj-measure">SJ Academy is an independent tuition centre and is not affiliated with or endorsed by Cambridge. Question wording belongs to Cambridge University Press &amp; Assessment.</p>
    </div>
  </section>

  <!-- 7. CLASS OFFER -->
  <section class="sj-section sj-bg-yellow">
    <div class="sj-wrap sj-stack sjk-final">
      <h2 class="sj-h2">Notes can't mark your answer. We can.</h2>
      <p class="sj-measure">Reading model answers helps. Having your own answers marked, with the lost marks shown, helps faster. O and A Level classes in DHA Phase 7, Karachi, and live online.</p>
      <div class="sj-row"><a class="sj-btn sj-btn-primary" href="DEMO" target="_blank" rel="noopener" data-loc="final_band">Book a free demo on WhatsApp</a></div>
      <p><a class="sj-link" href="POPUP" data-loc="final_band">or register for a class</a></p>
    </div>
  </section>

  <!-- Phone bottom bar -->
  <div class="sj-bar">
    <a class="sj-btn sj-btn-primary" href="#sjk-shelf" data-loc="bottom_bar">Browse library</a>
    <a class="sj-btn sj-btn-wa" href="QUESTION" target="_blank" rel="noopener" data-loc="bottom_bar">WhatsApp us</a>
  </div>
</div>

STYLE

<script>
/* Standard page script, copied unchanged from 02 Website/Scripts/sj-page-script.js */
PAGESCRIPT
</script>

<script>
LIBSCRIPT
</script>

<script type="application/ld+json">LDCRUMBS</script>
<script type="application/ld+json">LDFAQ</script>
"""

LIBSCRIPT = r"""/* Library: reads products in the WooCommerce category sj-library from the public Store API and draws the shelf.
   Cached for 5 minutes per visitor. Reads ?type=, ?subject=, ?level=, ?status=, ?q= from the address. */
(function(){
  var root=document.querySelector('#sj.sj-p-ebooks');
  if(!root){return;}
  var API='/wp-json/wc/store/v1/products?per_page=100&orderby=menu_order&order=asc';
  var CAT='sj-library',CACHE='sjk-lib-v2',TTL=300000;
  var WA='https://wa.me/923362144454?text=';
  var LEVELS={'a-level':'A Level','o-level':'O Level','igcse':'IGCSE','sat':'SAT'};
  var LEVEL_ORDER=['a-level','o-level','igcse','sat'];
  var TYPES={'ebook':'Ebook','notes':'Notes','resource':'Resource'};
  var TABS=[['all','All'],['ebook','Ebooks'],['notes','Notes'],['resource','Resources']];
  var SKIP={'coming-soon':1,'notes':1,'resource':1,'ebook':1,'free':1,'paid':1};
  var TICK='<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>';
  var DOT=' \u00b7 ';
  var grid=root.querySelector('#sjk-grid'),pile=root.querySelector('#sjk-pile'),tabsBox=root.querySelector('#sjk-tabs');
  var q=root.querySelector('#sjk-q'),lv=root.querySelector('#sjk-level'),sb=root.querySelector('#sjk-subject');
  var count=root.querySelector('#sjk-count'),empty=root.querySelector('#sjk-empty'),errBox=root.querySelector('#sjk-error');
  var reset=root.querySelector('#sjk-reset'),more=root.querySelector('#sjk-more'),moreWrap=root.querySelector('#sjk-more-wrap');
  var radios=Array.prototype.slice.call(root.querySelectorAll('input[name="sjk-status"]'));
  var LIMIT=window.matchMedia('(max-width:599px)').matches?6:8,open=false,items=[],tabs=[];

  var parser=new DOMParser();
  var text=function(html){return (parser.parseFromString(html||'','text/html').body.textContent||'').replace(/\s+/g,' ').trim();};
  var esc=function(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');};
  var attr=function(p,name){
    var a=(p.attributes||[]).filter(function(x){return text(x.name).toLowerCase()===name;})[0];
    if(!a||!a.terms||!a.terms.length){return '';}
    return a.terms.map(function(t){return text(typeof t==='string'?t:(t.name||''));}).join(', ');
  };

  /* Turn one Store API product into the shape the cards need */
  var shape=function(p){
    var tags=(p.tags||[]).map(function(t){return {slug:t.slug,name:text(t.name)};});
    var has=function(s){return tags.some(function(t){return t.slug===s;});};
    var level='',subject='',subjectName='';
    tags.forEach(function(t){
      if(LEVELS[t.slug]){if(!level){level=t.slug;}}
      else if(!SKIP[t.slug]&&!subject){subject=t.slug;subjectName=t.name;}
    });
    var pr=p.prices||{},minor=Math.pow(10,pr.currency_minor_unit||0),val=parseInt(pr.price||'0',10)/minor;
    var label=(pr.currency_code==='PKR'?'Rs. ':text(pr.currency_prefix||''))+val.toLocaleString('en-US')+text(pr.currency_suffix||'');
    var url=text((p.add_to_cart&&p.add_to_cart.url)||'');
    var img=(p.images||[])[0]||null;
    return {
      id:p.id,slug:p.slug,name:text(p.name),desc:text(p.short_description),
      type:has('notes')?'notes':has('resource')?'resource':'ebook',
      level:level||'a-level',subject:subject||'other',subjectName:subjectName||'Other',
      soon:has('coming-soon'),paid:val>0,price:val,priceLabel:label,currency:pr.currency_code||'PKR',
      external:p.type==='external',url:url,landing:attr(p,'landing page'),
      code:attr(p,'syllabus code'),details:attr(p,'details'),
      img:img?{src:img.src,srcset:img.srcset||'',alt:text(img.alt)||('Cover of '+text(p.name))}:null
    };
  };

  var waNotify=function(it){return WA+encodeURIComponent('Hi SJ Academy, please tell me when '+it.name+' is out.\n(Ref: EB-SOON-'+it.id+')\nMy name is ');};

  var cover=function(it){
    if(it.img){return '<img src="'+esc(it.img.src)+'"'+(it.img.srcset?' srcset="'+esc(it.img.srcset)+'" sizes="(min-width:1200px) 330px,(min-width:600px) 45vw,92vw"':'')+' alt="'+esc(it.img.alt)+'" width="1280" height="720" loading="lazy" decoding="async">';}
    return '<div class="sjk-gen" aria-hidden="true"><b>'+esc(it.code||LEVELS[it.level]||'SJ')+'</b><small>'+({ebook:'SJ Academy',notes:'Notes',resource:'Resource'})[it.type]+'</small></div>';
  };

  var card=function(it){
    var cls='sjk-book sjk-t-'+it.type+(it.soon?' is-soon':'')+(it.paid&&!it.soon?' is-paid':'');
    var tag,price,act;
    if(it.soon){
      tag='soon';
      price='<p class="sjk-price">Coming soon</p>';
      act='<a class="sj-btn sj-btn-ghost sj-btn-block" href="'+esc(waNotify(it))+'" target="_blank" rel="noopener" data-loc="shelf_'+it.id+'">Notify me on WhatsApp</a>';
    }else if(it.paid){
      tag=it.priceLabel;
      price='<p class="sjk-price"><b>'+esc(it.priceLabel)+'</b> <span>one-time'+DOT+'instant PDF</span></p>';
      var href=it.landing||('/checkout/?add-to-cart='+it.id);
      var label=it.landing?'Get it for '+it.priceLabel:'Buy now';
      act='<a class="sj-btn sj-btn-primary sj-btn-block" href="'+esc(href)+'" data-event="ebook_buy" data-loc="shelf_'+it.id+'">'+esc(label)+'</a>'+
          '<p class="sjk-secure">'+TICK+' Secure checkout with SmartPay</p><p class="sjk-methods">Card'+DOT+'SadaPay'+DOT+'JazzCash'+DOT+'Easypaisa</p>';
    }else{
      tag='free';
      price='<p class="sjk-price">Free</p>';
      var pdf=/\.pdf(\?|$)/i.test(it.url);
      var go=it.url||('/product/'+it.slug+'/');
      act='<a class="sj-btn sj-btn-primary sj-btn-block" href="'+esc(go)+'"'+(pdf?' download':' data-event="ebook_free"')+' data-loc="shelf_'+it.id+'">'+(pdf?'Download PDF':(it.type==='notes'?'Get the notes':'Get it free'))+'</a>';
    }
    var kicker=TYPES[it.type]+DOT+(LEVELS[it.level]||'')+(it.code?DOT+it.code:'');
    return '<article class="'+cls+'" data-type="'+it.type+'" data-status="'+(it.soon?'soon':'out')+'" data-price="'+(it.paid?'paid':'free')+'" data-level="'+esc(it.level)+'" data-subject="'+esc(it.subject)+'" data-keys="'+esc((it.subjectName+' '+it.code+' '+it.details).toLowerCase())+'">'+
      '<div class="sjk-cover sj-tagged">'+cover(it)+'<span class="sj-tag">'+esc(tag)+'</span></div>'+
      '<div class="sjk-body"><span class="sjk-kicker">'+esc(kicker)+'</span><h3 class="sj-h4">'+esc(it.name)+'</h3>'+
      (it.desc?'<p class="sjk-desc">'+esc(it.desc)+'</p>':'')+(it.details?'<p class="sjk-meta">'+esc(it.details)+'</p>':'')+price+
      '<div class="sjk-act">'+act+'</div></div></article>';
  };

  /* "All" view: available items first, mixing types so the first row shows ebooks, notes and resources together; coming soon last */
  var order=function(list){
    var out=list.filter(function(i){return !i.soon;}),soon=list.filter(function(i){return i.soon;});
    var qs=['ebook','notes','resource'].map(function(t){return out.filter(function(i){return i.type===t;});}),mixed=[];
    while(qs.some(function(x){return x.length;})){qs.forEach(function(x){if(x.length){mixed.push(x.shift());}});}
    return mixed.concat(soon);
  };

  var fillSelect=function(sel,pairs){pairs.forEach(function(p){var o=document.createElement('option');o.value=p[0];o.textContent=p[1];sel.appendChild(o);});};

  var type=function(){for(var i=0;i<tabs.length;i++){if(tabs[i].getAttribute('aria-selected')==='true'){return tabs[i].getAttribute('data-type');}}return 'all';};
  var pickType=function(v){tabs.forEach(function(t){var on=t.getAttribute('data-type')===v;t.setAttribute('aria-selected',on?'true':'false');t.tabIndex=on?0:-1;});};
  var status=function(){for(var i=0;i<radios.length;i++){if(radios[i].checked){return radios[i].value;}}return 'all';};
  var low=function(s){return (s||'').toLowerCase();};

  var run=function(){
    var t=low(q.value).replace(/^\s+|\s+$/g,''),ty=type(),l=lv.value,s=sb.value,x=status(),n=0;
    var cap=!open&&!t&&ty==='all'&&l==='all'&&s==='all'&&x==='all';
    items.forEach(function(b){
      var d=b.dataset,ok=true;
      if(ty!=='all'&&d.type!==ty){ok=false;}
      if(l!=='all'&&d.level!==l){ok=false;}
      if(s!=='all'&&d.subject!==s){ok=false;}
      if(x==='free'&&!(d.price==='free'&&d.status==='out')){ok=false;}
      if(x==='paid'&&d.price!=='paid'){ok=false;}
      if(x==='soon'&&d.status!=='soon'){ok=false;}
      if(t&&low(b.textContent+' '+d.keys).indexOf(t)<0){ok=false;}
      if(ok){n++;}
      b.hidden=!ok||(cap&&n>LIMIT);
    });
    moreWrap.hidden=!(cap&&n>LIMIT);
    more.textContent='Show all '+items.length;
    var shown=items.filter(function(b){return !b.hidden;}).length;
    count.textContent=shown===items.length?'Showing all '+shown:'Showing '+shown+' of '+items.length;
    empty.hidden=n>0||!items.length;
  };

  var schema=function(list){
    var s=document.createElement('script');s.type='application/ld+json';
    s.textContent=JSON.stringify({'@context':'https://schema.org','@type':'CollectionPage','name':'O and A Level ebooks and notes','url':location.origin+'/ebooks/',
      'publisher':{'@type':'EducationalOrganization','name':'SJ Academy','url':location.origin+'/'},
      'mainEntity':{'@type':'ItemList','itemListElement':list.filter(function(i){return !i.soon;}).map(function(i,n){
        var it={'@type':i.type==='ebook'?'Book':'CreativeWork','name':i.name,'inLanguage':'en','isAccessibleForFree':!i.paid,
          'url':location.origin+(i.paid?(i.landing||'/product/'+i.slug+'/'):(i.url||'/product/'+i.slug+'/')).replace(location.origin,''),
          'offers':{'@type':'Offer','price':String(i.price),'priceCurrency':i.currency,'availability':'https://schema.org/InStock'}};
        if(i.type==='ebook'){it.bookFormat='https://schema.org/EBook';}
        if(i.img){it.image=i.img.src;}
        return {'@type':'ListItem','position':n+1,'item':it};})}});
    document.head.appendChild(s);
  };

  var draw=function(data){
    var list=order((Array.isArray(data)?data:[]).filter(function(p){return (p.categories||[]).some(function(c){return c.slug===CAT;});}).map(shape));
    grid.innerHTML=list.map(card).join('');
    grid.removeAttribute('aria-busy');
    items=Array.prototype.slice.call(grid.querySelectorAll('.sjk-book'));

    /* Hero pile: first three available covers */
    var covers=list.filter(function(i){return i.img&&!i.soon;}).slice(0,3);
    if(covers.length===3){
      pile.innerHTML=covers.map(function(i,k){return '<div class="sjk-pc sjk-pc'+(k+1)+(k===2?' sj-tagged':'')+'"><img src="'+esc(i.img.src)+'" alt="" width="1280" height="720"'+(k===2?' fetchpriority="high"':'')+'>'+(k===2?'<span class="sj-tag">'+(i.paid?esc(i.priceLabel):'free')+'</span>':'')+'</div>';}).join('')+
        '<span class="sj-hand sj-hand-lg sj-tilt-l sjk-note">most of it is free.<br>no card, no catch</span>';
    }

    /* Filters only offer what exists */
    var lvls=LEVEL_ORDER.filter(function(l){return list.some(function(i){return i.level===l;});});
    fillSelect(lv,lvls.map(function(l){return [l,LEVELS[l]];}));
    var subs={};list.forEach(function(i){subs[i.subject]=i.subjectName;});
    fillSelect(sb,Object.keys(subs).sort(function(a,b){return subs[a].localeCompare(subs[b]);}).map(function(k){return [k,subs[k]];}));
    var present=TABS.slice(1).filter(function(t){return list.some(function(i){return i.type===t[0];});});
    if(present.length>1){
      tabsBox.innerHTML='<div class="sj-tabs" role="tablist" aria-label="Type">'+TABS.filter(function(t){return t[0]==='all'||present.some(function(p){return p[0]===t[0];});}).map(function(t){
        var c=t[0]==='all'?list.length:list.filter(function(i){return i.type===t[0];}).length;
        return '<button type="button" role="tab" aria-selected="'+(t[0]==='all')+'" tabindex="'+(t[0]==='all'?0:-1)+'" data-type="'+t[0]+'">'+t[1]+' <span class="sjk-n">'+c+'</span></button>';}).join('')+'</div>';
      tabs=Array.prototype.slice.call(tabsBox.querySelectorAll('[role="tab"]'));
      tabs.forEach(function(t,i){
        t.addEventListener('click',function(){pickType(t.getAttribute('data-type'));run();});
        t.addEventListener('keydown',function(e){var st=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;if(!st){return;}e.preventDefault();var nx=tabs[(i+st+tabs.length)%tabs.length];pickType(nx.getAttribute('data-type'));nx.focus();run();});
      });
    }

    try{
      var p=new URLSearchParams(window.location.search);
      var pick=function(sel,v){if(v&&sel.querySelector('option[value="'+v+'"]')){sel.value=v;}};
      pick(lv,p.get('level'));pick(sb,p.get('subject'));
      if(p.get('type')){pickType(p.get('type'));}
      radios.forEach(function(r){if(r.value===p.get('status')){r.checked=true;}});
      if(p.get('q')){q.value=p.get('q');}
    }catch(e){}

    if(!list.length){
      count.textContent='';
      empty.hidden=false;
      empty.querySelector('b').textContent='New books are on the way';
      empty.querySelector('p').textContent='The shelf is being restocked. Tell us what you need and we will send it over.';
    }else{run();}
    schema(list);
  };

  var fail=function(){grid.innerHTML='';grid.removeAttribute('aria-busy');count.textContent='';errBox.hidden=false;};

  var timer;
  q.addEventListener('input',function(){clearTimeout(timer);timer=setTimeout(run,120);});
  lv.addEventListener('change',run);
  sb.addEventListener('change',run);
  radios.forEach(function(r){r.addEventListener('change',run);});
  more.addEventListener('click',function(){open=true;run();var nx=items[LIMIT];if(nx){var a=nx.querySelector('a');if(a){a.focus();}}});
  reset.addEventListener('click',function(){q.value='';lv.value='all';sb.value='all';radios[0].checked=true;pickType('all');run();q.focus();});

  var cached=null;
  try{cached=JSON.parse(sessionStorage.getItem(CACHE)||'null');}catch(e){}
  if(cached&&Date.now()-cached.t<TTL){draw(cached.d);return;}
  fetch(API,{credentials:'same-origin',headers:{'Accept':'application/json'}})
    .then(function(r){if(!r.ok){throw new Error(r.status);}return r.json();})
    .then(function(d){try{sessionStorage.setItem(CACHE,JSON.stringify({t:Date.now(),d:d}));}catch(e){}draw(d);})
    .catch(fail);
})();"""

style = open(here + "/lib-style.txt").read().strip()
page = (HTML.replace("SKEL", skel).replace("FAQ\n", faq_html + "\n").replace("TICK", TICK)
        .replace("SITE", SITE).replace("REQUEST", REQUEST).replace("QUESTION", QUESTION)
        .replace("DEMO", DEMO).replace("POPUP", POPUP).replace("STYLE", style)
        .replace("PAGESCRIPT", open(here + "/sj-page-script.js").read().strip())
        .replace("LIBSCRIPT", LIBSCRIPT)
        .replace("LDCRUMBS", json.dumps(ld_crumbs)).replace("LDFAQ", json.dumps(ld_faq)))
page.encode("ascii")
open(here + "/ebooks-elementor-widget.html", "w").write(page)
print("ok", len(page))
