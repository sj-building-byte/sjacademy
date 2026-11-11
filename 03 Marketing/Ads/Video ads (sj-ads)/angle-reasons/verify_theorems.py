#!/usr/bin/env python3
"""Second solve for ACCURACY.md. Measures every value and marking from the coordinates
that are actually drawn in the reel, then re-derives each theorem at many random
positions. Run: python3 verify_theorems.py"""
import math
import random

from build import SCENES, O, P, R, angle_at

bad = 0

print("Drawn diagrams, measured from their coordinates:")
for sc in SCENES:
    for name, measured, expected in sc["check"]:
        ok = abs(measured - expected) < 1e-6
        bad += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {sc['name']:22s} {name:26s} measured {measured:10.4f}  expected {expected:10.4f}")

print("\nEach theorem re-tested at 2,000 random positions:")
random.seed(4024)
N = 2000


def tally(name, fn):
    global bad
    worst = 0.0
    for _ in range(N):
        worst = max(worst, abs(fn()))
    ok = worst < 1e-6
    bad += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name:58s} worst gap {worst:.2e}")


def ordered(n):
    return sorted(random.uniform(0, 360) for _ in range(n))


def centre():
    a, b = ordered(2)
    if b - a >= 180:
        a, b = b - 360, a  # keep the minor arc between a and b
    c = random.uniform(b + 1, a + 359)
    return angle_at(O, P(a), P(b)) - 2 * angle_at(P(c), P(a), P(b))


def semicircle():
    a = random.uniform(0, 360)
    c = a + random.uniform(1, 179)
    return angle_at(P(c), P(a), P(a + 180)) - 90


def segment():
    a, b = ordered(2)
    c = random.uniform(b + .5, a + 359.5)
    d = random.uniform(b + .5, a + 359.5)
    return angle_at(P(c), P(a), P(b)) - angle_at(P(d), P(a), P(b))


def cyclic():
    p, q, r, s = ordered(4)
    return angle_at(P(p), P(q), P(s)) + angle_at(P(r), P(q), P(s)) - 180


def tangent_radius():
    a = random.uniform(0, 360)
    t = P(a)
    along = (t[0] + 100 * math.sin(math.radians(a)), t[1] + 100 * math.cos(math.radians(a)))
    return angle_at(t, O, along) - 90


def alternate():
    t_deg = random.uniform(0, 360)
    arc = random.uniform(5, 175)  # minor arc from the contact point to the chord's other end
    t, b = P(t_deg), P(t_deg + arc)
    # tangent direction on the same side as b
    along = (t[0] - 100 * math.sin(math.radians(t_deg)), t[1] - 100 * math.cos(math.radians(t_deg)))
    a = P(t_deg + arc + random.uniform(1, 360 - arc - 1))
    return angle_at(t, along, b) - angle_at(a, t, b)


def equal_chords():
    half = random.uniform(5, 85)
    a, b = random.uniform(0, 360), random.uniform(0, 360)
    m1 = ((P(a - half)[0] + P(a + half)[0]) / 2, (P(a - half)[1] + P(a + half)[1]) / 2)
    m2 = ((P(b - half)[0] + P(b + half)[0]) / 2, (P(b - half)[1] + P(b + half)[1]) / 2)
    return math.dist(O, m1) - math.dist(O, m2)


def bisector():
    a, b = ordered(2)
    p, q = P(a), P(b)
    m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    # O must lie on the line through m at 90 degrees to the chord
    return (O[0] - m[0]) * (q[0] - p[0]) + (O[1] - m[1]) * (q[1] - p[1])


def external():
    d = random.uniform(R * 1.05, R * 4)
    dirn = random.uniform(0, 360)
    e = (O[0] + d * math.cos(math.radians(dirn)), O[1] - d * math.sin(math.radians(dirn)))
    al = math.degrees(math.acos(R / d))
    return math.dist(e, P(dirn + al)) - math.dist(e, P(dirn - al))


for name, fn in [
    ("Angle at the centre is twice the angle at the circumference", centre),
    ("Angle in a semicircle = 90", semicircle),
    ("Angles in the same segment are equal", segment),
    ("Opposite angles of a cyclic quadrilateral sum to 180", cyclic),
    ("Angle between tangent and radius = 90", tangent_radius),
    ("Alternate segment theorem", alternate),
    ("Equal chords are equidistant from the centre", equal_chords),
    ("Perpendicular bisector of a chord passes through the centre", bisector),
    ("Tangents from an external point are equal in length", external),
]:
    tally(name, fn)

print("\nAll checks pass" if not bad else f"\n{bad} FAILED")
raise SystemExit(bad)
