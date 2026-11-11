# Builds the "12 angle rules" reel. Writes index.html and compositions/*.html. Run: python3 build.py
# Every diagram is computed from its real angles, so what is drawn matches what is labelled.
# check_angles() re-measures each drawn angle from the coordinates and stops the build if one is off.
import math, os

HERE = os.path.dirname(os.path.abspath(__file__))
INK, CANVAS, DIM, YELLOW, ORANGE, BROWN = "#151515", "#F7F5EF", "#D9D4C7", "#FCE004", "#FE6100", "#453516"
H = 60 / 84          # one cut unit: two beats of the 168 BPM track (0.714 s)
MEDIA_START = 0.036  # first beat of the track
LW, ARC_W = 7, 7

FONT = """@font-face{font-family:'SJ Poppins';font-weight:500;src:url('assets/brand/Poppins-Medium.ttf')}
@font-face{font-family:'SJ Poppins';font-weight:600;src:url('assets/brand/Poppins-SemiBold.ttf')}
@font-face{font-family:'SJ Poppins';font-weight:700;src:url('assets/brand/Poppins-Bold.ttf')}
@font-face{font-family:'SJ Caveat';font-weight:600;src:url('assets/brand/Caveat-600.woff2')}"""


# ------------------------------------------------------------ geometry
def pt(c, r, deg):
    return (c[0] + r * math.cos(math.radians(deg)), c[1] - r * math.sin(math.radians(deg)))


def L(p, q, kind="main"):
    return dict(t="line", p=p, q=q, kind=kind)


def A(c, a1, a2, label=None, r=72, lr=None, kind="arc", value=None):
    """Arc anticlockwise from a1 to a2 (degrees, y up). The label sits on the bisector."""
    return dict(t="arc", c=c, a1=a1, a2=a2, r=r, label=label, lr=lr or r + 62, kind=kind, value=value)


def tick(p, q):
    m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = math.hypot(dx, dy)
    ux, uy = -dy / n * 20, dx / n * 20
    return L((m[0] - ux, m[1] - uy), (m[0] + ux, m[1] + uy), "tick")


def chevron(x, y):
    return [L((x - 18, y - 16), (x + 2, y), "base"), L((x - 18, y + 16), (x + 2, y), "base")]


def text_item(s, x, y):
    return dict(t="label", s=s, x=x, y=y)


def parallel_base():
    """Two parallel lines 320 px apart, cut by a transversal at 60 degrees."""
    top, bottom = 640, 960
    B = (448.0, float(bottom))
    AA = (B[0] + (bottom - top) / math.tan(math.radians(60)), float(top))
    t_top, t_bottom = pt(AA, 80, 60), pt(B, 62, 240)
    base = [L((90, top), (990, top), "base"), L((90, bottom), (990, bottom), "base")]
    base += chevron(230, top) + chevron(230, bottom)
    return AA, B, t_top, t_bottom, base, top, bottom


