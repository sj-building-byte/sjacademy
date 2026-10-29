# Themed generator for the SJ Academy 18s promo (9:16).
# Usage (from project root): python3 build/gen2.py <look>   looks: golden | noir | serif
import sys

LOOK = sys.argv[1] if len(sys.argv) > 1 else "golden"

# ── palette: brand anchors + expansion ─────────────────────────────────────
NB, ESP, BR, DB = "#140C04", "#2A1A08", "#453516", "#1F1408"
CR, CR2 = "#FFF4DC", "#F7EBD0"
Y, AM, OR, HO, CO, RUST = "#FCE004", "#FFB21A", "#FE6100", "#FF4D1A", "#FF7A59", "#8A3A00"

GRAD = {
    "night": (ESP, f"radial-gradient(120% 70% at 50% 0%, rgba(69,53,22,0.9) 0%, rgba(69,53,22,0) 70%), linear-gradient(175deg, {ESP} 0%, #1A1006 55%, #0D0803 100%)"),
    "sun": (AM, f"linear-gradient(160deg, #FFE94A 0%, {Y} 28%, {AM} 64%, {OR} 100%)"),
    "fire": (OR, f"linear-gradient(165deg, {AM} 0%, {OR} 42%, {HO} 78%, #E8452C 100%)"),
    "cream": ("#FFE6A8", f"linear-gradient(170deg, #FFF6DE 0%, #FFE9B0 45%, #FFC94D 80%, {AM} 100%)"),
}
TXT_HOT = f"linear-gradient(100deg, {Y} 0%, {AM} 45%, {OR} 100%)"
TXT_DEEP = f"linear-gradient(100deg, {ESP} 0%, {RUST} 100%)"

LOOKS = {
    "golden": dict(
        scenes=["night", "sun", "night", "fire", "night", "cream", "night"],
        head=dict(family="Poppins", weight=800, ls="-0.035em", lh=1.0, tt="none"),
        acc=dict(family="Instrument Serif", style="italic", weight=400, scale=1.18),
    ),
    "noir": dict(
        scenes=["night", "night", "fire", "night", "night", "sun", "night"],
        head=dict(family="Anton", weight=400, ls="0em", lh=1.0, tt="uppercase"),
        acc=dict(family="Poppins", style="normal", weight=800, scale=0.92),
    ),
    "serif": dict(
        scenes=["sun", "night", "cream", "fire", "night", "sun", "night"],
        head=dict(family="DM Serif Display", weight=400, ls="-0.02em", lh=1.0, tt="none"),
        acc=dict(family="DM Serif Display", style="italic", weight=400, scale=1.0),
    ),
}
L = LOOKS[LOOK]
H, A = L["head"], L["acc"]


def sc(i):
    """Per-scene token set derived from its ground."""
    g = L["scenes"][i]
    dark = g == "night"
    return dict(
        bgc=GRAD[g][0], bg=GRAD[g][1], dark=dark,
        fg=CR if dark else NB,
        sub=AM if dark else ESP,
        kick=AM if dark else ESP,
        txt=TXT_HOT if dark else TXT_DEEP,
        logo="assets/brand/sj-logo-on-dark.svg" if dark else "assets/brand/sj-logo-on-light.svg",
        glow1="rgba(254,97,0,0.55)" if dark else "rgba(255,255,255,0.55)",
        glow2="rgba(255,77,26,0.35)" if dark else "rgba(254,97,0,0.35)",
        ring="rgba(252,224,4,0.22)" if dark else "rgba(20,12,4,0.16)",
        glass="rgba(255,255,255,0.08)" if dark else "rgba(255,255,255,0.32)",
        glassb="rgba(255,255,255,0.22)" if dark else "rgba(255,255,255,0.6)",
        hi=Y if dark else NB, hitx=NB if dark else Y,
        alt=AM if dark else RUST, num=CO if dark else RUST,
    )


S = [sc(i) for i in range(7)]

O = ["Maths", "Physics", "Chemistry", "Biology", "Accounting", "Business", "Economics",
     "Computer Science", "English", "Urdu", "Pakistan Studies", "Islamiyat"]
