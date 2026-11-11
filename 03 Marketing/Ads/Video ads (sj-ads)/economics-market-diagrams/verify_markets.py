#!/usr/bin/env python3
"""Second solve for the market diagrams reel.
Part 1 measures every drawn diagram from its own coordinates (not from the Ln objects that built it):
equilibria are re-found by intersecting the drawn segments, and every dot, dashed line, axis label and
shaded area is checked against them.
Part 2 re-tests each rule on 2,000 random straight-line markets, by algebra.
Run: python3 verify_markets.py"""
import math
import random

import build

TOL = 0.6
fails = []


def seg_cross(p, q):
    (x1, y1), (x2, y2) = p
    (x3, y3), (x4, y4) = q
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


def y_on(seg, x):
    (x1, y1), (x2, y2) = seg
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)


def ok(name, cond):
    print(("  pass  " if cond else "  FAIL  ") + name)
    if not cond:
        fails.append(name)


def near(a, b):
    return math.dist(a, b) < TOL


def label_at(sc, txt):
    return next(pt for t, pt, _ in sc["vals"] if t == txt)


sc = {s["id"]: s for s in build.SCENES}

print("1 demand rises")
s = sc["demand"]
D1, S, D2 = s["draw"][0], s["draw"][1], s["thin"][0]
E1, E2 = seg_cross(D1, S), seg_cross(D2, S)
ok("dots sit on both equilibria", near(s["dots"][0][0], E1) and near(s["dots"][1][0], E2))
ok("D2 is right of D1 at every price", all(seg_cross(D2, [(0, y), (500, y)])[0] > seg_cross(D1, [(0, y), (500, y)])[0] for y in (100, 250, 380)))
ok("P2 above P1 (higher price)", E2[1] < E1[1] and abs(label_at(s, "P2")[1] - E2[1]) < TOL and abs(label_at(s, "P1")[1] - E1[1]) < TOL)
ok("Q2 right of Q1 (more quantity)", E2[0] > E1[0] and abs(label_at(s, "Q2")[0] - E2[0]) < TOL)
ok("labels Q1 and Q2 do not touch (gap > 60)", E2[0] - E1[0] > 60)

print("2 supply rises")
s = sc["supply"]
D, S1, S2 = s["draw"][0], s["draw"][1], s["thin"][0]
E1, E2 = seg_cross(D, S1), seg_cross(D, S2)
ok("dots sit on both equilibria", near(s["dots"][0][0], E1) and near(s["dots"][1][0], E2))
ok("P2 below P1 (price falls)", E2[1] > E1[1] and abs(label_at(s, "P2")[1] - E2[1]) < TOL)
ok("Q2 right of Q1 (quantity rises)", E2[0] > E1[0] and abs(label_at(s, "Q2")[0] - E2[0]) < TOL)
ok("labels Q1 and Q2 do not touch (gap > 60)", E2[0] - E1[0] > 60)

print("3 movement along versus shift")
s = sc["along"]
D1, D2 = s["draw"][0], s["late_thin"][0]
A, B = s["dots"][0][0], s["dots"][1][0]
ok("A and B both lie on D1", abs(y_on(D1, A[0]) - A[1]) < TOL and abs(y_on(D1, B[0]) - B[1]) < TOL)
ok("B has the lower price and the higher quantity", B[1] > A[1] and B[0] > A[0])
ok("D2 is parallel to D1 and to its right", abs((D2[1][1] - D2[0][1]) / (D2[1][0] - D2[0][0]) - (D1[1][1] - D1[0][1]) / (D1[1][0] - D1[0][0])) < 1e-9
   and seg_cross(D2, [(0, 250), (500, 250)])[0] > seg_cross(D1, [(0, 250), (500, 250)])[0])

for key, below in (("maxprice", True), ("minprice", False)):
    print(("4 maximum" if below else "5 minimum") + " price")
    s = sc[key]
    D, S, P = s["draw"]
    E = seg_cross(D, S)
    py = P[0][1]
    qd, qs = seg_cross(D, P)[0], seg_cross(S, P)[0]
    ok("E dot on the equilibrium", near(s["dots"][0][0], E))
    ok("price line is " + ("below" if below else "above") + " E", (py > E[1]) if below else (py < E[1]))
    ok("Qd and Qs labels at the curve crossings", abs(label_at(s, "Qd")[0] - qd) < TOL and abs(label_at(s, "Qs")[0] - qs) < TOL)
    ok("shortage: Qd > Qs" if below else "surplus: Qs > Qd", (qd > qs) if below else (qs > qd))
    band = s["fills"][0][0]
    ok("shaded gap runs from Qs to Qd", abs(min(p[0] for p in band) - min(qd, qs)) < TOL and abs(max(p[0] for p in band) - max(qd, qs)) < TOL)

