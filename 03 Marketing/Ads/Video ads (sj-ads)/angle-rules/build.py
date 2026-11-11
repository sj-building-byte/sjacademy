#!/usr/bin/env python3
"""Builds index.html and compositions/ for the 12 angle rules reel. Same system as the 14 area and volume
formulas reel, so the two read as one series. Edit SHAPES or the copy below, then run: python3 build.py"""
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
MEDIA_START = 15.045  # music starts on its beat 28, so the bass lift lands on the first triangle (beat 36)
SCENE_BEATS = 6
FPS = 30
N_SCENES = 12
V_RECAP = 72
V_PITCH = 82
V_END = 100
V_STOP = 108
GAIN_INTRO, GAIN_MID, GAIN_HIGH = 1.1, 0.84, 0.66

INK, CANVAS, BODY, YELLOW, ORANGE, BROWN, PEN = (
    "#151515", "#F7F5EF", "#D9D4C7", "#FCE004", "#FE6100", "#453516", "#D63A2F",
)


def beat(n):
    return round(n * BEAT, 4)


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


def pt(c, r, deg):
    return (c[0] + r * math.cos(math.radians(deg)), c[1] - r * math.sin(math.radians(deg)))


def ang(c, a1, a2, label, r=56, lr=None, hi=False):
    """An angle at c, anticlockwise from a1 to a2 degrees. The label sits on the bisector."""
    return dict(c=c, a1=a1, a2=a2, r=r, label=label, lr=lr or r + 56, hi=hi)


def tick(p, q, size=15):
    m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = math.hypot(dx, dy)
    ux, uy = -dy / n * size, dx / n * size
    return [(m[0] - ux, m[1] - uy), (m[0] + ux, m[1] + uy)]


def corner(p, q, r):
    """The angle at q, measured from the drawn points."""
    a = math.atan2(p[1] - q[1], p[0] - q[0]) - math.atan2(r[1] - q[1], r[0] - q[0])
    d = abs(math.degrees(a)) % 360
    return min(d, 360 - d)


def parallels():
    top, bot = 110.0, 380.0
    B = (170.0, bot)
    A = (B[0] + (bot - top) / math.tan(math.radians(60)), top)
    return A, B, pt(A, 72, 60), pt(B, 62, 240), top, bot


_S = (250.0, 395.0)
_P = (250.0, 250.0)
_X = (250.0, 250.0)
_A, _B, _TT, _TB, _T, _BT = parallels()
_PAR = [[(-100, _T), (600, _T)], [(-100, _BT), (600, _BT)], [_TB, _TT]]
_CH = chev(40, _T, 0) + chev(40, _BT, 0)

# triangle: 60, 45, 75
_ta, _tb = (-10.0, 440.0), (510.0, 440.0)
_th = (_tb[0] - _ta[0]) / (1 / math.tan(math.radians(60)) + 1)
_tc = (_ta[0] + _th / math.tan(math.radians(60)), _ta[1] - _th)
# isosceles: base angles 70
_ih = 370.0
_ihalf = _ih / math.tan(math.radians(70))
_ia, _ib, _ic = (250 - _ihalf, 440.0), (250 + _ihalf, 440.0), (250.0, 440 - _ih)
# exterior angle: 50, 70, exterior 120
_ea, _eb = (-10.0, 430.0), (360.0, 430.0)
_eh = (_eb[0] - _ea[0]) / (1 / math.tan(math.radians(50)) + 1 / math.tan(math.radians(60)))
_ec = (_ea[0] + _eh / math.tan(math.radians(50)), _ea[1] - _eh)
# quadrilateral: 70, 100, 80, 110 going round
_qa, _qb = (10.0, 430.0), (440.0, 430.0)
_qh = 320.0
_qd = (_qa[0] + _qh / math.tan(math.radians(70)), _qa[1] - _qh)
_qc = (_qb[0] + _qh / math.tan(math.radians(80)), _qb[1] - _qh)
# regular pentagon with its sides carried on
_PO = (250.0, 262.0)
_PV = [pt(_PO, 165, 90 + 72 * i) for i in range(5)]
_PD = [math.degrees(math.atan2(-(_PV[(i + 1) % 5][1] - _PV[i][1]), _PV[(i + 1) % 5][0] - _PV[i][0])) for i in range(5)]
# regular hexagon split into four triangles from one corner
_HO = (250.0, 250.0)
_HV = [pt(_HO, 225, 60 * i) for i in range(6)]
_HT = [(_HV[3], _HV[4], _HV[5]), (_HV[3], _HV[5], _HV[0]), (_HV[3], _HV[0], _HV[1]), (_HV[3], _HV[1], _HV[2])]