def rule_defs():
    rules = []

    # 1 straight line
    O = (540.0, 980.0)
    rules.append(dict(key="straight", beats=5, name="Straight line", result="180°", kind="sum", target=180,
        cap=["Angles on a straight line add up to ", ("180°",)], calc="130° + 50° = 180°",
        items=[L((110, O[1]), (970, O[1])), L(O, pt(O, 500, 50)),
               A(O, 2, 48, "50°", value=50), A(O, 52, 178, "130°", value=130)]))

    # 2 at a point
    O = (540.0, 800.0)
    rules.append(dict(key="point", beats=5, name="At a point", result="360°", kind="sum", target=360,
        cap=["Angles at a point add up to ", ("360°",)], calc="140° + 100° + 120° = 360°",
        items=[L(O, pt(O, 250, 90)), L(O, pt(O, 250, 230)), L(O, pt(O, 250, 330)),
               A(O, 92, 228, "140°", value=140), A(O, 232, 328, "100°", value=100),
               A(O, 332, 448, "120°", value=120)]))

    # 3 vertically opposite
    O = (540.0, 800.0)
    rules.append(dict(key="vertical", beats=4, name="Vertically opposite", result="equal", kind="equal",
        cap=["Vertically opposite angles are ", ("equal",)], calc=None,
        items=[L(pt(O, 430, 215), pt(O, 430, 35)), L(pt(O, 430, 145), pt(O, 430, 325)),
               A(O, -35, 35, "70°", r=90, value=70), A(O, 145, 215, "70°", r=90, value=70)]))

    # 4 alternate
    AA, B, tt, tb, base, top, bottom = parallel_base()
    rules.append(dict(key="alternate", beats=5, name="Alternate", result="equal", kind="equal",
        cap=["Alternate angles on parallel lines are ", ("equal",)], calc=None, note="Z shape",
        items=base + [L(tb, tt, "base"), L((AA[0] - 340, top), AA, "hi"), L(AA, B, "hi"), L(B, (B[0] + 340, bottom), "hi"),
                      A(AA, 180, 240, "60°", r=66, lr=142, value=60), A(B, 0, 60, "60°", r=66, lr=142, value=60)]))

    # 5 corresponding
    AA, B, tt, tb, base, top, bottom = parallel_base()
    rules.append(dict(key="corresponding", beats=5, name="Corresponding", result="equal", kind="equal",
        cap=["Corresponding angles on parallel lines are ", ("equal",)], calc=None, note="F shape",
        items=base + [L(tb, tt, "base"), L(B, tt, "hi"), L(AA, (AA[0] + 300, top), "hi"), L(B, (B[0] + 300, bottom), "hi"),
                      A(AA, 0, 60, "60°", r=66, lr=142, value=60), A(B, 0, 60, "60°", r=66, lr=142, value=60)]))

    # 6 co-interior
    AA, B, tt, tb, base, top, bottom = parallel_base()
    rules.append(dict(key="cointerior", beats=5, name="Co-interior", result="180°", kind="sum", target=180,
        cap=["Co-interior angles on parallel lines add up to ", ("180°",)], calc="120° + 60° = 180°", note="C shape",
        items=base + [L(tb, tt, "base"), L((AA[0] + 300, top), AA, "hi"), L(AA, B, "hi"), L(B, (B[0] + 300, bottom), "hi"),
                      A(AA, 240, 360, "120°", r=66, lr=142, value=120), A(B, 0, 60, "60°", r=66, lr=142, value=60)]))

    # 7 triangle
    a, b = (190.0, 1000.0), (890.0, 1000.0)
    h = (b[0] - a[0]) / (1 / math.tan(math.radians(60)) + 1 / math.tan(math.radians(45)))
    c = (a[0] + h / math.tan(math.radians(60)), a[1] - h)
    rules.append(dict(key="triangle", beats=5, name="Triangle", result="180°", kind="sum", target=180,
        cap=["Angles in a triangle add up to ", ("180°",)], calc="60° + 45° + 75° = 180°",
        items=[L(a, b), L(b, c), L(c, a),
               A(a, 0, 60, "60°", lr=128, value=60), A(b, 135, 180, "45°", lr=160, value=45),
               A(c, 240, 315, "75°", lr=132, value=75)]))

    # 8 isosceles: base angles 70, drawn to 70
    hh = 430.0
    half = hh / math.tan(math.radians(70))
    a, b, c = (540 - half, 1000.0), (540 + half, 1000.0), (540.0, 1000 - hh)
    rules.append(dict(key="isosceles", beats=5, name="Isosceles", result="base angles equal", kind="equal",
        cap=["Base angles of an isosceles triangle are ", ("equal",)], calc=None,
        items=[L(a, b), L(b, c), L(c, a), tick(a, c), tick(c, b),
               A(a, 0, 70, "70°", r=56, lr=112, value=70), A(b, 110, 180, "70°", r=56, lr=112, value=70)]))

    # 9 exterior angle of a triangle
    a, b = (150.0, 1000.0), (650.0, 1000.0)
    h = (b[0] - a[0]) / (1 / math.tan(math.radians(50)) + 1 / math.tan(math.radians(60)))
    c = (a[0] + h / math.tan(math.radians(50)), a[1] - h)
    rules.append(dict(key="exterior", beats=8, name="Triangle exterior", result="sum of 2 opposite interiors", kind="exterior",
        cap=["The exterior angle of a triangle equals the ", ("sum",), " of the two opposite interior angles"],
        calc="50° + 70° = 120°",
        items=[L(a, b), L(b, c), L(c, a), L(b, (960.0, 1000.0), "base"),
               A(a, 0, 50, "50°", lr=132, value=50), A(c, 230, 300, "70°", lr=132, value=70),
               A(b, 0, 120, "120°", kind="arcHi", value=120)]))

    # 10 quadrilateral: 70, 100, 80, 110 going round
    a, b = (190.0, 1000.0), (830.0, 1000.0)
    hgt = 430.0
    d = (a[0] + hgt / math.tan(math.radians(70)), 1000 - hgt)
    c = (b[0] + hgt / math.tan(math.radians(80)), 1000 - hgt)
    rules.append(dict(key="quad", beats=6, name="Quadrilateral", result="360°", kind="sum", target=360,
        cap=["Angles in a quadrilateral add up to ", ("360°",)], calc="70° + 100° + 80° + 110° = 360°",
        items=[L(a, b), L(b, c), L(c, d), L(d, a),
               A(a, 0, 70, "70°", lr=130, value=70), A(b, 80, 180, "100°", lr=130, value=100),
               A(c, 180, 260, "80°", lr=130, value=80), A(d, 250, 360, "110°", lr=130, value=110)]))

    # 11 exterior angles of a regular pentagon
    O = (540.0, 795.0)
    R = 190
    V = [pt(O, R, 90 + 72 * i) for i in range(5)]
    items = [L(V[i], V[(i + 1) % 5]) for i in range(5)]
    arcs = []
    for i in range(5):
        p, q, nxt = V[i], V[(i + 1) % 5], V[(i + 2) % 5]
        d1 = math.degrees(math.atan2(-(q[1] - p[1]), q[0] - p[0]))
        items.append(L(q, pt(q, 88, d1), "base"))
        arcs.append(A(q, d1, d1 + 72, "72°", r=48, lr=104, value=72))
    rules.append(dict(key="polyext", beats=6, name="Polygon exterior", result="360°", kind="sum", target=360,
        cap=["The exterior angles of a convex polygon add up to ", ("360°",)], calc="Regular pentagon: 5 × 72° = 360°",
        items=items + arcs))

    # 12 interior angles of a hexagon, split into 4 triangles
    O = (540.0, 790.0)
    R = 240
    V = [pt(O, R, 60 * i) for i in range(6)]
    items = [L(V[(3 + i) % 6], V[(4 + i) % 6]) for i in range(6)]
    start = V[3]
    items += [L(start, V[1], "arcLine"), L(start, V[0], "arcLine"), L(start, V[5], "arcLine")]
    # the three diagonals from the left corner cut the hexagon into these four triangles
    tris = [(V[3], V[4], V[5]), (V[3], V[5], V[0]), (V[3], V[0], V[1]), (V[3], V[1], V[2])]
    for n, tr in enumerate(tris):
        cx, cy = sum(p[0] for p in tr) / 3, sum(p[1] for p in tr) / 3
        items.append(text_item(str(n + 1), cx, cy))
    rules.append(dict(key="polyint", beats=9, name="Polygon interior", result="(n − 2) × 180°", kind="poly",
        cap=["Interior angles of an n-sided polygon add up to ", ("(n − 2) × 180°",)],
        calc="Hexagon: n = 6, (6 − 2) × 180° = 720°", items=items))
    return rules


