# Builds the "12 angle rules" reel (v2). Writes index.html, compositions/*.html, timing.txt and sync-events.json.
# Run: python3 build.py
#
# Everything is scheduled in beats of the music, never in seconds. One rule is an 8-beat cycle: the shape
# draws over the first beats, the angles land on the next hits, the sum resolves, and the cut hits the downbeat.
# check_angles() re-measures each drawn angle from the coordinates and stops the build if one is off.
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
INK, CANVAS, DIM, YELLOW, ORANGE, BROWN = "#151515", "#F7F5EF", "#D9D4C7", "#FCE004", "#FE6100", "#453516"

BPM = 127.995        # fitted to the kick attacks across the 144 beats used
BEAT = 60 / BPM
MEDIA_START = 75.626 # the first kick of the drop: beat 0 of the reel. The level steps down exactly on beat 128


def bt(b):
    return b * BEAT


FONT = """@font-face{font-family:'SJ Poppins';font-weight:500;src:url('assets/brand/Poppins-Medium.ttf')}
@font-face{font-family:'SJ Poppins';font-weight:600;src:url('assets/brand/Poppins-SemiBold.ttf')}
@font-face{font-family:'SJ Poppins';font-weight:700;src:url('assets/brand/Poppins-Bold.ttf')}
@font-face{font-family:'SJ Caveat';font-weight:600;src:url('assets/brand/Caveat-600.woff2')}"""


# ------------------------------------------------------------ geometry
def pt(c, r, deg):
    return (c[0] + r * math.cos(math.radians(deg)), c[1] - r * math.sin(math.radians(deg)))


def L(p, q, kind="main"):
    return dict(t="line", p=p, q=q, kind=kind)


def A(c, a1, a2, label, r=70, lr=None, hi=False):
    return dict(t="arc", c=c, a1=a1, a2=a2, r=r, label=label, lr=lr or r + 58, hi=hi, value=a2 - a1)


def tick(p, q):
    m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = math.hypot(dx, dy)
    ux, uy = -dy / n * 20, dx / n * 20
    return L((m[0] - ux, m[1] - uy), (m[0] + ux, m[1] + uy), "tick")


def arrowhead(x, y):
    return dict(t="head", x=x, y=y)


def parallel_base():
    top, bottom = 640.0, 960.0
    B = (448.0, bottom)
    AA = (B[0] + (bottom - top) / math.tan(math.radians(60)), top)
    t_top, t_bottom = pt(AA, 80, 60), pt(B, 70, 240)
    base = [L((40, top), (1040, top), "base"), L((40, bottom), (1040, bottom), "base"), L(t_bottom, t_top, "base")]
    return AA, B, t_top, t_bottom, base, [arrowhead(205, top), arrowhead(205, bottom)], top, bottom


