import os, re

source_path = '/Users/sunyyanjunaid/Documents/SJ Academy/02 Website/Pages/Programs and partners/sat-iba-preparation-elementor-widget.html'
with open(source_path, 'r', encoding='utf-8') as f:
    source_html = f.read()

sjlogo_match = re.search(r'class="pd-sjlogo" src="([^"]+)"', source_html)
sjlogo_b64 = sjlogo_match.group(1) if sjlogo_match else ''

# Live WordPress media URL for Talal Hussain
photo_url = "https://www.sjacademy.pk/wp-content/uploads/2026/10/Talal.jpg"

scoped_css = """
/* Page-only layout for the SAT & Business School Admissions Webinar. Scoped to #sj.sj-p-webinar-pd */
.joinchat { display: none !important; }
#sj.sj-p-webinar-pd .pd-head { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--sj-s3); margin-bottom: var(--sj-s5); }
#sj.sj-p-webinar-pd .pd-lockup { display: inline-flex; align-items: center; gap: 12px; background: #fff; border: 1.5px solid var(--sj-ink); border-radius: var(--sj-r-pill); padding: 6px 16px 6px 10px; }
#sj.sj-p-webinar-pd .pd-pd { display: inline-flex; align-items: center; gap: 6px; font-weight: 600; font-size: 17px; color: #152232; letter-spacing: -.01em; }
#sj.sj-p-webinar-pd .pd-pd svg { width: 30px; height: 30px; }
#sj.sj-p-webinar-pd .pd-x { font-size: 20px; color: var(--sj-muted); line-height: 1; }
#sj.sj-p-webinar-pd .pd-sjlogo { height: 28px; width: auto; }
#sj.sj-p-webinar-pd .pd-gap { margin-top: var(--sj-s6); }
#sj.sj-p-webinar-pd .pd-top { margin-top: var(--sj-s3); }
#sj.sj-p-webinar-pd .pd-rows { border-top: 1.5px solid var(--sj-ink); }
#sj.sj-p-webinar-pd .pd-rows li { display: grid; grid-template-columns: 84px minmax(0, 1fr); gap: 10px; padding: 11px 0; border-bottom: 1px solid var(--sj-line); color: var(--sj-ink); }
#sj.sj-p-webinar-pd .pd-rows li > span:first-child { font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--sj-muted); padding: 3px 0; }
#sj.sj-p-webinar-pd .pd-badge-free { display: inline-flex; align-items: center; background: var(--sj-yellow); color: var(--sj-ink); font-weight: 600; font-size: 13px; text-transform: uppercase; padding: 3px 8px; border-radius: var(--sj-r-sm); border: 1px solid var(--sj-ink); }
#sj.sj-p-webinar-pd .sj-ticket-header { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: var(--sj-s2); }
#sj.sj-p-webinar-pd .pd-two { display: grid; gap: var(--sj-s6); grid-template-columns: minmax(0, 1fr); }
#sj.sj-p-webinar-pd .pd-photo { display: grid; justify-items: center; }
#sj.sj-p-webinar-pd .pd-photo .sj-polaroid { max-width: 340px; }
#sj.sj-p-webinar-pd .pd-photo .sj-polaroid img { aspect-ratio: 4/5; object-fit: cover; }
#sj.sj-p-webinar-pd .pd-role { margin-top: 4px; }
#sj.sj-p-webinar-pd .pd-big { display: flex; align-items: center; gap: 14px; }
#sj.sj-p-webinar-pd .pd-big b { font-size: clamp(64px, calc(48px + 4vw), 104px); font-weight: 600; line-height: .9; letter-spacing: -.05em; color: var(--sj-cta); }
#sj.sj-p-webinar-pd .pd-big span { font-size: 14px; letter-spacing: .06em; text-transform: uppercase; color: var(--sj-muted); line-height: 1.4; }
#sj.sj-p-webinar-pd .pd-final { text-align: center; display: grid; justify-items: center; }
#sj.sj-p-webinar-pd .pd-final .sj-row { justify-content: center; }
#sj.sj-p-webinar-pd .pd-phone-cta { display: none; }
#sj.sj-p-webinar-pd .pd-agenda-card { background: #fff; border: 1.5px solid var(--sj-ink); border-radius: var(--sj-r-md); padding: 22px 20px; box-shadow: var(--sj-sh-soft); display: grid; gap: 10px; align-content: start; }
#sj.sj-p-webinar-pd .pd-agenda-num { font-family: var(--sj-hand); font-size: 32px; line-height: 1; font-weight: 600; color: var(--sj-cta); }
#sj.sj-p-webinar-pd .pd-agenda-card h3 { font-size: 19px; font-weight: 500; color: var(--sj-ink); line-height: 1.3; margin: 0; }
#sj.sj-p-webinar-pd .pd-agenda-card p { font-size: 15px; color: var(--sj-muted); line-height: 1.5; margin: 0; }
#sj.sj-p-webinar-pd .pd-wpforms-box { background: #fff; border: 1.5px solid var(--sj-ink); border-radius: var(--sj-r-lg); padding: var(--sj-s6) var(--sj-s4); box-shadow: var(--sj-sh-offset); max-width: 680px; margin: 0 auto; }

/* WPForms styling for SJ Academy brand */
#sj.sj-p-webinar-pd .wpforms-container { margin: 0 !important; padding: 0 !important; }
#sj.sj-p-webinar-pd .wpforms-container .wpforms-title { display: none !important; }
#sj.sj-p-webinar-pd .wpforms-form { display: grid; gap: 16px; }
#sj.sj-p-webinar-pd .wpforms-field { padding: 0 !important; margin: 0 !important; }
#sj.sj-p-webinar-pd .wpforms-field-label { font-family: var(--sj-font) !important; font-size: 15px !important; font-weight: 500 !important; color: var(--sj-ink) !important; margin-bottom: 6px !important; display: block !important; }
#sj.sj-p-webinar-pd .wpforms-field-sublabel { font-family: var(--sj-font) !important; font-size: 13px !important; color: var(--sj-muted) !important; margin-top: 4px !important; }
#sj.sj-p-webinar-pd .wpforms-form input[type="text"],
#sj.sj-p-webinar-pd .wpforms-form input[type="email"],
#sj.sj-p-webinar-pd .wpforms-form input[type="tel"],
#sj.sj-p-webinar-pd .wpforms-form select,
#sj.sj-p-webinar-pd .wpforms-form textarea {
  width: 100% !important;
  min-height: 52px !important;
  padding: 12px 14px !important;
  border: 1.5px solid var(--sj-ink) !important;
  border-radius: var(--sj-r-md) !important;
  font-family: var(--sj-font) !important;
  font-size: 16px !important;
  background-color: #fff !important;
  color: var(--sj-ink) !important;
  box-sizing: border-box !important;
}
#sj.sj-p-webinar-pd .wpforms-form input:focus,
#sj.sj-p-webinar-pd .wpforms-form textarea:focus {
  outline: 3px solid var(--sj-ink) !important;
  outline-offset: 2px !important;
  box-shadow: 4px 4px 0 var(--sj-yellow) !important;
}
#sj.sj-p-webinar-pd .wpforms-form textarea { min-height: 110px !important; resize: vertical !important; }
#sj.sj-p-webinar-pd .wpforms-field-row { display: grid; gap: 12px; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
#sj.sj-p-webinar-pd .wpforms-field-checkbox ul,
#sj.sj-p-webinar-pd .wpforms-field-radio ul {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 10px;
  padding: 0;
  margin: 0;
  list-style: none;
}
#sj.sj-p-webinar-pd .wpforms-field-checkbox li,
#sj.sj-p-webinar-pd .wpforms-field-radio li {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  color: var(--sj-ink);
}
#sj.sj-p-webinar-pd .wpforms-submit-container { padding: 0 !important; margin-top: 8px !important; }
#sj.sj-p-webinar-pd button.wpforms-submit {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  min-height: 52px !important;
  width: 100% !important;
  padding: 12px 24px !important;
  border-radius: var(--sj-r-md) !important;
  border: 1.5px solid var(--sj-ink) !important;
  background: var(--sj-cta) !important;
  color: #fff !important;
  font-family: var(--sj-font) !important;
  font-size: 16px !important;
  font-weight: 500 !important;
  box-shadow: 4px 4px 0 var(--sj-ink) !important;
  cursor: pointer !important;
  transition: transform 120ms ease-out, box-shadow 120ms ease-out !important;
}
#sj.sj-p-webinar-pd button.wpforms-submit:hover {
  background: var(--sj-cta-dark) !important;
  transform: translate(-1px, -1px) !important;
  box-shadow: 5px 5px 0 var(--sj-ink) !important;
}

@media (min-width: 600px) {
  #sj.sj-p-webinar-pd .pd-wpforms-box { padding: var(--sj-s6); }
}
@media (max-width: 599px) {
  #sj.sj-p-webinar-pd .sj-proof b { font-size: clamp(18px, 5.4vw, 22px); white-space: nowrap; }
}
@media (max-width: 899px) {
  #back-to-top { display: none !important; }
  #sj.sj-p-webinar-pd .pd-phone-cta { display: flex; width: fit-content; }
}
@media (min-width: 900px) {
  #sj.sj-p-webinar-pd .pd-two { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: var(--sj-s7); align-items: start; }
  #sj.sj-p-webinar-pd .pd-two-t { grid-template-columns: minmax(0, .8fr) minmax(0, 1.2fr); align-items: center; }
}
"""