SHAPES = [
    dict(id="straight", name="Straight line", label="Angles on a straight line", result="add to 180°", total=180,
         f=[t("130° + 50° = 180°")], defs=["Angles on a straight line add up to 180°"],
         draw=[[(-100, _S[1]), (600, _S[1])], [_S, pt(_S, 370, 50)]],
         angles=[ang(_S, 50, 180, "130°"), ang(_S, 0, 50, "50°")]),
    dict(id="point", name="At a point", label="Angles at a point", result="add to 360°", total=360,
         f=[t("140° + 100° + 120° = 360°")], defs=["Angles at a point add up to 360°"],
         draw=[[_P, pt(_P, 245, 90)], [_P, pt(_P, 245, 230)], [_P, pt(_P, 245, 330)]],
         angles=[ang(_P, 90, 230, "140°"), ang(_P, 230, 330, "100°"), ang(_P, 330, 450, "120°")]),
    dict(id="vertical", name="Vertically opposite", label="Vertically opposite angles", result="are equal", equal=True,
         f=[t("70° = 70°")], defs=["Vertically opposite angles are equal"],
         draw=[[pt(_X, 330, 215), pt(_X, 330, 35)], [pt(_X, 330, 145), pt(_X, 330, 325)]],
         angles=[ang(_X, 145, 215, "70°", r=78, lr=146), ang(_X, -35, 35, "70°", r=78, lr=146)]),
    dict(id="alternate", name="Alternate", label="Alternate angles", result="are equal", equal=True,
         f=[t("60° = 60°")], defs=["Alternate angles on parallel lines are equal", "Look for the Z shape"],
         draw=_PAR, mark=_CH, hi=[[(_A[0] - 300, _T), _A, _B, (_B[0] + 300, _BT)]],
         angles=[ang(_A, 180, 240, "60°", lr=116), ang(_B, 0, 60, "60°", lr=116)]),
    dict(id="corresponding", name="Corresponding", label="Corresponding angles", result="are equal", equal=True,
         f=[t("60° = 60°")], defs=["Corresponding angles on parallel lines are equal", "Look for the F shape"],
         draw=_PAR, mark=_CH, hi=[[_B, _TT], [_A, (_A[0] + 230, _T)], [_B, (_B[0] + 230, _BT)]],
         angles=[ang(_A, 0, 60, "60°", lr=116), ang(_B, 0, 60, "60°", lr=116)]),
    dict(id="cointerior", name="Co-interior", label="Co-interior angles", result="add to 180°", total=180,
         f=[t("120° + 60° = 180°")], defs=["Co-interior angles on parallel lines", "add up to 180°. Look for the C shape"],
         draw=_PAR, mark=_CH, hi=[[(_A[0] + 230, _T), _A, _B, (_B[0] + 230, _BT)]],
         angles=[ang(_A, 240, 360, "120°", lr=116), ang(_B, 0, 60, "60°", lr=116)]),
    dict(id="triangle", name="Triangle", label="Angles in a triangle", result="add to 180°", total=180,
         f=[t("60° + 45° + 75° = 180°")], defs=["Angles in a triangle add up to 180°"],
         draw=[[_ta, _tb, _tc, _ta]], fill=[_ta, _tb, _tc],
         angles=[ang(_ta, 0, 60, "60°", lr=108), ang(_tb, 135, 180, "45°", lr=132), ang(_tc, 240, 315, "75°", lr=112)],
         corners=[(_tc, _ta, _tb, 60), (_ta, _tb, _tc, 45), (_ta, _tc, _tb, 75)]),
    dict(id="isosceles", name="Isosceles", label="Isosceles triangle", result="base angles equal", equal=True,
         f=[t("70° = 70°")], defs=["Base angles of an isosceles triangle are equal", "The ticks mark the equal sides"],
         draw=[[_ia, _ib, _ic, _ia]], fill=[_ia, _ib, _ic], mark=[tick(_ia, _ic), tick(_ib, _ic)],
         angles=[ang(_ia, 0, 70, "70°", r=46, lr=98), ang(_ib, 110, 180, "70°", r=46, lr=98)],
         corners=[(_ic, _ia, _ib, 70), (_ia, _ib, _ic, 70)]),
    dict(id="exterior", name="Triangle exterior", label="Exterior angle of a triangle", result="= sum of 2 opposite interior angles", ext=True,
         f=[t("50° + 70° = 120°")], defs=["The exterior angle of a triangle equals", "the sum of the two opposite interior angles"],
         draw=[[_ea, _eb, _ec, _ea], [_eb, (580.0, 430.0)]], fill=[_ea, _eb, _ec],
         angles=[ang(_ea, 0, 50, "50°", lr=106), ang(_ec, 230, 300, "70°", r=46, lr=100), ang(_eb, 0, 120, "120°", lr=112)],
         corners=[(_ec, _ea, _eb, 50), (_ea, _ec, _eb, 70), (_ea, _eb, _ec, 60)]),
    dict(id="quad", name="Quadrilateral", label="Angles in a quadrilateral", result="add to 360°", total=360,
         f=[t("70° + 100° + 80° + 110° = 360°")], defs=["Angles in a quadrilateral add up to 360°"],
         draw=[[_qa, _qb, _qc, _qd, _qa]], fill=[_qa, _qb, _qc, _qd],
         angles=[ang(_qa, 0, 70, "70°", lr=110), ang(_qb, 80, 180, "100°", lr=112), ang(_qc, 180, 260, "80°", lr=110), ang(_qd, 250, 360, "110°", lr=112)],
         corners=[(_qd, _qa, _qb, 70), (_qa, _qb, _qc, 100), (_qb, _qc, _qd, 80), (_qc, _qd, _qa, 110)]),
    dict(id="polyext", name="Polygon exterior", label="Exterior angles of a polygon", result="add to 360°", total=360,
         f=[t("5 × 72° = 360°")], defs=["The exterior angles of a convex polygon", "add up to 360°. Regular pentagon shown"],
         draw=[[*_PV, _PV[0]]] + [[_PV[(i + 1) % 5], pt(_PV[(i + 1) % 5], 74, _PD[i])] for i in range(5)],
         angles=[ang(_PV[(i + 1) % 5], _PD[i], _PD[i] + 72, "72°", r=42, lr=88) for i in range(5)]),
    dict(id="polyint", name="Polygon interior", label="Interior angles of a polygon", result="(n − 2) × 180°", poly=True,
         f=[t("(6 − 2) × 180° = 720°")], defs=["Interior angles of an {n}-sided polygon", "add up to ({n} − 2) × 180°. Hexagon: {n} = 6"],
         draw=[[*(_HV[(3 + i) % 6] for i in range(6)), _HV[3]]], fill=[_HV[(3 + i) % 6] for i in range(6)],
         thin=[[_HV[3], _HV[5]], [_HV[3], _HV[0]], [_HV[3], _HV[1]]],
         nums=[(str(n + 1), sum(p[0] for p in tr) / 3, sum(p[1] for p in tr) / 3) for n, tr in enumerate(_HT)]),
]


