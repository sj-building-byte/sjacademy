#!/usr/bin/env python3
"""Builds index.html and compositions/ for the 14 area and volume formulas reel.
Edit the SHAPES table or the copy below, then run: python3 build.py"""
import html
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).parent
COMP = ROOT / "compositions"
COMP.mkdir(exist_ok=True)
METRICS = json.loads((ROOT / "assets/brand/poppins-metrics.json").read_text())

BEAT = 60 / 112  # "Fresh" is 112 BPM
MEDIA_START = 8.616  # music starts on its beat 16, so the bass lift lands on the cuboid (beat 48)
SCENE_BEATS = 6
FPS = 30
N_SCENES = 14
V_RECAP = 84
V_END = 94  # since 11 November 2026 the recap cuts straight to the end card (no phone scene)
V_PITCH = V_END
V_STOP = 108
GAIN_INTRO, GAIN_MID, GAIN_HIGH = 1.1, 0.84, 0.66

INK, CANVAS, BODY, YELLOW, ORANGE, BROWN, PEN = (
    "#151515", "#F7F5EF", "#D9D4C7", "#FCE004", "#FE6100", "#453516", "#D63A2F",
)


def beat(n):
    return round(n * BEAT, 4)


def land(b):
    """First visible frame of a move: one frame ahead of the beat."""
    return round(b * BEAT - 1 / FPS, 4)


FONT = """
@font-face{font-family:'Poppins';font-weight:400;src:url('assets/brand/Poppins-Regular.ttf')}
@font-face{font-family:'Poppins';font-weight:500;src:url('assets/brand/Poppins-Medium.ttf')}
@font-face{font-family:'Poppins';font-weight:600;src:url('assets/brand/Poppins-SemiBold.ttf')}
@font-face{font-family:'Poppins';font-weight:700;src:url('assets/brand/Poppins-Bold.ttf')}
@font-face{font-family:'Caveat';font-weight:600;src:url('assets/brand/Caveat-600.woff2')}
"""

MATH_CSS = """
.m{display:inline-flex;align-items:center;white-space:pre;font-family:'Poppins';font-weight:500;color:#F7F5EF}
.m i{font-style:italic}
.fr{display:inline-flex;flex-direction:column;align-items:center;font-size:.72em;margin:0 .14em;line-height:1.08}
.fr b{display:block;width:100%;height:.07em;min-height:3px;background:#F7F5EF;margin:.05em 0}
.fr span{font-weight:500;padding:0 .12em;display:inline-flex;align-items:center}
.th{display:inline-block;width:.6em;height:.76em;vertical-align:-.04em}
.ll{display:inline-block;width:.34em;height:.76em;vertical-align:-.04em;margin:0 .03em}
.m i{padding-right:.03em}
"""

LL = (
    '<svg class="ll" viewBox="0 0 34 76"><path transform="skewX(-9) translate(12 0)" d="M12 3V58Q12 72 27 71" '
    'fill="none" stroke="currentColor" stroke-width="8.5" stroke-linecap="round"/></svg>'
)

TH = (
    '<svg class="th" viewBox="0 0 60 76"><g transform="skewX(-9) translate(11 0)" fill="none" '
    'stroke="currentColor" stroke-width="8.5"><ellipse cx="29" cy="38" rx="19" ry="33"/>'
    '<line x1="10" y1="38" x2="48" y2="38"/></g></svg>'
)


# ---------- formula typesetting ----------
def t(s):
    return ("t", s)


def v(s):
    return ("v", s)


TH_TOKEN = ("th",)


def fr(n, d):
    return ("f", n, d)


def to_html(tokens):
    out = ""
    for k in tokens:
        if k[0] == "t":
            out += html.escape(k[1])
        elif k[0] == "v":
            out += LL if k[1] == "l" else f"<i>{html.escape(k[1])}</i>"
        elif k[0] == "th":
            out += TH
        else:
            out += f'<span class="fr"><span>{to_html(k[1])}</span><b></b><span>{to_html(k[2])}</span></span>'
    return out


def text_w(s, size, weight="500"):
    table = METRICS[weight]
    return sum(table.get(c, 600) for c in s) / 1000 * size


def tokens_w(tokens, size):
    w = 0.0
    for k in tokens:
        if k[0] == "v" and k[1] == "l":
            w += 0.4 * size
        elif k[0] in ("t", "v"):
            w += text_w(k[1], size) + 0.03 * size
        elif k[0] == "th":
            w += 0.6 * size
        else:
            w += max(tokens_w(k[1], size * 0.72), tokens_w(k[2], size * 0.72)) + size * (0.28 + 0.17)
    return w


def has_frac(tokens):
    return any(k[0] == "f" for k in tokens)


# ---------- geometry (shapes live in a 500 x 500 box) ----------
def ell(cx, cy, rx, ry, a0, a1, n=84):
    return [
        (cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
         cy - ry * math.sin(math.radians(a0 + (a1 - a0) * i / n)))
        for i in range(n + 1)
    ]


def chev(x, y, deg, count=1, size=13):
    """Parallel-side arrowheads on an edge, pointing along deg."""
    out = []
    ux, uy = math.cos(math.radians(deg)), -math.sin(math.radians(deg))
    nx, ny = -uy, ux
    for c in range(count):
        tipx, tipy = x + ux * (c * 13), y + uy * (c * 13)
        out.append([
            (tipx - ux * size + nx * size * 0.7, tipy - uy * size + ny * size * 0.7),
            (tipx, tipy),
            (tipx - ux * size - nx * size * 0.7, tipy - uy * size - ny * size * 0.7),
        ])
    return out