def rule_defs():
    r = []
    # stroke: (first stroke starts, beats per stroke). arcs: landing beats. eq: (text, beat[, is_result])

    O = (540.0, 960.0)
    r.append(dict(key="straight", beats=8, name="Straight line", result="180°", kind="sum", target=180,
        cap=["Angles on a straight line add up to ", ("180°",)], hl=5,
        items=[L((40, O[1]), (1040, O[1])), L(O, pt(O, 480, 50)), A(O, 50, 180, "130°"), A(O, 0, 50, "50°")],
        stroke=(0, 1), arcs=[3, 4], eq=[("130°", 3), ("+ 50°", 4), ("= 180°", 5, True)]))

    O = (540.0, 790.0)
    r.append(dict(key="point", beats=8, name="At a point", result="360°", kind="sum", target=360,
        cap=["Angles at a point add up to ", ("360°",)], hl=5,
        items=[L(O, pt(O, 245, 90)), L(O, pt(O, 245, 230)), L(O, pt(O, 245, 330)),
               A(O, 90, 230, "140°"), A(O, 230, 330, "100°"), A(O, 330, 450, "120°")],
        stroke=(0, 1), arcs=[3, 3.5, 4], eq=[("140°", 3), ("+ 100°", 3.5), ("+ 120°", 4), ("= 360°", 5, True)]))

    O = (540.0, 790.0)
    r.append(dict(key="vertical", beats=8, name="Vertically opposite", result="equal", kind="equal",
        cap=["Vertically opposite angles are ", ("equal",)], hl=5,
        items=[L(pt(O, 440, 215), pt(O, 440, 35)), L(pt(O, 440, 145), pt(O, 440, 325)),
               A(O, 145, 215, "70°", r=92), A(O, -35, 35, "70°", r=92)],
        stroke=(0, 1.5), arcs=[3, 4], eq=[("70°", 3), ("= 70°", 4, True)]))

    AA, B, tt, tb, base, heads, top, bottom = parallel_base()
    r.append(dict(key="alternate", beats=8, name="Alternate", result="equal", kind="equal",
        cap=["Alternate angles on parallel lines are ", ("equal",)], hl=5, note="Z shape",
        items=base + heads + [L((AA[0] - 340, top), AA, "hi"), L(AA, B, "hi"), L(B, (B[0] + 340, bottom), "hi"),
                              A(AA, 180, 240, "60°", r=66, lr=134), A(B, 0, 60, "60°", r=66, lr=134)],
        stroke=(1.5, 0.5), arcs=[3, 4], eq=[("60°", 3), ("= 60°", 4, True)]))

    AA, B, tt, tb, base, heads, top, bottom = parallel_base()
    r.append(dict(key="corresponding", beats=8, name="Corresponding", result="equal", kind="equal",
        cap=["Corresponding angles on parallel lines are ", ("equal",)], hl=5, note="F shape",
        items=base + heads + [L(B, tt, "hi"), L(AA, (AA[0] + 300, top), "hi"), L(B, (B[0] + 300, bottom), "hi"),
                              A(AA, 0, 60, "60°", r=66, lr=134), A(B, 0, 60, "60°", r=66, lr=134)],
        stroke=(1.5, 0.5), arcs=[3, 4], eq=[("60°", 3), ("= 60°", 4, True)]))

    AA, B, tt, tb, base, heads, top, bottom = parallel_base()
    r.append(dict(key="cointerior", beats=8, name="Co-interior", result="180°", kind="sum", target=180,
        cap=["Co-interior angles on parallel lines add up to ", ("180°",)], hl=5, note="C shape",
        items=base + heads + [L((AA[0] + 300, top), AA, "hi"), L(AA, B, "hi"), L(B, (B[0] + 300, bottom), "hi"),
                              A(AA, 240, 360, "120°", r=66, lr=134), A(B, 0, 60, "60°", r=66, lr=134)],
        stroke=(1.5, 0.5), arcs=[3, 4], eq=[("120°", 3), ("+ 60°", 4), ("= 180°", 5, True)]))

    a, b = (190.0, 975.0), (890.0, 975.0)
    h = (b[0] - a[0]) / (1 / math.tan(math.radians(60)) + 1 / math.tan(math.radians(45)))
    c = (a[0] + h / math.tan(math.radians(60)), a[1] - h)
    r.append(dict(key="triangle", beats=8, name="Triangle", result="180°", kind="sum", target=180,
        cap=["Angles in a triangle add up to ", ("180°",)], hl=5,
        items=[L(a, b), L(b, c), L(c, a), A(a, 0, 60, "60°", lr=124), A(b, 135, 180, "45°", lr=160), A(c, 240, 315, "75°", lr=130)],
        stroke=(0, 1), arcs=[3, 3.5, 4], eq=[("60°", 3), ("+ 45°", 3.5), ("+ 75°", 4), ("= 180°", 5, True)]))

    hh = 420.0
    half = hh / math.tan(math.radians(70))
    a, b, c = (540 - half, 975.0), (540 + half, 975.0), (540.0, 975 - hh)
    r.append(dict(key="isosceles", beats=8, name="Isosceles", result="base angles equal", kind="equal",
        cap=["Base angles of an isosceles triangle are ", ("equal",)], hl=5,
        items=[L(a, b), L(b, c), L(c, a), tick(a, c), tick(c, b), A(a, 0, 70, "70°", r=54, lr=108), A(b, 110, 180, "70°", r=54, lr=108)],
        stroke=(0, 0.5), ticks=[2, 2.5], arcs=[3, 4], eq=[("70°", 3), ("= 70°", 4, True)]))

    a, b = (150.0, 975.0), (650.0, 975.0)
    h = (b[0] - a[0]) / (1 / math.tan(math.radians(50)) + 1 / math.tan(math.radians(60)))
    c = (a[0] + h / math.tan(math.radians(50)), a[1] - h)
    r.append(dict(key="exterior", beats=12, name="Triangle exterior", result="sum of 2 opposite interiors", kind="exterior",
        cap=["The exterior angle of a triangle equals the ", ("sum",), " of the two opposite interior angles"], hl=7,
        items=[L(a, b), L(b, c), L(c, a), L(b, (1040.0, 975.0), "ext"),
               A(a, 0, 50, "50°", lr=128), A(c, 230, 300, "70°", lr=128), A(b, 0, 120, "120°", hi=True)],
        stroke=(0, 1), ext=(3, 4), arcs=[5, 6, 7], eq=[("50°", 5), ("+ 70°", 6), ("= 120°", 7, True)]))

    a, b = (190.0, 975.0), (830.0, 975.0)
    hgt = 420.0
    d = (a[0] + hgt / math.tan(math.radians(70)), 975 - hgt)
    c = (b[0] + hgt / math.tan(math.radians(80)), 975 - hgt)
    r.append(dict(key="quad", beats=8, name="Quadrilateral", result="360°", kind="sum", target=360,
        cap=["Angles in a quadrilateral add up to ", ("360°",)], hl=5,
        items=[L(a, b), L(b, c), L(c, d), L(d, a), A(a, 0, 70, "70°", lr=126), A(b, 80, 180, "100°", lr=126),
               A(c, 180, 260, "80°", lr=126), A(d, 250, 360, "110°", lr=126)],
        stroke=(0, 0.75), arcs=[3, 3.5, 4, 4.5], eq=[("70°", 3), ("+ 100°", 3.5), ("+ 80°", 4), ("+ 110°", 4.5), ("= 360°", 5, True)]))

    O = (540.0, 785.0)
    R = 185
    V = [pt(O, R, 90 + 72 * i) for i in range(5)]
    items = [L(V[i], V[(i + 1) % 5]) for i in range(5)]
    arcs = []
    for i in range(5):
        p, q = V[i], V[(i + 1) % 5]
        d1 = math.degrees(math.atan2(-(q[1] - p[1]), q[0] - p[0]))
        items.append(L(q, pt(q, 92, d1), "ext"))
        arcs.append(A(q, d1, d1 + 72, "72°", r=48, lr=100))
    r.append(dict(key="polyext", beats=12, name="Polygon exterior", result="360°", kind="sum", target=360,
        cap=["The exterior angles of a convex polygon add up to ", ("360°",)], hl=8,
        items=items + arcs, stroke=(0, 0.5), ext=(2.5, 3), arcs=[3, 4, 5, 6, 7],
        eq=[("Regular pentagon:", 7), ("5 × 72°", 7), ("= 360°", 8, True)]))

    O = (540.0, 780.0)
    R = 235
    V = [pt(O, R, 60 * i) for i in range(6)]
    items = [L(V[(3 + i) % 6], V[(4 + i) % 6]) for i in range(6)]
    start = V[3]
    items += [L(start, V[5], "diag"), L(start, V[0], "diag"), L(start, V[1], "diag")]
    tris = [(V[3], V[4], V[5]), (V[3], V[5], V[0]), (V[3], V[0], V[1]), (V[3], V[1], V[2])]
    for n, tr in enumerate(tris):
        items.append(dict(t="num", s=str(n + 1), x=sum(p[0] for p in tr) / 3, y=sum(p[1] for p in tr) / 3))
    r.append(dict(key="polyint", beats=16, name="Polygon interior", result="(n − 2) × 180°", kind="poly",
        cap=["Interior angles of an n-sided polygon add up to ", ("(n − 2) × 180°",)], hl=10, note="Hexagon",
        items=items, stroke=(0, 0.5), diag=[4, 4.5, 5], nums=[6, 6.5, 7, 7.5], arcs=[],
        eq=[("n = 6:", 8), ("(6 − 2)", 8.5), ("× 180°", 9), ("= 720°", 10, True)]))
    return r


