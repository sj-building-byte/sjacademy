# SJ Academy 20s launch film (9:16), built on brand guidelines v3.2.
# Run from the project root: python3 build/gen3.py
import json

INFO = json.load(open("assets/site/info.json"))

# ── brand tokens (sj-brand.css 3.1.1) ──────────────────────────────────────
YEL, YEL_L, ORG, CTA = "#FCE004", "#FFF9CC", "#FE6100", "#CC4A00"
BROWN, INK, TEXT, MUTED = "#453516", "#151515", "#2B2B2B", "#66625A"
CANVAS, LINE, KRAFT = "#F7F5EF", "#E2DDD0", "#E9DFC9"
PEN, PEN_T, EXAM = "#D63A2F", "#B92F25", "#1B2A4A"
CREAM = "#EDE6D3"  # text on the brown band (sj-bg-brown)

M = 96            # left margin
S = 820 / 390     # phone css px -> film px inside the screen

RT_PLACEHOLDER = None
TICK = "M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"
CIRCLE = "M14 38C10 18 40 6 68 7c27 1 44 13 42 30-2 16-30 24-56 23C28 59 8 50 13 30"

O_SUBJ = ["Maths", "Physics", "Chemistry", "Biology", "Accounting", "Business",
          "Economics", "Computer Science", "English", "Urdu", "Pakistan Studies", "Islamiyat"]
A_SUBJ = ["Maths", "Physics", "Chemistry", "Biology", "Accounting", "Business",
          "Economics", "Computer Science", "Psychology", "Sociology", "English", "Urdu"]


RT = f'<svg class="tk rt" viewBox="0 0 24 24"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5" stroke="#D63A2F" stroke-width="2.6" pathLength="1" /></svg>'


def tick(cls, color):
    return f'<svg class="tk {cls}" viewBox="0 0 24 24"><path d="{TICK}" stroke="{color}" stroke-width="2.6" pathLength="1" /></svg>'


def subj_list(items, cls):
    rows = []
    for i, s in enumerate(items):
        col, row = (0, i) if i < 6 else (1, i - 6)
        rows.append(f'<div class="it {cls}" style="left:{48 + col * 392}px; top:{row * 82}px">'
                    f'{tick("lt", CTA)}<span class="wr">{s}</span></div>')
    return "\n".join(rows)


def words(text, cls="w"):
    return " ".join(f'<span class="{cls}">{t}</span>' for t in text.split(" "))


def tabs(selected):
    a = ' sel' if selected == "O" else ''
    b = ' sel' if selected == "A" else ''
    return f'<div class="tabs"><div class="tab{a}">O Level</div><div class="tab{b}">A Level</div></div>'


# tap targets (viewport css px -> film px inside the screen; window starts at viewport y=50)
def btn(name):
    b = next(x for x in INFO["buttons_olevel"] if x["t"].startswith(name))
    return round((b["x"] + b["w"] / 2) * S), round((b["y"] + b["h"] / 2 - 50) * S)


TAP_TAB = btn("O Level")
TAP_PHY = btn("Physics")
FIND_END = -round(650 * S)      # scroll-find.png starts at doc y 78; end at doc 728
TOOLS_END = -round((840 - 630) * S)