def generate_widget(for_preview=False):
    if for_preview:
        form_content = """
          <div class="wpforms-container" id="wpforms-11306">
            <form id="wpforms-form-11306" class="wpforms-form" method="post" action="#" onsubmit="event.preventDefault(); document.getElementById('sj-form-feedback').style.display='block'; this.style.display='none';">
              <div class="wpforms-field wpforms-field-name">
                <label class="wpforms-field-label">Name <span class="wpforms-required-label">*</span></label>
                <div class="wpforms-field-row">
                  <div>
                    <input type="text" class="wpforms-field-name-first" name="wpforms[fields][1][first]" placeholder="First" required>
                    <label class="wpforms-field-sublabel">First</label>
                  </div>
                  <div>
                    <input type="text" class="wpforms-field-name-last" name="wpforms[fields][1][last]" placeholder="Last" required>
                    <label class="wpforms-field-sublabel">Last</label>
                  </div>
                </div>
              </div>

              <div class="wpforms-field wpforms-field-phone">
                <label class="wpforms-field-label" for="wpforms-11306-field_2">WhatsApp #: <span class="wpforms-required-label">*</span></label>
                <input type="tel" id="wpforms-11306-field_2" class="wpforms-field-medium" name="wpforms[fields][2]" placeholder="+92 336 2144454" required>
                <span class="wpforms-field-sublabel">Zoom link and calendar reminder will be sent here</span>
              </div>

              <div class="wpforms-field wpforms-field-email">
                <label class="wpforms-field-label" for="wpforms-11306-field_3">Email <span class="wpforms-required-label">*</span></label>
                <input type="email" id="wpforms-11306-field_3" class="wpforms-field-medium" name="wpforms[fields][3]" placeholder="name@example.com" required>
              </div>

              <div class="wpforms-field wpforms-field-checkbox">
                <label class="wpforms-field-label">Current Level/Grade <span class="wpforms-required-label">*</span></label>
                <ul>
                  <li><label><input type="checkbox" name="wpforms[fields][4][]" value="O Level/IGCSE"> O Level/IGCSE</label></li>
                  <li><label><input type="checkbox" name="wpforms[fields][4][]" value="As Level"> As Level</label></li>
                  <li><label><input type="checkbox" name="wpforms[fields][4][]" value="A2 Level"> A2 Level</label></li>
                  <li><label><input type="checkbox" name="wpforms[fields][4][]" value="Parent"> Parent</label></li>
                </ul>
              </div>

              <div class="wpforms-field wpforms-field-text">
                <label class="wpforms-field-label" for="wpforms-11306-field_5">Current School/College</label>
                <input type="text" id="wpforms-11306-field_5" class="wpforms-field-medium" name="wpforms[fields][5]" placeholder="e.g. Nixor, Cedar, KGS, Beaconhouse, The Lyceum...">
              </div>

              <div class="wpforms-field wpforms-field-textarea">
                <label class="wpforms-field-label" for="wpforms-11306-field_6">Any Questions for the Webinar? (optional)</label>
                <textarea id="wpforms-11306-field_6" class="wpforms-field-medium" name="wpforms[fields][6]" placeholder="Ask anything about the SAT, IBA test format, score cut-offs, or preparation timelines..."></textarea>
              </div>

              <div class="wpforms-submit-container">
                <button type="submit" name="wpforms[submit]" id="wpforms-submit-11306" class="wpforms-submit" data-alt-text="Submitting..." data-submit-text="Reserve My Seat" data-loc="form_submit">Reserve My Seat</button>
              </div>
            </form>

            <div id="sj-form-feedback" class="sj-alert sj-alert-ok" style="display:none; text-align:center; padding: 24px; margin-top: 16px;">
              <b style="font-size: 20px;">You are registered.</b>
              <p style="margin-top: 8px;">Thank you! We have received your registration. We will send the Zoom link and calendar reminder to your WhatsApp shortly before the session.</p>
            </div>
          </div>
"""
    else:
        form_content = """
          <div class="wpforms-container" id="wpforms-11306-wrapper">
            [wpforms id="11306"]
          </div>
"""

    return f"""<!-- SJ Academy x PrepDesk: SAT and Business School Admissions Webinar. Elementor HTML widget. Version 1.2, November 2026.
     Built on the shared stylesheet sj-brand.css 3.1.1 (already in Additional CSS). Family: Event.
     Paste this whole file into one HTML widget. Section: full width, zero padding, no entrance animation.
     Page layout: Elementor Full Width. Hide Title: Yes.
     Suggested address: /sat-business-school-webinar/
     SEO title (Yoast, also social title): SAT &amp; Business School Admissions Webinar | SJ Academy
     Meta description: Free online session for O/A Level students and parents on the Digital SAT and IBA admissions with Talal Hussain (PrepDesk). Thursday, Nov 5 at 8:30 PM PKT on Zoom.
     Registration: Powered by WPForms (Form ID: 11306).
     Ref code for tracking: Ref: WEBINAR-PD
     This file is plain ASCII on purpose: symbols are written as codes so they cannot be garbled. -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>

<div id="sj" class="sj-p-webinar-pd" data-family="event">

  <!-- 1. HERO -->
  <section class="sj-section sj-bg-dots" data-sj-hero>
    <div class="sj-wrap pd-head">
      <nav class="sj-crumbs" aria-label="Breadcrumb"><ol><li><a href="https://www.sjacademy.pk/">Home</a></li><li><a href="https://www.sjacademy.pk/test-prep-with-prepdesk/">Test Prep</a></li><li aria-current="page">SAT &amp; Business School Webinar</li></ol></nav>
      <div class="pd-lockup" aria-label="PrepDesk in partnership with SJ Academy">
        <span class="pd-pd"><svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="14.5" cy="22" r="4.3" fill="none" stroke="#7D8A96" stroke-width="2.2"/><circle cx="26.5" cy="22" r="4.3" fill="none" stroke="#7D8A96" stroke-width="2.2"/><circle cx="38.5" cy="22" r="4.3" fill="none" stroke="#7D8A96" stroke-width="2.2"/><circle cx="50.5" cy="22" r="5.3" fill="#D8402A"/><rect x="6" y="29" width="52" height="5" rx="2.5" fill="#152232"/><rect x="12.5" y="34" width="4.4" height="13" rx="2.2" fill="#152232"/><rect x="47.1" y="34" width="4.4" height="13" rx="2.2" fill="#152232"/></svg>PrepDesk</span>
        <span class="pd-x" aria-hidden="true">&times;</span>
        <img class="pd-sjlogo" src="{sjlogo_b64}" alt="SJ Academy" width="150" height="40">
      </div>
    </div>
    <div class="sj-wrap sj-grid sj-grid-hero">
      <div class="sj-stack">
        <h1 class="sj-h1"><span class="sj-pill"><span>Free online session &middot; SJ Academy &times; PrepDesk</span></span>Stop guessing your university test. <span class="sj-hl">Get the strategy early.</span></h1>
        <p class="sj-lead sj-measure">A live 60&ndash;75 minute session on the Digital SAT, university admission requirements and IBA entry test strategies with Muhammad Talal Hussain (Founder, PrepDesk) and SJ Academy. Free for all SJ Academy students and parents.</p>
        <span class="sj-hand sj-tilt-l">one hour now saves months later</span>
        <a class="sj-btn sj-btn-primary pd-phone-cta" href="#register" data-loc="hero_phone">Reserve your free seat</a>
      </div>
      <div class="sj-offset sj-stack" id="pd-ticket-card">
        <div class="sj-ticket-header">
          <span class="pd-badge-free">100% Free Session</span>
          <span class="sj-stamp-box">Seats limited</span>
        </div>
        <h2 class="sj-h3">SAT &amp; Business School Admissions</h2>
        <ul class="pd-rows">
          <li><span>Date</span><span>Thursday, Nov 5 &middot; 8:30 PM PKT</span></li>
          <li><span>Duration</span><span>60&ndash;75 mins (includes live Q&amp;A)</span></li>
          <li><span>Where</span><span>Live online on Zoom (link sent on WhatsApp)</span></li>
          <li><span>Speaker</span><span>Muhammad Talal Hussain, PrepDesk</span></li>
          <li><span>Audience</span><span>O/A Level students and parents</span></li>
          <li><span>Fee</span><span>Free for all SJ Academy students &amp; parents</span></li>
        </ul>
        <a class="sj-btn sj-btn-primary sj-btn-block" href="#register" data-loc="hero_card">Reserve your free seat</a>
        <p class="sj-small sj-muted">Zoom link and session reminders sent to your WhatsApp and email.</p>
      </div>
    </div>
    <div class="sj-wrap pd-gap">
      <div class="sj-proof">
        <span><b>13 years</b>Talal teaching test prep, since 2013</span>
        <span><b>60&ndash;75 mins</b>With live Q&amp;A on Zoom</span>
        <span><b>100% Free</b>For all SJ students and parents</span>
      </div>
    </div>
  </section>

  <!-- 2. WHY THIS SESSION MATTERS -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap pd-two">
      <div class="sj-stack">
        <div class="sj-eyebrow">The problem</div>
        <h2 class="sj-h2">Good grades get you to the door. <span class="sj-hl">The test decides if it opens.</span></h2>
        <p class="sj-measure">Your Cambridge CAIE grades qualify you to apply, but top business schools like IBA rank applicants on entrance exam performance. The SAT and university entry tests reward timing, question patterns and composure under a clock: skills no school syllabus teaches.</p>
        <div class="sj-margin">
          <p>Most students wait until A2 exams end in June, leaving two rushed weeks to cram for tests that require months of strategy. Planning early gives you choices instead of panic.</p>
          <span class="sj-margin-note">habits take time to build</span>
        </div>
      </div>
      <div class="sj-stack">
        <div class="sj-card sj-clipped">
          <svg class="sj-clip" viewBox="0 0 22 52" aria-hidden="true"><path d="M11 2C6 2 2 6 2 11v30c0 5 4 9 9 9s9-4 9-9V15c0-3.5-2.8-6.3-6.3-6.3S7.4 11.5 7.4 15v25c0 2 1.6 3.6 3.6 3.6s3.6-1.6 3.6-3.6V16" fill="none" stroke="#453516" stroke-width="2.2" stroke-linecap="round"/></svg>
          <h3 class="sj-h3">The three mistakes students make</h3>
          <ul class="sj-ticks pd-top">
            <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg><span><b>Treating test prep like revision:</b> Standardized tests are not about subject knowledge; they are about question traps, pacing and score margins.</span></li>
            <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg><span><b>Misunderstanding SAT exemption at IBA:</b> Assuming any high SAT score guarantees test exemption. In reality, IBA has no fixed minimum SAT score for exemption; only top scorers on that round's SAT merit list qualify, cut-offs fluctuate (such as 1480 for Fall 2026 Round 2), and IBA strongly encourages taking its test.</span></li>
            <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg><span><b>Leaving preparation for the final month:</b> Scrambling between final A Level coursework and entry tests destroys both.</span></li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- 3. AGENDA -->
  <section class="sj-section sj-bg-dots">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <div class="sj-eyebrow">The agenda</div>
        <h2 class="sj-h2">Four parts. <span class="sj-hl">Every question answered.</span></h2>
        <p class="sj-lead">We respect your time. In 60 to 75 minutes, we walk through the exact roadmap from your current grade to university acceptance.</p>
      </div>

      <div class="sj-grid sj-grid-4">
        <div class="pd-agenda-card">
          <span class="pd-agenda-num">01</span>
          <h3>Early Planning &amp; Higher Education</h3>
          <p>Why early preparation matters. How leading universities evaluate applicants, how admissions committees look at A Levels vs tests, and the landscape after school.</p>
        </div>
        <div class="pd-agenda-card">
          <span class="pd-agenda-num">02</span>
          <h3>Understanding the Digital SAT</h3>
          <p>Format, scoring and the Bluebook adaptive testing system. Which universities require or accept SAT scores, when to sit the test, and how to build a 1400+ score plan.</p>
        </div>
        <div class="pd-agenda-card">
          <span class="pd-agenda-num">03</span>
          <h3>Business Schools &amp; IBA Admissions</h3>
          <p>Undergraduate programs at IBA Karachi. The admission process, entry test format (English and Maths), how the SAT merit list works, what recent cut-offs looked like, and interview preparation.</p>
        </div>
        <div class="pd-agenda-card">
          <span class="pd-agenda-num">04</span>
          <h3>Live Open Q&amp;A with the Speaker</h3>
          <p>Ask Talal Hussain questions directly. Get specific answers about your target university, current subject combinations, test timelines and next steps.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. WHO SHOULD ATTEND -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <div class="sj-eyebrow">Who this is for</div>
        <h2 class="sj-h2">Built for students and parents who want <span class="sj-hl">clarity before deadlines hit.</span></h2>
        <p class="sj-lead">Whether university applications feel far away or dangerously close, this session gives you a concrete timeline.</p>
      </div>

      <div class="sj-grid sj-grid-4">
        <div class="sj-card">
          <span class="sj-chip sj-chip-yellow">O Level / IGCSE</span>
          <h3 class="sj-h3 pd-top">Early Planners</h3>
          <p class="sj-small sj-muted">Understand admission criteria before you pick your A Level subjects, so you never get locked out of business or economics programs later.</p>
        </div>
        <div class="sj-card">
          <span class="sj-chip sj-chip-yellow">AS Level</span>
          <h3 class="sj-h3 pd-top">The Ideal Window</h3>
          <p class="sj-small sj-muted">AS Level is the best time to prepare and clear the SAT. Getting your test score out of the way leaves your final year completely free for A2 grades.</p>
        </div>
        <div class="sj-card">
          <span class="sj-chip sj-chip-yellow">A2 Level</span>
          <h3 class="sj-h3 pd-top">Immediate Applicants</h3>
          <p class="sj-small sj-muted">Navigating Round 1 and Round 2 admission cycles for IBA and top business schools. Learn how the rounds work and how to bridge your score gap.</p>
        </div>
        <div class="sj-card">
          <span class="sj-chip">Parents</span>
          <h3 class="sj-h3 pd-top">Parents &amp; Guardians</h3>
          <p class="sj-small sj-muted">Get unfiltered facts on university timelines, test requirements, fee expectations and how to support your child without unnecessary stress.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 5. SPEAKER -->
  <section class="sj-section sj-bg-brown">
    <div class="sj-wrap pd-two pd-two-t">
      <div class="pd-photo">
        <div class="sj-polaroid"><span class="sj-tape" aria-hidden="true"></span><img src="{photo_url}" alt="Muhammad Talal Hussain, Founder of PrepDesk" width="440" height="550" loading="lazy" decoding="async"><span class="sj-hand">13 years of test prep</span></div>
      </div>
      <div class="sj-stack">
        <div class="sj-eyebrow">Webinar speaker</div>
        <h2 class="sj-h2">Muhammad Talal Hussain</h2>
        <p class="sj-small sj-muted pd-role">Founder and lead instructor, PrepDesk</p>
        <div class="pd-big"><b>13</b><span>years teaching,<br>since 2013</span></div>
        <p class="sj-measure">Talal has led test-prep teams, built the courses other teachers use and guided thousands of students into top business schools and international universities. He knows where students lose points on the SAT and IBA tests, and how to fix technique early.</p>
        <ul class="sj-ticks">
          <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg><span>Former Director and Senior Instructor, IBAGRADS</span></li>
          <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg><span>Former Program Head, International Test Prep, Chaajao Technologies</span></li>
          <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg><span>Has built curricula for the SAT, GRE, GMAT and university entrance tests</span></li>
          <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg><span>Author of the PrepDesk course books and practice material</span></li>
          <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg><span>B.Sc. Economics and Finance, Institute of Business Management (IoBM)</span></li>
        </ul>
      </div>
    </div>
  </section>

  <!-- 6. REGISTRATION (WPFORMS: 11306) -->
  <section class="sj-section sj-bg-canvas" id="register">
    <div class="sj-wrap">
      <div class="pd-wpforms-box sj-stack">
        <div class="sj-stack" style="text-align:center;">
          <div class="sj-eyebrow" style="justify-content:center;">Free registration</div>
          <h2 class="sj-h2">Reserve your seat for the webinar</h2>
          <p class="sj-lead">Free for all SJ Academy students and parents. We will send the Zoom joining link and calendar reminder directly to your WhatsApp and email.</p>
        </div>

        <div id="sj-wpforms-wrapper">
{form_content}
        </div>
      </div>
    </div>
  </section>

  <!-- 7. FAQ -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <div class="sj-eyebrow">Common questions</div>
        <h2 class="sj-h2">Frequently asked questions</h2>
      </div>

      <div class="sj-faq">
        <details>
          <summary>Is this webinar completely free?</summary>
          <div class="sj-faq-a">
            <p>Yes. The webinar is 100% free for all SJ Academy students, alumni and parents through our official test-prep partnership with PrepDesk.</p>
          </div>
        </details>
        <details>
          <summary>How will I receive the Zoom joining link?</summary>
          <div class="sj-faq-a">
            <p>Once you register using the form above, we will send the Zoom link and calendar invite directly to your WhatsApp number and email address before the session begins on Thursday, Nov 5 at 8:30 PM PKT.</p>
          </div>
        </details>
        <details>
          <summary>Can parents attend the session?</summary>
          <div class="sj-faq-a">
            <p>Yes, parents are strongly encouraged to join. University requirements, admission timelines and fee structures are important family decisions, and Talal will address parent questions directly during the Q&amp;A.</p>
          </div>
        </details>
        <details>
          <summary>I am in O Levels or AS Level. Is it too early for me?</summary>
          <div class="sj-faq-a">
            <p>Not at all. In fact, AS Level is the ideal time to clear your SAT before A2 coursework intensifies. O Level students benefit from learning university subject requirements early so they choose the right A Level combinations.</p>
          </div>
        </details>
        <details>
          <summary>Can a SAT score exempt me from the IBA entry test?</summary>
          <div class="sj-faq-a">
            <p>IBA considers SAT scores for test exemption, but exemption, direct admission, or an interview call is never guaranteed. There is no fixed minimum SAT score for exemption; only the top scorers on the SAT merit list in each round receive an exemption, and thresholds change each cycle (for example, Fall 2026 Round 2 had a cut-off of 1480 total: 640 in Math and 600 in English). IBA strongly encourages all candidates to take its own test. In this session, Talal will explain how the SAT merit list works and what recent cut-offs looked like.</p>
          </div>
        </details>
        <details>
          <summary>Will a recording be sent out if I miss the live session?</summary>
          <div class="sj-faq-a">
            <p>We strongly recommend attending live so you can ask Talal questions during the open Q&amp;A. However, key notes and preparation checklists will be shared with all registered students after the session.</p>
          </div>
        </details>
      </div>
    </div>
  </section>

  <!-- 8. FINAL BAND -->
  <section class="sj-section sj-bg-yellow">
    <div class="sj-wrap pd-final sj-stack">
      <h2 class="sj-h2">One hour on Zoom. <span class="sj-hl">A clear plan for university.</span></h2>
      <p class="sj-lead sj-measure">Do not leave your higher education entrance tests to last-minute guesswork. Join Talal Hussain on Thursday, Nov 5 at 8:30 PM PKT and get your strategy in place early.</p>
      <div class="sj-row">
        <a class="sj-btn sj-btn-primary" href="#register" data-loc="final_band">Reserve your free seat</a>
        <a class="sj-btn sj-btn-ghost" href="https://wa.me/923362144454?text=Hi%20SJ%20Academy%2C%20I%20have%20a%20question%20about%20the%20SAT%20and%20PrepDesk%20webinar.%0A%28Ref%3A%20WEBINAR-PD%29%0AMy%20name%20is%20" target="_blank" rel="noopener" data-loc="final_wa">Have a question? WhatsApp us</a>
      </div>
    </div>
  </section>

</div>

<style>
{scoped_css}
</style>

<script>
/* Page tracking and smooth scroll for the SAT and Business School Admissions Webinar */
(function(){{
  var root = document.getElementById('sj'); if(!root || !root.classList.contains('sj-p-webinar-pd')) return;
  var send = function(ev, loc){{
    try {{
      if(window.dataLayer){{ window.dataLayer.push({{'event': ev, 'link_location': loc, 'page_family': 'Event'}}); }}
      if(window.gtag){{ window.gtag('event', ev, {{'link_location': loc, 'page_family': 'Event'}}); }}
    }} catch(e){{}}
  }};

  root.addEventListener('click', function(e){{
    var a = e.target.closest('a, button');
    if(!a) return;
    var href = a.getAttribute('href') || '';
    var loc = a.getAttribute('data-loc') || '';

    if(href.indexOf('wa.me') > -1){{
      send('whatsapp_click', loc);
    }} else if(href === '#register' || a.id === 'wpforms-submit-11306' || a.classList.contains('wpforms-submit')) {{
      send('webinar_register_click', loc);
    }}
  }});
}})();
</script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "EducationEvent",
  "name": "SAT & Business School Admissions Webinar",
  "description": "Informative online session for O/A Level students and parents on the Digital SAT, university admission requirements and IBA entry tests, led by Muhammad Talal Hussain (Founder, PrepDesk).",
  "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "startDate": "2026-11-05T20:30:00+05:00",
  "endDate": "2026-11-05T21:45:00+05:00",
  "location": {{
    "@type": "VirtualLocation",
    "url": "https://www.sjacademy.pk/sat-business-school-webinar/"
  }},
  "organizer": [
    {{
      "@type": "Organization",
      "name": "SJ Academy",
      "url": "https://www.sjacademy.pk"
    }},
    {{
      "@type": "Organization",
      "name": "PrepDesk",
      "url": "https://www.instagram.com/prepdesk_/"
    }}
  ],
  "performer": {{
    "@type": "Person",
    "name": "Muhammad Talal Hussain",
    "jobTitle": "Founder & Lead Instructor, PrepDesk"
  }},
  "isAccessibleForFree": true,
  "inLanguage": "en"
}}
</script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.sjacademy.pk/"
    }},
    {{
      "@type": "ListItem",
      "position": 2,
      "name": "Test Prep",
      "item": "https://www.sjacademy.pk/test-prep-with-prepdesk/"
    }},
    {{
      "@type": "ListItem",
      "position": 3,
      "name": "SAT & Business School Admissions Webinar",
      "item": "https://www.sjacademy.pk/sat-business-school-webinar/"
    }}
  ]
}}
</script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "Is this webinar completely free?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Yes. The webinar is 100% free for all SJ Academy students, alumni and parents through our official test-prep partnership with PrepDesk."
      }}
    }},
    {{
      "@type": "Question",
      "name": "How will I receive the Zoom joining link?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Once you register using the form above, we will send the Zoom link and calendar invite directly to your WhatsApp number and email address before the session begins on Thursday, Nov 5 at 8:30 PM PKT."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Can parents attend the session?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Yes, parents are strongly encouraged to join. University requirements, admission timelines and fee structures are important family decisions, and Talal will address parent questions directly during the Q&A."
      }}
    }},
    {{
      "@type": "Question",
      "name": "I am in O Levels or AS Level. Is it too early for me?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "Not at all. In fact, AS Level is the ideal time to clear your SAT before A2 coursework intensifies. O Level students benefit from learning university subject requirements early so they choose the right A Level combinations."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Can a SAT score exempt me from the IBA entry test?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "IBA considers SAT scores for test exemption, but exemption, direct admission, or an interview call is never guaranteed. There is no fixed minimum SAT score for exemption; only the top scorers on the SAT merit list in each round receive an exemption, and thresholds change each cycle (for example, Fall 2026 Round 2 had a cut-off of 1480 total: 640 in Math and 600 in English). IBA strongly encourages all candidates to take its own test. In this session, Talal will explain how the SAT merit list works and what recent cut-offs looked like."
      }}
    }},
    {{
      "@type": "Question",
      "name": "Will a recording be sent out if I miss the live session?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "We strongly recommend attending live so you can ask Talal questions during the open Q&A. However, key notes and preparation checklists will be shared with all registered students after the session."
      }}
    }}
  ]
}}
</script>
"""