def right_angle(x, y, s=20, dx=1, dy=-1):
    return [[(x, y + dy * s), (x + dx * s, y + dy * s), (x + dx * s, y)]]


O = (250, 420)
SR = 340
S1 = (O[0] + SR * math.cos(math.radians(58)), O[1] - SR * math.sin(math.radians(58)))
S2 = (O[0] + SR * math.cos(math.radians(122)), O[1] - SR * math.sin(math.radians(122)))
ARC = ell(O[0], O[1], SR, SR, 122, 58)
ANGLE = ell(O[0], O[1], 46, 46, 122, 58, 24)

# cone tangent points
_H, _rx, _ry = 320.0, 170.0, 48.0
_ty = _ry * _ry / _H
_tx = _rx * math.sqrt(1 - (_ry / _H) ** 2)
CONE_R = (250 + _tx, 390 - _ty)
CONE_L = (250 - _tx, 390 - _ty)
CONE_A = math.degrees(math.asin(_ty / _ry))

SHAPES = [
    dict(id="rectangle", name="Rectangle", label="Area of a rectangle",
         f=[v("A"), t(" = "), v("l"), t(" × "), v("w")],
         defs=["{l} = length, {w} = width"],
         draw=[[(60, 370), (440, 370), (440, 130), (60, 130), (60, 370)]],
         fill=[(60, 370), (440, 370), (440, 130), (60, 130)],
         labels=[("l", 250, 420), ("w", 478, 266)]),
    dict(id="triangle", name="Triangle", label="Area of a triangle",
         f=[v("A"), t(" = "), fr([t("1")], [t("2")]), v("b"), v("h")],
         defs=["{b} = base, {h} = perpendicular height"],
         draw=[[(60, 390), (440, 390), (190, 90), (60, 390)]],
         dash=[[(190, 90), (190, 390)]],
         mark=right_angle(190, 390),
         fill=[(60, 390), (440, 390), (190, 90)],
         labels=[("b", 250, 440), ("h", 168, 255)]),
    dict(id="parallelogram", name="Parallelogram", label="Area of a parallelogram",
         f=[v("A"), t(" = "), v("b"), v("h")],
         defs=["{b} = base, {h} = perpendicular height"],
         draw=[[(40, 360), (350, 360), (460, 130), (150, 130), (40, 360)]],
         dash=[[(150, 130), (150, 360)]],
         mark=right_angle(150, 360) + chev(255, 360, 0) + chev(350, 130, 0)
         + chev(405, 245, 64.4, 2) + chev(95, 245, 64.4, 2),
         fill=[(40, 360), (350, 360), (460, 130), (150, 130)],
         labels=[("b", 195, 410), ("h", 172, 262)]),
    dict(id="trapezium", name="Trapezium", label="Area of a trapezium",
         f=[v("A"), t(" = "), fr([t("1")], [t("2")]), t("("), v("a"), t(" + "), v("b"), t(")"), v("h")],
         defs=["{a} and {b} = the parallel sides", "{h} = perpendicular height"],
         draw=[[(40, 370), (460, 370), (350, 130), (150, 130), (40, 370)]],
         dash=[[(250, 130), (250, 370)]],
         mark=right_angle(250, 370) + chev(350, 370, 0) + chev(305, 130, 0),
         fill=[(40, 370), (460, 370), (350, 130), (150, 130)],
         labels=[("a", 250, 104), ("b", 250, 420), ("h", 228, 262)]),
    dict(id="circle", name="Circle", label="Area of a circle",
         f=[v("A"), t(" = π"), v("r"), t("²")],
         defs=["{r} = radius"],
         draw=[ell(250, 250, 190, 190, 180, -180)],
         thin=[[(250, 250), (440, 250)]],
         fill=ell(250, 250, 190, 190, 0, 360),
         labels=[("r", 345, 232)]),
    dict(id="circumference", name="Circumference", label="Circumference of a circle",
         f=[v("C"), t(" = π"), v("d")],
         defs=["{d} = diameter, so {C} = 2π{r} as well"],
         draw=[ell(250, 250, 190, 190, 180, -180)],
         thin=[[(60, 250), (440, 250)]],
         labels=[("d", 250, 232), ("C", 412, 96)]),
    dict(id="sector", name="Sector", label="Area of a sector",
         f=[v("A"), t(" = "), fr([TH_TOKEN], [t("360")]), t(" × π"), v("r"), t("²")],
         defs=["{θ} = angle at the centre, in degrees", "{r} = radius"],
         draw=[[O, S2] + ARC + [O]],
         thin=[ANGLE],
         fill=[O, S2] + ARC,
         labels=[("θ", 250, 352), ("r", 372, 296)]),
    dict(id="arc", name="Arc length", label="Arc length",
         f=[v("L"), t(" = "), fr([TH_TOKEN], [t("360")]), t(" × 2π"), v("r")],
         defs=["{θ} = angle at the centre, in degrees", "{r} = radius"],
         draw=[ARC],
         heavy=True,
         ghost=[[O, S2], [O, S1]],
         thin=[[O, S2], [O, S1], ANGLE],
         labels=[("L", 250, 54), ("θ", 250, 352), ("r", 372, 296)]),
    dict(id="cuboid", name="Cuboid", label="Volume of a cuboid",
         f=[v("V"), t(" = "), v("l"), t(" × "), v("w"), t(" × "), v("h")],
         defs=["{l} = length, {w} = width, {h} = height"],
         draw=[[(60, 410), (320, 410), (320, 190), (60, 190), (60, 410)],
               [(60, 190), (180, 90), (440, 90), (440, 310), (320, 410)],
               [(320, 190), (440, 90)]],
         dash=[[(180, 90), (180, 310)], [(180, 310), (60, 410)], [(180, 310), (440, 310)]],
         fill=[(60, 410), (320, 410), (440, 310), (440, 90), (180, 90), (60, 190)],
         labels=[("l", 190, 458), ("h", 26, 312), ("w", 410, 392)]),
    dict(id="prism", name="Prism", label="Volume of a prism",
         f=[v("V"), t(" = "), v("A"), t(" × "), v("l")],
         defs=["{A} = area of the cross-section", "{l} = length of the prism"],
         draw=[[(50, 410), (270, 410), (160, 210), (50, 410)],
               [(160, 210), (350, 90), (460, 290), (270, 410)]],
         dash=[[(50, 410), (240, 290)], [(240, 290), (460, 290)], [(240, 290), (350, 90)]],
         fill=[(50, 410), (270, 410), (160, 210)],
         labels=[("A", 172, 400), ("l", 392, 388)]),
    dict(id="cylinder", name="Cylinder", label="Volume of a cylinder",
         f=[v("V"), t(" = π"), v("r"), t("²"), v("h")],
         defs=["{r} = radius, {h} = height"],
         draw=[ell(250, 130, 150, 42, 0, 360), [(400, 130), (400, 390)] + ell(250, 390, 150, 42, 0, -180) + [(100, 130)]],
         dash=[ell(250, 390, 150, 42, 0, 180), [(250, 130), (400, 130)]],
         fill=ell(250, 130, 150, 42, 0, 360),
         labels=[("r", 325, 120), ("h", 434, 272)]),
    dict(id="pyramid", name="Pyramid", label="Volume of a pyramid",
         f=[v("V"), t(" = "), fr([t("1")], [t("3")]), v("A"), v("h")],
         defs=["{A} = area of the base", "{h} = perpendicular height"],
         draw=[[(50, 400), (300, 400), (450, 290), (250, 70), (50, 400)], [(250, 70), (300, 400)]],
         dash=[[(250, 70), (200, 290)], [(50, 400), (200, 290)], [(200, 290), (450, 290)], [(250, 70), (250, 345)]],
         mark=right_angle(250, 345, 18),
         fill=[(50, 400), (300, 400), (450, 290), (200, 290)],
         labels=[("h", 229, 262), ("A", 146, 378)]),
    dict(id="cone", name="Cone", label="Volume of a cone",
         f=[v("V"), t(" = "), fr([t("1")], [t("3")]), t("π"), v("r"), t("²"), v("h")],
         defs=["{r} = radius of the base", "{h} = perpendicular height"],
         draw=[[(250, 70), CONE_R] + ell(250, 390, 170, 48, CONE_A, -180 - CONE_A) + [(250, 70)]],
         dash=[ell(250, 390, 170, 48, CONE_A, 180 - CONE_A), [(250, 70), (250, 390)], [(250, 390), (420, 390)]],
         mark=right_angle(250, 390, 18),
         fill=ell(250, 390, 170, 48, 0, 360),
         labels=[("h", 229, 250), ("r", 340, 378)]),
    dict(id="sphere", name="Sphere", label="Volume of a sphere",
         f=[v("V"), t(" = "), fr([t("4")], [t("3")]), t("π"), v("r"), t("³")],
         defs=["{r} = radius"],
         draw=[ell(250, 250, 190, 190, 180, -180)],
         thin=[ell(250, 250, 190, 40, 180, 360)],
         dash=[ell(250, 250, 190, 40, 0, 180), [(250, 250), (440, 250)]],
         fill=ell(250, 250, 190, 190, 0, 360),
         labels=[("r", 345, 242)]),
]