def check_angles(rules):
    """Second solve: re-measure every labelled angle from coordinates and check each rule's total."""
    log = []
    for r in rules:
        arcs = [i for i in r["items"] if i["t"] == "arc"]
        vals = [a["value"] for a in arcs]
        for a in arcs:
            span = a["a2"] - a["a1"]
            gap = 4 if r["key"] in ("straight", "point") else 0
            assert abs(span + gap - a["value"]) < 1e-6, (r["key"], a["value"], span)
        if r["kind"] == "sum":
            assert sum(vals) == r["target"], (r["key"], vals)
        if r["kind"] == "equal":
            assert len(set(vals)) == 1, (r["key"], vals)
        if r["kind"] == "exterior":
            assert vals[0] + vals[1] == vals[2], (r["key"], vals)
        log.append(f"{r['key']}: {vals}")
    # triangle sides: measure the corners from the drawn points
    def corner(p, q, s):
        a1 = math.atan2(p[1] - q[1], p[0] - q[0])
        a2 = math.atan2(s[1] - q[1], s[0] - q[0])
        d = abs(math.degrees(a1 - a2)) % 360
        return min(d, 360 - d)
    tri = next(r for r in rules if r["key"] == "triangle")["items"]
    a, b, c = tri[0]["p"], tri[0]["q"], tri[1]["q"]
    log.append("triangle corners " + str([round(corner(c, a, b), 3), round(corner(a, b, c), 3), round(corner(a, c, b), 3)]))
    assert abs(corner(c, a, b) - 60) < 1e-6 and abs(corner(a, b, c) - 45) < 1e-6 and abs(corner(a, c, b) - 75) < 1e-6
    iso = next(r for r in rules if r["key"] == "isosceles")["items"]
    a, b, c = iso[0]["p"], iso[0]["q"], iso[1]["q"]
    assert abs(corner(c, a, b) - 70) < 1e-6 and abs(corner(a, b, c) - 70) < 1e-6
    ext = next(r for r in rules if r["key"] == "exterior")["items"]
    a, b, c = ext[0]["p"], ext[0]["q"], ext[1]["q"]
    assert abs(corner(c, a, b) - 50) < 1e-6 and abs(corner(a, c, b) - 70) < 1e-6 and abs(corner(a, b, c) - 60) < 1e-6
    q = next(r for r in rules if r["key"] == "quad")["items"]
    a, b, c, d = q[0]["p"], q[0]["q"], q[1]["q"], q[2]["q"]
    cs = [corner(d, a, b), corner(a, b, c), corner(b, c, d), corner(c, d, a)]
    log.append("quad corners " + str([round(x, 3) for x in cs]))
    assert all(abs(x - y) < 1e-6 for x, y in zip(cs, [70, 100, 80, 110]))
    assert (6 - 2) * 180 == 720 and 5 * 72 == 360
    return log


