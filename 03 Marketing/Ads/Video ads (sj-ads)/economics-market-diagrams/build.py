#!/usr/bin/env python3
"""Builds index.html and compositions/ for the O Level A Level Economics market diagrams reel.
Edit SCENES, the copy or the music map below, then run: python3 build.py"""
import html
import json
import math
from pathlib import Path

ROOT = Path(__file__).parent
COMP = ROOT / "compositions"
METRICS = json.loads((ROOT / "assets/brand/poppins-metrics.json").read_text())
FPS = 30

# ---------- music map: SJ's own synth track (music/compose.py), 128 BPM ----------
# The track is written to this beat map, so video beat 0 is music beat 0.
# v1 used "Fresh" from the Music Folder at track beat 24 (12.902 s).
BEAT = 60 / 128
MUSIC = "assets/music/sj-market-synth.wav"
MEDIA_START = 0.0
V_LIFT1, V_LIFT2, V_DROP = 8, 40, 108  # v1's Fresh sections; the synth track lifts at beat 40
SCENE_BEATS = 8  # two bars, so every theorem starts on a bar start
V_RECAP, V_END, V_STOP = 72, 84, 98
V_PITCH = V_END  # no phone scene since 11 November 2026: the end card follows the recap

INK, CANVAS, BODY, YELLOW, ORANGE, BROWN, PEN = (
    "#151515", "#F7F5EF", "#D9D4C7", "#FCE004", "#FE6100", "#453516", "#D63A2F",
)
RING = "#A9A69C"
EXIT = 0.17  # exits start on the hit and glide after it


def at(b):
    """Clock time of a beat."""
    return round(b * BEAT, 4)


def land(b):
    """First visible frame of a move: one frame ahead of the sound. The eye catches the
    moment something appears, so moves start here and settle after the hit."""
    return round(b * BEAT - 1 / FPS, 4)


FONT = """
@font-face{font-family:'Poppins';font-weight:400;src:url('assets/brand/Poppins-Regular.ttf')}
@font-face{font-family:'Poppins';font-weight:500;src:url('assets/brand/Poppins-Medium.ttf')}
@font-face{font-family:'Poppins';font-weight:600;src:url('assets/brand/Poppins-SemiBold.ttf')}
@font-face{font-family:'Poppins';font-weight:700;src:url('assets/brand/Poppins-Bold.ttf')}
@font-face{font-family:'Caveat';font-weight:600;src:url('assets/brand/Caveat-600.woff2')}
"""


# ---------- geometry: 500 x 500 box, price on the y axis, quantity on the x axis ----------
XL, XR, YT, YB = 60.0, 470.0, 40.0, 440.0  # axes: left, right, top, bottom
AX = [(XL, YT), (XL, YB), (XR, YB)]
CLIP_Y = (60.0, 405.0)
CLIP_X = (72.0, 450.0)


class Ln:
    """A straight line in box coordinates (y grows downward, so a higher price is a smaller y)."""

    def __init__(self, x0, y0, m):
        self.x0, self.y0, self.m = x0, y0, m

    def y(self, x):
        return self.y0 + self.m * (x - self.x0)

    def x(self, y):
        return self.x0 + (y - self.y0) / self.m

    def shift(self, dx=0.0, dy=0.0):
        return Ln(self.x0 + dx, self.y0 + dy, self.m)

    def pts(self):
        xs = sorted([self.x(CLIP_Y[0]), self.x(CLIP_Y[1])])
        xa, xb = max(xs[0], CLIP_X[0]), min(xs[1], CLIP_X[1])
        pts = [(xa, self.y(xa)), (xb, self.y(xb))]
        return sorted(pts)


def cross(a, b):
    x = (b.y0 - a.y0 + a.m * a.x0 - b.m * b.x0) / (a.m - b.m)
    return (x, a.y(x))


def to_p(pt):
    """Dashed line from a point to the price axis."""
    return [(XL, pt[1]), pt]