def color(i):
    return YELLOW if i % 2 == 0 else ORANGE


def pts_d(pts, ox, oy, s, close=False):
    d = "M" + " L".join(f"{ox + x * s:.1f} {oy + y * s:.1f}" for x, y in pts)
    return d + ("Z" if close else "")


def plen(pts):
    return sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))


def label_svg(txt, x, y, ox, oy, s, fs, id_):
    px, py = ox + x * s, oy + y * s
    if txt == "θ":
        h = fs * 0.78
        k = h / 76
        return (
            f'<g id="{id_}" opacity="0"><g transform="translate({px - 25 * k:.1f} {py - h * 0.86:.1f}) scale({k:.3f}) skewX(-9)" '
            f'fill="none" stroke="{CANVAS}" stroke-width="8.5"><ellipse cx="29" cy="38" rx="19" ry="33"/>'
            f'<line x1="10" y1="38" x2="48" y2="38"/></g></g>'
        )
    if txt == "l":
        h = fs * 0.78
        k = h / 76
        return (
            f'<g id="{id_}" opacity="0"><g transform="translate({px - 18 * k:.1f} {py - h * 0.92:.1f}) scale({k:.3f}) skewX(-9)" '
            f'fill="none" stroke="{CANVAS}" stroke-width="8.5" stroke-linecap="round"><path d="M12 3V58Q12 72 27 71"/></g></g>'
        )
    italic = ' font-style="italic" paint-order="stroke" stroke="#151515" stroke-width="7" stroke-linejoin="round"'
    return (
        f'<text id="{id_}" x="{px:.1f}" y="{py:.1f}" opacity="0" text-anchor="middle" font-family="Poppins" '
        f'font-weight="500"{italic} font-size="{fs}" fill="{CANVAS}">{txt}</text>'
    )