A_SUBJ = ["Maths", "Physics", "Chemistry", "Biology", "Accounting", "Business", "Economics",
          "Computer Science", "Psychology", "Sociology", "English", "Urdu"]

o_lines = "\n".join(
    f'          <div class="ol-row"><span class="ol-n">{i+1:02d}</span><span class="ol-w">{s}</span></div>'
    for i, s in enumerate(O))
tag_kind = ["k1", "k2", "k3", "k1", "k2", "k1", "k3", "k1", "k2", "k1", "k3", "k2"]
a_tags = "\n".join(f'          <div class="al-tag {tag_kind[i]}">{s}</div>' for i, s in enumerate(A_SUBJ))
TICK = '<svg class="tick" viewBox="0 0 60 44"><path d="M5 24 L21 38 L55 6" /></svg>'
STAR = '<svg viewBox="0 0 24 24"><path d="M12 1.8l3.1 6.6 7.2.9-5.3 5 1.4 7.1L12 17.9 5.6 21.4 7 14.3 1.7 9.3l7.2-.9z"/></svg>'


def chars(t, cls=""):
    out = []
    for c in t:
        c2 = "&nbsp;" if c == " " else ("&amp;" if c == "&" else c)
        out.append(f'<span class="ch {cls}">{c2}</span>')
    return "".join(out)


def glows(i, a, b):
    s = S[i]
    return (f'<div class="glow g1" style="left: {a[0]}px; top: {a[1]}px; width: {a[2]}px; height: {a[2]}px; '
            f'background-image: radial-gradient(circle, {s["glow1"]} 0%, {s["glow1"].rsplit(",", 1)[0]},0) 68%);"></div>\n'
            f'          <div class="glow g2" style="left: {b[0]}px; top: {b[1]}px; width: {b[2]}px; height: {b[2]}px; '
            f'background-image: radial-gradient(circle, {s["glow2"]} 0%, {s["glow2"].rsplit(",", 1)[0]},0) 68%);"></div>')


def scene_css(i):
    s = S[i]
    n = i + 1
    return f"""
      #s{n} {{ background-color: {s['bgc']}; background-image: {s['bg']}; color: {s['fg']}; }}
      #s{n} .kicker {{ color: {s['kick']}; }}
      #s{n} .ring {{ border-color: {s['ring']}; }}
      #s{n} .gtx {{ background-image: {s['txt']}; }}"""


