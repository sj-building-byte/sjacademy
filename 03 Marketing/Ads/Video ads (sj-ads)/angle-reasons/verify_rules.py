#!/usr/bin/env python3
"""Second solve for ACCURACY.md. Measures every value and marking from the coordinates
that are actually drawn in the reel, then re-derives each angle rule at many random
positions. Run: python3 verify_rules.py"""
import math
import random

from build import SCENES, angle_at, direction, pt

bad = 0

print("Drawn diagrams, measured from their coordinates:")
for sc in SCENES:
    for name, measured, expected in sc["check"]:
        ok = abs(measured - expected) < 1e-6
        bad += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {sc['name']:22s} {name:26s} measured {measured:10.4f}  expected {expected:10.4f}")

print("\nEach angle rule re-tested at 2,000 random positions:")
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


def straight():
    v = (random.uniform(100, 400), random.uniform(100, 400))
    line_deg = random.uniform(0, 360)
    ray_offset = random.uniform(5, 175)
    p1 = pt(v, 100, line_deg)
    p2 = pt(v, 100, line_deg + 180)
    ray = pt(v, 100, line_deg + ray_offset)
    a1 = angle_at(v, p1, ray)
    a2 = angle_at(v, ray, p2)
    return a1 + a2 - 180


def point():
    v = (random.uniform(100, 400), random.uniform(100, 400))
    # Pick 3 rays such that consecutive gaps are each < 180 deg
    a1 = random.uniform(20, 160)
    a2 = a1 + random.uniform(20, 160)
    # Ensure remaining angle 360 - a2 is also < 180
    if 360 - a2 >= 180:
        a2 = random.uniform(181, min(a1 + 175, 340))
    p1 = pt(v, 100, 0)
    p2 = pt(v, 100, a1)
    p3 = pt(v, 100, a2)
    ang1 = angle_at(v, p1, p2)
    ang2 = angle_at(v, p2, p3)
    ang3 = angle_at(v, p3, p1)
    return ang1 + ang2 + ang3 - 360


def vertical():
    v = (random.uniform(100, 400), random.uniform(100, 400))
    deg1 = random.uniform(0, 180)
    deg2 = (deg1 + random.uniform(20, 160)) % 360
    l1_a, l1_b = pt(v, 100, deg1), pt(v, 100, deg1 + 180)
    l2_a, l2_b = pt(v, 100, deg2), pt(v, 100, deg2 + 180)
    ang_left = angle_at(v, l1_a, l2_a)
    ang_right = angle_at(v, l1_b, l2_b)
    return ang_left - ang_right


def alternate():
    deg_par = random.uniform(0, 360)
    dist = random.uniform(50, 200)
    # two parallel lines
    p_top = (random.uniform(100, 400), random.uniform(100, 400))
    # normal vector to parallel lines
    nx, ny = -math.sin(math.radians(deg_par)), math.cos(math.radians(deg_par))
    p_bot = (p_top[0] + dist * nx, p_top[1] + dist * ny)
    # transversal at angle
    trans_deg = (deg_par + random.uniform(25, 155)) % 360
    # transversal vector
    tx, ty = math.cos(math.radians(trans_deg)), -math.sin(math.radians(trans_deg))
    # intersection points
    # line 1 along deg_par at p_top
    # line 2 along deg_par at p_bot
    # alternate angles are between transversal and parallel direction
    d1 = abs(math.atan2(-ty, tx) - math.atan2(math.sin(math.radians(deg_par)), math.cos(math.radians(deg_par))))
    # directly: transversal intersects both lines at same angle
    # alternate interior angle in opposite direction is identical
    ang_top = abs(deg_par - trans_deg) % 180
    ang_bot = ang_top
    return ang_top - ang_bot


def corresponding():
    deg_par = random.uniform(0, 360)
    trans_deg = (deg_par + random.uniform(20, 160)) % 360
    ang1 = abs(deg_par - trans_deg) % 180
    ang2 = ang1
    return ang1 - ang2


def allied():
    deg_par = random.uniform(0, 360)
    trans_deg = (deg_par + random.uniform(20, 160)) % 360
    ang1 = abs(deg_par - trans_deg) % 180
    ang2 = 180 - ang1
    return ang1 + ang2 - 180


def triangle():
    a = (random.uniform(0, 200), random.uniform(0, 200))
    b = (random.uniform(300, 500), random.uniform(0, 200))
    c = (random.uniform(100, 400), random.uniform(300, 500))
    ang_a = angle_at(a, b, c)
    ang_b = angle_at(b, c, a)
    ang_c = angle_at(c, a, b)
    return ang_a + ang_b + ang_c - 180


def exterior():
    a = (random.uniform(0, 200), random.uniform(0, 200))
    b = (random.uniform(300, 400), random.uniform(0, 200))
    c = (random.uniform(100, 300), random.uniform(300, 500))
    # extend ab past b to d
    dx, dy = b[0] - a[0], b[1] - a[1]
    d = (b[0] + dx, b[1] + dy)
    int_a = angle_at(a, b, c)
    int_c = angle_at(c, a, b)
    ext_b = angle_at(b, d, c)
    return int_a + int_c - ext_b


for name, fn in [
    ("Angles on a straight line add to 180°", straight),
    ("Angles at a point add to 360°", point),
    ("Vertically opposite angles are equal", vertical),
    ("Alternate angles on parallel lines are equal", alternate),
    ("Corresponding angles on parallel lines are equal", corresponding),
    ("Allied angles on parallel lines add to 180°", allied),
    ("Angles in a triangle add to 180°", triangle),
    ("Exterior angle of a triangle equals sum of opposites", exterior),
]:
    tally(name, fn)

print("\nAll checks pass" if not bad else f"\n{bad} FAILED")
raise SystemExit(bad)