def sample_pen(polys, ox, oy, s, dur):
    """Pen dot position every frame, at constant speed across all strokes."""
    lens = [plen(p) for p in polys]
    total = sum(lens)
    frames = max(2, round(dur * FPS))
    out = []
    for f in range(frames + 1):
        dist = total * f / frames
        for p, L in zip(polys, lens):
            if dist <= L or p is polys[-1]:
                rem = min(dist, L)
                for a, b in zip(p, p[1:]):
                    seg = math.dist(a, b)
                    if rem <= seg or (a, b) == (p[-2], p[-1]):
                        k = rem / seg if seg else 0
                        out.append((round(ox + (a[0] + (b[0] - a[0]) * k) * s, 1),
                                    round(oy + (a[1] + (b[1] - a[1]) * k) * s, 1)))
                        break
                    rem -= seg
                break
            dist -= L
    return out


def shape_parts(sh, i, ox, oy, s, sw, pre, labels=True, fs=50):
    """SVG markup plus the ids the timeline needs."""
    col = color(i)
    heavy = sh.get("heavy")
    w = sw * (1.6 if heavy else 1)
    thin_w = sw * 0.72
    fill = ghost = lines = ""
    ids = dict(draw=[], thin=[], dash=[], mark=[], labels=[])
    if sh.get("fill"):
        fill = f'<path id="{pre}fill" d="{pts_d(sh["fill"], ox, oy, s, True)}" fill="{BROWN}" opacity="0"/>'
    for p in sh["draw"] + sh.get("ghost", []) + sh.get("dash", [])[:0]:
        ghost += f'<path d="{pts_d(p, ox, oy, s)}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round"/>'
    for j, p in enumerate(sh["draw"]):
        id_ = f"{pre}d{j}"
        ids["draw"].append((id_, plen(p)))
        lines += (
            f'<path id="{id_}" d="{pts_d(p, ox, oy, s)}" pathLength="1" fill="none" stroke="{col}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0"/>'
        )
    for j, p in enumerate(sh.get("thin", [])):
        id_ = f"{pre}t{j}"
        ids["thin"].append(id_)
        lines += (
            f'<path id="{id_}" d="{pts_d(p, ox, oy, s)}" pathLength="1" fill="none" stroke="{col}" stroke-width="{thin_w}" '
            f'stroke-linecap="round" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0"/>'
        )
    for j, p in enumerate(sh.get("dash", [])):
        id_ = f"{pre}h{j}"
        ids["dash"].append(id_)
        lines += (
            f'<path id="{id_}" d="{pts_d(p, ox, oy, s)}" fill="none" stroke="{col}" stroke-width="{thin_w}" '
            f'stroke-dasharray="{max(4, 13 * s):.1f} {max(4, 10 * s):.1f}" opacity="0"/>'
        )
    for j, p in enumerate(sh.get("mark", [])):
        id_ = f"{pre}m{j}"
        ids["mark"].append(id_)
        lines += (
            f'<path id="{id_}" d="{pts_d(p, ox, oy, s)}" fill="none" stroke="{CANVAS}" stroke-width="{max(1.6, sw * 0.5):.1f}" '
            f'stroke-linecap="round" stroke-linejoin="round" opacity="0"/>'
        )
    text = ""
    if labels:
        for j, (txt, x, y) in enumerate(sh.get("labels", [])):
            id_ = f"{pre}l{j}"
            ids["labels"].append(id_)
            text += label_svg(txt, x, y, ox, oy, s, fs, id_)
    return fill, ghost, lines, text, ids


def write_scene(i, sh):
    cid = f"s{i + 1:02d}"
    ox, oy, s, sw = 265, 505, 1.1, 6
    fill, ghost, lines, text, ids = shape_parts(sh, i, ox, oy, s, sw, f"{cid}-")
    t_draw, d_draw = beat(1), beat(2)
    total = sum(L for _, L in ids["draw"])
    pen = sample_pen(sh["draw"], ox, oy, s, d_draw)
    js = ["const tl=gsap.timeline({paused:true});"]
    if i == 0:
        js.append(f"tl.set('#{cid}-ghost',{{opacity:.17}},0);")
    else:
        js.append(f"tl.fromTo('#{cid}-ghost',{{opacity:0}},{{opacity:.17,duration:.22,ease:'power1.out'}},{beat(.5)});")
    cur = t_draw
    for id_, L in ids["draw"]:
        dur = round(d_draw * L / total, 4)
        js.append(f"tl.set('#{id_}',{{opacity:1}},{cur:.4f});tl.fromTo('#{id_}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:{dur},ease:'none'}},{cur:.4f});")
        cur += dur
    dt = round(d_draw / (len(pen) - 1), 5)
    js.append(f"const P={json.dumps(pen, separators=(',', ':'))};")
    js.append(f"tl.set('#{cid}-pen',{{x:P[0][0],y:P[0][1]}},0);tl.fromTo('#{cid}-pen',{{opacity:0}},{{opacity:1,duration:.1}},{t_draw - .1:.4f});")
    js.append(f"P.slice(1).forEach((p,k)=>tl.to('#{cid}-pen',{{x:p[0],y:p[1],duration:{dt},ease:'none'}},{t_draw}+k*{dt}));")
    js.append(f"tl.to('#{cid}-pen',{{opacity:0,duration:.14}},{t_draw + d_draw:.4f});")
    t3 = beat(3)
    for id_ in ids["thin"]:
        js.append(f"tl.set('#{id_}',{{opacity:1}},{t3});tl.fromTo('#{id_}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.3,ease:'sine.inOut'}},{t3});")
    for id_ in ids["dash"] + ids["mark"]:
        js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:1,duration:.24,ease:'power1.out'}},{t3});")
    for j, id_ in enumerate(ids["labels"]):
        at = beat(3.5 + j * .5)
        js.append(f"tl.fromTo('#{id_}',{{opacity:0,y:10}},{{opacity:1,y:0,duration:.27,ease:'expo.out'}},{at});")
    if sh.get("fill"):
        js.append(f"tl.fromTo('#{cid}-fill',{{opacity:0}},{{opacity:1,duration:.2,ease:'power1.out'}},{beat(4.5)});")
    js.append(f"tl.to('#{cid}-all',{{opacity:0,duration:.22,ease:'power2.in'}},{beat(SCENE_BEATS) - .25:.4f});")
    js.append(f"window.__timelines['{cid}']=tl;")
    (COMP / f"{cid}.html").write_text(
        f"""<template>
<style>{FONT}#root{{position:absolute;inset:0}}</style>
<div id="root" data-composition-id="{cid}" data-width="1080" data-height="1920">
<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0" data-layout-allow-overlap data-layout-allow-overflow>
<g id="{cid}-all">{fill}<g id="{cid}-ghost" opacity="0">{ghost}</g>{lines}{text}<circle id="{cid}-pen" r="10" cx="0" cy="0" fill="{CANVAS}" opacity="0"/></g>
</svg>
</div>
<script>{''.join(js)}</script>
</template>
""")