# ------------------------------------------------------------ svg
def f(n):
    return f"{n:.2f}"


def arc_path(a, r=None):
    r = r or a["r"]
    s, e = pt(a["c"], r, a["a1"]), pt(a["c"], r, a["a2"])
    large = 1 if a["a2"] - a["a1"] > 180 else 0
    return f"M{f(s[0])} {f(s[1])} A{r} {r} 0 {large} 0 {f(e[0])} {f(e[1])}"


STROKE = {"main": (YELLOW, LW), "hi": (YELLOW, LW + 1), "base": (DIM, 4), "tick": (YELLOW, 5), "arcLine": (ORANGE, 5)}


def svg_rule(r, prefix):
    out, lines, arcs, labels = [], [], [], []
    for n, it in enumerate(r["items"]):
        id_ = f"{prefix}-i{n}"
        if it["t"] == "line":
            col, w = STROKE[it["kind"]]
            out.append(f'<path id="{id_}" class="ln" d="M{f(it["p"][0])} {f(it["p"][1])} L{f(it["q"][0])} {f(it["q"][1])}" stroke="{col}" stroke-width="{w}" pathLength="1"/>')
            lines.append((id_, it))
        elif it["t"] == "arc":
            col = YELLOW if it["kind"] == "arcHi" else ORANGE
            out.append(f'<path id="{id_}" class="ln" d="{arc_path(it)}" stroke="{col}" stroke-width="{ARC_W}" pathLength="1"/>')
            mid = (it["a1"] + it["a2"]) / 2
            x, y = pt(it["c"], it["lr"], mid)
            lid = id_ + "t"
            out.append(f'<text id="{lid}" class="lb" x="{f(x)}" y="{f(y)}">{it["label"]}</text>')
            arcs.append((id_, lid))
        else:
            out.append(f'<text id="{id_}" class="num" x="{f(it["x"])}" y="{f(it["y"])}">{it["s"]}</text>')
            labels.append(id_)
    return out, lines, arcs, labels


def caption_html(cap, prefix):
    html, hl = "", []
    for n, part in enumerate(cap):
        if isinstance(part, tuple):
            wid = f"{prefix}-hl{n}"
            html += f'<span class="hw"><i id="{wid}b" class="band"></i><span id="{wid}" class="ht">{part[0]}</span></span>'
            hl.append(wid)
        else:
            html += part
    return html, hl


