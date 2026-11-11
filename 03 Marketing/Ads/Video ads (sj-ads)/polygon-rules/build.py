#!/usr/bin/env python3
"""Builds index.html and compositions/ for the 6 polygon rules reel.
Follows the circle theorems v4 / angle rules v2 standard:
Single beat map at 150 BPM (matching reference track tempo and groove),
6 scenes * 8 beats (whole bars of 4/4), exact Cambridge O Level 4024 / IGCSE 0580 syllabus rules,
symmetrical 2x3 recap grid, clear angle/formula values with halos, and black neon follow end card.
Run: python3 build.py
"""
import html
import json
import math
from pathlib import Path

ROOT = Path(__file__).parent
COMP = ROOT / "compositions"
COMP.mkdir(exist_ok=True)
METRICS = json.loads((ROOT / "assets/brand/poppins-metrics.json").read_text())
FPS = 30

# ---------- music map: SJ's original synth track (music/compose.py), 150 BPM ----------
# 150 BPM: 1 beat = 0.400 s, 8 beats (3.200 s) per rule scene.
BEAT = 60 / 150.0  # 0.400 s
MUSIC = "assets/music/sj-polygon-synth.wav"
MEDIA_START = 0.0
SCENE_BEATS = 8  # whole bars (2 bars of 4/4 per rule)
N_SCENES = 6
V_LIFT = 24       # track switches to 4-on-the-floor on scene 4 (regular exterior)
V_RECAP = 48      # 6 scenes * 8 beats = 48 beats (19.20 s)
V_END = 60        # 12 beats for recap (beats 48 to 60, 19.20 s to 24.00 s)
V_STOP = 74       # 14 beats for black neon end card (beats 60 to 74, 24.00 s to 29.60 s total)
V_PITCH = V_END   # recap cuts straight to black neon follow end card

INK, CANVAS, BODY, YELLOW, ORANGE, BROWN, PEN = (
    "#151515", "#F7F5EF", "#D9D4C7", "#FCE004", "#FE6100", "#453516", "#D63A2F",
)
EXIT = 0.17  # exits start on the hit and glide after it


def at(b):
    """Clock time of a beat."""
    return round(b * BEAT, 4)


def land(b):
    """First visible frame of a move: one frame ahead of the hit."""
    return round(b * BEAT - 1 / FPS, 4)


FONT = """
@font-face{font-family:'Poppins';font-weight:400;src:url('assets/brand/Poppins-Regular.ttf')}
@font-face{font-family:'Poppins';font-weight:500;src:url('assets/brand/Poppins-Medium.ttf')}
@font-face{font-family:'Poppins';font-weight:600;src:url('assets/brand/Poppins-SemiBold.ttf')}
@font-face{font-family:'Poppins';font-weight:700;src:url('assets/brand/Poppins-Bold.ttf')}
@font-face{font-family:'Caveat';font-weight:600;src:url('assets/brand/Caveat-600.woff2')}
"""


# ---------- geometry helpers (500 x 500 bounding box) ----------
def direction(a, b):
    return math.atan2(-(b[1] - a[1]), b[0] - a[0])


def angle_at(v, p, q):
    """Measured angle pvq in degrees, from coordinates."""
    d = abs(direction(v, p) - direction(v, q))
    d = min(d, 2 * math.pi - d)
    return math.degrees(d)


def pt(c, r, deg):
    return (c[0] + r * math.cos(math.radians(deg)), c[1] - r * math.sin(math.radians(deg)))


def reg_polygon(n, center, radius, start_angle=90):
    cx, cy = center
    pts = []
    for i in range(n):
        ang = math.radians(start_angle + i * (360 / n))
        pts.append((round(cx + radius * math.cos(ang), 1), round(cy - radius * math.sin(ang), 1)))
    return pts


def wedge(v, p, q, r=46, n=20):
    a0 = direction(v, p)
    d = direction(v, q) - a0
    while d > math.pi:
        d -= 2 * math.pi
    while d < -math.pi:
        d += 2 * math.pi
    return [(v[0] + r * math.cos(a0 + d * i / n), v[1] - r * math.sin(a0 + d * i / n)) for i in range(n + 1)]


