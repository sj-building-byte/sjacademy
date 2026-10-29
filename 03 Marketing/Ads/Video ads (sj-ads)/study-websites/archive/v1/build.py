"""Builds ../index.html: "7 websites, 7 exam problems, 60 seconds" (9:16 speedrun reel), plus build/sfx.json for the mix.
Timing comes from build/vo/timing.json (python3 build/vo/assemble.py).   python3 build/build.py
"""
import html
import json
import re
from pathlib import Path

root = Path(__file__).parent.parent
E = html.escape
VO = json.loads((root / "build/vo/timing.json").read_text())
L = {s["key"]: (s["start"], s["end"]) for s in VO["lines"]}
TEXT = dict(l.split("|", 1) for l in (root / "build/vo/lines.txt").read_text().splitlines() if l.strip())
END_CARD = L["17"][1] + 0.4
DUR = round(END_CARD + 3.2, 2)
GO = L["01"][1]          # the timer starts on "Let's go!"
STOP = L["17"][0]        # and stops on "Time!"

# window: browser bar + content, all crops land in a 940 x 384 content area
WX, WY, WW, WH, BAR = 70, 712, 940, 430, 46
CH = WH - BAR

VIEWS = {  # name: (file, crop x, crop y, crop width) in source pixels
    "desmos": ("desmos-solved.jpg", 700, 170, 640),
    "phet0": ("phet-500.jpg", 200, 200, 1110),
    "phet1": ("phet-1000.jpg", 200, 200, 1110),
    "cam": ("cambridge-command-words.jpg", 290, 420, 875),
    "grade": ("grade-strategy.jpg", 255, 268, 1002),
    "combo0": ("combos-step1.jpg", 405, 300, 650),
    "combo1": ("combos-result.jpg", 380, 240, 700),
    "papers": ("papers-table.jpg", 56, 413, 880),
}


def at(view, sx, sy):
    """Where a source pixel lands inside the window content."""
    f, cx, cy, cw = VIEWS[view]
    s = WW / cw
    return round((sx - cx) * s), round((sy - cy) * s)


def view_img(view, vid):
    f, cx, cy, cw = VIEWS[view]
    s = WW / cw
    src_w = {"desmos-solved.jpg": 1427, "grade-strategy.jpg": 1512}.get(f, 1456)  # capture widths
    return (f'<img class="vimg" id="{vid}" src="assets/captures/{f}" '
            f'style="width:{round(src_w * s)}px;left:{-round(cx * s)}px;top:{-round(cy * s)}px" alt="">')


TOOLS = [  # key, split name, chip, question, url, done time
    ("desmos", "Desmos", "A Level Maths · 9709 P1", 'Where does <span class="nw">y = x − 1</span> meet <span class="nw">y = x² − 4x + 3?</span>', "desmos.com/calculator", L["04"][1]),
    ("phet", "PhET", "O Level Physics", "Double the resistance. What happens to the current?", "phet.colorado.edu", L["07"][0] + 2.0),
    ("anki", "Anki", "A Level Business · Paper 1", "40 definitions before Paper 1?", "ankiweb.net", L["09"][1]),
    ("cam", "Cambridge syllabus", "Every subject", "Lost marks on “evaluate”?", "cambridgeinternational.org", L["11"][1]),
    ("grade", "Grade Comeback Calc", "SJ Academy tool", "B at AS. Want an A?", "sjacademy.pk", L["14"][1]),
    ("combo", "Subject combinations", "SJ Academy tool", "Which A Levels fit your degree?", "sjacademy.pk", L["15"][1]),
    ("papers", "Past papers", "SJ Academy", "Past papers + mark schemes", "sjacademy.pk", L["16"][1] - 0.3),
]
SEG = {  # when each tool owns the stage
    "desmos": (L["02"][0], L["06"][0]), "phet": (L["06"][0], L["08"][0]), "anki": (L["08"][0], L["10"][0]),
    "cam": (L["10"][0], L["12"][0]), "grade": (L["13"][0], L["15"][0]), "combo": (L["15"][0], L["16"][0]),
    "papers": (L["16"][0], L["17"][0]),
}