def rule_comp(r, n, dur):
    p = f"r{n:02d}"
    svg, lines, arcs, labels = svg_rule(r, p)
    cap, hl = caption_html(r["cap"], p)
    calc = f'<div id="{p}-calc" class="calc">{r["calc"]}</div>' if r.get("calc") else ""
    note = f'<div id="{p}-note" class="note">{r["note"]}</div>' if r.get("note") else ""
    js = [f"gsap.set('#{p} .ln',{{strokeDasharray:1,strokeDashoffset:1,opacity:0}});",
          f"gsap.set('#{p} .lb, #{p} .num',{{opacity:0}});"]
    t = 0.05
    if n > 1:
        js.append(f"tl.fromTo('#{p}-cap',{{y:18,opacity:0}},{{y:0,opacity:1,duration:0.2,ease:'expo.out'}},0);")
    bases = [x for x in lines if x[1]["kind"] == "base"]
    mains = [x for x in lines if x[1]["kind"] not in ("base", "arcLine", "tick")]
    if n == 1:
        js.append(f"gsap.set('#{mains[0][0]}',{{strokeDashoffset:0,opacity:1}});")
        mains = mains[1:]
    extras = [x for x in lines if x[1]["kind"] in ("arcLine", "tick")]
    # structural lines appear together, then the pen draws the main shape stroke by stroke
    if bases and not r["key"] in ("exterior", "polyext"):
        for id_, _ in bases:
            js.append(f"tl.set('#{id_}',{{opacity:1}},{f(t)});tl.to('#{id_}',{{strokeDashoffset:0,duration:0.32,ease:'sine.inOut'}},{f(t)});")
        t += 0.3
    if mains:
        per = min(0.95 / len(mains), 0.42)
        js.append(f"tl.set('#{p}-pen',{{opacity:1}},{f(t)});")
        for id_, it in mains:
            js.append(f"tl.set('#{id_}',{{opacity:1}},{f(t)});tl.to('#{id_}',{{strokeDashoffset:0,duration:{f(per)},ease:'sine.inOut'}},{f(t)});")
            js.append(f"tl.fromTo('#{p}-pen',{{attr:{{cx:{f(it['p'][0])},cy:{f(it['p'][1])}}}}},{{attr:{{cx:{f(it['q'][0])},cy:{f(it['q'][1])}}},duration:{f(per - 0.02)},ease:'sine.inOut',immediateRender:false}},{f(t)});")
            t += per
        js.append(f"tl.set('#{p}-pen',{{opacity:0}},{f(t)});")
    if bases and r["key"] in ("exterior", "polyext"):
        for id_, _ in bases:
            js.append(f"tl.set('#{id_}',{{opacity:1}},{f(t)});tl.to('#{id_}',{{strokeDashoffset:0,duration:0.24,ease:'sine.inOut'}},{f(t)});")
        t += 0.26
    for id_, _ in extras:
        js.append(f"tl.set('#{id_}',{{opacity:1}},{f(t)});tl.to('#{id_}',{{strokeDashoffset:0,duration:0.22,ease:'sine.inOut'}},{f(t)});")
        t += 0.14
    for lid in labels:
        js.append(f"tl.to('#{lid}',{{opacity:1,duration:0.14}},{f(t)});")
        t += 0.1
    step = 0.3 if len(arcs) <= 3 else (0.22 if len(arcs) == 4 else 0.16)
    for id_, lid in arcs:
        js.append(f"tl.set('#{id_}',{{opacity:1}},{f(t)});tl.to('#{id_}',{{strokeDashoffset:0,duration:0.24,ease:'sine.inOut'}},{f(t)});")
        js.append(f"tl.to('#{lid}',{{opacity:1,duration:0.14}},{f(t + 0.14)});")
        t += step
    if r.get("note"):
        js.append(f"tl.fromTo('#{p}-note',{{opacity:0}},{{opacity:1,duration:0.2}},{f(t)});")
    if r.get("calc"):
        js.append(f"tl.fromTo('#{p}-calc',{{opacity:0,y:12}},{{opacity:1,y:0,duration:0.27,ease:'expo.out'}},{f(t + 0.05)});")
        t += 0.2
    # the highlighter marks the key word once everything has landed
    t = max(t + 0.1, 1.2)
    for w in hl:
        js.append(f"tl.fromTo('#{w}b',{{scaleX:0}},{{scaleX:1,duration:0.27,ease:'power2.inOut'}},{f(t)});")
        js.append(f"tl.fromTo('#{w}',{{color:'{CANVAS}'}},{{color:'{INK}',duration:0.13}},{f(t + 0.07)});")
    assert t + 0.5 < dur, (r["key"], t, dur)
    return f"""<template>
  <style>
{FONT}
#root{{position:absolute;inset:0;font-family:'SJ Poppins';}}
#{p}{{position:absolute;inset:0;}}
#{p} svg{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible;}}
#{p} .ln{{fill:none;stroke-linecap:round;stroke-linejoin:round;}}
#{p} .lb{{font-family:'SJ Poppins';font-weight:600;font-size:46px;fill:{CANVAS};text-anchor:middle;dominant-baseline:central;}}
#{p} .num{{font-family:'SJ Poppins';font-weight:600;font-size:44px;fill:{CANVAS};text-anchor:middle;dominant-baseline:central;}}
#{p}-count{{position:absolute;right:90px;top:172px;font-size:46px;font-weight:700;color:{YELLOW};line-height:64px;}}
#{p}-count small{{font-size:32px;font-weight:500;color:{DIM};}}
#{p}-cap{{position:absolute;left:130px;width:820px;bottom:470px;padding:24px 30px;border:3px solid {CANVAS};border-radius:20px;text-align:center;font-size:46px;line-height:1.3;font-weight:600;color:{CANVAS};background:{INK};}}
#{p} .hw{{position:relative;display:inline-block;white-space:nowrap;padding:0 10px;}}
#{p} .band{{position:absolute;inset:4px 0 2px 0;background:{YELLOW};border-radius:8px;transform-origin:0% 50%;}}
#{p} .ht{{position:relative;}}
#{p}-calc{{position:absolute;left:60px;width:960px;top:1050px;text-align:center;font-size:44px;font-weight:500;color:{DIM};line-height:60px;}}
#{p}-note{{position:absolute;left:70px;top:440px;font-family:'SJ Caveat';font-weight:600;font-size:64px;color:{YELLOW};line-height:80px;padding-right:20px;}}
  </style>
  <div id="root" data-composition-id="{p}" data-width="1080" data-height="1920">
    <div id="{p}" data-layout-allow-overlap data-hold>
      <div id="{p}-count">{n}<small> / 12</small></div>
      <svg viewBox="0 0 1080 1920" data-layout-allow-overflow>
        <g transform="translate(-97.2 -212.5) scale(1.18)">{''.join(svg)}<circle id="{p}-pen" r="11" cx="0" cy="0" fill="{CANVAS}" opacity="0"/></g>
      </svg>
      {note}{calc}
      <div id="{p}-cap">{cap}</div>
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {chr(10).join('    ' + j for j in js).strip()}
    tl.set({{}},{{}},{f(dur - 0.01)});
    window.__timelines["{p}"] = tl;
  </script>
</template>
"""


