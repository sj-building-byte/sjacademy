import os
import subprocess

DIR = "/Users/sunyyanjunaid/Documents/SJ Academy/03 Marketing/Instagram/Stories"
ASSETS_DIR = os.path.join(DIR, "assets")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

with open(os.path.join(ASSETS_DIR, "logos/sj-academy-logo-horizontal-on-light.svg"), "r", encoding="utf-8") as f:
    sj_logo_light = f.read()

with open(os.path.join(ASSETS_DIR, "logos/sj-academy-logo-horizontal-on-yellow.svg"), "r", encoding="utf-8") as f:
    sj_logo_yellow = f.read()

pd_svg = """<svg viewBox="0 0 64 64" width="34" height="34" aria-hidden="true" style="vertical-align:middle;flex-shrink:0;"><circle cx="14.5" cy="22" r="4.3" fill="none" stroke="#7D8A96" stroke-width="2.2"/><circle cx="26.5" cy="22" r="4.3" fill="none" stroke="#7D8A96" stroke-width="2.2"/><circle cx="38.5" cy="22" r="4.3" fill="none" stroke="#7D8A96" stroke-width="2.2"/><circle cx="50.5" cy="22" r="5.3" fill="#D8402A"/><rect x="6" y="29" width="52" height="5" rx="2.5" fill="#152232"/><rect x="12.5" y="34" width="4.4" height="13" rx="2.2" fill="#152232"/><rect x="47.1" y="34" width="4.4" height="13" rx="2.2" fill="#152232"/></svg>"""