def check_maths():
    """Second solve: every label against its drawn span, every total, and each corner measured from the points."""
    for sh in SHAPES:
        vals = [a["a2"] - a["a1"] for a in sh.get("angles", [])]
        for a, v_ in zip(sh.get("angles", []), vals):
            assert a["label"] == f"{round(v_)}°", (sh["id"], a["label"], v_)
        if "total" in sh:
            assert round(sum(vals)) == sh["total"], (sh["id"], vals)
        if sh.get("equal"):
            assert len({round(v_) for v_ in vals}) == 1, (sh["id"], vals)
        if sh.get("ext"):
            assert round(vals[0] + vals[1]) == round(vals[2]), (sh["id"], vals)
        for p, q, r, want in sh.get("corners", []):
            assert abs(corner(p, q, r) - want) < 1e-6, (sh["id"], want, corner(p, q, r))
    assert (6 - 2) * 180 == 720 and 5 * 72 == 360
    # the pentagon's carried-on sides turn 72 degrees at every corner, and the hexagon really is 4 triangles
    assert all(abs(((_PD[(i + 1) % 5] - _PD[i]) % 360) - 72) < 1e-6 for i in range(5))
    assert len(_HT) == 6 - 2
    print("maths check passed: labels, totals and measured corners all agree")


def color(i):
    return YELLOW if i % 2 == 0 else ORANGE