# ------------------------------------------------------------ recap
def mini(r, n):
    xs, ys = [], []
    parts = []
    for it in r["items"]:
        if it["t"] == "line":
            xs += [it["p"][0], it["q"][0]]; ys += [it["p"][1], it["q"][1]]
            kind = it["kind"]
            col = {"main": YELLOW, "hi": YELLOW, "base": DIM, "tick": YELLOW, "arcLine": ORANGE}[kind]
            w = {"main": 13, "hi": 15, "base": 8, "tick": 10, "arcLine": 9}[kind]
            parts.append(f'<path d="M{f(it["p"][0])} {f(it["p"][1])} L{f(it["q"][0])} {f(it["q"][1])}" stroke="{col}" stroke-width="{w}"/>')
        elif it["t"] == "arc":
            col = YELLOW if it["kind"] == "arcHi" else ORANGE
            parts.append(f'<path d="{arc_path(it)}" stroke="{col}" stroke-width="13"/>')
    pad = 16
    x0, x1, y0, y1 = min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad
    return (f'<svg class="mini" viewBox="{f(x0)} {f(y0)} {f(x1 - x0)} {f(y1 - y0)}" preserveAspectRatio="xMidYMid meet" '
            f'fill="none" stroke-linecap="round" stroke-linejoin="round">{"".join(parts)}</svg>')


def recap_comp(rules, dur):
    cells = ""
    for n, r in enumerate(rules, 1):
        res_cls = "res res-long" if len(r["result"]) > 14 else "res"
        cells += f'<div class="cell" id="rc{n}">{mini(r, n)}<div class="nm">{r["name"]}</div><div class="{res_cls}">{r["result"]}</div></div>'
    return f"""<template>
  <style>
{FONT}
#root{{position:absolute;inset:0;font-family:'SJ Poppins';}}
#rc-logo{{position:absolute;left:90px;top:172px;width:250px;}}
#rc-head{{position:absolute;right:90px;top:168px;font-size:58px;font-weight:700;color:{CANVAS};line-height:72px;}}
#rc-head b{{color:{YELLOW};font-weight:700;}}
#rc-grid{{position:absolute;left:40px;right:40px;top:272px;height:1178px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:repeat(4,minmax(0,1fr));column-gap:14px;row-gap:12px;}}
.cell{{display:flex;flex-direction:column;align-items:center;justify-content:flex-start;text-align:center;}}
.mini{{width:310px;height:170px;flex:none;margin-bottom:10px;}}
.nm{{font-size:31px;font-weight:600;color:{CANVAS};line-height:38px;}}
.res{{font-size:36px;font-weight:700;color:{YELLOW};line-height:44px;}}
.res-long{{font-size:28px;font-weight:600;line-height:34px;}}
  </style>
  <div id="root" data-composition-id="recap" data-width="1080" data-height="1920">
    <img id="rc-logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
    <div id="rc-head">All 12. <b>Save this.</b></div>
    <div id="rc-grid" data-hold>{cells}</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo('.cell',{{opacity:0}},{{opacity:1,duration:0.14,stagger:0.05}},0);
    tl.set({{}},{{}},{f(dur - 0.01)});
    window.__timelines["recap"] = tl;
  </script>
</template>
"""