def write_title():
    js = f"""const tl=gsap.timeline({{paused:true}});
tl.fromTo('#title-band',{{clipPath:'inset(0 100% 0 0)'}},{{clipPath:'inset(0 0% 0 0)',duration:.3,ease:'sine.inOut'}},.2);
tl.to('#title-box',{{opacity:0,duration:.3,ease:'power2.in'}},{beat(V_RECAP) - .32:.4f});
window.__timelines['title']=tl;"""
    (COMP / "title.html").write_text(
        f"""<template>
<style>{FONT}#root{{position:absolute;inset:0}}
#title-box{{position:absolute;left:60px;width:960px;top:356px;text-align:center;font:700 56px/68px 'Poppins';letter-spacing:-.02em;color:{CANVAS}}}
.hlw{{display:inline-block;position:relative;margin-left:.08em}}
#title-band{{position:absolute;left:-.14em;right:-.14em;top:7px;height:58px;overflow:hidden;background:linear-gradient(100deg,transparent 0,{YELLOW} .14em,{YELLOW} calc(100% - .14em),transparent 100%)}}
#title-band span{{position:absolute;left:.14em;top:-7px;color:{INK};white-space:nowrap}}
</style>
<div id="root" data-composition-id="title" data-width="1080" data-height="1920">
<div id="title-box" data-layout-allow-overlap>14 area and volume formulas<br>for <span class="hlw">O Level Maths<span id="title-band" data-layout-allow-overflow data-layout-ignore><span>O Level Maths</span></span></span></div>
</div>
<script>{js}</script>
</template>
""")


def write_formula():
    cy = 1190
    boxes = []
    fhtml = dhtml = ""
    fsize = 66
    for i, sh in enumerate(SHAPES):
        fw = tokens_w(sh["f"], fsize)
        lw = text_w(sh["label"], 32, "600")
        W = max(fw, lw) + 104
        H = 208 if has_frac(sh["f"]) else 168
        boxes.append((round(W), H))
        fhtml += (
            f'<div class="fw"><div class="f" id="f{i}"><div class="lb">{sh["label"]}</div>'
            f'<div class="m" style="font-size:{fsize}px">{to_html(sh["f"])}</div></div></div>'
        )
        lines = "<br>".join(html.escape(d) for d in sh["defs"])
        lines = lines.replace("{θ}", TH).replace("{l}", LL)
        lines = re.sub(r"\{(\w)\}", r"<i>\1</i>", lines)
        dhtml += f'<div class="d" id="d{i}">{lines}</div>'
    js = ["const tl=gsap.timeline({paused:true});"]
    for i in range(N_SCENES):
        at = beat(SCENE_BEATS * i)
        W, H = boxes[i]
        attr = f"x:{540 - W / 2},y:{cy - H / 2},width:{W},height:{H}"
        if i == 0:
            js.append(f"tl.set('#f0',{{opacity:1,y:0}},0);tl.set('#d0',{{opacity:1,y:0}},0);")
        else:
            js.append(f"tl.to('#fbox',{{attr:{{{attr}}},stroke:'{color(i)}',duration:.34,ease:'power3.inOut'}},{at - .2:.4f});")
            js.append(f"tl.to('#f{i - 1}',{{opacity:0,y:-10,duration:.16,ease:'power2.in'}},{at - .17:.4f});")
            js.append(f"tl.to('#d{i - 1}',{{opacity:0,duration:.16,ease:'power2.in'}},{at - .17:.4f});")
            js.append(f"tl.fromTo('#f{i}',{{opacity:0,y:16}},{{opacity:1,y:0,duration:.3,ease:'expo.out'}},{at:.4f});")
            js.append(f"tl.fromTo('#d{i}',{{opacity:0,y:10}},{{opacity:1,y:0,duration:.3,ease:'expo.out'}},{at + .05:.4f});")
    end = beat(V_RECAP)
    js.append(f"tl.to('#fall',{{opacity:0,duration:.28,ease:'power2.in'}},{end - .3:.4f});")
    js.append("window.__timelines['formula']=tl;")
    W0, H0 = boxes[0]
    (COMP / "formula.html").write_text(
        f"""<template>
<style>{FONT}#root{{position:absolute;inset:0}}
#fall{{position:absolute;inset:0}}
.fw{{position:absolute;left:0;top:{cy - 150}px;width:1080px;height:300px;display:flex;align-items:center;justify-content:center}}
.f{{display:flex;flex-direction:column;align-items:center;gap:2px;opacity:0}}
.lb{{font:600 32px/1.3 'Poppins';color:{YELLOW}}}
.d{{position:absolute;left:90px;width:900px;top:1312px;text-align:center;font:400 34px/1.34 'Poppins';color:{BODY};opacity:0}}
.d .th,.d .ll{{color:{BODY}}}
.d i{{font-style:italic}}
{MATH_CSS}
</style>
<div id="root" data-composition-id="formula" data-width="1080" data-height="1920">
<div id="fall" data-layout-allow-overlap data-layout-allow-overflow>
<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0"><rect id="fbox" x="{540 - W0 / 2}" y="{cy - H0 / 2}" width="{W0}" height="{H0}" rx="22" fill="none" stroke="{color(0)}" stroke-width="4"/></svg>
{fhtml}{dhtml}
</div>
</div>
<script>{''.join(js)}</script>
</template>
""")