def to_q(pt):
    """Dashed line from a point down to the quantity axis."""
    return [pt, (pt[0], YB)]


def arrow(a, b, head=17, wing=8):
    L = math.dist(a, b)
    ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
    bx, by = b[0] - ux * head, b[1] - uy * head
    return [a, b, (bx - uy * wing, by + ux * wing), b, (bx + uy * wing, by - ux * wing)]


def ylab(txt, y, b):
    return (txt, (22, y), b)


def xlab(txt, x, b):
    return (txt, (x, YB + 36), b)


def curve_label(txt, line, end, dx, dy, b=3.5):
    x, y = line.pts()[end]
    return (txt, x + dx, y + dy + 12, b)


def band(x0, x1, y, h=7):
    return [(x0, y - h), (x1, y - h), (x1, y + h), (x0, y + h)]


def scenes():
    out = []
    D = Ln(110, 110, 0.9)
    S = Ln(110, 420, -0.75)
    E = cross(D, S)

    # 1 demand rises
    D2 = D.shift(dx=130)
    E2 = cross(D2, S)
    ya = 160
    out.append(dict(
        id="demand", name="Demand rises",
        lines=[("When demand rises, ", False)],
        line2=[("price", True), (" and ", False), ("quantity", True), (" rise", False)],
        note=["Demand shifts right, D1 to D2. Supply stays put.", "Old: P1, Q1. New: P2, Q2."],
        draw=[D.pts(), S.pts()], thin=[D2.pts()],
        dash=[to_p(E), to_q(E), to_p(E2), to_q(E2)],
        marks=[arrow((D.x(ya) + 8, ya), (D2.x(ya) - 8, ya))],
        dots=[(E, 3, 8), (E2, 3, 8)],
        words=[curve_label("D1", D, 1, 24, 4), curve_label("D2", D2, 1, 24, 4), curve_label("S", S, 1, 24, -4)],
        vals=[ylab("P1", E[1], 4), ylab("P2", E2[1], 4), xlab("Q1", E[0], 5), xlab("Q2", E2[0], 5)],
        check=[("price rises", E[1] - E2[1], None), ("quantity rises", E2[0] - E[0], None)]))

    # 2 supply rises
    S2 = S.shift(dx=170)
    E2 = cross(D, S2)
    ya = 365
    out.append(dict(
        id="supply", name="Supply rises",
        lines=[("When supply rises, ", False)],
        line2=[("price", True), (" falls and ", False), ("quantity", True), (" rises", False)],
        note=["Supply shifts right, S1 to S2. Demand stays put.", "Old: P1, Q1. New: P2, Q2."],
        draw=[D.pts(), S.pts()], thin=[S2.pts()],
        dash=[to_p(E), to_q(E), to_p(E2), to_q(E2)],
        marks=[arrow((S.x(ya) + 8, ya), (S2.x(ya) - 8, ya))],
        dots=[(E, 3, 8), (E2, 3, 8)],
        words=[curve_label("D", D, 1, 24, 4), curve_label("S1", S, 1, 24, -4), curve_label("S2", S2, 1, 24, -4)],
        vals=[ylab("P1", E[1], 4), ylab("P2", E2[1], 4), xlab("Q1", E[0], 5), xlab("Q2", E2[0], 5)],
        check=[("price falls", E2[1] - E[1], None), ("quantity rises", E2[0] - E[0], None)]))

    # 3 movement along versus shift
    A, B = (D.x(170), 170.0), (D.x(300), 300.0)
    n = (-0.669 * 20, 0.743 * 20)
    D2 = D.shift(dx=100)
    out.append(dict(
        id="along", name="Move or shift",
        lines=[("A change in its own price moves", False)],
        line2=[("along", True), (" the curve. Other causes ", False), ("shift", True), (" it", False)],
        note=["Its own price falls: A to B along D1.", "More buyers: D1 shifts to D2."],
        draw=[D.pts()], thin=[],
        dash=[to_p(A), to_p(B)],
        marks=[arrow((A[0] + n[0], A[1] + n[1]), (B[0] + n[0], B[1] + n[1]))],
        dots=[(A, 4, 8), (B, 4, 8)],
        late_thin=[D2.pts()], late_marks=[arrow((D.x(215) + 8, 215), (D2.x(215) - 8, 215))],
        words=[curve_label("D1", D, 1, 24, 4), curve_label("D2", D2, 1, 24, 4, 5), ("A", A[0] + 18, A[1] - 14 + 12, 3.5), ("B", B[0] + 18, B[1] - 14 + 12, 3.5)],
        vals=[("Move", (128, 238), 4), ("Shift", (412, 215), 5)],
        check=[("B is on D", B[1] - D.y(B[0]), 0), ("A is on D", A[1] - D.y(A[0]), 0), ("price falls", B[1] - A[1], None)]))

    # 4 maximum price
    py = E[1] + 60
    qs, qd = S.x(py), D.x(py)
    out.append(dict(
        id="maxprice", name="Maximum price",
        lines=[("A maximum price below", False)],
        line2=[("equilibrium causes a ", False), ("shortage", True)],
        note=["E is equilibrium. Buyers want Qd,", "sellers supply only Qs."],
        draw=[D.pts(), S.pts(), [(XL, py), (CLIP_X[1], py)]],
        dash=[to_q((qs, py)), to_q((qd, py))],
        fills=[(band(qs, qd, py), 5)],
        dots=[(E, 3, 8)],
        words=[curve_label("D", D, 1, 24, 4), curve_label("S", S, 1, 24, -4), ("E", E[0], E[1] - 22 + 12, 3.5), ("Max price", 128, py - 18, 3.5)],
        vals=[xlab("Qs", qs, 4), xlab("Qd", qd, 4), ("Shortage", ((qs + qd) / 2, py + 40), 5)],
        check=[("price below E", py - E[1], None), ("demand exceeds supply", qd - qs, None)]))

    # 5 minimum price
    py = E[1] - 60
    qs, qd = S.x(py), D.x(py)
    out.append(dict(
        id="minprice", name="Minimum price",
        lines=[("A minimum price above", False)],
        line2=[("equilibrium causes a ", False), ("surplus", True)],
        note=["E is equilibrium. Sellers supply Qs,", "buyers want only Qd."],
        draw=[D.pts(), S.pts(), [(XL, py), (CLIP_X[1], py)]],
        dash=[to_q((qd, py)), to_q((qs, py))],
        fills=[(band(qd, qs, py), 5)],
        dots=[(E, 3, 8)],
        words=[curve_label("D", D, 1, 24, 4), curve_label("S", S, 1, 24, -4), ("E", E[0], E[1] + 38 + 12, 3.5), ("Min price", 128, py - 18, 3.5)],
        vals=[xlab("Qd", qd, 4), xlab("Qs", qs, 4), ("Surplus", ((qs + qd) / 2, py - 44), 5)],
        check=[("price above E", E[1] - py, None), ("supply exceeds demand", qs - qd, None)]))

    # 6 indirect tax
    t = 110
    S2 = S.shift(dy=-t)
    E2 = cross(D, S2)
    pp = S.y(E2[0])
    out.append(dict(
        id="tax", name="Indirect tax",
        lines=[("An indirect tax shifts ", False), ("supply up", True)],
        line2=[("and buyers and sellers share it", False)],
        note=["S1 shifts up by the tax, to S2.", "P1: old price. Buyers pay Pc, sellers keep Pp.", "The split depends on elasticity."],
        draw=[D.pts(), S.pts()], thin=[S2.pts()],
        dash=[to_p(E), to_p(E2), [(XL, pp), (E2[0], pp)], to_q(E2)],
        marks=[],
        dots=[(E, 3, 8), (E2, 3, 8), ((E2[0], pp), 3, 8)],
        words=[curve_label("D", D, 1, 24, 4), curve_label("S1", S, 1, 24, -4), curve_label("S2", S2, 1, 24, -4), ("tax", E2[0] - 28, (E2[1] + pp) / 2 + 12 - 8, 3.5)],
        vals=[ylab("Pc", E2[1], 4), ylab("Pp", pp, 4), ylab("P1", E[1], 5)],
        check=[("tax = Pc - Pp", pp - E2[1], t), ("buyers pay more", E[1] - E2[1], None), ("sellers keep less", pp - E[1], None)]))

    # 7 subsidy
    s_ = 110
    S2 = S.shift(dy=s_)
    E2 = cross(D, S2)
    pp = S.y(E2[0])
    out.append(dict(
        id="subsidy", name="Subsidy",
        lines=[("A subsidy shifts ", False), ("supply down", True)],
        line2=[("so buyers pay less, sellers get more", False)],
        note=["S1 shifts down by the subsidy, to S2.", "P1: old price. Buyers pay Pc, sellers get Pp.", "The split depends on elasticity."],
        draw=[D.pts(), S.pts()], thin=[S2.pts()],
        dash=[to_p(E), to_p(E2), [(XL, pp), (E2[0], pp)], to_q(E2)],
        marks=[],
        dots=[(E, 3, 8), (E2, 3, 8), ((E2[0], pp), 3, 8)],
        words=[curve_label("D", D, 1, 24, 4), curve_label("S1", S, 1, 24, -4), curve_label("S2", S2, 1, 24, -4)],
        vals=[ylab("Pp", pp, 4), ylab("Pc", E2[1], 4), ylab("P1", E[1], 5)],
        check=[("subsidy = Pp - Pc", E2[1] - pp, s_), ("buyers pay less", E2[1] - E[1], None), ("sellers get more", E[1] - pp, None)]))

    # 8 negative externality
    ec = 140
    SC = S.shift(dy=-ec)
    Eo = cross(D, SC)
    tri = [Eo, (E[0], SC.y(E[0])), E]
    out.append(dict(
        id="negext", name="Negative production externality",
        lines=[("Social cost is ", False), ("above", True), (" private cost", False)],
        line2=[("so the market over-produces", False)],
        note=["A negative production externality.", "SC is PC plus the external cost.", "Qm: market output. Qo: socially optimal.", "Shaded: deadweight welfare loss."],
        draw=[D.pts(), S.pts(), SC.pts()],
        dash=[to_q(E), to_q(Eo)],
        fills=[(tri, 5)],
        dots=[(E, 3, 8), (Eo, 3, 8)],
        words=[curve_label("D", D, 1, 24, 4), curve_label("PC", S, 1, 26, -4), curve_label("SC", SC, 1, 26, -8)],
        vals=[xlab("Qo", Eo[0], 4), xlab("Qm", E[0], 4)],
        check=[("SC above PC by the external cost", S.y(250) - SC.y(250), ec), ("Qo below Qm", E[0] - Eo[0], None)]))

    # 9 positive externality
    eb = 140
    SB = D.shift(dy=-eb)
    Eo = cross(SB, S)
    tri = [E, (E[0], SB.y(E[0])), Eo]
    out.append(dict(
        id="posext", name="Positive consumption externality",
        lines=[("Social benefit is ", False), ("above", True), (" private benefit", False)],
        line2=[("so the market under-produces", False)],
        note=["A positive consumption externality.", "SB is PB plus the external benefit.", "Qm: market output. Qo: socially optimal.", "Shaded: deadweight welfare loss."],
        draw=[D.pts(), S.pts(), SB.pts()],
        dash=[to_q(E), to_q(Eo)],
        fills=[(tri, 5)],
        dots=[(E, 3, 8), (Eo, 3, 8)],
        words=[curve_label("PB", D, 1, 26, 4), curve_label("S", S, 1, 24, -4), curve_label("SB", SB, 1, 26, -4)],
        vals=[xlab("Qm", E[0], 4), xlab("Qo", Eo[0], 4)],
        check=[("SB above PB by the external benefit", D.y(250) - SB.y(250), eb), ("Qo above Qm", Eo[0] - E[0], None)]))
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
                        out.append((round(ox + (a[0] + (b[0] - a[0]) * k) * s, 1), round(oy + (a[1] + (b[1] - a[1]) * k) * s, 1)))
                        break
                    rem -= seg
                break
            dist -= L
    return out