for key, tax in (("tax", True), ("subsidy", False)):
    print(("6 indirect tax" if tax else "7 subsidy"))
    s = sc[key]
    D, S1 = s["draw"]
    S2 = s["thin"][0]
    E1, E2 = seg_cross(D, S1), seg_cross(D, S2)
    gap = y_on(S1, 250) - y_on(S2, 250)
    ok("S2 is S1 moved " + ("up" if tax else "down") + " by a constant amount", abs((y_on(S1, 150) - y_on(S2, 150)) - gap) < 1e-6 and ((gap > 0) if tax else (gap < 0)))
    pc, pp = E2[1], y_on(S1, E2[0])
    ok("Pc is where buyers pay (on D and S2)", abs(label_at(s, "Pc")[1] - pc) < TOL)
    ok("Pp is on S1 at the new quantity", abs(label_at(s, "Pp")[1] - pp) < TOL)
    ok("Pc and Pp differ by exactly the " + ("tax" if tax else "subsidy"), abs(abs(pp - pc) - abs(gap)) < TOL)
    if tax:
        ok("buyers pay more than P1 and sellers keep less: both share it", pc < E1[1] < pp)
    else:
        ok("buyers pay less than P1 and sellers get more", pc > E1[1] > pp)
    ok("P labels at least 40 apart", min(abs(pc - E1[1]), abs(pp - E1[1])) >= 40)

for key, neg in (("negext", True), ("posext", False)):
    print(("8 negative" if neg else "9 positive") + " externality")
    s = sc[key]
    D, S, X = s["draw"]
    Em = seg_cross(D, S)
    Eo = seg_cross(D, X) if neg else seg_cross(X, S)
    ok("social curve is " + ("above PC" if neg else "above PB") + " by a constant amount",
       abs((y_on(S if neg else D, 200) - y_on(X, 200)) - (y_on(S if neg else D, 300) - y_on(X, 300))) < 1e-6
       and (y_on(S if neg else D, 300) - y_on(X, 300)) > 0)
    ok("Qm and Qo labels on the two equilibria", abs(label_at(s, "Qm")[0] - Em[0]) < TOL and abs(label_at(s, "Qo")[0] - Eo[0]) < TOL)
    ok("market " + ("over" if neg else "under") + "-produces", (Em[0] > Eo[0]) if neg else (Em[0] < Eo[0]))
    tri = s["fills"][0][0]
    want = {(round(Eo[0], 1), round(Eo[1], 1)), (round(Em[0], 1), round(Em[1], 1)), (round(Em[0], 1), round(y_on(X, Em[0]), 1))}
    ok("shaded triangle = between the social curve and the private curve, from Qo to Qm",
       {(round(p[0], 1), round(p[1], 1)) for p in tri} == want)

print("random markets (2,000 each): every rule by algebra")
rng = random.Random(9708)
bad = 0
for _ in range(2000):
    a, b = rng.uniform(50, 200), rng.uniform(0.2, 3)   # demand  P = a - bQ
    c, d = rng.uniform(0, 40), rng.uniform(0.2, 3)     # supply  P = c + dQ
    if a <= c:
        continue
    q = (a - c) / (b + d); p = a - b * q
    k = rng.uniform(1, 30)
    q2 = (a + k - c) / (b + d); bad += not (q2 > q and a + k - b * q2 > p)            # demand up
    q3 = (a - c + k) / (b + d); bad += not (q3 > q and a - b * q3 < p)                  # supply up (cost down)
    pm = p - k / 4; bad += not ((a - pm) / b > (pm - c) / d)                           # max price: shortage
    pn = p + k / 4; bad += not ((pn - c) / d > (a - pn) / b)                           # min price: surplus
    t = k
    qt = (a - c - t) / (b + d)
    if qt > 0:
        pct = a - b * qt; ppt = pct - t
        bad += not (pct > p > ppt and abs(pct - ppt - t) < 1e-9)                       # tax shared
    qs_ = (a - c + t) / (b + d); pcs = a - b * qs_; pps = pcs + t
    bad += not (pcs < p < pps)                                                         # subsidy shared
    qo = (a - c - t) / (b + d); bad += not (qo < q)                                    # neg. externality
    qo2 = (a + t - c) / (b + d); bad += not (qo2 > q)                                  # pos. externality
ok("no counter-example in 2,000 random markets", bad == 0)

print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
raise SystemExit(1 if fails else 0)