def bisect_point(v, p, q, dist):
    a0 = direction(v, p)
    d = direction(v, q) - a0
    while d > math.pi:
        d -= 2 * math.pi
    while d < -math.pi:
        d += 2 * math.pi
    m = a0 + d / 2
    return (round(v[0] + dist * math.cos(m), 1), round(v[1] - dist * math.sin(m), 1))


def scenes():
    out = []

    # 1. Interior angle sum: Pentagon split into 3 triangles from top vertex
    C1 = (250.0, 265.0)
    p5 = reg_polygon(5, C1, 155, start_angle=90)
    p0, p1, p2, p3, p4 = p5
    # Centroids of the 3 triangles from p0
    c_tri1 = (round((p0[0] + p1[0] + p2[0]) / 3, 1), round((p0[1] + p1[1] + p2[1]) / 3, 1))
    c_tri2 = (round((p0[0] + p2[0] + p3[0]) / 3, 1), round((p0[1] + p2[1] + p3[1]) / 3, 1))
    c_tri3 = (round((p0[0] + p3[0] + p4[0]) / 3, 1), round((p0[1] + p3[1] + p4[1]) / 3, 1))

    out.append(dict(
        id="interior_sum", name="Interior angle sum",
        lines=[("Sum of interior angles", False)],
        line2=[("equals ", False), ("(n - 2) × 180°", True)],
        note=["Split into (n - 2) triangles", "Pentagon: 3 × 180° = 540°"],
        draw=[p5 + [p0], [p0, p2], [p0, p3]],
        wedges=[],
        vals=[("180°", c_tri1, 4), ("180°", c_tri2, 4.5), ("180°", c_tri3, 5)],
        check=[
            ("triangles count", 3, 3),
            ("interior angle sum", (5 - 2) * 180, 540),
        ]
    ))

    # 2. Exterior angle sum: Pentagon with 5 extended pinwheel sides summing to 360°
    C2 = (250.0, 260.0)
    p5_ext = reg_polygon(5, C2, 135, start_angle=90)
    ext_pts = []
    pinwheel_draw = []
    ext_wedges = []
    for i in range(5):
        prev_p = p5_ext[(i - 1) % 5]
        curr_p = p5_ext[i]
        dx = curr_p[0] - prev_p[0]
        dy = curr_p[1] - prev_p[1]
        L = math.hypot(dx, dy)
        e_pt = (round(curr_p[0] + dx / L * 75, 1), round(curr_p[1] + dy / L * 75, 1))
        ext_pts.append(e_pt)
        pinwheel_draw.append([prev_p, e_pt])
        next_p = p5_ext[(i + 1) % 5]
        ext_wedges.append((curr_p, e_pt, next_p))

    # Place values on 3 exterior wedges: p1, p3, p0
    v_ext1 = bisect_point(p5_ext[1], ext_pts[1], p5_ext[2], 75)
    v_ext3 = bisect_point(p5_ext[3], ext_pts[3], p5_ext[4], 75)
    v_ext0 = bisect_point(p5_ext[0], ext_pts[0], p5_ext[1], 75)

    out.append(dict(
        id="exterior_sum", name="Exterior angle sum",
        lines=[("Sum of exterior angles", False)],
        line2=[("is always ", False), ("360°", True)],
        note=["One exterior angle per vertex", "5 × 72° = 360° for any polygon"],
        draw=pinwheel_draw,
        wedges=ext_wedges,
        vals=[("72°", v_ext1, 4), ("72°", v_ext3, 4.5), ("72°", v_ext0, 5)],
        check=[
            ("exterior angle 1", angle_at(p5_ext[0], ext_pts[0], p5_ext[1]), 72),
            ("exterior angle 2", angle_at(p5_ext[1], ext_pts[1], p5_ext[2]), 72),
            ("exterior sum", 5 * angle_at(p5_ext[0], ext_pts[0], p5_ext[1]), 360),
        ]
    ))

    # 3. Regular interior angle: Regular hexagon interior angle = (6-2)*180/6 = 120°
    C3 = (250.0, 260.0)
    h = reg_polygon(6, C3, 155, start_angle=30)
    h0, h1, h2, h3, h4, h5 = h
    # Corner wedge at h2 (top-left)
    w_h2 = (h2, h1, h3)
    val_h2 = bisect_point(h2, h1, h3, 85)

    out.append(dict(
        id="reg_interior", name="Regular interior angle",
        lines=[("Interior angle of regular polygon", False)],
        line2=[("equals ", False), ("(n - 2) × 180° / n", True)],
        note=["Equal angles in regular polygons", "Hexagon: 4 × 180° / 6 = 120°"],
        draw=[h + [h0]],
        wedges=[w_h2],
        vals=[("120°", val_h2, 4)],
        check=[
            ("hexagon interior angle", angle_at(h2, h1, h3), 120),
            ("regular interior formula", (6 - 2) * 180 / 6, 120),
        ]
    ))

    # 4. Regular exterior angle: Regular hexagon exterior angle = 360 / 6 = 60°
    # Vertex h2, side h3->h2 extended straight up past h2
    e2 = (h2[0], round(h2[1] - 90, 1))
    w_ext_h2 = (h2, e2, h1)
    val_ext_h2 = bisect_point(h2, e2, h1, 80)

    out.append(dict(
        id="reg_exterior", name="Regular exterior angle",
        lines=[("Exterior angle of regular polygon", False)],
        line2=[("equals ", False), ("360° / n", True)],
        note=["Equal exterior angles in regular polygons", "Hexagon: 360° / 6 = 60°"],
        draw=[h + [h0], [h2, e2]],
        wedges=[w_ext_h2],
        vals=[("60°", val_ext_h2, 4)],
        check=[
            ("hexagon exterior angle", angle_at(h2, e2, h1), 60),
            ("regular exterior formula", 360 / 6, 60),
        ]
    ))

    # 5. Interior + exterior on straight line = 180°
    # Showing both angles at vertex h2 along the straight line h3 -> h2 -> e2
    out.append(dict(
        id="straight_line", name="Interior + exterior",
        lines=[("Interior + exterior angle", False)],
        line2=[("always add up to ", False), ("180°", True)],
        note=["They sit together on a straight line", "120° + 60° = 180°"],
        draw=[h + [h0], [h3, e2]],
        wedges=[w_h2, w_ext_h2],
        vals=[("120°", val_h2, 4), ("60°", val_ext_h2, 5)],
        check=[
            ("straight line angle", angle_at(h2, h3, e2), 180),
            ("interior + exterior sum", angle_at(h2, h1, h3) + angle_at(h2, e2, h1), 180),
        ]
    ))

    # 6. Number of sides formula: n = 360 / exterior angle (Regular octagon, ext = 45° -> n = 8)
    C6 = (250.0, 260.0)
    oct_pts = reg_polygon(8, C6, 145, start_angle=22.5)
    # Side oct[2] -> oct[1] extended past oct[1]
    dx = oct_pts[1][0] - oct_pts[2][0]
    dy = oct_pts[1][1] - oct_pts[2][1]
    L = math.hypot(dx, dy)
    oct_ext = (round(oct_pts[1][0] + dx / L * 80, 1), round(oct_pts[1][1] + dy / L * 80, 1))
    w_oct = (oct_pts[1], oct_ext, oct_pts[0])
    val_oct_ext = bisect_point(oct_pts[1], oct_ext, oct_pts[0], 75)

    out.append(dict(
        id="num_sides", name="Number of sides",
        lines=[("Number of sides of regular polygon", False)],
        line2=[("n = ", False), ("360° / exterior angle", True)],
        note=["Rearrange exterior = 360° / n", "45° gives n = 360° / 45° = 8"],
        draw=[oct_pts + [oct_pts[0]], [oct_pts[2], oct_ext]],
        wedges=[w_oct],
        vals=[("45°", val_oct_ext, 4), ("n = 8", (250.0, 265.0), 5)],
        check=[
            ("octagon exterior angle", angle_at(oct_pts[1], oct_ext, oct_pts[0]), 45),
            ("number of sides", 360 / angle_at(oct_pts[1], oct_ext, oct_pts[0]), 8),
        ]
    ))

    return out