def pts_d(pts, ox, oy, s, close=False):
    d = "M" + " L".join(f"{ox + x * s:.1f} {oy + y * s:.1f}" for x, y in pts)
    return d + ("Z" if close else "")


def plen(pts):
    return sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))


def label_svg(txt, x, y, ox, oy, s, fs, id_):
    px, py = ox + x * s, oy + y * s + fs * 0.36
    return (
        f'<text id="{id_}" x="{px:.1f}" y="{py:.1f}" opacity="0" text-anchor="middle" font-family="Poppins" font-weight="600" '
        f'paint-order="stroke" stroke="#151515" stroke-width="7" stroke-linejoin="round" font-size="{fs}" fill="{CANVAS}">{txt}</text>'
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
    ids["hi"], ids["angles"] = [], []
    for j, a in enumerate(sh.get("angles", [])):
        c, r_ = a["c"], a["r"]
        arc = ell(c[0], c[1], r_, r_, a["a1"], a["a2"], 28)
        fill += f'<path id="{pre}w{j}" d="{pts_d([c] + arc, ox, oy, s, True)}" fill="{ORANGE}" opacity="0"/>'
    for p in sh["draw"] + sh.get("ghost", []) + sh.get("dash", [])[:0]:
        ghost += f'<path d="{pts_d(p, ox, oy, s)}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round"/>'
    for j, p in enumerate(sh["draw"]):
        id_ = f"{pre}d{j}"
        ids["draw"].append((id_, plen(p)))
        lines += (
            f'<path id="{id_}" d="{pts_d(p, ox, oy, s)}" pathLength="1" fill="none" stroke="{BODY if sh.get("hi") else col}" stroke-width="{w * .5 if sh.get("hi") else w}" '
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
    for j, p in enumerate(sh.get("hi", [])):
        id_ = f"{pre}x{j}"
        ids["hi"].append(id_)
        lines += (
            f'<path id="{id_}" d="{pts_d(p, ox, oy, s)}" pathLength="1" fill="none" stroke="{col}" stroke-width="{sw * 1.25}" '
            f'stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0"/>'
        )
    text = ""
    for j, a in enumerate(sh.get("angles", [])):
        c, r_ = a["c"], a["r"]
        arc = ell(c[0], c[1], r_, r_, a["a1"], a["a2"], 28)
        lines += (
            f'<path id="{pre}a{j}" d="{pts_d(arc, ox, oy, s)}" pathLength="1" fill="none" stroke="{col}" stroke-width="{thin_w}" '
            f'stroke-linecap="butt" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0"/>'
        )
        lid = f"{pre}l{j}"
        ids["angles"].append((f"{pre}a{j}", f"{pre}w{j}", lid))
        if labels:
            lx, ly = pt(c, a["lr"], (a["a1"] + a["a2"]) / 2)
            text += label_svg(a["label"], lx, ly, ox, oy, s, fs, lid)
    if labels:
        for j, (txt, x, y) in enumerate(sh.get("nums", [])):
            id_ = f"{pre}n{j}"
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
    for id_ in ids["hi"]:
        js.append(f"tl.set('#{id_}',{{opacity:1}},{t3});tl.fromTo('#{id_}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:{beat(.5)},ease:'sine.inOut'}},{t3});")
    count = len(ids["angles"]) + len(ids["labels"])
    step = .5 if count <= 3 else .25
    for j, (arc_id, wedge_id, lid) in enumerate(ids["angles"]):
        at = beat(3.5 + j * step)
        lead = beat(.25)
        js.append(f"tl.set('#{arc_id}',{{opacity:1}},{at - lead:.4f});tl.fromTo('#{arc_id}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:{lead},ease:'sine.in'}},{at - lead:.4f});")
        js.append(f"tl.fromTo('#{wedge_id}',{{opacity:0}},{{opacity:.34,duration:.12,ease:'power1.out'}},{at:.4f});")
        js.append(f"tl.fromTo('#{lid}',{{opacity:0,y:10}},{{opacity:1,y:0,duration:.27,ease:'expo.out'}},{at:.4f});")
    for j, id_ in enumerate(ids["labels"]):
        at = beat(3.5 + j * step)
        js.append(f"tl.fromTo('#{id_}',{{opacity:0,y:10}},{{opacity:1,y:0,duration:.27,ease:'expo.out'}},{at});")
    if sh.get("fill"):
        js.append(f"tl.fromTo('#{cid}-fill',{{opacity:0}},{{opacity:1,duration:.2,ease:'power1.out'}},{beat(3)});")
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
<div id="title-box" data-layout-allow-overlap>12 angle rules<br>for <span class="hlw">O Level Maths<span id="title-band" data-layout-allow-overflow data-layout-ignore><span>O Level Maths</span></span></span></div>
</div>
<script>{js}</script>
</template>
""")


def write_formula():
    cy = 1190
    boxes = []
    fhtml = dhtml = ""
    for i, sh in enumerate(SHAPES):
        fsize = min(66, int(66 * 880 / max(1, tokens_w(sh["f"], 66))))
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
        col_i = 0 if i < 6 else 1
        row = i if i < 6 else i - 6
        cx = 40 if col_i == 0 else 548
        cy = 416 + row * 170
        xs = [p[0] for poly in sh["draw"] for p in poly]
        ys = [p[1] for poly in sh["draw"] for p in poly]
        s = min(140 / (max(xs) - min(xs)), 130 / (max(ys) - min(ys)))
        ox = cx + (140 - (max(xs) - min(xs)) * s) / 2 - min(xs) * s
        oy = cy + (130 - (max(ys) - min(ys)) * s) / 2 - min(ys) * s
        pre = f"r{i}-"
        fill, ghost, lines, _, ids = shape_parts(sh, i, ox, oy, s, 3, pre, labels=False)
        svg_all += f'{fill}<g id="{pre}ghost" opacity="0">{ghost}</g>{lines}<circle id="{pre}pen" r="4.5" fill="{CANVAS}" opacity="0"/>'
        text += (
            f'<div class="rc" id="{pre}txt" style="left:{cx + 154}px;top:{cy + 8}px"><div class="rn">{sh["name"]}</div>'
            f'<div class="rr{" rl" if len(sh["result"]) > 15 else ""}">{sh["result"].replace("(n", "(<i>n</i>")}</div></div>'
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
        pen = sample_pen(sh["draw"], ox, oy, s, dur)
        step = round(dur / (len(pen) - 1), 5)
        js.append(f"(()=>{{const P={json.dumps(pen, separators=(',', ':'))};tl.set('#{pre}pen',{{x:P[0][0],y:P[0][1]}},0);tl.set('#{pre}pen',{{opacity:1}},{start:.4f});P.slice(1).forEach((p,k)=>tl.to('#{pre}pen',{{x:p[0],y:p[1],duration:{step},ease:'none'}},{start:.4f}+k*{step}));tl.set('#{pre}pen',{{opacity:0}},{start + dur:.4f});}})();")
        for id_ in ids["thin"]:
            js.append(f"tl.set('#{id_}',{{opacity:1}},{start + dur:.4f});tl.fromTo('#{id_}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.2,ease:'none'}},{start + dur:.4f});")
        for id_ in ids["dash"] + ids["mark"]:
            js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:1,duration:.2}},{start + dur:.4f});")
        for id_ in ids["hi"]:
            js.append(f"tl.set('#{id_}',{{opacity:1}},{start + dur:.4f});tl.fromTo('#{id_}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.2,ease:'none'}},{start + dur:.4f});")
        if sh.get("fill"):
            js.append(f"tl.fromTo('#{pre}fill',{{opacity:0}},{{opacity:1,duration:.2}},{beat(4):.4f});")
        for arc_id, wedge_id, _l in ids["angles"]:
            js.append(f"tl.set('#{arc_id}',{{opacity:1}},{beat(4):.4f});tl.fromTo('#{arc_id}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.2,ease:'none'}},{beat(4):.4f});")
            js.append(f"tl.fromTo('#{wedge_id}',{{opacity:0}},{{opacity:.5,duration:.2}},{beat(4):.4f});")
        js.append(f"tl.fromTo('#{pre}txt',{{opacity:0,x:-10}},{{opacity:1,x:0,duration:.34,ease:'expo.out'}},{start + .1:.4f});")
    js.append("window.__timelines['recap']=tl;")
    (COMP / "recap.html").write_text(
        f"""<template>
<style>{FONT}{MATH_CSS}#root{{position:absolute;inset:0}}
#rc-note{{position:absolute;left:0;width:1080px;top:338px;text-align:center;font:600 60px/1 'Caveat';color:{YELLOW};opacity:0}}
.rc{{position:absolute;display:flex;flex-direction:column;align-items:flex-start;width:345px;height:116px;justify-content:center;opacity:0}}
.rn{{font:600 30px/1.2 'Poppins';color:{YELLOW}}}
.rr{{font:500 38px/1.2 'Poppins';color:{CANVAS};white-space:nowrap}}
.rr i{{font-style:italic}}
.rl{{font:500 29px/1.2 'Poppins';white-space:normal;width:330px}}
</style>
<div id="root" data-composition-id="recap" data-width="1080" data-height="1920" data-layout-allow-overlap>
<div id="rc-note" data-hold>screenshot this one</div>
<svg width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0" data-layout-ignore>{svg_all}</svg>
{text}
</div>
<script>{''.join(js)}</script>
</template>
""")


CAPTIONS = [
    (0, 6, "Think you know them now?"),
    (6, 12, "Try them on real past papers."),
    (12, 18, "Free. No sign-up."),
]


def write_pitch():
    px, py, pw, ph = 280, 372, 520, 840
    scale = 496 / 780
    circle = ell(0, 0, 112, 36, 150, -235, 60)
    # chip on the captured page: x 16, y 559.6, w 140.8, h 32.4 at 390 wide; the page is shown 1.272x
    chip_x = (16 + 70.4) * 1.272
    chip_y = (559.6 + 16.2) * 1.272
    top_offset = 74
    cc = [(round(chip_x + x, 1), round(chip_y - top_offset + y, 1)) for x, y in circle]
    d_circle = "M" + " L".join(f"{x} {y}" for x, y in cc)
    words = ""
    js = ["const tl=gsap.timeline({paused:true});"]
    js.append("tl.fromTo('#pt-scrim',{opacity:0},{opacity:.82,duration:.4,ease:'power1.out'},0);")
    js.append("tl.fromTo('#pt-phone',{opacity:0,y:70},{opacity:1,y:0,duration:.6,ease:'expo.out'},.02);")
    js.append("tl.fromTo('#pt-cap',{opacity:0,y:30},{opacity:1,y:0,duration:.5,ease:'expo.out'},.1);")
    js.append(f"tl.set('#pt-img',{{y:-{top_offset}}},0);")
    js.append(f"tl.to('#pt-img',{{y:-1580,duration:{beat(4)},ease:'power2.inOut'}},{beat(7):.4f});")
    js.append(f"tl.to('#pt-img',{{y:-{top_offset},duration:{beat(1.5)},ease:'power2.inOut'}},{beat(12):.4f});")
    js.append(f"tl.set('#pt-circle',{{opacity:1}},{beat(14):.4f});tl.fromTo('#pt-circle',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.55,ease:'sine.inOut'}},{beat(14):.4f});")
    for c, (a, b_, line) in enumerate(CAPTIONS):
        parts = line.split(" ")
        spans = "".join(f'<span id="w{c}-{j}">{html.escape(w)}</span> ' for j, w in enumerate(parts))
        words += f'<div class="cp" id="cp{c}">{spans.strip()}</div>'
        ta, tb = beat(a), beat(b_)
        if c:
            js.append(f"tl.fromTo('#cp{c}',{{opacity:0,y:12}},{{opacity:1,y:0,duration:.24,ease:'expo.out'}},{ta:.4f});")
        else:
            js.append("tl.set('#cp0',{opacity:1},0);")
        if c < len(CAPTIONS) - 1:
            js.append(f"tl.to('#cp{c}',{{opacity:0,y:-10,duration:.14,ease:'power2.in'}},{tb - .15:.4f});")
        span = (tb - ta - .5) / len(parts)
        for j in range(len(parts)):
            on = ta + .1 + j * span
            js.append(f"tl.to('#w{c}-{j}',{{color:'{YELLOW}',duration:.06}},{on:.4f});")
            if j < len(parts) - 1:
                js.append(f"tl.to('#w{c}-{j}',{{color:'{CANVAS}',duration:.1}},{on + span:.4f});")
    js.append("window.__timelines['pitch']=tl;")
    sw, sh = pw - 24, ph - 24
    (COMP / "pitch.html").write_text(
        f"""<template>
<style>{FONT}#root{{position:absolute;inset:0}}
#pt-scrim{{position:absolute;inset:0;background:{INK};opacity:0}}
#pt-phone{{position:absolute;left:{px}px;top:{py}px;width:{pw}px;height:{ph}px;border-radius:64px;background:#000;border:3px solid #55524a;opacity:0}}
#pt-screen{{position:absolute;left:9px;top:9px;width:{sw - 0}px;height:{sh}px;border-radius:52px;overflow:hidden;background:{CANVAS}}}
#pt-bar{{position:absolute;left:0;top:0;width:100%;height:76px;background:#fff;display:flex;align-items:center;justify-content:center;z-index:2;border-bottom:1px solid #e6e3da}}
#pt-url{{font:500 28px/1 'Poppins';color:{INK};background:#F1EFE8;border-radius:30px;padding:9px 30px}}
#pt-view{{position:absolute;left:0;top:76px;width:100%;bottom:0;overflow:hidden}}
#pt-img{{position:absolute;left:0;top:0;width:{sw}px;height:auto}}
#pt-pen{{position:absolute;left:0;top:0}}
#pt-cap{{position:absolute;left:130px;width:820px;top:1232px;height:104px;border-radius:24px;background:{INK};border:3px solid {CANVAS};opacity:0}}
.cp{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:0 .3em;font:600 44px/1 'Poppins';color:{CANVAS};opacity:0;white-space:nowrap}}
</style>
<div id="root" data-composition-id="pitch" data-width="1080" data-height="1920" data-layout-allow-overlap data-layout-allow-occlusion>
<div id="pt-scrim" data-layout-ignore></div>
<div id="pt-phone" data-layout-allow-overflow data-layout-allow-occlusion><div id="pt-screen">
<div id="pt-bar"><span id="pt-url">sjacademy.pk</span></div>
<div id="pt-view"><img id="pt-img" src="assets/page/maths-past-papers.png" alt="SJ Academy O Level Mathematics D past papers page">
<svg id="pt-pen" width="{sw}" height="{sh}" viewBox="0 0 {sw} {sh}"><path id="pt-circle" d="{d_circle}" pathLength="1" fill="none" stroke="{PEN}" stroke-width="5" stroke-linecap="round" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0"/></svg>
</div></div></div>
<div id="pt-cap">{words}</div>
</div>
<script>{''.join(js)}</script>
</template>
""")


def write_end():
    wipe = round(14 / FPS, 3)
    t_land = BEAT  # host starts one beat before V_END
    t_wipe = round(t_land - wipe, 3)
    js = f"""const tl=gsap.timeline({{paused:true}});
tl.fromTo('#en-wipe',{{scaleX:0}},{{scaleX:1,duration:{wipe},ease:'power2.inOut'}},{t_wipe});
tl.fromTo('#en-logo',{{opacity:0}},{{opacity:1,duration:.4,ease:'power1.out'}},{t_land - .05:.3f});
tl.fromTo('#en-chip',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.4,ease:'expo.out'}},{t_land:.3f});
tl.fromTo('#en-h1',{{opacity:0,y:26}},{{opacity:1,y:0,duration:.4,ease:'expo.out'}},{t_land:.3f});
tl.fromTo('#en-h2',{{opacity:0,y:26}},{{opacity:1,y:0,duration:.4,ease:'expo.out'}},{t_land + beat(1):.3f});
tl.fromTo('#en-band',{{scaleX:0}},{{scaleX:1,duration:.27,ease:'sine.inOut'}},{t_land + beat(1) + .14:.3f});
tl.fromTo('#en-btn',{{opacity:0,y:26}},{{opacity:1,y:0,duration:.4,ease:'expo.out'}},{t_land + beat(2):.3f});
tl.fromTo('#en-ph',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.4,ease:'expo.out'}},{t_land + beat(2.5):.3f});
tl.fromTo('#en-web',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.4,ease:'expo.out'}},{t_land + beat(3):.3f});
window.__timelines['endcard']=tl;"""
    (COMP / "endcard.html").write_text(
        f"""<template>