def check_angles(rules):
    """Second solve: re-measure labelled angles from the drawn coordinates and check each rule's total."""
    log = []
    for r in rules:
        arcs = [i for i in r["items"] if i["t"] == "arc"]
        vals = [a["value"] for a in arcs]
        for a in arcs:
            assert str(int(round(a["value"]))) + "°" == a["label"], (r["key"], a["label"], a["value"])
        if r["kind"] == "sum":
            assert round(sum(vals)) == r["target"], (r["key"], vals)
        if r["kind"] == "equal":
            assert len({round(v) for v in vals}) == 1, (r["key"], vals)
        if r["kind"] == "exterior":
            assert round(vals[0] + vals[1]) == round(vals[2]), (r["key"], vals)
        log.append(f"{r['key']}: {[round(v) for v in vals]}")

    def corner(p, q, s):
        a1 = math.atan2(p[1] - q[1], p[0] - q[0])
        a2 = math.atan2(s[1] - q[1], s[0] - q[0])
        d = abs(math.degrees(a1 - a2)) % 360
        return min(d, 360 - d)

    get = lambda k: next(r for r in rules if r["key"] == k)["items"]
    i = get("triangle"); a, b, c = i[0]["p"], i[0]["q"], i[1]["q"]
    assert abs(corner(c, a, b) - 60) < 1e-6 and abs(corner(a, b, c) - 45) < 1e-6 and abs(corner(a, c, b) - 75) < 1e-6
    i = get("isosceles"); a, b, c = i[0]["p"], i[0]["q"], i[1]["q"]
    assert abs(corner(c, a, b) - 70) < 1e-6 and abs(corner(a, b, c) - 70) < 1e-6
    i = get("exterior"); a, b, c = i[0]["p"], i[0]["q"], i[1]["q"]
    assert abs(corner(c, a, b) - 50) < 1e-6 and abs(corner(a, c, b) - 70) < 1e-6 and abs(corner(a, b, c) - 60) < 1e-6
    i = get("quad"); a, b, c, d = i[0]["p"], i[0]["q"], i[1]["q"], i[2]["q"]
    cs = [corner(d, a, b), corner(a, b, c), corner(b, c, d), corner(c, d, a)]
    assert all(abs(x - y) < 1e-6 for x, y in zip(cs, [70, 100, 80, 110])), cs
    log.append("corners measured: triangle 60 45 75, isosceles 70 70, exterior 50 70 60, quad 70 100 80 110")
    assert (6 - 2) * 180 == 720 and 5 * 72 == 360
    return log


# ------------------------------------------------------------ drawing
def f(n):
    return f"{n:.2f}"


def arc_d(c, a1, a2, r):
    s, e = pt(c, r, a1), pt(c, r, a2)
    large = 1 if a2 - a1 > 180 else 0
    return f"M{f(s[0])} {f(s[1])} A{f(r)} {f(r)} 0 {large} 0 {f(e[0])} {f(e[1])}"


STROKE = {"main": (YELLOW, 6), "hi": (YELLOW, 6.5), "base": (DIM, 2.4), "ext": (DIM, 3), "tick": (YELLOW, 5), "diag": (ORANGE, 4)}
TX, TY, SCALE = -135, -351.25, 1.25   # raw diagram coordinates to the frame


def split_words(text, prefix, start):
    out, n = "", start
    for w in text.split(" "):
        if w:
            out += f'<span id="{prefix}-w{n}" class="w">{w}</span> '
            n += 1
    return out, n