SCENES = scenes()


def color(i):
    return YELLOW if i % 2 == 0 else ORANGE


def path_d(pts, ox, oy, s):
    return "M" + " L".join(f"{ox + x * s:.1f} {oy + y * s:.1f}" for x, y in pts)


def plen(pts):
    return sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))


def text_w(txt, size, weight="600"):
    table = METRICS[weight]
    return sum(table.get(c, 600) for c in txt) / 1000 * size


def pen_samples(polys, ox, oy, s, dur):
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


def parts(sc, i, ox, oy, s, sw, pre, full=True, val_fs=42):
    col = color(i)
    wfill = ghost = lines = over = ""
    ids = dict(draw=[], thin=[], dash=[], mark=[], hi=[], wedge=[], ticks=[], vals=[], words=[], dots=[])

    # wedges
    for j, w in enumerate(sc.get("wedges", [])):
        v, p, q = w
        arc = wedge(v, p, q)
        wfill += f'<path id="{pre}wf{j}" d="{path_d([v] + arc, ox, oy, s)}Z" fill="{BROWN}" opacity="0"/>'
        lines += (f'<path id="{pre}wa{j}" d="{path_d(arc, ox, oy, s)}" pathLength="1" fill="none" '
                  f'stroke="{CANVAS}" stroke-width="{max(2, sw * .55):.1f}" stroke-dasharray="1 1" '
                  f'stroke-dashoffset="1" opacity="0"/>')
        ids["wedge"].append((f"{pre}wf{j}", f"{pre}wa{j}"))

    # ghost outlines for base drawing
    for p in sc["draw"]:
        ghost += f'<path d="{path_d(p, ox, oy, s)}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round"/>'

    # drawing strokes (animated pen)
    for j, p in enumerate(sc["draw"]):
        id_ = f"{pre}d{j}"
        ids["draw"].append((id_, plen(p)))
        lines += (f'<path id="{id_}" d="{path_d(p, ox, oy, s)}" pathLength="1" fill="none" stroke="{col}" '
                  f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
                  f'stroke-dasharray="1 1.2" stroke-dashoffset="1.1" opacity="0"/>')

    # arrows / marks
    for j, p in enumerate(sc.get("marks", [])):
        id_ = f"{pre}m{j}"
        ids["mark"].append(id_)
        lines += (f'<path id="{id_}" d="{path_d(p, ox, oy, s)}" fill="none" stroke="{CANVAS}" '
                  f'stroke-width="{max(2.4, sw * .55):.1f}" stroke-linecap="round" stroke-linejoin="round" opacity="0"/>')

    # dots
    for j, (pt_, b, rad) in enumerate(sc.get("dots", [])):
        id_ = f"{pre}o{j}"
        ids["dots"].append((id_, b))
        over += f'<circle id="{id_}" cx="{ox + pt_[0] * s:.1f}" cy="{oy + pt_[1] * s:.1f}" r="{rad * s:.1f}" fill="{CANVAS}" opacity="0"/>'

    # values / labels (data-layout-ignore prevents font-floor warning for diagram texture text in recap)
    halo = f'paint-order="stroke" stroke="{INK}" stroke-width="{max(3, 6 * s):.0f}" stroke-linejoin="round"'
    for j, (txt, pt_, b) in enumerate(sc.get("vals", [])):
        id_ = f"{pre}v{j}"
        ids["vals"].append((id_, b))
        over += (f'<text id="{id_}" x="{ox + pt_[0] * s:.1f}" y="{oy + pt_[1] * s + val_fs * .36:.1f}" '
                 f'text-anchor="middle" font-family="Poppins" font-weight="700" font-size="{val_fs}" '
                 f'fill="{CANVAS}" {halo} opacity="0" data-layout-ignore>{txt}</text>')

    return wfill, ghost, lines, over, ids