def write_brand():
    (COMP / "brand.html").write_text(
        f"""<template>
<style>#root{{position:absolute;inset:0}}#logo{{position:absolute;left:420px;top:272px;width:240px;height:auto}}</style>
<div id="root" data-composition-id="brand" data-width="1080" data-height="1920" data-no-timeline>
<img id="logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
</div>
</template>
""")


def write_recap():
    t0 = 0.12
    svg_all = ""
    text = ""
    js = ["const tl=gsap.timeline({paused:true});"]
    js.append(f"tl.fromTo('#rc-note',{{opacity:0,y:12}},{{opacity:1,y:0,duration:.4,ease:'expo.out'}},{beat(1)});")
    for i, sh in enumerate(SHAPES):
        col_i = 0 if i < 7 else 1
        row = i if i < 7 else i - 7
        cx = 40 if col_i == 0 else 524
        cy = 408 + row * 138
        s = 0.24
        pre = f"r{i}-"
        fill, ghost, lines, _, ids = shape_parts(sh, i, cx, cy, s, 3, pre, labels=False)
        svg_all += f'{fill}<g id="{pre}ghost" opacity="0">{ghost}</g>{lines}<circle id="{pre}pen" r="4.5" fill="{CANVAS}" opacity="0"/>'
        text += (
            f'<div class="rc" id="{pre}txt" style="left:{cx + 130}px;top:{cy + 4}px"><div class="rn">{sh["name"]}</div>'
            f'<div class="m" style="font-size:41px">{to_html(sh["f"])}</div></div>'
        )
        start = t0 + i * 0.035
        dur = beat(2)
        total = sum(L for _, L in ids["draw"])
        cur = start
        js.append(f"tl.fromTo('#{pre}ghost',{{opacity:0}},{{opacity:.2,duration:.14}},{start - .1:.4f});")
        for id_, L in ids["draw"]:
            d = round(dur * L / total, 4)
            js.append(f"tl.set('#{id_}',{{opacity:1}},{cur:.4f});tl.fromTo('#{id_}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:{d},ease:'none'}},{cur:.4f});")
            cur += d
        pen = sample_pen(sh["draw"], cx, cy, s, dur)
        step = round(dur / (len(pen) - 1), 5)
        js.append(f"(()=>{{const P={json.dumps(pen, separators=(',', ':'))};tl.set('#{pre}pen',{{x:P[0][0],y:P[0][1]}},0);tl.set('#{pre}pen',{{opacity:1}},{start:.4f});P.slice(1).forEach((p,k)=>tl.to('#{pre}pen',{{x:p[0],y:p[1],duration:{step},ease:'none'}},{start:.4f}+k*{step}));tl.set('#{pre}pen',{{opacity:0}},{start + dur:.4f});}})();")
        for id_ in ids["thin"]:
            js.append(f"tl.set('#{id_}',{{opacity:1}},{start + dur:.4f});tl.fromTo('#{id_}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.2,ease:'none'}},{start + dur:.4f});")
        for id_ in ids["dash"] + ids["mark"]:
            js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:1,duration:.2}},{start + dur:.4f});")
        if sh.get("fill"):
            js.append(f"tl.fromTo('#{pre}fill',{{opacity:0}},{{opacity:1,duration:.2}},{beat(4):.4f});")
        js.append(f"tl.fromTo('#{pre}txt',{{opacity:0,x:-10}},{{opacity:1,x:0,duration:.34,ease:'expo.out'}},{start + .1:.4f});")
    js.append("window.__timelines['recap']=tl;")
    (COMP / "recap.html").write_text(
        f"""<template>
<style>{FONT}{MATH_CSS}#root{{position:absolute;inset:0}}
#rc-note{{position:absolute;left:0;width:1080px;top:338px;text-align:center;font:600 60px/1 'Caveat';color:{YELLOW};opacity:0}}
.rc{{position:absolute;display:flex;flex-direction:column;align-items:flex-start;width:350px;height:112px;justify-content:center;opacity:0}}
.rn{{font:600 28px/1.15 'Poppins';color:{YELLOW}}}
</style>
<div id="root" data-composition-id="recap" data-width="1080" data-height="1920" data-layout-allow-overlap>
<div id="rc-note" data-hold>screenshot this one</div>
<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0" data-layout-ignore>{svg_all}</svg>
{text}
</div>
<script>{''.join(js)}</script>
</template>
""")


NEON_Y, NEON_O = YELLOW, ORANGE


def flicker(sel, b, glow_sel=None):
    """Neon tube switching on: a few uneven flashes starting on the hit, fully lit 6 frames later."""
    t0 = land(b)
    f = 1 / FPS
    steps = [(0, 1), (1, .15), (2, .9), (3, .3), (5, 1)]
    js = [f"tl.set('{sel}',{{opacity:0}},0);"]
    js += [f"tl.set('{sel}',{{opacity:{o}}},{t0 + k * f:.4f});" for k, o in steps]
    if glow_sel:
        js.append(f"tl.set('{glow_sel}',{{opacity:0}},0);")
        js += [f"tl.set('{glow_sel}',{{opacity:{o}}},{t0 + k * f:.4f});" for k, o in steps]
    return "".join(js)


