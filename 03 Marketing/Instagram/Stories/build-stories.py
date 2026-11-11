import os
import subprocess

DIR = "/Users/sunyyanjunaid/Documents/SJ Academy/03 Marketing/Instagram/Stories"
ASSETS_DIR = os.path.join(DIR, "assets")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Read logo SVG
with open(os.path.join(ASSETS_DIR, "logos/sj-academy-logo-horizontal-on-light.svg"), "r", encoding="utf-8") as f:
    sj_logo_light = f.read()

with open(os.path.join(ASSETS_DIR, "logos/sj-academy-logo-horizontal-on-yellow.svg"), "r", encoding="utf-8") as f:
    sj_logo_yellow = f.read()

# PrepDesk SVG icon
pd_svg = """<svg viewBox="0 0 64 64" width="34" height="34" aria-hidden="true" style="vertical-align:middle;"><circle cx="14.5" cy="22" r="4.3" fill="none" stroke="#7D8A96" stroke-width="2.2"/><circle cx="26.5" cy="22" r="4.3" fill="none" stroke="#7D8A96" stroke-width="2.2"/><circle cx="38.5" cy="22" r="4.3" fill="none" stroke="#7D8A96" stroke-width="2.2"/><circle cx="50.5" cy="22" r="5.3" fill="#D8402A"/><rect x="6" y="29" width="52" height="5" rx="2.5" fill="#152232"/><rect x="12.5" y="34" width="4.4" height="13" rx="2.2" fill="#152232"/><rect x="47.1" y="34" width="4.4" height="13" rx="2.2" fill="#152232"/></svg>"""

# HTML template for Variation 1: Speaker & Ticket Card (Canvas Ground)
html_v1 = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>SAT & IBA Admissions Webinar Story - Variation 1</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
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
  background-image: radial-gradient(#D8D2C0 2.2px, transparent 2.4px);
  background-size: 32px 32px;
  font-family: 'Poppins', -apple-system, sans-serif;
  color: #151515;
  -webkit-font-smoothing: antialiased;
}}

.story-container {{
  position: relative;
  width: 1080px;
  height: 1920px;
  padding: 285px 76px 360px 76px;
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
  height: 48px;
  display: flex;
  align-items: center;
}}
.logo-wrap svg {{
  height: 48px;
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
  padding: 7px 16px;
  border-radius: 999px;
  border: 2px solid #151515;
}}
.status-badge {{
  background: #FFFFFF;
  color: #CC4A00;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 7px 16px;
  border-radius: 999px;
  border: 2px solid #151515;
}}

/* Main Hook Headline */
.headline-wrap {{
  margin-top: 24px;
}}
.headline {{
  font-size: 64px;
  font-weight: 800;
  line-height: 1.14;
  letter-spacing: -0.035em;
  color: #151515;
}}
.highlight {{
  background-color: #FCE004;
  color: #151515;
  padding: 0 12px;
  border-radius: 8px;
  display: inline;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
}}

.subhead {{
  margin-top: 18px;
  font-size: 26px;
  font-weight: 500;
  line-height: 1.42;
  color: #453516;
  max-width: 900px;
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
  gap: 24px;
  box-shadow: 6px 6px 0 #151515;
}}
.speaker-avatar {{
  width: 104px;
  height: 104px;
  border-radius: 16px;
  object-fit: cover;
  border: 3px solid #151515;
  flex-shrink: 0;
}}
.speaker-info {{
  display: flex;
  flex-direction: column;
  gap: 4px;
}}
.speaker-tag {{
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.08em;
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
  font-size: 18px;
  font-weight: 500;
  color: #66625A;
  line-height: 1.35;
}}

/* Ticket / Details Card */
.ticket-box {{
  margin-top: 28px;
  background: #FFFFFF;
  border: 3.5px solid #151515;
  border-radius: 22px;
  padding: 26px 28px 24px 28px;
  box-shadow: 8px 8px 0 #FCE004, 8px 8px 0 3.5px #151515;
  position: relative;
}}
.ticket-rows {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px 24px;
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
.item-val strong {{
  color: #151515;
}}
.badge-free-mini {{
  display: inline-block;
  background: #FCE004;
  color: #151515;
  font-weight: 700;
  font-size: 13px;
  padding: 2px 8px;
  border-radius: 4px;
  border: 1px solid #151515;
  margin-left: 6px;
  vertical-align: middle;
}}

.handwritten-aside {{
  position: absolute;
  right: 20px;
  top: -26px;
  font-family: 'Caveat', cursive;
  font-size: 36px;
  font-weight: 600;
  color: #B92F25;
  transform: rotate(-3deg);
  white-space: nowrap;
}}

/* Bottom Action & Sticker Safe Zone */
.action-zone {{
  margin-top: 36px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
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
  font-size: 17px;
  font-weight: 500;
  color: #66625A;
  text-align: center;
}}
.link-note span {{
  font-weight: 600;
  color: #151515;
}}
</style>
</head>
<body>

<div class="story-container">
  <div>
    <!-- Top Header (in safe zone) -->
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
      <span class="status-badge">Thu, Nov 5 &bull; 8:30 PM PKT</span>
    </div>

    <!-- Hook Headline -->
    <div class="headline-wrap">
      <h1 class="headline">
        Good grades get you to the door. <span class="highlight">The test decides if it opens.</span>
      </h1>
      <p class="subhead">
        Stop guessing your university tests. A live strategy session on the Digital SAT, IBA entry test format, and university admissions.
      </p>
    </div>

    <!-- Speaker Spotlight Card -->
    <div class="speaker-card">
      <img src="assets/talal.jpg" alt="Muhammad Talal Hussain" class="speaker-avatar">
      <div class="speaker-info">
        <span class="speaker-tag">Featured Speaker</span>
        <span class="speaker-name">Muhammad Talal Hussain</span>
        <span class="speaker-cred">Founder, PrepDesk &bull; 13 years test prep experience (former Lead at IBAGRADS &amp; Chaajao)</span>
      </div>
    </div>

    <!-- Ticket / Details Card -->
    <div class="ticket-box">
      <span class="handwritten-aside">one hour now saves months later</span>
      <div class="ticket-rows">
        <div class="ticket-item">
          <span class="item-label">When</span>
          <span class="item-val">Thursday, Nov 5 &bull; 8:30 PM</span>
        </div>
        <div class="ticket-item">
          <span class="item-label">Where</span>
          <span class="item-val">Live Zoom (Link on WhatsApp)</span>
        </div>
        <div class="ticket-item">
          <span class="item-label">Audience</span>
          <span class="item-val">O &amp; A Level Students + Parents</span>
        </div>
        <div class="ticket-item">
          <span class="item-label">Fee</span>
          <span class="item-val">100% Free <span class="badge-free-mini">Free</span></span>
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
      Direct registration at <span>sjacademy.pk/sat-iba-test-webinar</span>
    </div>
  </div>
</div>

</body>
</html>
"""

with open(os.path.join(DIR, "story-speaker-ticket.html"), "w", encoding="utf-8") as f:
    f.write(html_v1)

print("Saved story-speaker-ticket.html")