def stamp_js(sel, b):
    t0 = land(b)
    return (f"tl.set('{sel}',{{opacity:1}},{t0});tl.fromTo('{sel}',{{scale:1.3,transformOrigin:'50% 50%'}},"
            f"{{scale:1,duration:{round(4 / FPS, 4)},ease:'back.out(1.7)'}},{t0});")


def scene_timeline(sc, ids, pre, pen_dur, t_pen, ox, oy, s, ghost_at=None):
    js = []
    if ghost_at is not None:
        js.append(f"tl.fromTo('#{pre}ghost',{{opacity:0}},{{opacity:.17,duration:.2,ease:'power1.out'}},{ghost_at});")
    cur = t_pen
    total = sum(L for _, L in ids["draw"])
    for id_, L in ids["draw"]:
        d = round(pen_dur * L / total, 4)
        js.append(f"tl.set('#{id_}',{{opacity:1}},{cur:.4f});tl.fromTo('#{id_}',{{strokeDashoffset:1.1}},{{strokeDashoffset:0,duration:{d},ease:'none'}},{cur:.4f});")
        cur += d
    pen = pen_samples(sc["draw"], ox, oy, s, pen_dur)
    dt = round(pen_dur / (len(pen) - 1), 5)
    js.append(f"(()=>{{const P={json.dumps(pen, separators=(',', ':'))};tl.set('#{pre}pen',{{x:P[0][0],y:P[0][1]}},0);tl.set('#{pre}pen',{{opacity:1}},{t_pen:.4f});"
              f"P.slice(1).forEach((p,k)=>tl.to('#{pre}pen',{{x:p[0],y:p[1],duration:{dt},ease:'none'}},{t_pen:.4f}+k*{dt}));tl.set('#{pre}pen',{{opacity:0}},{t_pen + pen_dur:.4f});}})();")
    return js