# ---------------------------------------------------------------- captions: 2 to 4 word chunks, timed by characters
KEY = re.compile(r"^(Desmos|Anki|evaluate\??|judge\.?|halves!?|free|Free|Done\.|go!|Go!|Sixty|Seven|Forty|B|A\?|AS,|May\?|October,|SJ|Academy\.|Time!|thirty-seven|mark|schemes\.|No|sign-up|four|Four)$")
caps = []
for k, (a, b) in L.items():
    if k in ("01", "12", "17"):  # the hook, bonus and end already show these words big
        continue
    words = TEXT[k].replace("S J", "SJ").replace("A S", "AS").split()
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) >= 4 or w[-1] in ".?!," and len(cur) >= 2:
            chunks.append(cur); cur = []
    if cur:
        if chunks and len(cur) == 1:
            chunks[-1] += cur
        else:
            chunks.append(cur)
    total = sum(len(" ".join(c)) for c in chunks)
    t = a
    for c in chunks:
        d = (b - a) * len(" ".join(c)) / total
        caps.append((round(t, 2), round(t + d, 2), c))
        t += d

# ---------------------------------------------------------------- html
media, layers, track = [], [], [3]


def section(sid, start, dur, inner, z=20):
    track[0] += 1
    layers.append(f'<section id="{sid}" class="clip layer" style="z-index:{z}" data-start="{start:.2f}" data-duration="{dur:.2f}" data-track-index="{track[0]}">{inner}</section>')


def window(tid, url, inner):
    return (f'<div class="win" id="win-{tid}" style="left:{WX}px;top:{WY}px;width:{WW}px;height:{WH}px">'
            f'<div class="bar"><i></i><i></i><i></i><span class="url">{E(url)}</span></div>'
            f'<div class="content" style="height:{CH}px">{inner}</div></div>')


def head(tid, chip, q):
    return (f'<div class="qh" id="qh-{tid}"><span class="chip">{E(chip)}</span>'
            f'<div class="qt">{q}</div></div>')


# HUD: timer, pips, splits (whole film)
pips = "".join(f'<i id="pip{i}"></i>' for i in range(7))
rows = "".join(f'<div class="srow" id="sr{i}"><span class="sn"><b>{i + 1}</b><span class="nm">???</span><span class="real">{E(t[1])}</span></span>'
               f'<span class="st" id="st{i}">–</span></div>' for i, t in enumerate(TOOLS))
section("s-hud", 0, DUR - 0.01,
        '<div id="hudlab">Speedrun · Any% · O &amp; A Level</div>'
        '<div id="timer" class="num">0:00.00</div>'
        f'<div id="pips">{pips}</div>'
        f'<div id="splits">{rows}</div>', z=30)

# hook
section("s-hook", 0, GO + 0.6,
        '<div class="hk" id="hk1">7 websites.</div><div class="hk" id="hk2">7 exam problems.</div>'
        '<div class="hk y" id="hk3">60 seconds.</div><div id="go" class="stamp big">GO!</div>', z=40)