def parts(sc, i, ox, oy, s, sw, pre, full=True, val_fs=42):
    col = color(i)
    thin_w = sw * 0.72
    wfill = ghost = lines = over = ""
    ids = dict(draw=[], thin=[], dash=[], mark=[], wedge=[], ticks=[], vals=[], words=[], dots=[], fills=[])
    for j, (poly, fb) in enumerate(sc.get("fills", [])):
        wfill += f'<path id="{pre}fl{j}" d="{path_d(poly, ox, oy, s)}Z" fill="{col}" opacity="0"/>'
        ids["fills"].append((f"{pre}fl{j}", fb))
    for j, w in enumerate(sc.get("wedges", [])):
        v, p, q = w
        arc = wedge(v, p, q)
        wfill += f'<path id="{pre}wf{j}" d="{path_d([v] + arc, ox, oy, s)}Z" fill="{BROWN}" opacity="0"/>'
        lines += f'<path id="{pre}wa{j}" d="{path_d(arc, ox, oy, s)}" pathLength="1" fill="none" stroke="{CANVAS}" stroke-width="{max(2, sw * .55):.1f}" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0"/>'
        ids["wedge"].append((f"{pre}wf{j}", f"{pre}wa{j}"))
    for p in sc["draw"]:
        ghost += f'<path d="{path_d(p, ox, oy, s)}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round"/>'
    for j, p in enumerate(sc["draw"]):
        id_ = f"{pre}d{j}"
        ids["draw"].append((id_, plen(p)))
        lines += f'<path id="{id_}" d="{path_d(p, ox, oy, s)}" pathLength="1" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0"/>'
    for j, (p, tb) in enumerate([(q, 3) for q in sc.get("thin", [])] + [(q, 5) for q in sc.get("late_thin", [])]):
        id_ = f"{pre}t{j}"
        ids["thin"].append((id_, tb))
        lines += f'<path id="{id_}" d="{path_d(p, ox, oy, s)}" pathLength="1" fill="none" stroke="{col}" stroke-width="{thin_w}" stroke-linecap="round" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0"/>'
    for j, p in enumerate(sc.get("dash", [])):
        id_ = f"{pre}h{j}"
        ids["dash"].append(id_)
        lines += f'<path id="{id_}" d="{path_d(p, ox, oy, s)}" fill="none" stroke="{col}" stroke-width="{thin_w}" stroke-dasharray="{max(4, 13 * s):.1f} {max(4, 10 * s):.1f}" opacity="0"/>'
    for j, (p, mb) in enumerate([(q, 3) for q in sc.get("marks", [])] + [(q, 5) for q in sc.get("late_marks", [])]):
        id_ = f"{pre}m{j}"
        ids["mark"].append((id_, mb))
        lines += f'<path id="{id_}" d="{path_d(p, ox, oy, s)}" fill="none" stroke="{CANVAS}" stroke-width="{max(2, sw * .55):.1f}" stroke-linejoin="round" opacity="0"/>'
    for j, (ts, b) in enumerate(sc.get("ticks", [])):
        id_ = f"{pre}k{j}"
        d = " ".join(path_d(t_, ox, oy, s) for t_ in ts)
        ids["ticks"].append((id_, b))
        lines += f'<path id="{id_}" d="{d}" fill="none" stroke="{CANVAS}" stroke-width="{max(2.4, sw * .6):.1f}" stroke-linecap="round" opacity="0"/>'
    for j, (pt, b, rad) in enumerate(sc.get("dots", [])):
        id_ = f"{pre}o{j}"
        ids["dots"].append((id_, b))
        over += f'<circle id="{id_}" cx="{ox + pt[0] * s:.1f}" cy="{oy + pt[1] * s:.1f}" r="{rad * s:.1f}" fill="{YELLOW}" opacity="0"/>'
    halo = f'paint-order="stroke" stroke="{INK}" stroke-width="{max(4, 8 * s):.0f}" stroke-linejoin="round"'
    for j, (txt, pt, b) in enumerate(sc.get("vals", [])):
        id_ = f"{pre}v{j}"
        ids["vals"].append((id_, b))
        over += (f'<text id="{id_}" x="{ox + pt[0] * s:.1f}" y="{oy + pt[1] * s + val_fs * .36:.1f}" text-anchor="middle" font-family="Poppins" '
                 f'font-weight="700" font-size="{val_fs}" fill="{CANVAS}" {halo} opacity="0">{txt}</text>')
    for j, (txt, x, y, b) in enumerate(sc.get("words", [])):
        short = len(txt) <= 3
        if full or short:
            id_ = f"{pre}w{j}"
            ids["words"].append((id_, b))
            size = (40 if short else 32) * (1 if full else 0.55)
            weight = 600 if short else 500
            fillc = CANVAS if short else BODY
            over += (f'<text id="{id_}" x="{ox + x * s:.1f}" y="{oy + y * s:.1f}" text-anchor="middle" font-family="Poppins" font-weight="{weight}" '
                     f'font-size="{size}" fill="{fillc}" {halo} opacity="0">{txt}</text>')
    return wfill, ghost, lines, over, ids