def write_scene(i, sc):
    cid = f"s{i + 1:02d}"
    ox, oy, s, sw = 265, 505, 1.1, 6
    pre = f"{cid}-"
    wfill, ghost, lines, over, ids = parts(sc, i, ox, oy, s, sw, pre, val_fs=42)
    pen_dur = round(at(2), 4)
    t_pen = land(1)
    t_arcs = land(3)

    js = ["const tl=gsap.timeline({paused:true});"]
    js += scene_timeline(sc, ids, pre, pen_dur, t_pen, ox, oy, s, ghost_at=land(0.5))

    for id_ in ids["mark"]:
        js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:1,duration:.1}},{t_arcs});")

    for id_, b in ids.get("dots", []):
        js.append(stamp_js(f"#{id_}", b))

    for wf, wa in ids["wedge"]:
        js.append(f"tl.fromTo('#{wf}',{{opacity:0}},{{opacity:1,duration:.12}},{t_arcs});")
        js.append(f"tl.set('#{wa}',{{opacity:1}},{t_arcs});tl.fromTo('#{wa}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.18,ease:'none'}},{t_arcs});")

    for id_, b in ids["vals"]:
        js.append(stamp_js(f"#{id_}", b))

    t_exit = land(SCENE_BEATS)
    js.append(f"tl.to('#{pre}all',{{opacity:0,duration:{EXIT},ease:'power2.out'}},{t_exit:.4f});")
    js.append(f"window.__timelines['{cid}']=tl;")

    (COMP / f"{cid}.html").write_text(
        f"""<template>
<style>{FONT}#root{{position:absolute;inset:0}}</style>
<div id="root" data-composition-id="{cid}" data-width="1080" data-height="1920">
<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0" data-layout-allow-overlap data-layout-allow-overflow>
<g id="{pre}all">{wfill}<g id="{pre}ghost" opacity="0">{ghost}</g>{lines}{over}<circle id="{pre}pen" r="10" fill="{CANVAS}" opacity="0"/></g>
</svg>
</div>
<script>{''.join(js)}</script>
</template>
""")


def write_title():
    js = f"""const tl=gsap.timeline({{paused:true}});
tl.fromTo('#title-band',{{clipPath:'inset(0 100% 0 0)'}},{{clipPath:'inset(0 0% 0 0)',duration:.3,ease:'sine.inOut'}},.2);
tl.to('#title-box',{{opacity:0,duration:{EXIT},ease:'power2.out'}},{land(V_RECAP):.4f});
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
<div id="title-box" data-layout-allow-overlap>6 polygon rules<br>for <span class="hlw">O Level Maths<span id="title-band" data-layout-allow-overflow data-layout-ignore><span>O Level Maths</span></span></span></div>
</div>
<script>{js}</script>
</template>
""")