# tools
for tid, name, chip, q, url, done in TOOLS:
    a, b = SEG[tid]
    if tid == "desmos":
        r1, r2 = at("desmos", 967, 438), at("desmos", 1121, 286)
        inner = (view_img("desmos", "img-desmos") +
                 '<img class="abs" id="d-eq" src="assets/captures/desmos-eq.png" style="left:14px;top:12px;width:380px;border-radius:10px;box-shadow:0 6px 20px rgba(0,0,0,0.18)" alt="">'
                 f'<div class="ping" id="ping1" style="left:{r1[0] - 40}px;top:{r1[1] - 40}px"></div>'
                 f'<div class="ping" id="ping2" style="left:{r2[0] - 40}px;top:{r2[1] - 40}px"></div>'
                 '<div class="tag" id="d-ans" style="right:18px;bottom:18px">(1, 0) and (4, 3)</div>')
        extra = '<div class="sticker" id="d-note" style="right:60px;top:668px">still show your working!</div>'
    elif tid == "phet":
        c = at("phet0", 527, 548)
        inner = (view_img("phet0", "img-p0") + view_img("phet1", "img-p1") +
                 f'<div class="ring" id="p-ring" style="left:{c[0] - 190}px;top:{c[1] - 46}px;width:380px;height:92px"></div>'
                 f'<div class="tag" id="p-half" style="left:{c[0] + 200}px;top:{c[1] - 40}px">÷ 2</div>')
        extra = '<div class="sticker" id="p-note" style="right:60px;top:668px">no lab booking needed</div>'
    elif tid == "anki":
        inner = ('<div class="flash" id="card"><div class="face front"><div class="fk">A Level Business</div><div class="fw">Opportunity cost</div><div class="fh">tap to flip</div></div>'
                 '<div class="face back"><div class="fk">Opportunity cost</div><div class="fd">The benefit of the next best alternative given up.</div>'
                 '<div class="btns"><span>Again</span><span>Hard</span><span class="on">Good</span><span>Easy</span></div></div></div>')
        extra = '<div class="sticker" id="a-note" style="right:60px;top:668px">it brings it back just in time</div>'
    elif tid == "cam":
        ry = at("cam", 0, 557)[1]
        inner = (view_img("cam", "img-cam") +
                 f'<div class="rowhl" id="c-hl" style="top:{ry - 26}px"></div>')
        inner += '<div class="src" id="c-src">Cambridge AS &amp; A Level Economics 9708 syllabus, 2026 to 2028, p37</div>'
        extra = '<div class="stamp" id="c-judge" style="left:650px;top:676px">JUDGE.</div>'
    elif tid == "grade":
        cards = [at("grade", x, 365) + (at("grade", x + 320, 683)) for x in (256, 596, 936)]
        inner = view_img("grade", "img-grade") + "".join(
            f'<div class="cardhl" id="g-c{i}" style="left:{c[0] - 4}px;top:{c[1] - 4}px;width:{c[2] - c[0] + 8}px;height:{c[3] - c[1] + 8}px"></div>'
            for i, c in enumerate(cards))
        m = at("grade", 483, 468)
        inner += f'<div class="ping" id="g-ping" style="left:{m[0] - 40}px;top:{m[1] - 40}px"></div>'
        extra = '<div class="sticker" id="g-note" style="right:60px;top:668px">104/125 in A2. Doable.</div>'
    elif tid == "combo":
        inner = (view_img("combo0", "img-c0") + view_img("combo1", "img-c1") +
                 '<div class="steps" id="c-steps"><i></i><i></i><i></i><i></i></div>')
        extra = '<div class="sticker" id="co-note" style="right:60px;top:668px">Medicine? Bio + Chem.</div>'
    else:
        inner = view_img("papers", "img-pp")
        extra = '<div class="stamp" id="pp-free" style="left:400px;top:676px;font-size:58px">FREE · NO SIGN-UP</div>'
    section(f"s-{tid}", a, b - a, head(tid, chip, q) + window(tid, url, inner) + extra, z=20)

# bonus level and the end
section("s-bonus", L["12"][0] - 0.1, L["13"][0] - L["12"][0] + 0.1,
        '<div class="bonusbg" id="bn-bg"></div><div class="abs" id="bn" style="left:0;right:0;top:600px;text-align:center">'
        '<div class="bn1" id="bn1">BONUS LEVEL</div><div class="bn2" id="bn2">3 we built at</div>'
        '<img id="bn-logo" src="assets/brand/sj-academy-logo-horizontal-on-yellow.svg" style="width:560px;margin-top:26px" alt="SJ Academy"></div>', z=45)
tabs = "".join('<i></i>' for _ in range(37))
section("s-end", STOP, DUR - STOP,
        '<div class="abs" id="tm" style="left:0;right:0;top:560px;text-align:center"><div class="tm1" id="tm1">TIME!</div>'
        '<div class="tm2" id="tm2">Under 60. GG.</div></div>'
        f'<div class="tabs" id="tabs">{tabs}</div>'
        '<div class="abs" id="sendt" style="left:70px;right:70px;top:930px;text-align:center"><div class="send">Send this to the friend with <span class="y">37 tabs</span> open.</div></div>', z=40)