# Write Elementor widget file
widget_dest = '/Users/sunyyanjunaid/Documents/SJ Academy/02 Website/Pages/Programs and partners/sat-business-school-webinar-elementor-widget.html'
with open(widget_dest, 'w', encoding='utf-8') as f:
    f.write(generate_widget(for_preview=False))

print("Updated widget:", widget_dest)

# Write preview file
preview_source = '/Users/sunyyanjunaid/Documents/SJ Academy/02 Website/Pages/Previews/sat-iba-preparation-PREVIEW.html'
with open(preview_source, 'r', encoding='utf-8') as f:
    preview_full = f.read()

header_match = re.search(r'^(<!doctype html>.*?<body>)', preview_full, re.DOTALL)
if header_match:
    preview_header = header_match.group(1).replace('<title>SAT and IBA preview</title>', '<title>SAT & Business School Admissions Webinar Preview | SJ Academy</title>')
    preview_html = preview_header + generate_widget(for_preview=True) + '</body></html>'
    preview_dest = '/Users/sunyyanjunaid/Documents/SJ Academy/02 Website/Pages/Previews/sat-business-school-webinar-PREVIEW.html'
    with open(preview_dest, 'w', encoding='utf-8') as f:
        f.write(preview_html)
    print("Updated preview:", preview_dest)