def rule_comp(r, n, dur, events, abs_start):
    p = f"r{n:02d}"
    beats = r["beats"]
    svg, wedges, js = [], [], []
    lines, arcs, nums, ids = [], [], [], 0

    for it in r["items"]:
        id_ = f"{p}-i{ids}"
        ids += 1
        if it["t"] == "line":
            col, w = STROKE[it["kind"]]
            svg.append(f'<path id="{id_}" class="ln" d="M{f(it["p"][0])} {f(it["p"][1])} L{f(it["q"][0])} {f(it["q"][1])}" stroke="{col}" stroke-width="{w}" pathLength="1"/>')
            lines.append((id_, it))
        elif it["t"] == "head":
            x, y = it["x"], it["y"]
            svg.append(f'<path id="{id_}" class="hd" d="M{x - 15} {y - 13} L{x + 9} {y} L{x - 15} {y + 13} Z" fill="{DIM}"/>')
            lines.append((id_, it))
        elif it["t"] == "arc":
            col = YELLOW if it["hi"] else ORANGE
            wedges.append(f'<path id="{id_}f" class="wd" d="{arc_d(it["c"], it["a1"], it["a2"], it["r"] / 2)}" stroke="{col}" stroke-width="{it["r"]}" pathLength="1"/>')
            svg.append(f'<path id="{id_}" class="ar" d="{arc_d(it["c"], it["a1"], it["a2"], it["r"])}" stroke="{col}" stroke-width="5" pathLength="1"/>')
            lx, ly = pt(it["c"], it["lr"], (it["a1"] + it["a2"]) / 2)
            svg.append(f'<text id="{id_}t" class="lb" x="{f(lx)}" y="{f(ly)}">{it["label"]}</text>')
            arcs.append((id_, it))
        elif it["t"] == "num":
            svg.append(f'<text id="{id_}" class="num" x="{f(it["x"])}" y="{f(it["y"])}">{it["s"]}</text>')
            nums.append(id_)

    def hit(kind, b):
        events.append(dict(rule=n, kind=kind, beat_in_rule=b, t=round(abs_start + bt(b), 3)))

    # caption, word by word
    cap_html, wn = "", 0
    hl_id = None
    for part in r["cap"]:
        if isinstance(part, tuple):
            hl_id = f"{p}-hl"
            cap_html += f'<span id="{p}-w{wn}" class="w hw"><i id="{hl_id}b" class="band"></i><span id="{hl_id}" class="ht">{part[0]}</span></span> '
            wn += 1
        else:
            h, wn = split_words(part, p, wn)
            cap_html += h

    js.append(f"gsap.set('#{p} .ln, #{p} .ar, #{p} .wd',{{strokeDasharray:1,strokeDashoffset:1,opacity:0}});")
    js.append(f"gsap.set('#{p} .lb, #{p} .num, #{p} .hd',{{opacity:0}});")
    js.append(f"gsap.set('#{hl_id}b',{{scaleX:0}});")
    if n > 1:
        js.append(f"tl.fromTo('#{p}-cap .w',{{opacity:0,filter:'blur(6px)'}},{{opacity:1,filter:'blur(0px)',duration:0.13,stagger:0.05}},0);")

    def draw(id_, s, e, ease="power2.inOut"):
        js.append(f"tl.set('#{id_}',{{opacity:1}},{f(bt(s))});tl.to('#{id_}',{{strokeDashoffset:0,duration:{f(bt(e - s))},ease:'{ease}'}},{f(bt(s))});")

    # hairlines lay in on the first beat
    for id_, it in lines:
        if it.get("kind") == "base":
            draw(id_, 0, 1)
        if it["t"] == "head":
            js.append(f"tl.to('#{id_}',{{opacity:1,duration:0.13}},{f(bt(1))});")

    # the main shape, stroke by stroke, each landing on the grid
    s0, per = r["stroke"]
    mains = [x for x in lines if x[1].get("kind") in ("main", "hi")]
    t = s0
    js.append(f"tl.set('#{p}-pen',{{opacity:1}},{f(bt(t))});")
    for id_, it in mains:
        draw(id_, t, t + per)
        js.append(f"tl.fromTo('#{p}-pen',{{attr:{{cx:{f(it['p'][0])},cy:{f(it['p'][1])}}}}},{{attr:{{cx:{f(it['q'][0])},cy:{f(it['q'][1])}}},duration:{f(bt(per) - 0.01)},ease:'power2.inOut',immediateRender:false}},{f(bt(t))});")
        t += per
        hit("stroke", t)
    js.append(f"tl.set('#{p}-pen',{{opacity:0}},{f(bt(t))});")

    if r.get("ext"):
        s, e = r["ext"]
        for id_, it in lines:
            if it.get("kind") == "ext":
                draw(id_, s, e)
        hit("stroke", e)
    for key, kind in (("ticks", "tick"), ("diag", "diag")):
        if r.get(key):
            for (id_, it), b in zip([x for x in lines if x[1].get("kind") == kind], r[key]):
                draw(id_, b - 0.5, b)
                hit(kind, b)
    if r.get("nums"):
        for id_, b in zip(nums, r["nums"]):
            js.append(f"tl.fromTo('#{id_}',{{opacity:0,scale:0.5,transformOrigin:'50% 50%'}},{{opacity:1,scale:1,duration:0.2,ease:'back.out(1.7)'}},{f(bt(b))});")
            hit("number", b)

    # each angle sweeps open and lands on a hit: the wedge flashes and the arc is thick, then both settle
    for (id_, it), b in zip(arcs, r["arcs"]):
        sweep = 0.5
        js.append(f"tl.set('#{id_}, #{id_}f',{{opacity:1}},{f(bt(b - sweep))});")
        js.append(f"tl.to('#{id_}, #{id_}f',{{strokeDashoffset:0,duration:{f(bt(sweep))},ease:'power2.in'}},{f(bt(b - sweep))});")
        js.append(f"tl.fromTo('#{id_}',{{attr:{{'stroke-width':12}}}},{{attr:{{'stroke-width':5}},duration:{f(bt(1))},ease:'power2.out',immediateRender:false}},{f(bt(b))});")
        js.append(f"tl.fromTo('#{id_}f',{{opacity:0.75}},{{opacity:0.24,duration:{f(bt(1))},ease:'power2.out',immediateRender:false}},{f(bt(b))});")
        js.append(f"tl.fromTo('#{id_}t',{{opacity:0,scale:0.5,transformOrigin:'50% 50%'}},{{opacity:1,scale:1,duration:0.22,ease:'back.out(1.7)'}},{f(bt(b))});")
        hit("angle", b)

    # the sum builds term by term on the same hits
    eq_html = ""
    for i, term in enumerate(r["eq"]):
        res = len(term) > 2
        eq_html += f'<span id="{p}-e{i}" class="{"tm rs" if res else "tm"}">{term[0]}</span>'
        ease = "back.out(1.7)" if res else "expo.out"
        js.append(f"tl.fromTo('#{p}-e{i}',{{opacity:0,scale:{0.6 if res else 0.85},transformOrigin:'50% 60%'}},{{opacity:1,scale:1,duration:0.22,ease:'{ease}'}},{f(bt(term[1]))});")
        hit("sum-result" if res else "sum-term", term[1])

    # the highlighter marks the key word on a hit
    b = r["hl"]
    js.append(f"tl.fromTo('#{hl_id}b',{{scaleX:0}},{{scaleX:1,duration:{f(bt(0.5))},ease:'power3.out',immediateRender:false}},{f(bt(b))});")
    js.append(f"tl.fromTo('#{hl_id}',{{color:'{CANVAS}'}},{{color:'{INK}',duration:0.08,immediateRender:false}},{f(bt(b) + 0.03)});")
    hit("highlight", b)

    if r.get("note"):
        nb = 2 if r["key"] != "polyint" else 3
        js.append(f"tl.fromTo('#{p}-note',{{opacity:0,x:-14}},{{opacity:1,x:0,duration:0.27,ease:'expo.out'}},{f(bt(nb))});")

    # clean exit, finishing exactly on the next downbeat
    ex = bt(beats - 0.45)
    js.append(f"tl.to('#{p}-main',{{opacity:0,scale:1.035,duration:{f(bt(0.45) - 0.01)},ease:'power3.in',transformOrigin:'50% 40%'}},{f(ex)});")
    hit("cut", beats)

    note = f'<div id="{p}-note" class="note">{r["note"]}</div>' if r.get("note") else ""
    pen = f'<circle id="{p}-pen" r="9" cx="0" cy="0" fill="{CANVAS}" opacity="0"/>'
    return f"""<template>
  <style>
{FONT}
#root{{position:absolute;inset:0;font-family:'SJ Poppins';}}
#{p}-main{{position:absolute;inset:0;}}
#{p}-main svg{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible;}}
#{p} .ln{{fill:none;stroke-linecap:round;}}
#{p} .ar,#{p} .wd{{fill:none;stroke-linecap:butt;}}
#{p} .lb{{font-family:'SJ Poppins';font-weight:600;font-size:40px;fill:{CANVAS};text-anchor:middle;dominant-baseline:central;}}
#{p} .num{{font-family:'SJ Poppins';font-weight:600;font-size:38px;fill:{CANVAS};text-anchor:middle;dominant-baseline:central;}}
#{p}-eq{{position:absolute;left:30px;width:1020px;top:1022px;height:84px;display:flex;justify-content:center;align-items:center;gap:16px;font-size:50px;font-weight:600;color:{CANVAS};white-space:nowrap;}}
#{p} .rs{{font-weight:700;color:{YELLOW};}}
#{p}-cap{{position:absolute;left:100px;width:880px;top:1138px;text-align:center;font-size:52px;line-height:1.26;font-weight:600;color:{CANVAS};}}
#{p} .w{{display:inline-block;}}
#{p} .hw{{position:relative;white-space:nowrap;padding:0 12px;}}
#{p} .band{{position:absolute;inset:6px 0 2px 0;background:{YELLOW};border-radius:6px;transform-origin:0% 50%;}}
#{p} .ht{{position:relative;}}
#{p}-note{{position:absolute;left:60px;top:352px;font-family:'SJ Caveat';font-weight:600;font-size:66px;color:{YELLOW};line-height:80px;padding-right:20px;}}
#{p}-count{{position:absolute;right:90px;top:158px;font-size:48px;font-weight:700;color:{YELLOW};line-height:64px;}}
#{p}-count small{{font-size:30px;font-weight:500;color:{DIM};}}
  </style>
  <div id="root" data-composition-id="{p}" data-width="1080" data-height="1920">
    <div id="{p}" data-layout-allow-overlap data-hold>
      <div id="{p}-count">{n}<small> / 12</small></div>
      <div id="{p}-main">
        <svg viewBox="0 0 1080 1920" data-layout-allow-overflow><g transform="translate({TX} {TY}) scale({SCALE})">{''.join(wedges)}{''.join(svg)}{pen}</g></svg>
        {note}
        <div id="{p}-eq">{eq_html}</div>
        <div id="{p}-cap">{cap_html}</div>
      </div>
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


# ------------------------------------------------------------ background and header, full length
def bg_comp(total_beats, dur):
    pulses = "".join(f"tl.fromTo('#bg-lines',{{opacity:0.5}},{{opacity:0.26,duration:{f(bt(2))},ease:'power2.out',immediateRender:false}},{f(bt(b))});" for b in range(0, total_beats, 4))
    return f"""<template>
  <style>