def stamp_js(sel, b):
    """Appears at 130% one frame ahead of the hit, then settles to 100% in 4 frames."""
    t0 = land(b)
    return (f"tl.set('{sel}',{{opacity:1}},{t0});tl.fromTo('{sel}',{{scale:1.3,transformOrigin:'50% 50%'}},"
            f"{{scale:1,duration:{round(4 / FPS, 4)},ease:'back.out(1.7)'}},{t0});")


def scene_timeline(sc, ids, pre, pen_dur, t_pen, ox, oy, s, ghost_at=None, exit_at=None, extra_beat=0):
    js = []
    if ghost_at is not None:
        js.append(f"tl.fromTo('#{pre}ghost',{{opacity:0}},{{opacity:.17,duration:.2,ease:'power1.out'}},{ghost_at});")
    cur = t_pen
    total = sum(L for _, L in ids["draw"])
    for id_, L in ids["draw"]:
        d = round(pen_dur * L / total, 4)
        js.append(f"tl.set('#{id_}',{{opacity:1}},{cur:.4f});tl.fromTo('#{id_}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:{d},ease:'none'}},{cur:.4f});")
        cur += d
    pen = pen_samples(sc["draw"], ox, oy, s, pen_dur)
    dt = round(pen_dur / (len(pen) - 1), 5)
    js.append(f"(()=>{{const P={json.dumps(pen, separators=(',', ':'))};tl.set('#{pre}pen',{{x:P[0][0],y:P[0][1]}},0);tl.set('#{pre}pen',{{opacity:1}},{t_pen:.4f});"
              f"P.slice(1).forEach((p,k)=>tl.to('#{pre}pen',{{x:p[0],y:p[1],duration:{dt},ease:'none'}},{t_pen:.4f}+k*{dt}));tl.set('#{pre}pen',{{opacity:0}},{t_pen + pen_dur:.4f});}})();")
    return js