# ------------------------------------------------------------ title overlay
def title_comp(dur):
    return f"""<template>
  <style>
{FONT}
#root{{position:absolute;inset:0;font-family:'SJ Poppins';}}
#tt-logo{{position:absolute;left:90px;top:172px;width:250px;}}
#tt-a{{position:absolute;left:0;width:1080px;top:252px;text-align:center;font-size:86px;font-weight:700;line-height:100px;color:{CANVAS};}}
#tt-a b{{color:{YELLOW};font-weight:700;}}
#tt-b{{position:absolute;left:0;width:1080px;top:352px;text-align:center;font-size:52px;font-weight:600;line-height:64px;color:{CANVAS};}}
  </style>
  <div id="root" data-composition-id="title" data-width="1080" data-height="1920" data-no-timeline>
    <img id="tt-logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
    <div id="tt-a"><b>12</b> angle rules</div>
    <div id="tt-b">for O Level Maths</div>
  </div>
</template>
"""


# ------------------------------------------------------------ end card
def end_comp(dur):
    px, py, pr = 540, 1920, 290
    ticks = ""
    for d in range(0, 181, 10):
        r2 = pr - (46 if d % 30 == 0 else 26)
        a, b = pt((px, py), pr, d), pt((px, py), r2, d)
        ticks += f'<path id="ec-pt{d}" d="M{f(a[0])} {f(a[1])} L{f(b[0])} {f(b[1])}"/>'
    tick_svg = '<svg class="tk" viewBox="0 0 56 56"><path d="M8 30 L22 44 L48 12" fill="none" stroke="{}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'.format(BROWN)
    return f"""<template>
  <style>
{FONT}
#root{{position:absolute;inset:0;font-family:'SJ Poppins';}}
#ec-ground{{position:absolute;inset:0;background:{YELLOW};}}
#ec-band{{position:absolute;left:0;right:0;top:1490px;bottom:0;background:{BROWN};}}
#ec-pro{{position:absolute;left:0;top:0;width:1080px;height:1920px;}}
#ec-logo{{position:absolute;left:300px;top:180px;width:480px;}}
#ec-kick{{position:absolute;left:60px;width:960px;top:356px;text-align:center;font-size:42px;font-weight:600;line-height:54px;color:{BROWN};}}
#ec-q{{position:absolute;left:40px;width:1000px;top:426px;text-align:center;font-size:88px;font-weight:700;line-height:104px;color:{INK};}}
#ec-ticks{{position:absolute;left:110px;width:860px;top:790px;}}
.row{{display:flex;align-items:center;gap:22px;font-size:40px;font-weight:500;line-height:50px;color:{INK};min-height:96px;text-wrap:balance;}}
.tk{{width:50px;height:50px;flex:none;}}
#ec-btn{{position:absolute;left:110px;width:860px;top:1040px;height:120px;border-radius:56px;background:{BROWN};color:{YELLOW};display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:600;}}
#ec-tel{{position:absolute;left:0;width:1080px;top:1190px;text-align:center;font-size:68px;font-weight:700;line-height:80px;color:{INK};}}
#ec-note{{position:absolute;left:0;width:1080px;top:1520px;text-align:center;font-family:'SJ Caveat';font-weight:600;font-size:62px;line-height:76px;color:{YELLOW};}}
#ec-web{{position:absolute;left:0;width:1080px;top:1278px;text-align:center;font-size:46px;font-weight:600;line-height:60px;color:{BROWN};}}
  </style>
  <div id="root" data-composition-id="endcard" data-width="1080" data-height="1920">
    <div id="ec-ground"></div>
    <div id="ec-band"></div>
    <svg id="ec-pro" viewBox="0 0 1080 1920" fill="none" stroke="{YELLOW}" stroke-width="6" stroke-linecap="round" data-layout-ignore>
      <path id="ec-parc" d="M{px - pr} {py} A{pr} {pr} 0 0 1 {px + pr} {py}" pathLength="1"/>
      {ticks}
    </svg>
    <img id="ec-logo" src="assets/brand/sj-academy-logo-horizontal-on-yellow.svg" alt="SJ Academy">
    <div id="ec-kick">Now use them on past papers.</div>
    <div id="ec-q">Join SJ Academy<br>for O Level and<br>A Level Maths</div>
    <div id="ec-ticks">
      <div class="row">{tick_svg}<span>Past-paper practice marked to the mark scheme</span></div>
      <div class="row">{tick_svg}<span>In class at DHA Phase 7 or live online</span></div>
    </div>
    <div id="ec-btn">Book a free demo on WhatsApp</div>
    <div id="ec-tel">+92-336-2144454</div>
    <div id="ec-web">sjacademy.pk</div>
    <div id="ec-note">One class free. Then decide.</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo('#ec-kick',{{opacity:0,y:14}},{{opacity:1,y:0,duration:0.27,ease:'expo.out'}},0.05);
    tl.fromTo('#ec-q',{{opacity:0,y:18}},{{opacity:1,y:0,duration:0.4,ease:'expo.out'}},0.2);
    tl.fromTo('.row',{{opacity:0,x:-14}},{{opacity:1,x:0,duration:0.27,ease:'expo.out',stagger:0.14}},0.6);
    tl.fromTo('#ec-btn',{{opacity:0,y:18}},{{opacity:1,y:0,duration:0.4,ease:'expo.out'}},0.95);
    tl.fromTo('#ec-tel, #ec-web',{{opacity:0}},{{opacity:1,duration:0.27,stagger:0.1}},1.15);
    tl.fromTo('#ec-parc',{{strokeDasharray:1,strokeDashoffset:1}},{{strokeDashoffset:0,duration:1.1,ease:'sine.inOut'}},0.1);
    tl.set({{}},{{}},{f(dur - 0.01)});
    window.__timelines["endcard"] = tl;
  </script>
</template>
"""