#root{{position:absolute;inset:0;}}
#bg-g{{position:absolute;inset:0;background:{INK};}}
#bg-lines{{position:absolute;left:0;top:-240px;width:1080px;height:2400px;opacity:0.26;
 background-image:linear-gradient(rgba(252,224,4,.16) 2px,transparent 2px),linear-gradient(90deg,rgba(252,224,4,.16) 2px,transparent 2px),
 linear-gradient(rgba(247,245,239,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(247,245,239,.06) 1px,transparent 1px);
 background-size:240px 240px,240px 240px,60px 60px,60px 60px;}}
#bg-v{{position:absolute;inset:0;background:radial-gradient(ellipse 72% 52% at 50% 42%,rgba(21,21,21,0) 40%,rgba(21,21,21,.92) 100%);}}
  </style>
  <div id="root" data-composition-id="bg" data-width="1080" data-height="1920">
    <div id="bg-g"></div>
    <div id="bg-lines" data-layout-ignore></div>
    <div id="bg-v"></div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo('#bg-lines',{{y:0}},{{y:-240,duration:{f(dur - 0.01)},ease:'none'}},0);
    {pulses}
    window.__timelines["bg"] = tl;
  </script>
</template>
"""


def chrome_comp(rules, dur, first_dur):
    segs, js, b = "", [], 0
    for i, r in enumerate(rules):
        segs += f'<i id="ch-s{i}" class="sg"><b id="ch-f{i}"></b></i>'
        js.append(f"tl.fromTo('#ch-f{i}',{{scaleX:0,transformOrigin:'0% 50%'}},{{scaleX:1,duration:{f(bt(r['beats']) - 0.02)},ease:'none'}},{f(bt(b))});")
        b += r["beats"]
    return f"""<template>
  <style>
{FONT}
#root{{position:absolute;inset:0;font-family:'SJ Poppins';}}
#ch-logo{{position:absolute;left:90px;top:160px;width:240px;}}
#ch-bar{{position:absolute;left:90px;width:900px;top:232px;height:6px;display:flex;gap:6px;}}
.sg{{flex:1;height:6px;background:rgba(247,245,239,.16);border-radius:3px;overflow:hidden;display:block;}}
.sg b{{display:block;width:100%;height:100%;background:{YELLOW};}}
#ch-big{{position:absolute;left:0;width:1080px;top:252px;text-align:center;}}
#ch-big1{{font-size:88px;font-weight:700;line-height:96px;color:{CANVAS};}}
#ch-big1 em{{font-style:normal;color:{YELLOW};}}
#ch-big2{{font-size:46px;font-weight:600;line-height:58px;color:{CANVAS};}}
#ch-small{{position:absolute;left:0;width:1080px;top:256px;text-align:center;font-size:34px;font-weight:500;line-height:44px;color:{DIM};}}
#ch-small em{{font-style:normal;color:{YELLOW};font-weight:600;}}
  </style>
  <div id="root" data-composition-id="chrome" data-width="1080" data-height="1920">
    <img id="ch-logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
    <div id="ch-bar">{segs}</div>
    <div id="ch-big"><div id="ch-big1"><em>12</em> angle rules</div><div id="ch-big2">for O Level Maths</div></div>
    <div id="ch-small"><em>12</em> angle rules for O Level Maths</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    gsap.set('#ch-small',{{opacity:0}});
    {chr(10).join('    ' + j for j in js).strip()}
    tl.to('#ch-big',{{opacity:0,y:-20,duration:{f(bt(0.45) - 0.01)},ease:'power3.in'}},{f(first_dur - bt(0.45))});
    tl.to('#ch-small',{{opacity:1,duration:0.1}},{f(first_dur)});
    tl.set({{}},{{}},{f(dur - 0.01)});
    window.__timelines["chrome"] = tl;
  </script>