section("s-card", END_CARD, DUR - END_CARD,
        '<div class="endbg"></div><div class="abs" style="left:0;right:0;top:560px;text-align:center">'
        '<img id="e-logo" src="assets/brand/sj-academy-logo-horizontal-on-yellow.svg" style="width:640px" alt="SJ Academy">'
        '<div class="e1" id="e1">More free tools at</div><div class="e2" id="e2">sjacademy.pk</div>'
        '<div class="e3" id="e3">Save this for exam season.</div></div>', z=60)

# captions
cap_html = "".join(
    f'<div class="cap" id="cp{i}" data-a="{a}" data-b="{b}">' + " ".join(
        f'<span class="cw{" k" if KEY.match(w) else ""}">{E(w)}</span>' for w in ws) + "</div>"
    for i, (a, b, ws) in enumerate(caps))
section("s-caps", 0, STOP + 4.0, cap_html, z=50)

# ---------------------------------------------------------------- sound effects (mixed after render)
sfx = []
def fx(t, name, gain=1.0):
    sfx.append({"t": round(t, 3), "f": name, "g": gain})
for f in (0.0, 0.3, 0.62):
    fx(L["01"][0] + f * (L["01"][1] - L["01"][0]), "fx-impact.wav", 0.45)
fx(GO - 0.05, "sj-sfx-stamp.wav", 0.9)
fx(GO, "fx-riser.wav", 0.25)
for tid, *_ , done in TOOLS:
    a, _b = SEG[tid]
    fx(a, "fx-whoosh.wav", 0.6)
    fx(done, "fx-chime.wav", 0.6)
for i in range(10):
    fx(L["03"][0] + 0.1 + i * 0.09, "fx-key.wav", 0.5)
fx(L["04"][0] + 0.05, "fx-pop.wav", 0.6); fx(L["04"][0] + 0.75, "fx-pop.wav", 0.6)
fx(L["07"][0] + 0.9, "sj-sfx-paper-slide.wav", 0.5)
fx(L["09"][0] + 0.4, "sj-sfx-paper-slide.wav", 0.6)
fx(L["11"][0] + 2.6, "sj-sfx-highlighter-swipe.wav", 0.8)
fx(L["11"][1] - 0.55, "sj-sfx-stamp.wav", 0.9)
fx(L["12"][0] - 0.1, "fx-twinkle.wav", 0.7)
fx(L["16"][0] + 1.6, "sj-sfx-stamp.wav", 0.8)
fx(STOP, "fx-impact.wav", 0.7)
fx(END_CARD + 0.2, "sj-sonic-logo-short.wav", 0.8)
(root / "build/sfx.json").write_text(json.dumps({"dur": DUR, "go": GO, "stop": STOP, "fx": sfx}, indent=1))

CSS = (root / "build/style.css").read_text()
JS = (root / "build/timeline.js").read_text()
cfg = {"DUR": DUR, "GO": GO, "STOP": STOP, "END_CARD": END_CARD, "L": L,
       "SEG": SEG, "DONE": [t[5] for t in TOOLS], "TOOLS": [t[0] for t in TOOLS], "NCAP": len(caps)}
page = f"""<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>7 websites speedrun</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>{CSS}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
      <audio id="mix" src="assets/audio/mix.wav" data-start="0" data-duration="{DUR}" data-track-index="1" data-volume="1"></audio>
      {"".join(media)}
      {"".join(layers)}
    </div>
    <script>
      const CFG = {json.dumps(cfg)};
{JS}
    </script>
  </body>
</html>
"""
(root / "index.html").write_text(page)
print(f"built: {DUR}s, go {GO:.2f}, stop {STOP:.2f} (run {STOP - GO:.2f}s), {len(caps)} captions, {len(sfx)} sfx")