def write_reason():
    cy = 1200
    boxes = []
    fhtml = nhtml = ""
    fs = 42

    def row(parts_):
        return "".join(
            f'<span class="key">{html.escape(t_)}</span>' if key else html.escape(t_) for t_, key in parts_
        )

    for i, sc in enumerate(SCENES):
        rows = [sc["lines"]] + ([sc["line2"]] if sc.get("line2") else [])
        w = max(text_w("".join(t_ for t_, _ in r), fs) for r in rows)
        w = w + 96
        h = 56 * len(rows) + 52
        boxes.append((round(w), h))
        body = "<br>".join(row(r) for r in rows)
        fhtml += f'<div class="fw"><div class="f" id="f{i}"><div class="st">{body}</div></div></div>'
        nhtml += f'<div class="d" id="d{i}">' + "<br>".join(html.escape(n) for n in sc["note"]) + "</div>"

    js = ["const tl=gsap.timeline({paused:true});"]
    frame = round(1 / FPS, 4)
    for i in range(len(SCENES)):
        b = SCENE_BEATS * i
        W, H = boxes[i]
        attr = f"x:{540 - W / 2},y:{cy - H / 2},width:{W},height:{H}"
        if i == 0:
            js.append("tl.set('#f0',{opacity:1,y:0},0);tl.set('#d0',{opacity:1},0);")
        else:
            t_land = land(b)
            js.append(f"tl.to('#fbox',{{attr:{{{attr}}},stroke:'{color(i)}',duration:.34,ease:'expo.out'}},{t_land:.4f});")
            js.append(f"tl.to('#f{i - 1}',{{opacity:0,duration:{2 * frame}}},{t_land:.4f});")
            js.append(f"tl.to('#d{i - 1}',{{opacity:0,duration:{2 * frame}}},{t_land:.4f});")
            js.append(f"tl.fromTo('#f{i}',{{opacity:0,y:18}},{{opacity:1,y:0,duration:{5 * frame},ease:'expo.out'}},{t_land:.4f});")
            js.append(f"tl.fromTo('#d{i}',{{opacity:0}},{{opacity:1,duration:{3 * frame}}},{t_land:.4f});")

    js.append(f"tl.to('#fall',{{opacity:0,duration:{EXIT},ease:'power2.out'}},{land(V_RECAP):.4f});")
    js.append("window.__timelines['reason']=tl;")
    W0, H0 = boxes[0]

    (COMP / "reason.html").write_text(
        f"""<template>
<style>{FONT}#root{{position:absolute;inset:0}}
#fall{{position:absolute;inset:0}}
.fw{{position:absolute;left:0;top:{cy - 150}px;width:1080px;height:300px;display:flex;align-items:center;justify-content:center}}
.f{{display:flex;flex-direction:column;align-items:center;gap:2px;opacity:0;text-align:center}}
.st{{font:600 {fs}px/56px 'Poppins';color:{CANVAS};white-space:nowrap}}
.key{{color:{YELLOW}}}
.d{{position:absolute;left:70px;width:940px;top:1322px;text-align:center;font:400 34px/1.34 'Poppins';color:{BODY};opacity:0}}
</style>
<div id="root" data-composition-id="reason" data-width="1080" data-height="1920">
<div id="fall" data-layout-allow-overlap data-layout-allow-overflow>
<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0"><rect id="fbox" x="{540 - W0 / 2}" y="{cy - H0 / 2}" width="{W0}" height="{H0}" rx="22" fill="none" stroke="{color(0)}" stroke-width="4"/></svg>
{fhtml}{nhtml}
</div>
</div>
<script>{''.join(js)}</script>
</template>
""")


def write_brand():
    # Logo positioned at top: 230px, leaving 56px breathing room above screenshot note at top: 350px
    (COMP / "brand.html").write_text(
        f"""<template>
<style>#root{{position:absolute;inset:0}}#logo{{position:absolute;left:420px;top:230px;width:240px;height:auto}}</style>
<div id="root" data-composition-id="brand" data-width="1080" data-height="1920" data-no-timeline>
<img id="logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
</div>
</template>
""")