# end card layout: tops in px, chosen so the five groups have equal gaps inside the
# Reels safe zone (top 250, bottom 1500, sides 60 left and 120 right); checked by measuring the frame
EC = dict(logo=296, l1=502, l2=622, rule=803, fol=916, for_=1031, r1=1213, r2=1345)


def write_end():
    """Black end card, no border. The neon lives in the motion: elements switch on like tubes
    on the beat, and their glow pulses on the bar hits."""
    f5 = round(5 / FPS, 4)
    beats_total = V_STOP - V_END
    js = ["const tl=gsap.timeline({paused:true});"]
    js.append(flicker('#ec-logo', 0))
    js.append(f"tl.fromTo('#ec-l1',{{opacity:0,scale:1.12,filter:'blur(10px)'}},{{opacity:1,scale:1,filter:'blur(0px)',duration:.32,ease:'expo.out'}},{land(1):.4f});")
    js.append(f"tl.fromTo('#ec-l2a',{{opacity:0,y:16}},{{opacity:1,y:0,duration:{f5},ease:'expo.out'}},{land(2):.4f});")
    js.append(flicker('#ec-friend', 2.5))
    js.append(f"tl.fromTo('#ec-rule',{{scaleX:0}},{{scaleX:1,duration:.3,ease:'expo.out'}},{land(3):.4f});")
    js.append(f"tl.fromTo('#ec-fol,#ec-folglow',{{y:26,scale:1.1,transformOrigin:'50% 50%'}},{{y:0,scale:1,duration:.45,ease:'expo.out'}},{land(4):.4f});tl.fromTo('#ec-fol',{{opacity:0}},{{opacity:1,duration:.16}},{land(4):.4f});")
    js.append(flicker('#ec-folglow', 4))
    js.append(f"tl.fromTo('#ec-for',{{opacity:0,y:14}},{{opacity:1,y:0,duration:{f5},ease:'expo.out'}},{land(5):.4f});")
    js.append(flicker('#ec-r1', 6))
    js.append(flicker('#ec-r2', 7))
    # a light sweep across the follow line on the bar hit, then the glows breathe on every bar
    js.append(f"tl.fromTo('#ec-sweep',{{x:-700,opacity:1}},{{x:900,opacity:1,duration:.55,ease:'power2.inOut'}},{land(8):.4f});")
    for b in range(8, beats_total - 1, 4):
        for g in ('#ec-folglow', '#ec-friend', '#ec-r1', '#ec-r2'):
            js.append(f"tl.fromTo('{g}',{{filter:'brightness(1.6)'}},{{filter:'brightness(1)',duration:{round(BEAT * 2, 4)},ease:'power2.out'}},{land(b):.4f});")
    js.append("window.__timelines['endcard']=tl;")
    gy = "0 0 3px rgba(255,255,255,.7),0 0 12px rgba(252,224,4,.75),0 0 30px rgba(252,224,4,.4),0 0 60px rgba(254,97,0,.35)"
    pill_y = f"0 0 14px {NEON_Y},0 0 34px rgba(252,224,4,.45),inset 0 0 14px rgba(252,224,4,.3)"
    pill_o = f"0 0 14px {NEON_O},0 0 34px rgba(254,97,0,.45),inset 0 0 14px rgba(254,97,0,.3)"
    globe = (f'<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="{NEON_Y}" stroke-width="1.8"><circle cx="12" cy="12" r="9.5"/>'
             '<path d="M2.5 12h19M12 2.5c3 3.2 3 15.8 0 19M12 2.5c-3 3.2-3 15.8 0 19"/></svg>')
    wa = (f'<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="{NEON_O}" stroke-width="1.8" stroke-linejoin="round"><path d="M4 20l1.3-4A8.5 8.5 0 1 1 8.4 19z"/>'
          f'<path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.6-2-1-1 .8c-1-.5-2-1.5-2.5-2.5l.8-1-1-2z" fill="{NEON_O}" stroke="none"/></svg>')
    (COMP / "endcard.html").write_text(
        f"""<template>
<style>{FONT}
@font-face{{font-family:'Gilroy';font-weight:800;src:url('assets/brand/Gilroy-ExtraBold.ttf')}}
@font-face{{font-family:'Gilroy';font-weight:500;src:url('assets/brand/Gilroy-Medium.ttf')}}
@font-face{{font-family:'SJ Mono';src:local('PT Mono'),local('PTMono-Regular')}}
#root{{position:absolute;inset:0;background:#000}}
#ec-logo{{position:absolute;left:370px;top:{EC['logo']}px;width:340px;height:auto;filter:drop-shadow(0 0 14px rgba(252,224,4,.55)) drop-shadow(0 0 40px rgba(254,97,0,.35))}}
.ec{{position:absolute;left:0;width:1080px;text-align:center}}
#ec-l1{{top:{EC['l1']}px;font:800 96px/1 'Gilroy';letter-spacing:-.025em;color:#fff}}
#ec-l2{{top:{EC['l2']}px;font:500 66px/1 'Gilroy';letter-spacing:-.01em;color:#cfcfcf}}
#ec-l2 span{{display:inline-block}}
#ec-friend{{color:{NEON_Y};text-shadow:0 0 16px {NEON_Y},0 0 40px {NEON_Y}}}
#ec-rule{{position:absolute;left:390px;top:{EC['rule']}px;width:300px;height:3px;border-radius:2px;background:linear-gradient(90deg,transparent,{NEON_O},{NEON_Y},{NEON_O},transparent);box-shadow:0 0 18px {NEON_Y}}}
#ec-folwrap{{position:absolute;left:0;top:{EC['fol']}px;width:1080px;height:130px}}
#ec-sweepclip{{position:absolute;left:240px;top:10px;width:600px;height:80px;overflow:hidden}}
#ec-fol,#ec-folglow{{position:absolute;left:0;top:10px;width:1080px;text-align:center;font:700 59px/1.1 'Poppins';letter-spacing:-.015em;color:#fff}}
#ec-folglow{{text-shadow:{gy}}}
#ec-sweep{{position:absolute;left:0;top:0;width:240px;height:130px;background:linear-gradient(100deg,transparent,rgba(255,255,255,.55),transparent);mix-blend-mode:overlay;opacity:0}}
#ec-for{{top:{EC['for_']}px;font:500 52px/1 'Poppins';letter-spacing:.01em;color:#e9e4d6}}
#ec-for b{{font-weight:600;color:{NEON_Y};text-shadow:0 0 14px {NEON_Y}}}
.ec-row{{position:absolute;left:220px;width:640px;height:108px;border-radius:54px;display:flex;align-items:center;justify-content:center;gap:22px;font:400 42px/1 'SJ Mono';letter-spacing:.02em;color:#fff;background:rgba(255,255,255,.03)}}
#ec-r1{{top:{EC['r1']}px;border:3px solid {NEON_Y};box-shadow:{pill_y}}}
#ec-r2{{top:{EC['r2']}px;border:3px solid {NEON_O};box-shadow:{pill_o}}}
</style>
<div id="root" data-composition-id="endcard" data-width="1080" data-height="1920" data-layout-allow-overlap>
<img id="ec-logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
<div class="ec" id="ec-l1">Save this reel</div>
<div class="ec" id="ec-l2"><span id="ec-l2a">and share it with&nbsp;</span><span id="ec-friend">a friend</span></div>
<div id="ec-rule" data-layout-ignore></div>
<div id="ec-folwrap" data-layout-allow-overflow><div id="ec-folglow">Follow SJ Academy</div><div id="ec-fol">Follow SJ Academy</div><div id="ec-sweepclip" data-layout-ignore><div id="ec-sweep"></div></div></div>
<div class="ec" id="ec-for">for <b>O/A Level</b> Success</div>
<div class="ec-row" id="ec-r1">{globe}sjacademy.pk</div>
<div class="ec-row" id="ec-r2">{wa}+92-336-2144454</div>
</div>
<script>{''.join(js)}</script>
</template>
""")