css = f"""
@font-face {{ font-family: "Poppins"; font-weight: 400; src: url("assets/fonts/Poppins-Regular.ttf") format("truetype"); }}
@font-face {{ font-family: "Poppins"; font-weight: 500; src: url("assets/fonts/Poppins-Medium.ttf") format("truetype"); }}
@font-face {{ font-family: "Poppins"; font-weight: 600; src: url("assets/fonts/Poppins-SemiBold.ttf") format("truetype"); }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ width: 1080px; height: 1920px; overflow: hidden; background-color: {CANVAS}; font-family: "Poppins", sans-serif; color: {TEXT}; -webkit-font-smoothing: antialiased; }}
#root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background-color: {CANVAS}; }}
.dots {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; background-color: {CANVAS};
  background-image: radial-gradient(#DAD4C3 2.2px, rgba(218,212,195,0) 2.4px); background-size: 44px 44px; background-position: 22px 22px; }}
.clip {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; }}
.scene {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; }}
.cam {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; }}
.abs {{ position: absolute; }}
.h1 {{ font-weight: 600; font-size: 132px; line-height: 1.05; letter-spacing: -0.03em; color: {INK}; }}
.sub {{ font-weight: 500; font-size: 44px; line-height: 1.3; letter-spacing: -0.01em; color: {INK}; }}
.ln {{ display: block; overflow: hidden; padding-bottom: 0.12em; margin-bottom: -0.12em; white-space: nowrap; }}
.w {{ display: inline-block; }}
.hl {{ position: relative; display: inline-block; }}
.hl .bg {{ position: absolute; left: -0.08em; right: -0.08em; top: 0.16em; bottom: -0.02em; background-color: {YEL}; transform-origin: 0% 50%; }}
.hl .tx {{ position: relative; }}
svg.tk path, svg.pen path {{ fill: none; stroke-linecap: round; stroke-linejoin: round; }}
svg.tk, svg.pen {{ opacity: 0; }}

/* persistent kicker pill (top right) */
#pill {{ position: absolute; right: {M}px; top: 132px; height: 76px; padding: 0 30px; border: 3px solid {INK}; border-radius: 999px;
  background-color: #FFFFFF; box-shadow: 6px 6px 0 rgba(0,0,0,0.14); display: flex; align-items: center; z-index: 50;
  font-weight: 500; font-size: 28px; letter-spacing: 0.05em; text-transform: uppercase; color: {INK}; white-space: nowrap; }}
.logo {{ position: absolute; left: {M}px; top: 136px; }}

/* S1 hook */
#s1 .h1 {{ left: {M}px; top: 520px; }}

/* S2 method: exam paper */
#s2 .lab {{ left: {M}px; top: 330px; }}
#s2 .paper {{ left: {M}px; top: 420px; width: 888px; height: 900px; background-color: #FFFEF9; border-radius: 8px; box-shadow: 0 28px 68px rgba(0,0,0,0.18); overflow: hidden; }}
#s2 .paper .mline {{ position: absolute; left: 72px; top: 0; width: 3px; height: 900px; background-color: #E9A29C; }}
#s2 .pq {{ position: absolute; left: 104px; top: 40px; width: 740px; color: #111111; font-size: 38px; line-height: 1.38; font-weight: 400; }}
#s2 .pq small {{ display: block; font-size: 36px; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; color: #5E5E5E; margin-bottom: 10px; }}
#s2 .rule {{ position: absolute; left: 0; top: 268px; width: 888px; height: 3px; background-color: {EXAM}; }}
#s2 .ruled {{ position: absolute; left: 0; top: 271px; width: 888px; height: 860px; background-image: repeating-linear-gradient(rgba(216,226,238,0) 0px, rgba(216,226,238,0) 70px, #D8E2EE 70px, #D8E2EE 72px); }}
#s2 .ans {{ position: absolute; left: 104px; top: 286px; width: 760px; color: {EXAM}; font-size: 40px; line-height: 72px; }}
#s2 .ans .al {{ display: block; white-space: nowrap; position: relative; }}
#s2 .mark {{ position: absolute; right: 48px; top: 292px; color: {PEN_T}; font-size: 64px; font-weight: 500; line-height: 1; }}
#s2 .mnote {{ position: absolute; left: 104px; top: 528px; border-left: 5px solid {PEN}; padding: 4px 0 4px 26px; color: {PEN_T}; font-size: 40px; font-weight: 500; line-height: 1.25; }}
#s2 .rt {{ display: inline-block; width: 52px; height: 52px; vertical-align: -10px; margin-left: 6px; }}
#s2 .stamp {{ position: absolute; left: 604px; top: 620px; width: 236px; height: 236px; border: 6px solid {PEN}; border-radius: 50%;
  display: flex; align-items: center; justify-content: center; color: {PEN_T}; font-size: 78px; font-weight: 500; letter-spacing: -0.02em; }}

/* website screens */
.screen {{ position: absolute; left: 130px; width: 820px; border-radius: 40px; overflow: hidden; background-color: #FFFFFF; box-shadow: 0 28px 68px rgba(0,0,0,0.18); }}
.screen .pic {{ position: absolute; left: 0; top: 0; }}
.tap {{ position: absolute; width: 120px; height: 120px; margin: -60px 0 0 -60px; border-radius: 50%; background-color: rgba(21,21,21,0.18); border: 3px solid rgba(21,21,21,0.35); opacity: 0; }}
#s3 .screen {{ top: 320px; height: {round(625 * S)}px; }}
#s6 .screen {{ top: 336px; height: {round(630 * S)}px; }}
#s6 .lab {{ left: {M}px; top: 252px; }}

/* notebook (O Level / A Level) */
.nb {{ position: absolute; left: {M}px; top: 360px; width: 888px; height: 1150px; transform-origin: 0px 50%; }}
.tabs {{ position: absolute; left: 24px; top: 0; display: flex; gap: 8px; }}
.tab {{ height: 92px; padding: 0 40px; display: flex; align-items: center; border: 3px solid {INK}; border-bottom: 0; border-radius: 24px 24px 0 0; background-color: {KRAFT}; color: {INK}; font-size: 38px; font-weight: 400; }}
.tab.sel {{ background-color: #FFFFFF; font-weight: 500; box-shadow: inset 0 8px 0 {YEL}; }}
.page {{ position: absolute; left: 0; top: 89px; width: 888px; height: 930px; border: 3px solid {INK}; border-radius: 0 24px 24px 24px; background-color: #FFFFFF;
  background-image: repeating-linear-gradient(rgba(226,221,208,0) 0px, rgba(226,221,208,0) 80px, {LINE} 80px, {LINE} 82px); background-position: 0 6px; box-shadow: 0 28px 68px rgba(0,0,0,0.18); }}
.page .h1 {{ position: absolute; left: 56px; top: 50px; font-size: 140px; }}
.page .plab {{ position: absolute; left: 56px; top: 236px; color: {TEXT}; }}
.page .list {{ position: absolute; left: 0; top: 400px; width: 888px; }}
.it {{ position: absolute; height: 82px; display: flex; align-items: center; gap: 18px; }}
.it svg {{ width: 44px; height: 44px; flex: none; }}
.it .wr {{ display: block; font-size: 38px; font-weight: 400; color: {TEXT}; white-space: nowrap; }}
#s5 .list {{ top: 400px; }}
#s4, #s5 {{ perspective: 2600px; }}

/* S7 proof: the one brown band */
#s7 .band {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; background-color: {BROWN}; }}
#s7 .num {{ position: absolute; left: {M}px; color: #FFFFFF; font-size: 150px; font-weight: 600; letter-spacing: -0.03em; line-height: 1.05; white-space: nowrap; }}
#s7 .nl {{ position: absolute; left: {M}px; color: {CREAM}; font-size: 44px; font-weight: 500; }}
#s7 .circ {{ position: absolute; left: {M - 34}px; top: 524px; width: 470px; height: 230px; }}
#s7 .hr {{ position: absolute; left: {M}px; top: 1226px; width: 888px; height: 3px; background-color: rgba(237,230,211,0.35); transform-origin: 0% 50%; }}
#s7 .fact {{ position: absolute; left: {M}px; color: {CREAM}; font-size: 44px; font-weight: 500; line-height: 1.3; }}

/* S8 close: the one yellow band */
#s8 .band {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; background-color: {YEL};
  background-image: radial-gradient(rgba(0,0,0,0.12) 2.2px, rgba(0,0,0,0) 2.4px); background-size: 44px 44px; background-position: 22px 22px; }}
#s8 .yl {{ position: absolute; left: {M}px; top: 136px; }}
#s8 .line {{ position: absolute; left: {M}px; top: 600px; font-size: 92px; font-weight: 500; line-height: 1.08; letter-spacing: -0.025em; color: {INK}; }}
#s8 .btn {{ position: absolute; left: {M}px; top: 900px; height: 128px; padding: 0 56px; border: 3px solid {INK}; border-radius: 24px; background-color: {CTA};
  box-shadow: 8px 8px 0 {INK}; display: flex; align-items: center; color: #FFFFFF; font-size: 48px; font-weight: 500; white-space: nowrap; }}
#s8 .url {{ position: absolute; left: {M}px; top: 1110px; font-size: 56px; font-weight: 500; color: {INK}; letter-spacing: -0.01em; }}
#s8 .legal {{ position: absolute; left: {M}px; top: 1700px; width: 888px; font-size: 26px; line-height: 1.45; font-weight: 400; color: {TEXT}; }}
"""

html = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>SJ Academy, May/June 2027</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>{css}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="20" data-fps="60" data-width="1080" data-height="1920">
      <audio id="bgm" src="assets/audio/bgm20.wav" data-start="0" data-duration="20" data-track-index="10" data-volume="0.9"></audio>
      <audio id="sfx-swipe1" src="assets/sfx3/swipe.wav" data-start="1.3" data-duration="0.5" data-track-index="11" data-volume="0.7"></audio>
      <audio id="sfx-pen1" src="assets/sfx3/pen.wav" data-start="3.25" data-duration="0.4" data-track-index="12" data-volume="0.8"></audio>
      <audio id="sfx-pen2" src="assets/sfx3/pen.wav" data-start="4.45" data-duration="0.4" data-track-index="11" data-volume="0.8"></audio>
      <audio id="sfx-stamp" src="assets/sfx3/stamp.wav" data-start="4.95" data-duration="0.4" data-track-index="12" data-volume="0.9"></audio>
      <audio id="sfx-tap1" src="assets/sfx3/tap.wav" data-start="7.05" data-duration="0.2" data-track-index="11" data-volume="0.7"></audio>
      <audio id="sfx-tap2" src="assets/sfx3/tap.wav" data-start="7.55" data-duration="0.2" data-track-index="12" data-volume="0.7"></audio>
      <audio id="sfx-swipe2" src="assets/sfx3/swipe.wav" data-start="8.85" data-duration="0.5" data-track-index="11" data-volume="0.6"></audio>
      <audio id="sfx-pen3" src="assets/sfx3/pen.wav" data-start="9.2" data-duration="0.4" data-track-index="12" data-volume="0.6"></audio>
      <audio id="sfx-turn" src="assets/sfx3/pageturn.wav" data-start="10.95" data-duration="0.7" data-track-index="11" data-volume="0.9"></audio>
      <audio id="sfx-pen4" src="assets/sfx3/pen.wav" data-start="11.9" data-duration="0.4" data-track-index="12" data-volume="0.6"></audio>
      <audio id="sfx-pen5" src="assets/sfx3/pen.wav" data-start="16.75" data-duration="0.4" data-track-index="11" data-volume="0.8"></audio>

      <div class="dots"></div>

      <!-- S1 · 0–2.5 · hook -->
      <div id="s1" class="scene"><div class="cam">
        <div class="logo pic" role="img" aria-label="SJ Academy" style="background-image: url('assets/brand-v3/sj-academy-logo-horizontal-on-light.svg'); background-size: contain; background-position: left center; background-repeat: no-repeat; width: 290px; height: 69px;"></div>
        <div class="abs h1">
          <span class="ln">{words("Cambridge")}</span>
          <span class="ln">{words("doesn't mark")}</span>
          <span class="ln">{words("effort.")}</span>
          <span class="ln">{words("It marks")}</span>
          <span class="ln"><span class="w hl"><i class="bg"></i><span class="tx">method.</span></span></span>
        </div>
      </div></div>

      <!-- S2 · 2.5–5.5 · method -->
      <div id="s2" class="scene"><div class="cam">
        <div class="abs sub lab"><span class="l1">First attempt</span></div>
        <div class="abs sub lab lab2" style="opacity: 0">After SJ method</div>
        <div class="abs paper">
          <div class="ruled"></div>
          <div class="mline"></div>
          <div class="pq"><small>Sample answer</small>Analyse the benefits to a business of training its employees. [8]</div>
          <div class="rule"></div>
          <div class="ans a1"><span class="al">Training is good because</span><span class="al">workers learn new skills</span><span class="al">and work better.</span></div>
          <div class="mark">3/8</div>
          <div class="mnote">Describes.<br />No chain of reasoning.</div>
          <div class="ans a2"><span class="al">Training raises productivity, {RT}</span><span class="al">so unit costs fall. {RT}</span><span class="al">Lower costs allow lower prices,</span><span class="al">which can raise market share</span><span class="al">and profit. {RT}</span></div>
          <div class="stamp">8/8</div>
        </div>
      </div></div>

      <!-- S3 · 5.5–8.5 · website: find your class (real capture) -->
      <div id="s3" class="scene"><div class="cam">
        <div class="screen">
          <div class="sc pic" role="img" aria-label="sjacademy.pk homepage" style="background-image: url('assets/site/scroll-find.png'); background-size: 100% 100%; background-repeat: no-repeat; width: 820px; height: 2864px;"></div>
          <div class="fo pic" role="img" aria-label="Find your class, O Level tab" style="background-image: url('assets/site/find-olevel-crop.png'); background-size: 100% 100%; background-repeat: no-repeat; width: 820px; height: 1314px; opacity: 0"></div>
          <div class="ft pic" role="img" aria-label="Find your class, Physics selected" style="background-image: url('assets/site/find-tapped-crop.png'); background-size: 100% 100%; background-repeat: no-repeat; width: 820px; height: 1314px; opacity: 0"></div>
          <div class="tap t1" style="left: {TAP_TAB[0]}px; top: {TAP_TAB[1]}px"></div>
          <div class="tap t2" style="left: {TAP_PHY[0]}px; top: {TAP_PHY[1]}px"></div>
        </div>
      </div></div>

      <!-- S5 · 11–13.5 · A Level (sits under the O Level page for the page-turn) -->
      <div id="s5" class="scene"><div class="cam">
        <div class="nb">
          {tabs("A")}
          <div class="page">
            <div class="h1"><span class="w hl"><i class="bg"></i><span class="tx">A Level</span></span></div>
            <div class="sub plab">Cambridge International<br />AS and A Level</div>
            <div class="list">{subj_list(A_SUBJ, "ai")}</div>
          </div>
        </div>
      </div></div>

      <!-- S4 · 8.5–11 · O Level -->
      <div id="s4" class="scene"><div class="cam">
        <div class="nb">
          {tabs("O")}
          <div class="page">
            <div class="h1"><span class="w hl"><i class="bg"></i><span class="tx">O Level</span></span></div>
            <div class="sub plab">Cambridge O Level</div>
            <div class="list">{subj_list(O_SUBJ, "oi")}</div>
          </div>
        </div>
      </div></div>

      <!-- S6 · 13.5–15.5 · website: free tools (real capture) -->
      <div id="s6" class="scene"><div class="cam">
        <div class="abs sub lab">Free for every O and A Level student</div>
        <div class="screen"><div class="sc pic" role="img" aria-label="sjacademy.pk free tools" style="background-image: url('assets/site/scroll-tools.png'); background-size: 100% 100%; background-repeat: no-repeat; width: 820px; height: 1766px;"></div></div>
      </div></div>

      <!-- S7 · 15.5–18 · proof (the one brown band) -->
      <div id="s7" class="scene">
        <div class="band"></div>
        <div class="cam">
          <div class="num n1" style="top: 520px"><span id="c950">0</span>+</div>
          <svg class="pen circ" viewBox="0 0 120 70" preserveAspectRatio="none"><path d="{CIRCLE}" stroke="{ORG}" stroke-width="1.8" pathLength="1" /></svg>
          <div class="nl l1" style="top: 692px">A*s</div>
          <div class="num n2" style="top: 820px"><span id="c4500">0</span>+</div>
          <div class="nl l2" style="top: 992px">students taught</div>
          <div class="hr"></div>
          <div class="fact f1" style="top: 1270px">Rated 5.0 on Google from 226 reviews</div>
          <div class="fact f2" style="top: 1350px">Teachers from LUMS, IBA and KGS</div>
        </div>
      </div>

      <!-- S8 · 18–20 · close (the one yellow band) -->
      <div id="s8" class="scene">
        <div class="band"></div>
        <div class="cam">
          <div class="yl pic" role="img" aria-label="SJ Academy" style="background-image: url('assets/brand-v3/sj-academy-logo-horizontal-on-yellow.svg'); background-size: contain; background-position: left center; background-repeat: no-repeat; width: 290px; height: 69px;"></div>
          <div class="line"><span class="ln">{words("One class free,")}</span><span class="ln">{words("then decide")}</span></div>
          <div class="btn">Book a free demo on WhatsApp</div>
          <div class="url">sjacademy.pk</div>
          <div class="legal">SJ Academy is an independent tuition centre and is not affiliated with or endorsed by Cambridge.</div>
        </div>
      </div>

      <div id="pill">O &amp; A Level · May/June 2027</div>
    </div>
    <script>
      const FIND_END = {FIND_END}, TOOLS_END = {TOOLS_END};
{open("build/timeline3.js").read()}
    </script>
  </body>
</html>
"""
WIN = {"s1": (0, 3.25), "s2": (2.4, 3.3), "s3": (5.65, 3.75), "s4": (8.45, 3.4), "s5": (10.9, 3.5),
       "s6": (13.45, 2.95), "s7": (15.45, 3.31), "s8": (17.95, 2.05)}
import re as _re
for i, (sid, (st, du)) in enumerate(WIN.items()):
    open_tag = f'<div id="{sid}" class="scene">'
    a = html.index(open_tag)
    b = _re.search(r"\n\s*(<!--|<div id=\"pill\")", html[a:]).start() + a
    html = (html[:a] + f'<div class="clip" id="clip-{sid}" data-start="{st}" data-duration="{du}" data-track-index="{1 + i % 2}">'
            + html[a:b] + "</div>" + html[b:])
open("index.html", "w").write(html)
print("ok")