<style>{FONT}#root{{position:absolute;inset:0}}
#en-wipe{{position:absolute;inset:0;background:{YELLOW};transform-origin:left center}}
#en-logo{{position:absolute;left:310px;top:276px;width:460px;height:auto;opacity:0}}
.en{{position:absolute;left:70px;width:940px;text-align:center;color:{INK};opacity:0}}
#en-chip{{top:470px;left:220px;width:640px;height:64px;border-radius:32px;background:{BROWN};color:{CANVAS};display:flex;align-items:center;justify-content:center;font:500 30px/1 'Poppins';letter-spacing:.06em}}
#en-h1{{top:590px;font:700 88px/100px 'Poppins';letter-spacing:-.03em}}
#en-h2{{top:808px;font:600 52px/68px 'Poppins';letter-spacing:-.01em}}
.en2{{position:relative;display:inline-block}}
#en-band{{position:absolute;left:-.14em;right:-.14em;top:.62em;height:.46em;background:#fff;transform-origin:left center;z-index:0}}
#en-h2 .tx{{position:relative;z-index:1}}
#en-btn{{top:984px;left:120px;width:840px;height:128px;border-radius:62px;background:{BROWN};color:{CANVAS};display:flex;align-items:center;justify-content:center;font:600 44px/1 'Poppins'}}
#en-ph{{top:1176px;font:700 76px/1.1 'Poppins';letter-spacing:-.02em}}
#en-web{{top:1276px;font:500 50px/1.2 'Poppins'}}
</style>
<div id="root" data-composition-id="endcard" data-width="1080" data-height="1920">
<div id="en-wipe" data-layout-ignore></div>
<img id="en-logo" src="assets/brand/sj-academy-logo-horizontal-on-yellow.svg" alt="SJ Academy">
<div class="en" id="en-chip">O LEVEL AND A LEVEL MATHS</div>
<div class="en" id="en-h1">Knowing the rule<br>is the easy part.</div>
<div class="en" id="en-h2" data-layout-allow-overlap>Join our Maths classes.<br><span class="en2"><span id="en-band" data-layout-ignore></span><span class="tx">One class free.</span></span> Then decide.</div>
<div class="en" id="en-btn">Book a free demo on WhatsApp</div>
<div class="en" id="en-ph">+92-336-2144454</div>
<div class="en" id="en-web">sjacademy.pk</div>
</div>
<script>{js}</script>
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
    hosts.append(host("pitch", beat(V_PITCH), beat(V_END - V_PITCH) + .1, 8, 6))
    hosts.append(host("endcard", beat(V_END - 1), beat(V_STOP - V_END + 1), 9, 7))
    fade = round(beat(3), 3)
    # Evens out the track's three sections so the opening is audible on a phone and the mix sits at -14 LUFS.
    # Each change happens across the last moment before the music's own lift, so it is heard as the lift.
    lift1, lift2 = beat(4), beat(36)
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
    check_maths()
    for i, sh in enumerate(SHAPES):
        write_scene(i, sh)
    write_title()
    write_formula()
    write_brand()
    write_recap()
    write_pitch()
    write_end()
    total = write_index()
    print(f"built {N_SCENES} shape scenes, {total}s")


if __name__ == "__main__":
    main()
