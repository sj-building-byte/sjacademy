# Generates index.html for the SJ Academy 18s launch promo (9:16).
# Run from the project root: python3 build/gen.py
O = ["Maths", "Physics", "Chemistry", "Biology", "Accounting", "Business", "Economics",
     "Computer Science", "English", "Urdu", "Pakistan Studies", "Islamiyat"]
A = ["Maths", "Physics", "Chemistry", "Biology", "Accounting", "Business", "Economics",
     "Computer Science", "Psychology", "Sociology", "English", "Urdu"]

Y, B, OR, CR = "#FCE004", "#453516", "#FE6100", "#F7F5EF"

o_lines = "\n".join(
    f'          <div class="ol-row"><span class="ol-n">{i+1:02d}</span><span class="ol-w">{s}</span></div>'
    for i, s in enumerate(O))

tag_styles = ["t-b", "t-y", "t-c", "t-b", "t-y", "t-b", "t-c", "t-b", "t-y", "t-b", "t-c", "t-y"]
a_tags = "\n".join(f'          <div class="al-tag {tag_styles[i]}">{s}</div>' for i, s in enumerate(A))

TICK = '<svg class="tick" viewBox="0 0 60 44"><path d="M5 24 L21 38 L55 6" /></svg>'

html = f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>SJ Academy — May/June 2027</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@hyperframes/shader-transitions@0.8.143/dist/index.global.js"></script>
    <style>
      @font-face {{ font-family: "Poppins"; font-weight: 400; src: url("assets/fonts/Poppins-Regular.ttf") format("truetype"); }}
      @font-face {{ font-family: "Poppins"; font-weight: 600; src: url("assets/fonts/Poppins-SemiBold.ttf") format("truetype"); }}
      @font-face {{ font-family: "Poppins"; font-weight: 700; src: url("assets/fonts/Poppins-Bold.ttf") format("truetype"); }}
      @font-face {{ font-family: "Poppins"; font-weight: 800; src: url("assets/fonts/Poppins-ExtraBold.ttf") format("truetype"); }}
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background-color: {B}; font-family: "Poppins", sans-serif; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background-color: {B}; }}
      .scene {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; overflow: hidden; }}
      .cam {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; }}
      .abs {{ position: absolute; }}
      .shape {{ position: absolute; border-radius: 50%; }}
      .mask {{ display: block; overflow: hidden; }}
      .w {{ display: inline-block; }}
      .kicker {{ font-size: 34px; font-weight: 600; letter-spacing: 6px; text-transform: uppercase; }}

      /* S1 — brand reveal (orange) */
      #s1 {{ background-color: {OR}; }}
      #s1 .sun {{ left: 520px; top: -260px; width: 860px; height: 860px; background-color: {Y}; }}
      #s1 .ring {{ left: -300px; top: 1180px; width: 760px; height: 760px; border: 34px solid {B}; opacity: 0.18; }}
      #s1 .plate {{ left: 60px; top: 190px; width: 680px; height: 190px; background-color: {CR}; border-radius: 28px; display: flex; align-items: center; justify-content: center; }}
      #s1 .plate img {{ width: 600px; height: auto; display: block; }}
      #s1 .k1 {{ left: 64px; top: 450px; color: {B}; }}
      #s1 .big {{ left: 52px; top: 520px; color: {B}; font-size: 180px; font-weight: 800; line-height: 1.02; letter-spacing: -6px; white-space: nowrap; }}
      #s1 .big .ch {{ display: inline-block; }}
      #s1 .bar {{ left: 60px; top: 920px; height: 150px; padding: 0 44px; background-color: {B}; border-radius: 22px; display: flex; align-items: center; }}
      #s1 .bar span {{ color: {Y}; font-size: 92px; font-weight: 800; letter-spacing: -2px; white-space: nowrap; }}
      #s1 .yr {{ left: 40px; top: 1190px; color: {B}; font-size: 400px; font-weight: 800; line-height: 1; letter-spacing: -20px; white-space: nowrap; }}
      #s1 .band {{ left: -40px; top: 1660px; width: 1160px; height: 150px; background-color: {B}; overflow: hidden; }}
      #s1 .mq {{ position: absolute; left: 0; top: 0; height: 150px; display: flex; align-items: center; color: {Y}; font-size: 66px; font-weight: 700; white-space: nowrap; letter-spacing: -1px; }}

      /* S2 — hook (brown) */
      #s2 {{ background-color: {B}; }}
      #s2 .ghost {{ left: 430px; top: 1060px; width: 900px; height: 900px; border-radius: 50%; background-color: #4F3E1C; }}
      #s2 .gt {{ opacity: 0.16; width: 260px; height: 190px; }}
      #s2 .gt path {{ stroke: {OR}; }}
      #s2 .k2 {{ left: 64px; top: 250px; color: {OR}; }}
      #s2 .hl {{ left: 56px; top: 360px; color: {CR}; font-weight: 800; letter-spacing: -5px; line-height: 1.04; white-space: nowrap; }}
      #s2 .l1 {{ font-size: 190px; }}
      #s2 .l2 {{ font-size: 140px; }}
      #s2 .l3 {{ font-size: 300px; letter-spacing: -10px; }}
      #s2 .l4 {{ font-size: 165px; }}
      #s2 .bt {{ left: 560px; top: 1430px; width: 440px; height: 330px; }}
      #s2 .bt path {{ fill: none; stroke: {OR}; stroke-width: 9; stroke-linecap: round; stroke-linejoin: round; }}
      #s2 .mk {{ position: relative; display: inline-block; padding: 0 22px; color: {B}; }}
      #s2 .mk .hi {{ position: absolute; left: 0; top: 10%; width: 100%; height: 84%; background-color: {Y}; border-radius: 16px; transform-origin: 0% 50%; }}
      #s2 .mk .tx {{ position: relative; display: inline-block; }}
      #s2 .sub {{ left: 64px; top: 1290px; width: 900px; color: {Y}; font-size: 50px; font-weight: 600; line-height: 1.3; }}

      /* S3 — O Level (yellow) */
      #s3 {{ background-color: {Y}; }}
      #s3 .blob {{ left: 700px; top: -160px; width: 560px; height: 560px; background-color: {OR}; }}
      #s3 .lab {{ left: 56px; top: 190px; color: {B}; font-size: 190px; font-weight: 800; letter-spacing: -7px; line-height: 1; white-space: nowrap; }}
      #s3 .k3 {{ left: 64px; top: 405px; color: {B}; }}
      #s3 .stack {{ left: 60px; top: 480px; width: 960px; }}
      #s3 .ol-row {{ display: flex; align-items: baseline; gap: 22px; height: 104px; border-top: 3px solid rgba(69,53,22,0.22); overflow: hidden; }}
      #s3 .ol-n {{ flex: none; width: 58px; font-size: 30px; font-weight: 700; color: #8A3A00; }}
      #s3 .ol-w {{ display: block; font-size: 86px; font-weight: 800; letter-spacing: -3px; line-height: 1.18; color: {B}; white-space: nowrap; }}
      #s3 .ol-row:nth-child(even) .ol-w {{ color: #8A3A00; }}
      #s3 .scan {{ left: 40px; top: 483px; width: 1000px; height: 101px; background-color: {B}; border-radius: 12px; opacity: 0; }}

      /* S4 — A Level (orange) */
      #s4 {{ background-color: {OR}; }}
      #s4 .disc {{ left: -260px; top: -200px; width: 720px; height: 720px; background-color: {Y}; opacity: 0.9; }}
      #s4 .lab {{ left: 56px; top: 210px; color: {B}; font-size: 220px; font-weight: 800; letter-spacing: -8px; line-height: 1; white-space: nowrap; }}
      #s4 .k4 {{ left: 64px; top: 460px; color: {B}; }}
      #s4 .cloud {{ left: 40px; top: 600px; width: 1000px; display: flex; flex-wrap: wrap; justify-content: center; align-content: flex-start; gap: 24px 16px; }}
      #s4 .al-tag {{ display: block; font-size: 60px; font-weight: 700; line-height: 1; padding: 30px 36px 32px; border-radius: 999px; white-space: nowrap; }}
      #s4 .t-b {{ background-color: {B}; color: {Y}; }}
      #s4 .t-y {{ background-color: {Y}; color: {B}; }}
      #s4 .t-c {{ background-color: {CR}; color: {B}; }}
      #s4 .as {{ left: 56px; top: 1610px; color: {B}; font-size: 200px; font-weight: 800; letter-spacing: -8px; line-height: 1; white-space: nowrap; }}

      /* S5 — method (brown) */
      #s5 {{ background-color: {B}; }}
      #s5 .glow {{ left: 380px; top: 420px; width: 1000px; height: 1000px; background-color: #5A4622; }}
      #s5 .hd {{ left: 60px; top: 200px; width: 980px; color: {CR}; font-size: 70px; font-weight: 800; line-height: 1.08; letter-spacing: -2px; }}
      #s5 .hd .y {{ color: {Y}; }}
      #s5 .paper {{ left: 110px; top: 470px; width: 860px; height: 980px; background-color: #FFFDF6; border-radius: 10px; box-shadow: 0 30px 80px rgba(0,0,0,0.35); padding: 54px 60px; overflow: hidden; }}
      #s5 .pmeta {{ font-size: 24px; font-weight: 600; color: #8A7A55; letter-spacing: 2px; text-transform: uppercase; }}
      #s5 .pq {{ margin-top: 14px; font-size: 34px; font-weight: 700; color: {B}; line-height: 1.25; }}
      #s5 .pq b {{ color: {OR}; }}
      #s5 .rule {{ margin-top: 26px; height: 3px; background-color: #E2DDD0; }}
      #s5 .ln {{ position: relative; height: 66px; display: flex; align-items: center; border-bottom: 2px solid #EFEAE0; }}
      #s5 .ln i {{ display: block; height: 16px; border-radius: 8px; background-color: #B9B2A2; }}
      #s5 .tick {{ position: absolute; right: 120px; top: 8px; width: 60px; height: 44px; }}
      #s5 svg path {{ fill: none; stroke: {OR}; stroke-width: 7; stroke-linecap: round; stroke-linejoin: round; }}
      #s5 .note {{ position: absolute; right: -6px; top: 14px; font-size: 26px; font-weight: 700; color: {OR}; border: 3px solid {OR}; border-radius: 10px; padding: 2px 10px; }}
      #s5 .score {{ right: 50px; bottom: 50px; width: 190px; height: 190px; border-radius: 50%; border: 8px solid {OR}; color: {OR}; display: flex; align-items: center; justify-content: center; font-size: 78px; font-weight: 800; letter-spacing: -2px; }}
      #s5 .pnote {{ left: 60px; bottom: 90px; font-size: 30px; font-weight: 700; color: {OR}; }}
      #s5 .photo {{ left: 60px; top: 560px; width: 960px; height: 720px; border-radius: 28px; overflow: hidden; background-color: #2E230E; }}
      #s5 .photo img {{ position: absolute; left: -180px; top: 0; width: 1320px; height: 722px; object-fit: cover; }}
      #s5 .cap {{ left: 30px; bottom: 30px; background-color: {Y}; color: {B}; font-size: 36px; font-weight: 700; padding: 12px 26px; border-radius: 14px; }}
      #s5 .sub {{ left: 60px; top: 1500px; width: 980px; color: {Y}; font-size: 82px; font-weight: 800; line-height: 1.08; letter-spacing: -2px; }}

      /* S6 — proof (yellow) */
      #s6 {{ background-color: {Y}; }}
      #s6 .blob {{ left: 640px; top: 1300px; width: 760px; height: 760px; background-color: {OR}; }}
      #s6 .row {{ left: 60px; width: 960px; height: 300px; border-top: 4px solid {B}; }}
      #s6 .num {{ display: block; color: {B}; font-size: 210px; font-weight: 800; letter-spacing: -9px; line-height: 1.05; white-space: nowrap; }}
      #s6 .lbl {{ display: block; color: {B}; font-size: 44px; font-weight: 600; line-height: 1.1; }}
      #s6 .r1 {{ top: 170px; }}
      #s6 .r2 {{ top: 500px; }}
      #s6 .r3 {{ top: 830px; }}
      #s6 .stars {{ position: absolute; left: 430px; top: 90px; display: flex; gap: 12px; }}
      #s6 .stars svg {{ width: 82px; height: 82px; }}
      #s6 .stars path {{ fill: {OR}; }}
      #s6 .teach {{ left: 60px; top: 1210px; width: 960px; color: {B}; }}
      #s6 .tl {{ font-size: 58px; font-weight: 800; letter-spacing: -1px; line-height: 1.1; }}
      #s6 .pills {{ margin-top: 30px; display: flex; gap: 22px; }}
      #s6 .pill {{ display: block; background-color: {B}; color: {Y}; font-size: 92px; font-weight: 800; letter-spacing: -2px; padding: 16px 44px 20px; border-radius: 26px; }}

      /* S7 — close (brown) */
      #s7 {{ background-color: {B}; }}
      #s7 .c1 {{ left: 560px; top: 1560px; width: 760px; height: 760px; background-color: {OR}; }}
      #s7 .c2 {{ left: 700px; top: -220px; width: 600px; height: 600px; border: 30px solid {Y}; opacity: 0.25; }}
      #s7 .hl {{ left: 56px; top: 210px; color: {CR}; font-weight: 800; letter-spacing: -6px; line-height: 1.04; white-space: nowrap; }}
      #s7 .a {{ font-size: 170px; }}
      #s7 .a2 {{ font-size: 170px; color: {Y}; }}
      #s7 .b {{ font-size: 130px; }}
      #s7 .plate {{ left: 60px; top: 800px; width: 660px; height: 180px; background-color: {CR}; border-radius: 26px; display: flex; align-items: center; justify-content: center; }}
      #s7 .plate img {{ width: 580px; height: auto; display: block; }}
      #s7 .adm {{ left: 64px; top: 1030px; color: {Y}; font-size: 60px; font-weight: 800; letter-spacing: -1px; line-height: 1.1; }}
      #s7 .mode {{ left: 64px; top: 1120px; width: 960px; color: {CR}; font-size: 44px; font-weight: 600; line-height: 1.25; }}
      #s7 .url {{ left: 60px; top: 1250px; background-color: {OR}; color: {B}; font-size: 104px; font-weight: 800; letter-spacing: -3px; padding: 18px 50px 26px; border-radius: 30px; white-space: nowrap; }}

      #s7 .demo {{ left: 64px; top: 1470px; color: {CR}; font-size: 50px; font-weight: 700; line-height: 1.2; }}
      #s7 .demo b {{ color: {Y}; }}
      #grain {{ position: absolute; left: -60px; top: -60px; width: 1200px; height: 2040px; z-index: 100; pointer-events: none; opacity: 0.13; mix-blend-mode: overlay;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E"); }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="18" data-width="1080" data-height="1920">
      <audio id="bgm" src="assets/audio/bgm.wav" data-start="0" data-duration="18" data-track-index="10" data-volume="0.8"></audio>
      <audio id="sfx-1" src="assets/sfx/impact-bass-1.mp3" data-start="2.0" data-duration="2.1" data-track-index="11" data-volume="0.45"></audio>
      <audio id="sfx-2" src="assets/sfx/whoosh-short.mp3" data-start="4.25" data-duration="0.57" data-track-index="12" data-volume="0.55"></audio>
      <audio id="sfx-3" src="assets/sfx/whoosh.mp3" data-start="6.75" data-duration="0.57" data-track-index="11" data-volume="0.55"></audio>
      <audio id="sfx-4" src="assets/sfx/whoosh-short.mp3" data-start="9.25" data-duration="0.57" data-track-index="12" data-volume="0.55"></audio>
      <audio id="sfx-5" src="assets/sfx/impact-bass-2.mp3" data-start="12.5" data-duration="2.5" data-track-index="11" data-volume="0.45"></audio>
      <audio id="sfx-6" src="assets/sfx/whoosh.mp3" data-start="15.25" data-duration="0.57" data-track-index="12" data-volume="0.5"></audio>

      <!-- S1 · 0–2s · brand reveal -->
      <div id="s1" class="scene">
        <div class="cam">
          <div class="shape sun"></div>
          <div class="shape ring"></div>
          <div class="abs yr">2027</div>
          <div class="abs plate"><img src="assets/brand/sj-logo.svg" alt="SJ Academy" /></div>
          <div class="abs kicker k1">O &amp; A Level coaching · Karachi</div>
          <div class="abs big">
            <div class="ln1">{''.join(f'<span class="ch">{c if c != " " else "&nbsp;"}</span>' for c in "O Level")}</div>
            <div class="ln2">{''.join(f'<span class="ch">{c if c != " " else "&nbsp;"}</span>' for c in "& A Level").replace(">&<", ">&amp;<")}</div>
          </div>
          <div class="abs bar"><span>May/June 2027</span></div>
          <div class="abs band"><div class="mq">Maths · Physics · Chemistry · Biology · Accounting · Business · Economics · Computer Science · English · Urdu · </div></div>
        </div>
      </div>

      <!-- S2 · 2–4.5s · hook -->
      <div id="s2" class="scene">
        <div class="cam">
          <div class="shape ghost"></div>
          <svg class="abs gt gt1" viewBox="0 0 60 44" style="left: 700px; top: 160px"><path d="M5 24 L21 38 L55 6" fill="none" stroke-width="7" stroke-linecap="round" /></svg>
          <svg class="abs gt gt2" viewBox="0 0 60 44" style="left: 40px; top: 1640px"><path d="M5 24 L21 38 L55 6" fill="none" stroke-width="7" stroke-linecap="round" /></svg>
          <div class="abs kicker k2">The SJ Academy method</div>
          <div class="abs hl">
            <div class="mask l1"><span class="w">Learn</span> <span class="w">to</span></div>
            <div class="mask l2"><span class="w">think</span> <span class="w">like</span> <span class="w">a</span></div>
            <div class="mask l3"><span class="w mk mk1"><i class="hi"></i><span class="tx">CAIE</span></span></div>
            <div class="mask l4"><span class="w mk mk2"><i class="hi"></i><span class="tx">examiner.</span></span></div>
          </div>
          <div class="abs sub">See the paper the way the person marking it does.</div>
          <svg class="abs bt" viewBox="0 0 60 44"><path d="M5 24 L21 38 L55 6" /></svg>
        </div>
      </div>

      <!-- S3 · 4.5–7s · O Level -->
      <div id="s3" class="scene">
        <div class="cam">
          <div class="shape blob"></div>
          <div class="abs lab">O Level</div>
          <div class="abs kicker k3">May/June 2027 · CAIE</div>
          <div class="abs scan"></div>
          <div class="abs stack">
{o_lines}
          </div>
        </div>
      </div>

      <!-- S4 · 7–9.5s · A Level -->
      <div id="s4" class="scene">
        <div class="cam">
          <div class="shape disc"></div>
          <div class="abs lab">A Level</div>
          <div class="abs kicker k4">AS and A2 · May/June 2027</div>
          <div class="abs cloud">
{a_tags}
          </div>
          <div class="abs as">AS &amp; A2.</div>
        </div>
      </div>

      <!-- S5 · 9.5–12.5s · method -->
      <div id="s5" class="scene">
        <div class="cam">
          <div class="shape glow"></div>
          <div class="abs hd"><span class="w">Past</span> <span class="w">papers</span> <span class="w">marked</span> <span class="w">to</span> <span class="w">the</span> <span class="w y">Cambridge</span> <span class="w y">scheme.</span></div>
          <div class="abs paper">
            <div class="pmeta">Sample answer · Paper 1</div>
            <div class="pq">Analyse two benefits of the decision for the business. <b>[8]</b></div>
            <div class="rule"></div>
            <div class="ln"><i style="width: 92%"></i>{TICK}<span class="note">AO1</span></div>
            <div class="ln"><i style="width: 78%"></i></div>
            <div class="ln"><i style="width: 86%"></i>{TICK}<span class="note">AO2</span></div>
            <div class="ln"><i style="width: 64%"></i></div>
            <div class="ln"><i style="width: 90%"></i>{TICK}<span class="note">AO3</span></div>
            <div class="ln"><i style="width: 72%"></i></div>
            <div class="ln"><i style="width: 58%"></i><span class="note nx">AO4 ?</span></div>
            <div class="abs pnote">Link back to the question.</div>
            <div class="abs score">6/8</div>
          </div>
          <div class="abs photo"><img src="assets/brand/classroom.jpg" alt="A class at SJ Academy" /><div class="abs cap">A class at DHA Phase 7</div></div>
          <div class="abs sub"><span class="w">See</span> <span class="w">exactly</span> <span class="w">where</span> <span class="w">marks</span> <span class="w">were</span> <span class="w">lost.</span></div>
        </div>
      </div>

      <!-- S6 · 12.5–15.5s · proof -->
      <div id="s6" class="scene">
        <div class="cam">
          <div class="shape blob"></div>
          <div class="abs row r1"><span class="num" id="n1">950+</span><span class="lbl">A*s achieved at SJ Academy</span></div>
          <div class="abs row r2"><span class="num" id="n2">4,500+</span><span class="lbl">students taught</span></div>
          <div class="abs row r3"><span class="num" id="n3">5.0</span><span class="lbl">Google rating from 226 reviews</span>
            <div class="stars">{''.join('<svg viewBox="0 0 24 24"><path d="M12 1.8l3.1 6.6 7.2.9-5.3 5 1.4 7.1L12 17.9 5.6 21.4 7 14.3 1.7 9.3l7.2-.9z"/></svg>' for _ in range(5))}</div>
          </div>
          <div class="abs teach"><div class="tl">Teachers from</div><div class="pills"><span class="pill">LUMS</span><span class="pill">IBA</span><span class="pill">KGS</span></div></div>
        </div>
      </div>

      <!-- S7 · 15.5–18s · close -->
      <div id="s7" class="scene">
        <div class="cam">
          <div class="shape c1"></div>
          <div class="shape c2"></div>
          <div class="abs hl">
            <div class="mask a"><span class="w">One</span> <span class="w">class</span></div>
            <div class="mask a2"><span class="w">free.</span></div>
            <div class="mask b"><span class="w">Then</span> <span class="w">decide.</span></div>
          </div>
          <div class="abs plate"><img src="assets/brand/sj-logo-end.svg" alt="SJ Academy" /></div>
          <div class="abs adm">May/June 2027 admissions open</div>
          <div class="abs mode">In class in DHA Phase 7 or live online</div>
          <div class="abs url">sjacademy.pk</div>
          <div class="abs demo">Book a <b>free demo</b> class.</div>
        </div>
      </div>

      <div id="grain"></div>
    </div>

    <script>
{open("build/timeline.js").read()}    </script>
  </body>
</html>
'''
open("index.html", "w").write(html)
print("ok")