# ==============================================================================
# VARIATION 1: The Speaker Event / Ticket Format (Canvas Ground - F5/F1)
# ==============================================================================
html_v1 = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>SAT & IBA Admissions Webinar Story - Variation 1 (Speaker Ticket)</title>
<style>
@font-face {{
  font-family: 'Poppins';
  font-weight: 400;
  src: url('assets/fonts/poppins-latin-400-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 500;
  src: url('assets/fonts/poppins-latin-500-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 600;
  src: url('assets/fonts/poppins-latin-600-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 700;
  src: url('assets/fonts/poppins-latin-700-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 800;
  src: url('assets/fonts/poppins-latin-800-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Caveat';
  font-weight: 600;
  src: url('assets/fonts/caveat-latin-600-normal.woff2') format('woff2');
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{
  width: 1080px;
  height: 1920px;
  overflow: hidden;
  background-color: #F7F5EF;
  background-image: radial-gradient(#D6D0BD 2.4px, transparent 2.5px);
  background-size: 32px 32px;
  font-family: 'Poppins', -apple-system, sans-serif;
  color: #151515;
  -webkit-font-smoothing: antialiased;
}}

.story-container {{
  position: relative;
  width: 1080px;
  height: 1920px;
  padding: 290px 72px 300px 72px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}}

/* Top Brand Header */
.top-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}}

.logo-wrap {{
  height: 46px;
  display: flex;
  align-items: center;
}}
.logo-wrap svg {{
  height: 46px;
  width: auto;
}}

.partner-lockup {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: #FFFFFF;
  border: 2.5px solid #151515;
  border-radius: 999px;
  padding: 6px 18px 6px 12px;
  box-shadow: 3px 3px 0 #151515;
}}
.partner-x {{
  font-size: 16px;
  font-weight: 600;
  color: #66625A;
}}
.partner-brand {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-weight: 700;
  font-size: 17px;
  color: #152232;
  letter-spacing: -0.01em;
}}

/* Eyebrow & Badges */
.badge-row {{
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 36px;
}}
.pill-badge {{
  background: #FCE004;
  color: #151515;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 7px 18px;
  border-radius: 999px;
  border: 2px solid #151515;
}}
.status-badge {{
  background: #FFFFFF;
  color: #151515;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.04em;
  padding: 7px 18px;
  border-radius: 999px;
  border: 2px solid #151515;
}}

/* Main Hook Headline */
.headline-wrap {{
  margin-top: 26px;
}}
.headline {{
  font-size: 64px;
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.035em;
  color: #151515;
}}
.sj-hl {{
  background-image: linear-gradient(100deg, transparent 0, #FCE004 0.14em, #FCE004 calc(100% - 0.14em), transparent 100%);
  background-repeat: no-repeat;
  background-size: 100% 0.44em;
  background-position: 0 calc(100% - 0.18em);
  padding: 0 0.14em;
  margin: 0 -0.14em;
  -webkit-box-decoration-break: clone;
  box-decoration-break: clone;
  white-space: nowrap;
}}

.subhead {{
  margin-top: 18px;
  font-size: 25px;
  font-weight: 500;
  line-height: 1.45;
  color: #453516;
}}

/* Speaker Profile Card */
.speaker-card {{
  margin-top: 32px;
  background: #FFFFFF;
  border: 3.5px solid #151515;
  border-radius: 20px;
  padding: 20px 24px;
  display: flex;
  align-items: center;
  gap: 22px;
  box-shadow: 6px 6px 0 #151515;
}}
.speaker-avatar {{
  width: 104px;
  height: 104px;
  border-radius: 16px;
  object-fit: cover;
  border: 2.5px solid #151515;
  flex-shrink: 0;
}}
.speaker-info {{
  display: flex;
  flex-direction: column;
  gap: 4px;
}}
.speaker-tag {{
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #CC4A00;
}}
.speaker-name {{
  font-size: 28px;
  font-weight: 700;
  color: #151515;
  letter-spacing: -0.02em;
}}
.speaker-cred {{
  font-size: 17px;
  font-weight: 500;
  color: #66625A;
  line-height: 1.35;
}}

/* Ticket / Details Card */
.ticket-box {{
  margin-top: 30px;
  background: #FFFFFF;
  border: 3.5px solid #151515;
  border-radius: 22px;
  padding: 28px 28px 24px 28px;
  box-shadow: 8px 8px 0 #FCE004, 8px 8px 0 3.5px #151515;
  position: relative;
}}
.ticket-rows {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px 24px;
}}
.ticket-item {{
  display: flex;
  flex-direction: column;
  gap: 4px;
}}
.item-label {{
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #8C7E6A;
}}
.item-val {{
  font-size: 21px;
  font-weight: 600;
  color: #151515;
  line-height: 1.25;
}}
.badge-free-mini {{
  display: inline-block;
  background: #FCE004;
  color: #151515;
  font-weight: 700;
  font-size: 12px;
  padding: 2px 7px;
  border-radius: 4px;
  border: 1px solid #151515;
  margin-left: 6px;
  vertical-align: middle;
}}

/* Agenda points inside ticket */
.agenda-strip {{
  margin-top: 22px;
  padding-top: 18px;
  border-top: 1.5px solid #E2DDD0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px 18px;
}}
.agenda-bullet {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 500;
  color: #453516;
}}
.agenda-bullet svg {{
  flex-shrink: 0;
}}

.handwritten-tag {{
  position: absolute;
  right: 24px;
  top: -24px;
  background: #FFF9CC;
  border: 2px solid #151515;
  border-radius: 8px;
  padding: 4px 14px;
  font-family: 'Caveat', cursive;
  font-size: 28px;
  font-weight: 600;
  color: #B92F25;
  transform: rotate(-2.5deg);
  box-shadow: 3px 3px 0 #151515;
  white-space: nowrap;
}}

/* Bottom Action & Link Sticker Target Area */
.action-zone {{
  margin-top: 36px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}}

.cta-button {{
  width: 100%;
  background: #CC4A00;
  color: #FFFFFF;
  border: 3.5px solid #151515;
  border-radius: 999px;
  padding: 22px 32px;
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -0.01em;
  text-align: center;
  box-shadow: 5px 6px 0 #151515;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
}}
.cta-button .arrow {{
  font-size: 32px;
  line-height: 1;
}}

.link-note {{
  font-size: 16px;
  font-weight: 500;
  color: #66625A;
  text-align: center;
}}
.link-note strong {{
  color: #151515;
  font-weight: 600;
}}
</style>
</head>
<body>

<div class="story-container">
  <div>
    <!-- Top Header -->
    <div class="top-header">
      <div class="logo-wrap">
        {sj_logo_light}
      </div>
      <div class="partner-lockup">
        <span class="partner-x">&times;</span>
        <span class="partner-brand">
          {pd_svg}
          PrepDesk
        </span>
      </div>
    </div>

    <!-- Eyebrow Badges -->
    <div class="badge-row">
      <span class="pill-badge">Free Online Session</span>
      <span class="status-badge">Thursday, Nov 5 &bull; 8:30 PM PKT</span>
    </div>

    <!-- Hook Headline -->
    <div class="headline-wrap">
      <h1 class="headline">
        Good grades get you to the door. <span class="sj-hl">The test decides if it opens.</span>
      </h1>
      <p class="subhead">
        A live 60&ndash;75 minute session on the Digital SAT, university admission requirements and IBA entry test strategies.
      </p>
    </div>

    <!-- Speaker Spotlight Card -->
    <div class="speaker-card">
      <img src="assets/talal.jpg" alt="Muhammad Talal Hussain" class="speaker-avatar">
      <div class="speaker-info">
        <span class="speaker-tag">Session Speaker</span>
        <span class="speaker-name">Muhammad Talal Hussain</span>
        <span class="speaker-cred">Founder, PrepDesk &bull; 13 years test prep experience (former Lead at IBAGRADS &amp; Chaajao)</span>
      </div>
    </div>

    <!-- Ticket / Details Card -->
    <div class="ticket-box">
      <div class="handwritten-tag">one hour now saves months later</div>
      <div class="ticket-rows">
        <div class="ticket-item">
          <span class="item-label">Date &amp; Time</span>
          <span class="item-val">Thursday, Nov 5 &bull; 8:30 PM</span>
        </div>
        <div class="ticket-item">
          <span class="item-label">Platform</span>
          <span class="item-val">Live Zoom (Link on WhatsApp)</span>
        </div>
        <div class="ticket-item">
          <span class="item-label">Audience</span>
          <span class="item-val">O &amp; A Level Students + Parents</span>
        </div>
        <div class="ticket-item">
          <span class="item-label">Fee</span>
          <span class="item-val">100% Free <span class="badge-free-mini">FREE</span></span>
        </div>
      </div>

      <!-- Quick 4 Agenda Points -->
      <div class="agenda-strip">
        <div class="agenda-bullet">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="7" fill="#FCE004" stroke="#151515" stroke-width="1.5"/><path d="M5 8l2 2 4-4" stroke="#151515" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Digital SAT &amp; Bluebook format
        </div>
        <div class="agenda-bullet">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="7" fill="#FCE004" stroke="#151515" stroke-width="1.5"/><path d="M5 8l2 2 4-4" stroke="#151515" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          IBA 1480 SAT merit cut-off
        </div>
        <div class="agenda-bullet">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="7" fill="#FCE004" stroke="#151515" stroke-width="1.5"/><path d="M5 8l2 2 4-4" stroke="#151515" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Why AS Level is the ideal window
        </div>
        <div class="agenda-bullet">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="7" fill="#FCE004" stroke="#151515" stroke-width="1.5"/><path d="M5 8l2 2 4-4" stroke="#151515" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Live open Q&amp;A with Talal
        </div>
      </div>
    </div>
  </div>

  <!-- Bottom CTA & Sticker Area -->
  <div class="action-zone">
    <div class="cta-button">
      Tap Link To Reserve Free Seat <span class="arrow">&rarr;</span>
    </div>
    <div class="link-note">
      Reserve seat at <strong>sjacademy.pk/sat-iba-test-webinar</strong>
    </div>
  </div>
</div>

</body>
</html>
"""

# ==============================================================================
# VARIATION 2: Big Type Reality Check (Yellow Ground - F2)
# ==============================================================================
html_v2 = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>SAT & IBA Admissions Webinar Story - Variation 2 (Big Type)</title>
<style>
@font-face {{
  font-family: 'Poppins';
  font-weight: 400;
  src: url('assets/fonts/poppins-latin-400-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 500;
  src: url('assets/fonts/poppins-latin-500-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 600;
  src: url('assets/fonts/poppins-latin-600-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 700;
  src: url('assets/fonts/poppins-latin-700-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 800;
  src: url('assets/fonts/poppins-latin-800-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Caveat';
  font-weight: 600;
  src: url('assets/fonts/caveat-latin-600-normal.woff2') format('woff2');
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{
  width: 1080px;
  height: 1920px;
  overflow: hidden;
  background-color: #FCE004;
  background-image: radial-gradient(rgba(0,0,0,0.11) 2.2px, transparent 2.3px);
  background-size: 32px 32px;
  font-family: 'Poppins', -apple-system, sans-serif;
  color: #151515;
  -webkit-font-smoothing: antialiased;
}}

.story-container {{
  position: relative;
  width: 1080px;
  height: 1920px;
  padding: 290px 72px 300px 72px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}}

/* Top Brand Header */
.top-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}}

.logo-wrap {{
  height: 46px;
  display: flex;
  align-items: center;
}}
.logo-wrap svg {{
  height: 46px;
  width: auto;
}}

.partner-lockup {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: #FFFFFF;
  border: 2.5px solid #151515;
  border-radius: 999px;
  padding: 6px 18px 6px 12px;
  box-shadow: 3px 3px 0 #151515;
}}
.partner-x {{
  font-size: 16px;
  font-weight: 600;
  color: #66625A;
}}
.partner-brand {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-weight: 700;
  font-size: 17px;
  color: #152232;
  letter-spacing: -0.01em;
}}

/* Eyebrow & Badges */
.badge-row {{
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 36px;
}}
.pill-badge {{
  background: #151515;
  color: #FFFFFF;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 7px 18px;
  border-radius: 999px;
}}
.status-badge {{
  background: #FFFFFF;
  color: #151515;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.04em;
  padding: 7px 18px;
  border-radius: 999px;
  border: 2px solid #151515;
}}

/* Big Type Headline */
.headline-wrap {{
  margin-top: 28px;
}}
.headline {{
  font-size: 68px;
  font-weight: 800;
  line-height: 1.18;
  letter-spacing: -0.04em;
  color: #151515;
}}
.white-band {{
  background: #FFFFFF;
  color: #151515;
  padding: 4px 16px;
  border-radius: 12px;
  display: inline-block;
  border: 3px solid #151515;
  margin-top: 6px;
}}

.teacher-note {{
  margin-top: 18px;
  font-family: 'Caveat', cursive;
  font-size: 42px;
  font-weight: 600;
  color: #B92F25;
  transform: rotate(-2deg);
  display: inline-block;
}}

/* Insight Card */
.insight-card {{
  margin-top: 32px;
  background: #FFFFFF;
  border: 3.5px solid #151515;
  border-radius: 24px;
  padding: 28px 30px;
  box-shadow: 10px 10px 0 #151515;
  display: flex;
  flex-direction: column;
  gap: 20px;
}}

.stat-row {{
  display: flex;
  align-items: center;
  gap: 20px;
  padding-bottom: 18px;
  border-bottom: 2px solid #F0ECE1;
}}
.stat-number {{
  font-size: 78px;
  font-weight: 800;
  line-height: 0.95;
  color: #CC4A00;
  letter-spacing: -0.04em;
}}
.stat-desc {{
  font-size: 20px;
  font-weight: 600;
  color: #151515;
  line-height: 1.35;
}}
.stat-sub {{
  font-size: 14px;
  font-weight: 500;
  color: #66625A;
  display: block;
  margin-top: 3px;
}}

.truth-text {{
  font-size: 22px;
  font-weight: 500;
  color: #2B2B2B;
  line-height: 1.5;
}}
.truth-text strong {{
  font-weight: 700;
  color: #151515;
}}

.meta-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  background: #F7F5EF;
  border: 2px solid #151515;
  border-radius: 14px;
  padding: 16px 20px;
}}
.meta-box {{
  display: flex;
  flex-direction: column;
  gap: 2px;
}}
.meta-label {{
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #8C7E6A;
}}
.meta-value {{
  font-size: 19px;
  font-weight: 700;
  color: #151515;
}}

/* Bottom Action & Sticker Safe Zone */
.action-zone {{
  margin-top: 36px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}}

.cta-button {{
  width: 100%;
  background: #151515;
  color: #FFFFFF;
  border: 3.5px solid #151515;
  border-radius: 999px;
  padding: 22px 32px;
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -0.01em;
  text-align: center;
  box-shadow: 5px 6px 0 rgba(0,0,0,0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
}}
.cta-button .arrow {{
  font-size: 32px;
  line-height: 1;
  color: #FCE004;
}}

.link-note {{
  font-size: 16px;
  font-weight: 600;
  color: #453516;
  text-align: center;
}}
</style>
</head>
<body>

<div class="story-container">
  <div>
    <!-- Top Header -->
    <div class="top-header">
      <div class="logo-wrap">
        {sj_logo_yellow}
      </div>
      <div class="partner-lockup">
        <span class="partner-x">&times;</span>
        <span class="partner-brand">
          {pd_svg}
          PrepDesk
        </span>
      </div>
    </div>

    <!-- Badges -->
    <div class="badge-row">
      <span class="pill-badge">Free Masterclass</span>
      <span class="status-badge">Thursday, Nov 5 &bull; 8:30 PM PKT</span>
    </div>

    <!-- Big Type Headline -->
    <div class="headline-wrap">
      <h1 class="headline">
        Waiting until June to prep for <br>
        <span class="white-band">IBA &amp; the SAT?</span>
      </h1>
      <span class="teacher-note">two rushed weeks is not a strategy.</span>
    </div>

    <!-- Reality Check / Insight Card -->
    <div class="insight-card">
      <div class="stat-row">
        <div class="stat-number">1480</div>
        <div class="stat-desc">
          IBA SAT merit cut-off
          <span class="stat-sub">Recent Round 2 score requirement (640 Math, 600 English)</span>
        </div>
      </div>

      <p class="truth-text">
        Standardised tests are <strong>not about subject knowledge</strong>. They test question traps, pacing, and composure under a clock. Planning early gives you choices instead of panic.
      </p>

      <div class="meta-grid">
        <div class="meta-box">
          <span class="meta-label">Speaker</span>
          <span class="meta-value">Muhammad Talal Hussain</span>
        </div>
        <div class="meta-box">
          <span class="meta-label">Format</span>
          <span class="meta-value">Live on Zoom (60-75 min)</span>
        </div>
        <div class="meta-box">
          <span class="meta-label">When</span>
          <span class="meta-value">Thu, Nov 5 &bull; 8:30 PM</span>
        </div>
        <div class="meta-box">
          <span class="meta-label">Fee</span>
          <span class="meta-value">100% Free Session</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Bottom CTA -->
  <div class="action-zone">
    <div class="cta-button">
      Tap Link To Reserve Free Seat <span class="arrow">&rarr;</span>
    </div>
    <div class="link-note">
      Direct registration: <strong>sjacademy.pk/sat-iba-test-webinar</strong>
    </div>
  </div>
</div>

</body>
</html>
"""

# ==============================================================================
# VARIATION 3: The Phone / Notes App Checklist (F3 Format)
# ==============================================================================
html_v3 = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>SAT & IBA Admissions Webinar Story - Variation 3 (Notes App)</title>
<style>
@font-face {{
  font-family: 'Poppins';
  font-weight: 400;
  src: url('assets/fonts/poppins-latin-400-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 500;
  src: url('assets/fonts/poppins-latin-500-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 600;
  src: url('assets/fonts/poppins-latin-600-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 700;
  src: url('assets/fonts/poppins-latin-700-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Poppins';
  font-weight: 800;
  src: url('assets/fonts/poppins-latin-800-normal.woff2') format('woff2');
}}
@font-face {{
  font-family: 'Caveat';
  font-weight: 600;
  src: url('assets/fonts/caveat-latin-600-normal.woff2') format('woff2');
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{
  width: 1080px;
  height: 1920px;
  overflow: hidden;
  background-color: #F7F5EF;
  background-image: radial-gradient(#D6D0BD 2.4px, transparent 2.5px);
  background-size: 32px 32px;
  font-family: 'Poppins', -apple-system, sans-serif;
  color: #151515;
  -webkit-font-smoothing: antialiased;
}}

.story-container {{
  position: relative;
  width: 1080px;
  height: 1920px;
  padding: 290px 72px 300px 72px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}}

/* Top Brand Header */
.top-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}}

.logo-wrap {{
  height: 46px;
  display: flex;
  align-items: center;
}}
.logo-wrap svg {{
  height: 46px;
  width: auto;
}}

.partner-lockup {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: #FFFFFF;
  border: 2.5px solid #151515;
  border-radius: 999px;
  padding: 6px 18px 6px 12px;
  box-shadow: 3px 3px 0 #151515;
}}
.partner-x {{
  font-size: 16px;
  font-weight: 600;
  color: #66625A;
}}
.partner-brand {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-weight: 700;
  font-size: 17px;
  color: #152232;
  letter-spacing: -0.01em;
}}

/* Eyebrow & Badges */
.badge-row {{
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 36px;
}}
.pill-badge {{
  background: #FCE004;
  color: #151515;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 7px 18px;
  border-radius: 999px;
  border: 2px solid #151515;
}}
.status-badge {{
  background: #FFFFFF;
  color: #151515;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.04em;
  padding: 7px 18px;
  border-radius: 999px;
  border: 2px solid #151515;
}}

/* Headline */
.headline-wrap {{
  margin-top: 26px;
}}
.headline {{
  font-size: 60px;
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.035em;
  color: #151515;
}}
.sj-hl {{
  background-image: linear-gradient(100deg, transparent 0, #FCE004 0.14em, #FCE004 calc(100% - 0.14em), transparent 100%);
  background-repeat: no-repeat;
  background-size: 100% 0.44em;
  background-position: 0 calc(100% - 0.18em);
  padding: 0 0.14em;
  margin: 0 -0.14em;
  -webkit-box-decoration-break: clone;
  box-decoration-break: clone;
  white-space: nowrap;
}}

/* Recreated Notes App Window */
.notes-window {{
  margin-top: 32px;
  background: #FFFFFF;
  border: 3.5px solid #151515;
  border-radius: 24px;
  box-shadow: 9px 9px 0 #FCE004, 9px 9px 0 3.5px #151515;
  overflow: hidden;
  position: relative;
}}

.notes-top-bar {{
  background: #F4EEDC;
  border-bottom: 2.5px solid #151515;
  padding: 12px 22px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}
.notes-dots {{
  display: flex;
  gap: 7px;
}}
.notes-dot {{
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 1.5px solid #151515;
}}
.notes-dot.red {{ background: #FF5F56; }}
.notes-dot.yellow {{ background: #FFBD2E; }}
.notes-dot.green {{ background: #27C93F; }}
.notes-date {{
  font-size: 13px;
  font-weight: 600;
  color: #7D7362;
  letter-spacing: 0.04em;
}}

.notes-body {{
  padding: 26px 28px 28px 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}}

.notes-title {{
  font-size: 26px;
  font-weight: 700;
  color: #151515;
  letter-spacing: -0.02em;
  border-bottom: 2px dashed #E2DDD0;
  padding-bottom: 12px;
}}

.checklist {{
  display: flex;
  flex-direction: column;
  gap: 14px;
}}

.check-item {{
  display: flex;
  align-items: flex-start;
  gap: 14px;
  font-size: 20px;
  font-weight: 500;
  color: #2B2B2B;
  line-height: 1.35;
}}
.check-box {{
  width: 28px;
  height: 28px;
  border-radius: 7px;
  border: 2.5px solid #D63A2F;
  background: #FFF0EE;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin-top: 2px;
}}
.check-box svg {{
  stroke: #D63A2F;
  stroke-width: 3;
  width: 16px;
  height: 16px;
}}

.highlight-box {{
  margin-top: 10px;
  background: #FFF9CC;
  border: 2px solid #151515;
  border-radius: 12px;
  padding: 14px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}
.hb-left {{
  display: flex;
  flex-direction: column;
}}
.hb-label {{
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #8C7E6A;
}}
.hb-title {{
  font-size: 19px;
  font-weight: 700;
  color: #151515;
}}
.hb-badge {{
  background: #151515;
  color: #FFFFFF;
  font-size: 13px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 6px;
}}

.handwritten-stamp {{
  position: absolute;
  right: 22px;
  bottom: 84px;
  font-family: 'Caveat', cursive;
  font-size: 32px;
  font-weight: 600;
  color: #B92F25;
  transform: rotate(-6deg);
  background: rgba(255, 255, 255, 0.95);
  padding: 2px 10px;
  border-radius: 6px;
  border: 1.5px dashed #B92F25;
}}

/* Bottom Action & Sticker Safe Zone */
.action-zone {{
  margin-top: 36px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}}

.cta-button {{
  width: 100%;
  background: #CC4A00;
  color: #FFFFFF;
  border: 3.5px solid #151515;
  border-radius: 999px;
  padding: 22px 32px;
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -0.01em;
  text-align: center;
  box-shadow: 5px 6px 0 #151515;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
}}
.cta-button .arrow {{
  font-size: 32px;
  line-height: 1;
}}

.link-note {{
  font-size: 16px;
  font-weight: 500;
  color: #66625A;
  text-align: center;
}}
.link-note strong {{
  color: #151515;
  font-weight: 600;
}}
</style>
</head>
<body>

<div class="story-container">
  <div>
    <!-- Top Header -->
    <div class="top-header">
      <div class="logo-wrap">
        {sj_logo_light}
      </div>
      <div class="partner-lockup">
        <span class="partner-x">&times;</span>
        <span class="partner-brand">
          {pd_svg}
          PrepDesk
        </span>
      </div>
    </div>

    <!-- Eyebrow Badges -->
    <div class="badge-row">
      <span class="pill-badge">Free Online Masterclass</span>
      <span class="status-badge">Thu, Nov 5 &bull; 8:30 PM PKT</span>
    </div>

    <!-- Headline -->
    <div class="headline-wrap">
      <h1 class="headline">
        Stop guessing your university tests. <span class="sj-hl">Get the strategy early.</span>
      </h1>
    </div>

    <!-- Recreated Notes App Window -->
    <div class="notes-window">
      <div class="notes-top-bar">
        <div class="notes-dots">
          <div class="notes-dot red"></div>
          <div class="notes-dot yellow"></div>
          <div class="notes-dot green"></div>
        </div>
        <div class="notes-date">Today &bull; 8:30 PM Prep Plan</div>
      </div>

      <div class="notes-body">
        <div class="notes-title">University Test Roadmap (O &amp; A Level)</div>

        <div class="checklist">
          <div class="check-item">
            <div class="check-box">
              <svg viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </div>
            <span><strong>Clear Digital SAT in AS Level:</strong> keeps final year coursework free for A2 grades.</span>
          </div>

          <div class="check-item">
            <div class="check-box">
              <svg viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </div>
            <span><strong>Understand IBA merit list:</strong> exemption is never automatic (Fall '26 Round 2 cut-off was 1480).</span>
          </div>

          <div class="check-item">
            <div class="check-box">
              <svg viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </div>
            <span><strong>Stop cramming in June:</strong> entry tests reward pacing and composure under a clock, not memorisation.</span>
          </div>

          <div class="check-item">
            <div class="check-box">
              <svg viewBox="0 0 24 24" fill="none"><path d="M5 13l4 4L19 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </div>
            <span><strong>Live Zoom with Talal Hussain:</strong> Founder PrepDesk, 13 years test prep experience.</span>
          </div>
        </div>

        <div class="highlight-box">
          <div class="hb-left">
            <span class="hb-label">Live Session</span>
            <span class="hb-title">Thursday, Nov 5 &bull; 8:30 PM PKT</span>
          </div>
          <span class="hb-badge">100% FREE</span>
        </div>
      </div>

      <div class="handwritten-stamp">parents welcome too!</div>
    </div>
  </div>

  <!-- Bottom CTA & Sticker Area -->
  <div class="action-zone">
    <div class="cta-button">
      Tap Link To Reserve Free Seat <span class="arrow">&rarr;</span>
    </div>
    <div class="link-note">
      Reserve seat at <strong>sjacademy.pk/sat-iba-test-webinar</strong>
    </div>
  </div>
</div>

</body>
</html>
"""

with open(os.path.join(DIR, "story-speaker-ticket.html"), "w", encoding="utf-8") as f:
    f.write(html_v1)

with open(os.path.join(DIR, "story-big-type.html"), "w", encoding="utf-8") as f:
    f.write(html_v2)

with open(os.path.join(DIR, "story-notes-app.html"), "w", encoding="utf-8") as f:
    f.write(html_v3)

print("Updated HTML for all 3 variations.")