def write_scene(i, sc):
    cid = f"s{i + 1:02d}"
    pre = f"{cid}-"
    ox, oy, s, sw = 265, 505, 1.1, 6
    wfill, ghost, lines, over, ids = parts(sc, i, ox, oy, s, sw, pre)
    js = ["const tl=gsap.timeline({paused:true});"]
    t_pen = land(1)
    pen_dur = round(land(3) - t_pen, 4)
    js += scene_timeline(sc, ids, pre, pen_dur, t_pen, ox, oy, s, ghost_at=0 if i == 0 else at(.5))
    if i == 0:
        js[1] = f"tl.set('#{pre}ghost',{{opacity:.17}},0);"
    t3 = land(3)
    for id_, b in ids["thin"]:
        tb = land(b)
        js.append(f"tl.set('#{id_}',{{opacity:1}},{tb});tl.fromTo('#{id_}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.26,ease:'sine.inOut'}},{tb});")
    for id_ in ids["dash"]:
        js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:1,duration:.1}},{t3});")
    for id_, b in ids["mark"]:
        js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:1,duration:.1}},{land(b)});")
    for id_, b in ids["fills"]:
        js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:.5,duration:.18,ease:'power1.out'}},{land(b)});")
    for f, a in ids["wedge"]:
        js.append(f"tl.fromTo('#{f}',{{opacity:0}},{{opacity:1,duration:.16,ease:'power1.out'}},{t3});")
        js.append(f"tl.set('#{a}',{{opacity:1}},{t3});tl.fromTo('#{a}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.2,ease:'sine.inOut'}},{t3});")
    for id_, b in ids["words"]:
        js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:1,duration:.12}},{land(b)});")
    for id_, b in ids["vals"] + ids["ticks"] + ids["dots"]:
        js.append(stamp_js(f"#{id_}", b))
    js.append(f"tl.to('#{pre}all',{{opacity:0,duration:EXIT,ease:'power2.out'}},{land(SCENE_BEATS):.4f});".replace('EXIT', str(EXIT)))
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