</template>
"""


# ------------------------------------------------------------ recap: 12 hits, then a hold to save
def mini(r):
    xs, ys, parts = [], [], []
    for it in r["items"]:
        if it["t"] == "line":
            xs += [it["p"][0], it["q"][0]]; ys += [it["p"][1], it["q"][1]]
            col = {"main": YELLOW, "hi": YELLOW, "base": DIM, "ext": DIM, "tick": YELLOW, "diag": ORANGE}[it["kind"]]
            w = {"main": 11, "hi": 12, "base": 5, "ext": 6, "tick": 8, "diag": 8}[it["kind"]]
            parts.append(f'<path d="M{f(it["p"][0])} {f(it["p"][1])} L{f(it["q"][0])} {f(it["q"][1])}" stroke="{col}" stroke-width="{w}"/>')
        elif it["t"] == "arc":
            col = YELLOW if it["hi"] else ORANGE
            parts.insert(0, f'<path d="{arc_d(it["c"], it["a1"], it["a2"], it["r"] * 0.65)}" stroke="{col}" stroke-opacity="0.55" stroke-width="{it["r"] * 1.3}"/>')
    pad = 12
    x0, x1, y0, y1 = min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad
    return (f'<svg class="mini" viewBox="{f(x0)} {f(y0)} {f(x1 - x0)} {f(y1 - y0)}" preserveAspectRatio="xMidYMid meet" '
            f'fill="none" stroke-linecap="butt" stroke-linejoin="round">{"".join(parts)}</svg>')


def recap_comp(rules, dur, events, abs_start):
    cells, js = "", []
    for n, r in enumerate(rules, 1):
        res_cls = "res res-long" if len(r["result"]) > 14 else "res"
        cells += f'<div class="cell" id="rc{n}">{mini(r)}<div class="nm">{r["name"]}</div><div class="{res_cls}">{r["result"]}</div></div>'
        b = 1 + (n - 1) * 0.5
        js.append(f"tl.fromTo('#rc{n}',{{opacity:0,scale:0.8}},{{opacity:1,scale:1,duration:0.2,ease:'back.out(1.5)'}},{f(bt(b))});")
        events.append(dict(rule="recap", kind="cell", beat_in_rule=b, t=round(abs_start + bt(b), 3)))
    events.append(dict(rule="recap", kind="headline", beat_in_rule=8, t=round(abs_start + bt(8), 3)))
    return f"""<template>
  <style>
{FONT}
#root{{position:absolute;inset:0;font-family:'SJ Poppins';}}
#rc-logo{{position:absolute;left:90px;top:160px;width:240px;}}
#rc-head{{position:absolute;left:0;width:1080px;top:232px;text-align:center;font-size:72px;font-weight:700;color:{CANVAS};line-height:90px;}}
#rc-save{{display:inline-block;color:{INK};background:{YELLOW};border-radius:8px;padding:0 14px;margin-left:18px;}}
#rc-grid{{position:absolute;left:40px;right:40px;top:344px;height:1130px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:repeat(4,minmax(0,1fr));column-gap:12px;row-gap:6px;}}
.cell{{display:flex;flex-direction:column;align-items:center;justify-content:flex-start;text-align:center;}}
.mini{{width:300px;height:150px;flex:none;margin-bottom:8px;}}
.nm{{font-size:30px;font-weight:600;color:{CANVAS};line-height:36px;}}
.res{{font-size:36px;font-weight:700;color:{YELLOW};line-height:42px;}}
.res-long{{font-size:28px;font-weight:600;line-height:33px;}}
  </style>
  <div id="root" data-composition-id="recap" data-width="1080" data-height="1920">
    <div id="rc-ground" style="position:absolute;inset:0;background:{INK};"></div>
    <img id="rc-logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
    <div id="rc-head">All 12.<span id="rc-save">Save this.</span></div>
    <div id="rc-grid" data-hold>{cells}</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    gsap.set('#rc-save',{{opacity:0}});
    {chr(10).join('    ' + j for j in js).strip()}
    tl.fromTo('#rc-save',{{opacity:0,scale:1.3,rotation:-5,transformOrigin:'50% 50%'}},{{opacity:1,scale:1,rotation:-2,duration:0.133,ease:'back.out(1.7)',immediateRender:false}},{f(bt(8))});
    tl.set({{}},{{}},{f(dur - 0.01)});
    window.__timelines["recap"] = tl;
  </script>