def host(id_, start, dur, z, track=1):
    return (
        f'<div id="{id_}" data-composition-id="{id_}" data-composition-src="compositions/{id_}.html" '
        f'data-start="{start:.4f}" data-duration="{dur:.4f}" data-track-index="{track}" data-track-kind="graphics" '
        f'data-width="1080" data-height="1920" style="position:absolute;inset:0;z-index:{z}"></div>'
    )


def write_index():
    total = round(V_STOP * BEAT, 3)
    hosts = [host("title", 0, beat(V_RECAP), 5, 1), host("formula", 0, beat(V_RECAP), 6, 2),
             host("brand", 0, beat(V_END), 7, 3)]
    for i in range(N_SCENES):
        hosts.append(host(f"s{i + 1:02d}", beat(SCENE_BEATS * i), beat(SCENE_BEATS), 4, 4))
    hosts.append(host("recap", beat(V_RECAP), beat(V_END - V_RECAP) + .1, 4, 5))
    hosts.append(host("endcard", beat(V_END), beat(V_STOP - V_END), 9, 7))
    fade = round(beat(3), 3)
    # Evens out the track's three sections so the opening is audible on a phone and the mix sits at -14 LUFS.
    # Each change happens across the last moment before the music's own lift, so it is heard as the lift.
    lift1, lift2 = beat(16), beat(48)
    lane = {"version": 1, "lanes": [{"target": "volume", "points": [
        {"t": 0, "v": GAIN_INTRO}, {"t": round(lift1 - .25, 3), "v": GAIN_INTRO},
        {"t": round(lift1 + .05, 3), "v": GAIN_MID}, {"t": round(lift2 - .25, 3), "v": GAIN_MID},
        {"t": round(lift2 + .05, 3), "v": GAIN_HIGH}, {"t": total, "v": GAIN_HIGH},
    ]}]}
    lane_attr = html.escape(json.dumps(lane, separators=(",", ":")), quote=True)
    audio = (
        f'<audio id="music" src="assets/music/fresh.mp3" data-start="0" data-duration="{total}" '
        f'data-media-start="{MEDIA_START}" data-volume="1" data-fade-out="{fade}" data-automation="{lane_attr}" data-track-index="10"></audio>'
    )
    joined = "\n      ".join(hosts)
    (ROOT / "index.html").write_text(
        f"""<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: {INK}; }}
      #root {{ width: 100%; height: 100%; position: relative; background: {INK}; }}
      #ground {{ position: absolute; inset: 0; background: {INK}; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
      <div id="ground" class="clip" data-start="0" data-duration="{total}" data-track-index="0"></div>
      {joined}
      {audio}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
""")
    return total


def main():
    for i, sh in enumerate(SHAPES):
        write_scene(i, sh)
    write_title()
    write_formula()
    write_brand()
    write_recap()
    write_end()
    total = write_index()
    print(f"built {N_SCENES} shape scenes, {total}s")


if __name__ == "__main__":
    main()