def write_recap():
    s = 0.40
    svg_all = names = ""
    js = ["const tl=gsap.timeline({paused:true});"]
    js.append(f"tl.fromTo('#rc-note',{{opacity:0}},{{opacity:1,duration:.16}},{land(2)});")

    # Perfectly symmetrical 2 columns x 3 rows
    # Canvas is 1080px wide. Column centers are at 295 and 785 (equidistant from center 540 by 245px).
    # Left margin = 195px, Right margin = 195px, Gap between diagrams = 290px.
    # 3 rows at y = 500, 800, 1100 (300px vertical spacing).
    col_x = [295, 785]
    row_y = [500, 800, 1100]

    for i, sc in enumerate(SCENES):
        c_idx = i % 2
        r_idx = i // 2
        ox = col_x[c_idx] - round(250 * s)
        oy = row_y[r_idx]
        pre = f"r{i}-"
        # val_fs = 16 ensures angle and formula numbers sit neatly without crowding lines
        wfill, ghost, lines, over, ids = parts(sc, i, ox, oy, s, 3.2, pre, full=False, val_fs=16)
        svg_all += f'{wfill}<g id="{pre}ghost" opacity="0">{ghost}</g>{lines}{over}<circle id="{pre}pen" r="5" fill="{CANVAS}" opacity="0"/>'
        names += f'<div class="rn" id="{pre}nm" style="left:{col_x[c_idx] - 200}px;top:{oy + round(500 * s) + 8}px">{sc["name"]}</div>'

        t0 = at(0) + 0.02 * i
        t_end = land(2)
        js += scene_timeline(sc, ids, pre, round(t_end - land(1), 4), land(1), ox, oy, s, ghost_at=None)
        for id_ in ids["mark"]:
            js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:1,duration:.1}},{t_end});")
        for wf, wa in ids["wedge"]:
            js.append(f"tl.fromTo('#{wf}',{{opacity:0}},{{opacity:1,duration:.1}},{t_end});")
            js.append(f"tl.set('#{wa}',{{opacity:1}},{t_end});tl.fromTo('#{wa}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.14,ease:'none'}},{t_end});")
        for id_, _ in ids["vals"] + ids.get("dots", []):
            js.append(stamp_js(f"#{id_}", 3))
        js.append(f"tl.fromTo('#{pre}nm',{{opacity:0,y:8}},{{opacity:1,y:0,duration:{round(5 / FPS, 4)},ease:'expo.out'}},{land(1):.4f});")

    js.append("window.__timelines['recap']=tl;")
    (COMP / "recap.html").write_text(
        f"""<template>
<style>{FONT}#root{{position:absolute;inset:0}}
#rc-note{{position:absolute;left:0;width:1080px;top:350px;text-align:center;font:600 58px/1 'Caveat';color:{YELLOW};opacity:0}}
.rn{{position:absolute;width:400px;text-align:center;font:600 28px/1.2 'Poppins';color:{YELLOW};opacity:0}}
</style>
<div id="root" data-composition-id="recap" data-width="1080" data-height="1920" data-layout-allow-overlap>
<div id="rc-note" data-hold>screenshot this one</div>
<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0" data-layout-ignore>{svg_all}</svg>
{names}
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
    """Black neon end card (standard since 11 November 2026). Elements switch on like tubes on the beat,
    with a light sweep and pulses on bar hits."""
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
#ec-logo{{position:absolute;left:370px;top:{EC['logo']}px;width:340px;height:auto;opacity:0;filter:drop-shadow(0 0 14px rgba(252,224,4,.55)) drop-shadow(0 0 40px rgba(254,97,0,.35))}}
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
    tail = EXIT + 0.05
    hosts = [
        host("title", 0, at(V_RECAP) + tail, 5, 2),
        host("reason", 0, at(V_RECAP) + tail, 6, 3),
        host("brand", 0, at(V_END), 7, 4),
    ]
    for i in range(len(SCENES)):
        hosts.append(host(f"s{i + 1:02d}", at(SCENE_BEATS * i), at(SCENE_BEATS) + tail, 4, 5))
    hosts.append(host("recap", at(V_RECAP), at(V_END - V_RECAP) + 0.1, 4, 6))
    hosts.append(host("endcard", at(V_END), at(V_STOP - V_END), 9, 8))
    audio = (
        f'<audio id="music" src="{MUSIC}" data-start="0" data-duration="{total}" '
        f'data-media-start="{MEDIA_START}" data-volume="1" data-fade-out="{at(4)}" data-track-index="10"></audio>'
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
    for i, sc in enumerate(SCENES):
        write_scene(i, sc)
    write_title()
    write_reason()
    write_brand()
    write_recap()
    write_end()
    total = write_index()
    print(f"built {len(SCENES)} rule scenes, {total}s, music from {MEDIA_START}s")


if __name__ == "__main__":
    main()