</template>
"""


# ------------------------------------------------------------ end card
def end_comp(dur, events, abs_start):
    px, py, pr = 540, 1920, 290
    ticks = ""
    for d in range(0, 181, 10):
        r2 = pr - (46 if d % 30 == 0 else 26)
        a, b = pt((px, py), pr, d), pt((px, py), r2, d)
        ticks += f'<path class="pt" d="M{f(a[0])} {f(a[1])} L{f(b[0])} {f(b[1])}"/>'
    tick_svg = lambda i: f'<svg class="tk" viewBox="0 0 56 56"><path id="ec-tk{i}" d="M8 30 L22 44 L48 12" fill="none" stroke="{BROWN}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" pathLength="1"/></svg>'
    for k, b in [("headline", 2), ("headline", 2.5), ("headline", 3), ("tick", 4), ("tick", 4.5), ("button", 5), ("phone", 6), ("website", 6.5)]:
        events.append(dict(rule="end", kind=k, beat_in_rule=b, t=round(abs_start + bt(b), 3)))
    return f"""<template>
  <style>
{FONT}
#root{{position:absolute;inset:0;font-family:'SJ Poppins';}}
#ec-ground{{position:absolute;inset:0;background:{YELLOW};}}
#ec-band{{position:absolute;left:0;right:0;top:1490px;bottom:0;background:{BROWN};}}
#ec-pro{{position:absolute;left:0;top:0;width:1080px;height:1920px;}}
#ec-logo{{position:absolute;left:300px;top:170px;width:480px;}}
#ec-kick{{position:absolute;left:60px;width:960px;top:340px;text-align:center;font-size:42px;font-weight:600;line-height:56px;color:{BROWN};}}
#ec-q{{position:absolute;left:30px;width:1020px;top:408px;text-align:center;font-size:92px;font-weight:700;line-height:106px;color:{INK};}}
#ec-q span{{display:block;}}
#ec-ticks{{position:absolute;left:110px;width:860px;top:750px;}}
.row{{display:flex;align-items:center;gap:22px;font-size:40px;font-weight:500;line-height:50px;color:{INK};min-height:108px;text-wrap:balance;}}
.tk{{width:52px;height:52px;flex:none;}}
#ec-btn{{position:absolute;left:100px;width:880px;top:980px;height:132px;border-radius:66px;background:{BROWN};color:{YELLOW};display:flex;align-items:center;justify-content:center;font-size:48px;font-weight:600;}}
#ec-tel{{position:absolute;left:0;width:1080px;top:1150px;text-align:center;font-size:76px;font-weight:700;line-height:96px;color:{INK};}}
#ec-web{{position:absolute;left:0;width:1080px;top:1250px;text-align:center;font-size:48px;font-weight:600;line-height:64px;color:{BROWN};}}
#ec-note{{position:absolute;left:0;width:1080px;top:1522px;text-align:center;font-family:'SJ Caveat';font-weight:600;font-size:62px;line-height:76px;color:{YELLOW};}}
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
    <div id="ec-q"><span id="ec-q1">Join SJ Academy</span><span id="ec-q2">for O Level and</span><span id="ec-q3">A Level Maths</span></div>
    <div id="ec-ticks">
      <div class="row" id="ec-r0">{tick_svg(0)}<span>Past-paper practice marked to the mark scheme</span></div>
      <div class="row" id="ec-r1">{tick_svg(1)}<span>In class at DHA Phase 7 or live online</span></div>
    </div>
    <div id="ec-btn">Book a free demo on WhatsApp</div>
    <div id="ec-tel">+92-336-2144454</div>
    <div id="ec-web">sjacademy.pk</div>
    <div id="ec-note">One class free. Then decide.</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    const pop=(s,b)=>tl.fromTo(s,{{opacity:0,y:26,filter:'blur(6px)'}},{{opacity:1,y:0,filter:'blur(0px)',duration:0.3,ease:'expo.out'}},b*{BEAT:.6f});
    gsap.set('#ec-parc',{{strokeDasharray:1,strokeDashoffset:1}});
    gsap.set('#ec-tk0, #ec-tk1',{{strokeDasharray:1,strokeDashoffset:1}});
    gsap.set('.pt',{{opacity:0}});
    tl.to('#ec-parc',{{strokeDashoffset:0,duration:{f(bt(4))},ease:'power2.inOut'}},0);
    tl.to('.pt',{{opacity:1,duration:0.05,stagger:{f(bt(4) / 19)}}},0);
    pop('#ec-kick',1); pop('#ec-q1',2); pop('#ec-q2',2.5); pop('#ec-q3',3);
    pop('#ec-r0',4); tl.to('#ec-tk0',{{strokeDashoffset:0,duration:0.25,ease:'power2.out'}},{f(bt(4))});
    pop('#ec-r1',4.5); tl.to('#ec-tk1',{{strokeDashoffset:0,duration:0.25,ease:'power2.out'}},{f(bt(4.5))});
    tl.fromTo('#ec-btn',{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:0.133,ease:'back.out(1.7)'}},{f(bt(5))});
    pop('#ec-tel',6); pop('#ec-web',6.5); pop('#ec-note',7);
    tl.set({{}},{{}},{f(dur - 0.01)});
    window.__timelines["endcard"] = tl;
  </script>