def write_ring():
    ox, oy, s = 265, 505, 1.1
    js = f"""const tl=gsap.timeline({{paused:true}});
tl.to('#ring-all',{{opacity:0,duration:{EXIT},ease:'power2.out'}},{land(V_RECAP):.4f});
window.__timelines['ring']=tl;"""
    lab = (f'font-family="Poppins" font-weight="600" font-size="34" fill="{BODY}"')
    (COMP / "ring.html").write_text(
        f"""<template>
<style>{FONT}#root{{position:absolute;inset:0}}</style>
<div id="root" data-composition-id="ring" data-width="1080" data-height="1920">
<svg id="ring-all" width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0" data-layout-ignore>
<path d="{path_d(AX, ox, oy, s)}" fill="none" stroke="{RING}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<text x="{ox + (XL - 20) * s}" y="{oy + (YT + 4) * s}" text-anchor="middle" {lab}>P</text>
<text x="{ox + XR * s}" y="{oy + (YB + 44) * s}" text-anchor="middle" {lab}>Q</text>
</svg>
</div>
<script>{js}</script>
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
<div id="title-box" data-layout-allow-overlap>9 market diagrams<br>for <span class="hlw">A Level Economics<span id="title-band" data-layout-allow-overflow data-layout-ignore><span>A Level Economics</span></span></span></div>
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
    (COMP / "brand.html").write_text(
        f"""<template>
<style>#root{{position:absolute;inset:0}}#logo{{position:absolute;left:420px;top:272px;width:240px;height:auto}}</style>
<div id="root" data-composition-id="brand" data-width="1080" data-height="1920" data-no-timeline>
<img id="logo" src="assets/brand/sj-academy-logo-horizontal-on-brown.svg" alt="SJ Academy">
</div>
</template>
""")


def write_recap():
    s = 0.5
    svg_all = names = ""
    js = ["const tl=gsap.timeline({paused:true});"]
    js.append(f"tl.fromTo('#rc-note',{{opacity:0}},{{opacity:1,duration:.16}},{land(2)});")
    for i, sc in enumerate(SCENES):
        col, row = i % 3, i // 3
        ox = 38 + col * 340
        oy = 392 + row * 306
        pre = f"r{i}-"
        wfill, ghost, lines, over, ids = parts(sc, i, ox, oy, s, 3.4, pre, full=False, val_fs=22)
        ringd = path_d(AX, ox, oy, s)
        svg_all += (f'<path id="{pre}ring" d="{ringd}" fill="none" stroke="{RING}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1"/>'
                    f'{wfill}<g id="{pre}ghost" opacity="0">{ghost}</g>{lines}{over}<circle id="{pre}pen" r="5" fill="{CANVAS}" opacity="0"/>')
        names += f'<div class="rn" id="{pre}nm" style="left:{ox - 30}px;top:{oy + 262}px">{sc["name"]}</div>'
        t0 = at(0) + .02 * i
        t_end = land(2)
        js.append(f"tl.fromTo('#{pre}ring',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:{land(1) - t0:.4f},ease:'sine.inOut'}},{t0:.4f});")
        js += scene_timeline(sc, ids, pre, round(t_end - land(1), 4), land(1), ox, oy, s, ghost_at=None)
        for id_, _ in ids["thin"]:
            js.append(f"tl.set('#{id_}',{{opacity:1}},{t_end});tl.fromTo('#{id_}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.2,ease:'none'}},{t_end});")
        for id_ in ids["dash"] + [m_ for m_, _ in ids["mark"]]:
            js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:1,duration:.1}},{t_end});")
        for id_, _ in ids["fills"]:
            js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:.5,duration:.12}},{t_end});")
        for f, a in ids["wedge"]:
            js.append(f"tl.fromTo('#{f}',{{opacity:0}},{{opacity:1,duration:.1}},{t_end});")
            js.append(f"tl.set('#{a}',{{opacity:1}},{t_end});tl.fromTo('#{a}',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:.14,ease:'none'}},{t_end});")
        for id_, _ in ids["vals"] + ids["ticks"] + ids["dots"]:
            js.append(stamp_js(f"#{id_}", 3))
        for id_, _ in ids["words"]:
            js.append(f"tl.fromTo('#{id_}',{{opacity:0}},{{opacity:1,duration:.12}},{t_end});")
        js.append(f"tl.fromTo('#{pre}nm',{{opacity:0,y:8}},{{opacity:1,y:0,duration:{round(5 / FPS, 4)},ease:'expo.out'}},{land(1):.4f});")
    js.append("window.__timelines['recap']=tl;")
    (COMP / "recap.html").write_text(
        f"""<template>
<style>{FONT}#root{{position:absolute;inset:0}}
#rc-note{{position:absolute;left:0;width:1080px;top:338px;text-align:center;font:600 60px/1 'Caveat';color:{YELLOW};opacity:0}}
.rn{{position:absolute;width:310px;text-align:center;font:600 28px/1.15 'Poppins';color:{YELLOW};opacity:0}}
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
    tail = EXIT + .05
    hosts = [host("ring", 0, at(V_RECAP) + tail, 3, 1), host("title", 0, at(V_RECAP) + tail, 5, 2), host("reason", 0, at(V_RECAP) + tail, 6, 3),
             host("brand", 0, at(V_END), 7, 4)]
    for i in range(len(SCENES)):
        hosts.append(host(f"s{i + 1:02d}", at(SCENE_BEATS * i), at(SCENE_BEATS) + tail, 4, 5))
    hosts.append(host("recap", at(V_RECAP), at(V_END - V_RECAP) + .1, 4, 6))
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
    write_ring()
    write_title()
    write_reason()
    write_brand()
    write_recap()
    write_end()
    total = write_index()
    print(f"built {len(SCENES)} market scenes, {total}s, music from {MEDIA_START}s")


if __name__ == "__main__":
    main()