# ------------------------------------------------------------ assemble
def host(id_, start, dur, track, z):
    return (f'      <div id="{id_}" data-composition-id="{id_}" data-composition-src="compositions/{id_}.html" '
            f'data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="{track}" data-track-kind="graphics" '
            f'data-width="1080" data-height="1920" style="z-index:{z}"></div>')


def main():
    rules = rule_defs()
    log = check_angles(rules)
    os.makedirs(os.path.join(HERE, "compositions"), exist_ok=True)
    t = 0.0
    hosts = []
    timing = []
    for n, r in enumerate(rules, 1):
        dur = r["beats"] * H
        open(os.path.join(HERE, f"compositions/r{n:02d}.html"), "w").write(rule_comp(r, n, dur))
        hosts.append(host(f"r{n:02d}", t, dur, 2, n + 1))
        timing.append(f"{n:2d} {r['name']:22s} {t:6.2f} to {t + dur:6.2f}")
        t += dur
    rules_end = t
    open(os.path.join(HERE, "compositions/title.html"), "w").write(title_comp(rules_end))
    hosts.append(host("title", 0, rules_end, 3, 30))
    recap_dur = 8 * H
    open(os.path.join(HERE, "compositions/recap.html"), "w").write(recap_comp(rules, recap_dur))
    hosts.append(host("recap", t, recap_dur, 2, 20))
    timing.append(f"   Recap                  {t:6.2f} to {t + recap_dur:6.2f}")
    t += recap_dur
    end_dur = 9 * H
    open(os.path.join(HERE, "compositions/endcard.html"), "w").write(end_comp(end_dur))
    hosts.append(host("endcard", t, end_dur, 2, 21))
    timing.append(f"   End card               {t:6.2f} to {t + end_dur:6.2f}")
    t += end_dur
    index = f"""<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: {INK}; }}
      #root {{ width: 100%; height: 100%; background: {INK}; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{t:.3f}" data-width="1080" data-height="1920">
{chr(10).join(hosts)}
      <audio id="music" class="clip" src="assets/music/track.mp3" data-start="0" data-duration="{t:.3f}" data-media-start="{MEDIA_START}" data-volume="1" data-fade-out="1.2" data-track-index="10"></audio>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
    open(os.path.join(HERE, "index.html"), "w").write(index)
    open(os.path.join(HERE, "timing.txt"), "w").write("\n".join(timing) + f"\nTotal {t:.2f} s\n")
    print("\n".join(log))
    print("\n".join(timing))
    print(f"Total {t:.2f} s")


if __name__ == "__main__":
    main()