</template>
"""


# ------------------------------------------------------------ yellow highlighter wipes
def wipes_comp(dur, t_recap, t_end):
    half = bt(0.5)
    return f"""<template>
  <style>
#root{{position:absolute;inset:0;}}
.wp{{position:absolute;left:0;top:0;width:1080px;height:1920px;background:{YELLOW};}}
  </style>
  <div id="root" data-composition-id="wipes" data-width="1080" data-height="1920">
    <div id="wp-a" class="wp" data-layout-ignore></div>
    <div id="wp-b" class="wp" data-layout-ignore></div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    gsap.set('#wp-a, #wp-b',{{x:-1100}});
    tl.fromTo('#wp-a',{{x:-1100}},{{x:0,duration:{f(half)},ease:'power3.in',immediateRender:false}},{f(t_recap - half)});
    tl.to('#wp-a',{{x:1100,duration:{f(half)},ease:'power3.out'}},{f(t_recap)});
    tl.fromTo('#wp-b',{{x:-1100}},{{x:0,duration:{f(half)},ease:'power3.in',immediateRender:false}},{f(t_end - half)});
    tl.set('#wp-b',{{x:-1100}},{f(t_end)});
    tl.set({{}},{{}},{f(dur - 0.01)});
    window.__timelines["wipes"] = tl;
  </script>
</template>
"""


def host(id_, start, dur, track, z):
    return (f'      <div id="{id_}" data-composition-id="{id_}" data-composition-src="compositions/{id_}.html" '
            f'data-start="{start:.4f}" data-duration="{dur:.4f}" data-track-index="{track}" data-track-kind="graphics" '
            f'data-width="1080" data-height="1920" style="z-index:{z}"></div>')


def main():
    rules = rule_defs()
    log = check_angles(rules)
    comp = os.path.join(HERE, "compositions")
    os.makedirs(comp, exist_ok=True)
    for name in os.listdir(comp):
        os.remove(os.path.join(comp, name))
    hosts, timing, events = [], [], []
    b = 0
    for n, r in enumerate(rules, 1):
        dur = bt(r["beats"])
        open(os.path.join(comp, f"r{n:02d}.html"), "w").write(rule_comp(r, n, dur, events, bt(b)))
        hosts.append(host(f"r{n:02d}", bt(b), dur, 2, 10 + n))
        timing.append(f"{n:2d} {r['name']:22s} beat {b:3d}  {bt(b):6.2f} to {bt(b + r['beats']):6.2f}")
        b += r["beats"]
    rules_end_b = b
    open(os.path.join(comp, "chrome.html"), "w").write(chrome_comp(rules, bt(rules_end_b), bt(rules[0]["beats"])))
    hosts.append(host("chrome", 0, bt(rules_end_b), 3, 30))

    t_recap = bt(b)
    open(os.path.join(comp, "recap.html"), "w").write(recap_comp(rules, bt(16), events, t_recap))
    hosts.append(host("recap", t_recap, bt(16), 2, 25))
    timing.append(f"   Recap                  beat {b:3d}  {t_recap:6.2f} to {bt(b + 16):6.2f}")
    b += 16
    t_end = bt(b)
    open(os.path.join(comp, "endcard.html"), "w").write(end_comp(bt(16), events, t_end))
    hosts.append(host("endcard", t_end, bt(16), 2, 26))
    timing.append(f"   End card               beat {b:3d}  {t_end:6.2f} to {bt(b + 16):6.2f}")
    b += 16
    total = bt(b)
    open(os.path.join(comp, "bg.html"), "w").write(bg_comp(rules_end_b, t_recap))
    hosts.insert(0, host("bg", 0, t_recap, 1, 1))
    open(os.path.join(comp, "wipes.html"), "w").write(wipes_comp(total, t_recap, t_end))
    hosts.append(host("wipes", 0, total, 4, 40))

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
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total:.4f}" data-width="1080" data-height="1920">
{chr(10).join(hosts)}
      <audio id="music" class="clip" src="assets/music/track.mp3" data-start="0" data-duration="{total:.4f}" data-media-start="{MEDIA_START}" data-volume="1" data-fade-out="1.0" data-track-index="10"></audio>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
    open(os.path.join(HERE, "index.html"), "w").write(index)
    open(os.path.join(HERE, "timing.txt"), "w").write("\n".join(timing) + f"\nTotal {total:.2f} s, {b} beats at {BPM} BPM\n")
    json.dump(dict(bpm=BPM, media_start=MEDIA_START, events=sorted(events, key=lambda e: e["t"])), open(os.path.join(HERE, "sync-events.json"), "w"), indent=0)
    print("\n".join(log))
    print("\n".join(timing))
    print(f"Total {total:.2f} s, {b} beats, {len(events)} synced events")


if __name__ == "__main__":
    main()