css_scenes = "".join(scene_css(i) for i in range(7))
s1, s2, s3, s4, s5, s6, s7 = S

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
      @font-face {{ font-family: "Instrument Serif"; font-style: normal; src: url("assets/fonts/InstrumentSerif-Regular.ttf") format("truetype"); }}
      @font-face {{ font-family: "Instrument Serif"; font-style: italic; src: url("assets/fonts/InstrumentSerif-Italic.ttf") format("truetype"); }}
      @font-face {{ font-family: "Anton"; src: url("assets/fonts/Anton-Regular.ttf") format("truetype"); }}
      @font-face {{ font-family: "DM Serif Display"; font-style: normal; src: url("assets/fonts/DMSerifDisplay-Regular.ttf") format("truetype"); }}
      @font-face {{ font-family: "DM Serif Display"; font-style: italic; src: url("assets/fonts/DMSerifDisplay-Italic.ttf") format("truetype"); }}
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background-color: {ESP}; font-family: "Poppins", sans-serif; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background-color: {ESP}; }}
      .scene {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; overflow: hidden; }}
      .cam {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; }}
      .abs {{ position: absolute; }}
      .glow {{ position: absolute; border-radius: 50%; }}
      .ring {{ position: absolute; border-radius: 50%; border-style: solid; }}
      .mask {{ display: block; overflow: hidden; }}
      .w {{ display: inline-block; }}
      .H {{ font-family: "{H['family']}", "Poppins", sans-serif; font-weight: {H['weight']}; letter-spacing: {H['ls']}; text-transform: {H['tt']}; }}
      .em {{ font-family: "{A['family']}", serif; font-style: {A['style']}; font-weight: {A['weight']}; font-size: {A['scale']}em; letter-spacing: -0.01em; text-transform: none; }}
      .gtx {{ -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: rgba(0,0,0,0); color: rgba(0,0,0,0); }}
      .kicker {{ font-size: 32px; font-weight: 600; letter-spacing: 7px; text-transform: uppercase; }}
      .glass {{ border: 2px solid; box-shadow: inset 0 1px 0 rgba(255,255,255,0.35), 0 24px 60px rgba(13,8,3,0.28); }}
{css_scenes}

      /* S1 — brand reveal */
      #s1 .logo {{ left: 60px; top: 190px; width: 660px; height: auto; display: block; }}
      #s1 .k1 {{ left: 64px; top: 400px; }}
      #s1 .big {{ left: 52px; top: 470px; font-size: 186px; line-height: 1.04; white-space: nowrap; }}
      #s1 .big .ch {{ display: inline-block; }}
      #s1 .bar {{ left: 60px; top: 900px; height: 150px; padding: 0 46px; border-radius: 999px; display: flex; align-items: center;
        background-image: {"linear-gradient(100deg, " + Y + " 0%, " + AM + " 50%, " + OR + " 100%)" if s1['dark'] else "none"}; background-color: {OR if s1['dark'] else NB}; }}
      #s1 .bar span {{ color: {NB if s1['dark'] else Y}; font-size: 86px; font-weight: 800; letter-spacing: -2px; white-space: nowrap; }}
      #s1 .yr {{ left: 30px; top: 1120px; font-size: 440px; line-height: 1.05; white-space: nowrap; }}
      #s1 .band {{ left: -40px; top: 1690px; width: 1160px; height: 130px; overflow: hidden; background-color: {s1['glass']}; border-color: {s1['glassb']}; border-left: 0; border-right: 0; }}
      #s1 .mq {{ position: absolute; left: 0; top: 0; height: 126px; display: flex; align-items: center; color: {Y if s1['dark'] else NB}; font-size: 58px; font-weight: 700; white-space: nowrap; letter-spacing: -1px; }}
      #s1 .sun {{ left: 420px; top: -300px; width: 1100px; height: 1100px; }}
      #s1 .ring {{ left: -320px; top: 1080px; width: 820px; height: 820px; border-width: 30px; }}

      /* S2 — hook */
      #s2 .ghost {{ left: 300px; top: 900px; width: 1100px; height: 1100px; }}
      #s2 .gt1 {{ left: -200px; top: -200px; width: 800px; height: 800px; }}
      #s2 .ring {{ left: 620px; top: 120px; width: 520px; height: 520px; border-width: 24px; }}
      #s2 .k2 {{ left: 64px; top: 280px; }}
      #s2 .hl {{ left: 56px; top: 360px; line-height: 1.04; white-space: nowrap; }}
      #s2 .l1 {{ font-size: 190px; }}
      #s2 .l2 {{ font-size: 140px; }}
      #s2 .l3 {{ font-size: 300px; }}
      #s2 .l4 {{ font-size: 165px; }}
      #s2 .mk {{ position: relative; display: inline-block; padding: 0 24px; }}
      #s2 .mk .hi {{ position: absolute; left: 0; top: 10%; width: 100%; height: 84%; background-color: {s2['hi']}; border-radius: 18px; transform-origin: 0% 50%; }}
      #s2 .mk .tx {{ position: relative; display: inline-block; color: {s2['fg']}; }}
      #s2 .sub {{ left: 64px; top: 1310px; width: 900px; color: {s2['sub']}; font-size: 50px; font-weight: 600; line-height: 1.3; }}
      #s2 .bt {{ left: 560px; top: 1440px; width: 440px; height: 330px; }}
      #s2 .bt path {{ fill: none; stroke: {OR if s2['dark'] else NB}; stroke-width: 9; stroke-linecap: round; stroke-linejoin: round; }}

      /* S3 — O Level */
      #s3 .blob {{ left: 500px; top: -320px; width: 900px; height: 900px; }}
      #s3 .g3b {{ left: -300px; top: 1100px; width: 900px; height: 900px; }}
      #s3 .lab {{ left: 56px; top: 180px; font-size: 200px; line-height: 1.02; white-space: nowrap; }}
      #s3 .k3 {{ left: 64px; top: 405px; }}
      #s3 .stack {{ left: 60px; top: 480px; width: 960px; }}
      #s3 .ol-row {{ display: flex; align-items: baseline; gap: 22px; height: 104px; border-top: 2px solid {s3['ring']}; overflow: hidden; }}
      #s3 .ol-n {{ flex: none; width: 70px; font-family: "Poppins"; font-size: 30px; font-weight: 700; color: {s3['num']}; }}
      #s3 .ol-w {{ display: block; font-size: 84px; line-height: 1.2; color: {s3['fg']}; white-space: nowrap; }}
      #s3 .ol-row:nth-child(even) .ol-w {{ color: {s3['alt']}; }}
      #s3 .scan {{ left: 40px; top: 483px; width: 1000px; height: 101px; border-radius: 14px; opacity: 0; background-image: linear-gradient(100deg, {Y} 0%, {AM} 55%, {OR} 100%); background-color: {AM}; }}

      /* S4 — A Level */
      #s4 .disc {{ left: -380px; top: -320px; width: 1000px; height: 1000px; }}
      #s4 .g4b {{ left: 420px; top: 1300px; width: 900px; height: 900px; }}
      #s4 .lab {{ left: 56px; top: 200px; font-size: 230px; line-height: 1.02; white-space: nowrap; }}
      #s4 .k4 {{ left: 64px; top: 460px; }}
      #s4 .cloud {{ left: 40px; top: 600px; width: 1000px; display: flex; flex-wrap: wrap; justify-content: center; align-content: flex-start; gap: 24px 16px; }}
      #s4 .al-tag {{ display: block; font-size: 60px; font-weight: 700; line-height: 1; padding: 30px 36px 32px; border-radius: 999px; white-space: nowrap; }}
      #s4 .k1 {{ background-color: {NB if not s4['dark'] else Y}; color: {Y if not s4['dark'] else NB}; }}
      #s4 .k2 {{ background-color: {s4['glass']}; border: 2px solid {s4['glassb']}; color: {s4['fg']}; box-shadow: inset 0 1px 0 rgba(255,255,255,0.4); }}
      #s4 .k3 {{ background-color: {CR}; color: {NB}; }}
      #s4 .as {{ left: 56px; top: 1600px; font-size: 210px; line-height: 1.02; white-space: nowrap; }}

      /* S5 — method */
      #s5 .glow.g5 {{ left: 140px; top: 360px; width: 1200px; height: 1200px; }}
      #s5 .hd {{ left: 60px; top: 190px; width: 980px; color: {s5['fg']}; font-size: 74px; line-height: 1.08; }}
      #s5 .hd .em {{ color: {Y if s5['dark'] else RUST}; }}
      #s5 .paper {{ left: 110px; top: 470px; width: 860px; height: 980px; background-image: linear-gradient(170deg, #FFFDF6 0%, #FFF6E2 100%); background-color: #FFFAEE; border-radius: 14px; box-shadow: 0 40px 90px rgba(0,0,0,0.45); padding: 54px 60px; overflow: hidden; }}
      #s5 .pmeta {{ font-size: 24px; font-weight: 600; color: #8A7A55; letter-spacing: 2px; text-transform: uppercase; }}
      #s5 .pq {{ margin-top: 14px; font-size: 34px; font-weight: 700; color: {ESP}; line-height: 1.25; }}
      #s5 .pq b {{ color: #D9361C; }}
      #s5 .rule {{ margin-top: 26px; height: 3px; background-color: #E2DDD0; }}
      #s5 .ln {{ position: relative; height: 66px; display: flex; align-items: center; border-bottom: 2px solid #EFEAE0; }}
      #s5 .ln i {{ display: block; height: 16px; border-radius: 8px; background-color: #B9B2A2; }}
      #s5 .tick {{ position: absolute; right: 120px; top: 8px; width: 60px; height: 44px; }}
      #s5 svg path {{ fill: none; stroke: #D9361C; stroke-width: 7; stroke-linecap: round; stroke-linejoin: round; }}
      #s5 .note {{ position: absolute; right: -6px; top: 14px; font-size: 26px; font-weight: 700; color: #D9361C; border: 3px solid #D9361C; border-radius: 10px; padding: 2px 10px; }}
      #s5 .score {{ right: 50px; bottom: 50px; width: 190px; height: 190px; border-radius: 50%; border: 8px solid #D9361C; color: #D9361C; display: flex; align-items: center; justify-content: center; font-size: 78px; font-weight: 800; letter-spacing: -2px; }}
      #s5 .pnote {{ left: 60px; bottom: 90px; font-size: 30px; font-weight: 700; color: #D9361C; }}
      #s5 .photo {{ left: 60px; top: 560px; width: 960px; height: 720px; border-radius: 30px; overflow: hidden; background-color: {DB}; box-shadow: 0 0 0 3px rgba(252,224,4,0.55), 0 40px 100px rgba(254,97,0,0.35); }}
      #s5 .photo img {{ position: absolute; left: -180px; top: 0; width: 1320px; height: 722px; object-fit: cover; }}
      #s5 .shade {{ left: 0; bottom: 0; width: 960px; height: 300px; background-image: linear-gradient(180deg, rgba(20,12,4,0) 0%, rgba(20,12,4,0.75) 100%); }}
      #s5 .cap {{ left: 34px; bottom: 30px; color: {CR}; font-size: 38px; font-weight: 700; }}
      #s5 .cap b {{ color: {Y}; }}
      #s5 .sub {{ left: 60px; top: 1500px; width: 980px; color: {Y if s5['dark'] else NB}; font-size: 84px; line-height: 1.08; }}

      /* S6 — proof */
      #s6 .blob {{ left: 520px; top: 1180px; width: 1000px; height: 1000px; }}
      #s6 .g6b {{ left: -400px; top: -300px; width: 900px; height: 900px; }}
      #s6 .row {{ left: 60px; width: 960px; height: 290px; border-radius: 34px; padding: 26px 40px; background-color: {s6['glass']}; border-color: {s6['glassb']}; }}
      #s6 .num {{ display: block; font-size: 180px; line-height: 1.0; white-space: nowrap; }}
      #s6 .lbl {{ display: block; color: {s6['fg']}; font-size: 40px; font-weight: 600; line-height: 1.15; margin-top: 8px; }}
      #s6 .r1 {{ top: 210px; }}
      #s6 .r2 {{ top: 540px; }}
      #s6 .r3 {{ top: 870px; }}
      #s6 .stars {{ position: absolute; left: 420px; top: 70px; display: flex; gap: 12px; }}
      #s6 .stars svg {{ width: 78px; height: 78px; }}
      #s6 .stars path {{ fill: {OR if not s6['dark'] else Y}; }}
      #s6 .teach {{ left: 60px; top: 1250px; width: 960px; color: {s6['fg']}; }}
      #s6 .tl {{ font-size: 64px; line-height: 1.1; }}
      #s6 .pills {{ margin-top: 30px; display: flex; gap: 22px; }}
      #s6 .pill {{ display: block; background-color: {NB if not s6['dark'] else Y}; color: {Y if not s6['dark'] else NB}; font-size: 92px; font-weight: 800; letter-spacing: -2px; padding: 18px 40px 24px; border-radius: 30px; }}

      /* S7 — close */
      #s7 .c1 {{ left: 200px; top: 1150px; width: 1300px; height: 1300px; }}
      #s7 .c2 {{ left: 640px; top: -260px; width: 640px; height: 640px; border-width: 28px; }}
      #s7 .g7b {{ left: -300px; top: -200px; width: 900px; height: 900px; }}
      #s7 .hl {{ left: 56px; top: 220px; line-height: 1.04; white-space: nowrap; }}
      #s7 .a {{ font-size: 170px; }}
      #s7 .a2 {{ font-size: 200px; }}
      #s7 .b {{ font-size: 130px; }}
      #s7 .logo {{ left: 60px; top: 860px; width: 640px; height: auto; display: block; }}
      #s7 .adm {{ left: 64px; top: 1060px; color: {Y if s7['dark'] else NB}; font-size: 60px; font-weight: 800; letter-spacing: -1px; line-height: 1.1; }}
      #s7 .mode {{ left: 64px; top: 1150px; width: 960px; color: {s7['fg']}; font-size: 44px; font-weight: 600; line-height: 1.25; }}
      #s7 .url {{ left: 60px; top: 1280px; color: {NB}; font-size: 104px; font-weight: 800; letter-spacing: -3px; padding: 18px 54px 26px; border-radius: 999px; white-space: nowrap;
        background-image: linear-gradient(100deg, {Y} 0%, {AM} 50%, {OR} 100%); background-color: {AM}; box-shadow: 0 30px 80px rgba(254,97,0,0.45); }}
      #s7 .demo {{ left: 64px; top: 1490px; color: {s7['fg']}; font-size: 50px; font-weight: 700; line-height: 1.2; }}
      #s7 .demo b {{ color: {Y if s7['dark'] else RUST}; }}

      #grain {{ position: absolute; left: -60px; top: -60px; width: 1200px; height: 2040px; z-index: 100; pointer-events: none; opacity: 0.12; mix-blend-mode: overlay;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E"); }}
      #vignette {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 99; pointer-events: none; background-image: radial-gradient(130% 90% at 50% 45%, rgba(13,8,3,0) 60%, rgba(13,8,3,0.35) 100%); }}
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
          {glows(0, (420, -300, 1100), (-400, 1000, 1000)).replace('class="glow g1"', 'class="glow g1 sun"')}
          <div class="ring"></div>
          <div class="abs yr H gtx">2027</div>
          <img class="abs logo" src="{s1['logo']}" alt="SJ Academy" />
          <div class="abs kicker k1">O &amp; A Level coaching · Karachi</div>
          <div class="abs big H">
            <div class="ln1">{chars("O Level")}</div>
            <div class="ln2">{chars("& ")}{chars("A Level", "gtx")}</div>
          </div>
          <div class="abs bar"><span>May/June 2027</span></div>
          <div class="abs band glass"><div class="mq">Maths · Physics · Chemistry · Biology · Accounting · Business · Economics · Computer Science · English · Urdu · </div></div>
        </div>
      </div>

      <!-- S2 · 2–4.5s · hook -->
      <div id="s2" class="scene">
        <div class="cam">
          {glows(1, (300, 900, 1100), (-200, -200, 800)).replace('class="glow g1"', 'class="glow g1 ghost"').replace('class="glow g2"', 'class="glow g2 gt1"')}
          <div class="ring"></div>
          <div class="abs kicker k2">The SJ Academy method</div>
          <div class="abs hl H">
            <div class="mask l1"><span class="w">Learn</span> <span class="w">to</span></div>
            <div class="mask l2"><span class="w">think</span> <span class="w">like</span> <span class="w">a</span></div>
            <div class="mask l3"><span class="w mk mk1"><i class="hi"></i><span class="tx">CAIE</span></span></div>
            <div class="mask l4"><span class="w mk mk2"><i class="hi"></i><span class="tx em">examiner.</span></span></div>
          </div>
          <div class="abs sub">See the paper the way the person marking it does.</div>
          <svg class="abs bt" viewBox="0 0 60 44"><path d="M5 24 L21 38 L55 6" /></svg>
        </div>
      </div>

      <!-- S3 · 4.5–7s · O Level -->
      <div id="s3" class="scene">
        <div class="cam">
          {glows(2, (500, -320, 900), (-300, 1100, 900)).replace('class="glow g1"', 'class="glow g1 blob"').replace('class="glow g2"', 'class="glow g2 g3b"')}
          <div class="abs lab H gtx">O Level</div>
          <div class="abs kicker k3">May/June 2027 · CAIE</div>
          <div class="abs scan"></div>
          <div class="abs stack H">
{o_lines}
          </div>
        </div>
      </div>

      <!-- S4 · 7–9.5s · A Level -->
      <div id="s4" class="scene">
        <div class="cam">
          {glows(3, (-380, -320, 1000), (420, 1300, 900)).replace('class="glow g1"', 'class="glow g1 disc"').replace('class="glow g2"', 'class="glow g2 g4b"')}
          <div class="abs lab H">A Level</div>
          <div class="abs kicker k4">AS and A2 · May/June 2027</div>
          <div class="abs cloud">
{a_tags}
          </div>
          <div class="abs as H"><span class="em">AS &amp; A2.</span></div>
        </div>
      </div>

      <!-- S5 · 9.5–12.5s · method -->
      <div id="s5" class="scene">
        <div class="cam">
          {glows(4, (140, 360, 1200), (-400, 1300, 900)).replace('class="glow g1"', 'class="glow g1 g5"')}
          <div class="abs hd H"><span class="w">Past</span> <span class="w">papers</span> <span class="w">marked</span> <span class="w">to</span> <span class="w">the</span> <span class="w em">Cambridge</span> <span class="w em">scheme.</span></div>
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
          <div class="abs photo"><img src="assets/brand/classroom.jpg" alt="A class at SJ Academy" /><div class="abs shade"></div><div class="abs cap">A class at <b>DHA Phase 7</b></div></div>
          <div class="abs sub H"><span class="w">See</span> <span class="w">exactly</span> <span class="w">where</span> <span class="w">marks</span> <span class="w">were</span> <span class="w em">lost.</span></div>
        </div>
      </div>

      <!-- S6 · 12.5–15.5s · proof -->
      <div id="s6" class="scene">
        <div class="cam">
          {glows(5, (520, 1180, 1000), (-400, -300, 900)).replace('class="glow g1"', 'class="glow g1 blob"').replace('class="glow g2"', 'class="glow g2 g6b"')}
          <div class="abs row glass r1"><span class="num H gtx" id="n1">0+</span><span class="lbl">A*s achieved at SJ Academy</span></div>
          <div class="abs row glass r2"><span class="num H gtx" id="n2">0+</span><span class="lbl">students taught</span></div>
          <div class="abs row glass r3"><span class="num H gtx" id="n3">0.0</span><span class="lbl">Google rating from 226 reviews</span>
            <div class="stars">{STAR * 5}</div>
          </div>
          <div class="abs teach"><div class="tl H">Teachers from</div><div class="pills"><span class="pill">LUMS</span><span class="pill">IBA</span><span class="pill">KGS</span></div></div>
        </div>
      </div>

      <!-- S7 · 15.5–18s · close -->
      <div id="s7" class="scene">
        <div class="cam">
          {glows(6, (200, 1150, 1300), (-300, -200, 900)).replace('class="glow g1"', 'class="glow g1 c1"').replace('class="glow g2"', 'class="glow g2 g7b"')}
          <div class="ring c2"></div>
          <div class="abs hl H">
            <div class="mask a"><span class="w">One</span> <span class="w">class</span></div>
            <div class="mask a2"><span class="w em gtx">free.</span></div>
            <div class="mask b"><span class="w">Then</span> <span class="w">decide.</span></div>
          </div>
          <img class="abs logo" src="{s7['logo'].replace('.svg', '-end.svg') if s7['dark'] else s7['logo']}" alt="SJ Academy" />
          <div class="abs adm">May/June 2027 admissions open</div>
          <div class="abs mode">In class in DHA Phase 7 or live online</div>
          <div class="abs url">sjacademy.pk</div>
          <div class="abs demo">Book a <b>free demo</b> class.</div>
        </div>
      </div>

      <div id="vignette"></div>
      <div id="grain"></div>
    </div>

    <script>
      window.THEME = {{ s2fg: "{s2['fg']}", s2hitx: "{s2['hitx']}", s3fg: "{s3['fg']}", s3alt: "{s3['alt']}", scanText: "{NB}" }};
{open("build/timeline2.js").read()}    </script>
  </body>
</html>
'''
open("index.html", "w").write(html)
print("ok", LOOK)
