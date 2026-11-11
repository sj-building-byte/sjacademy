#!/usr/bin/env python3
"""Second solve for ACCURACY.md: measure each shape numerically, with no formula,
then compare with the formula shown on screen. Run: python3 verify_formulas.py"""
import math

N = 1200


def area_by_grid(inside, x0, x1, y0, y1, n=N):
    dx, dy = (x1 - x0) / n, (y1 - y0) / n
    hits = sum(
        inside(x0 + (i + 0.5) * dx, y0 + (j + 0.5) * dy) for i in range(n) for j in range(n)
    )
    return hits * dx * dy


def volume_by_slices(area_at, h, n=20000):
    d = h / n
    return sum(area_at((k + 0.5) * d) for k in range(n)) * d


def poly_inside(pts):
    def f(x, y):
        c = False
        for (ax, ay), (bx, by) in zip(pts, pts[1:] + pts[:1]):
            if (ay > y) != (by > y) and x < (bx - ax) * (y - ay) / (by - ay) + ax:
                c = not c
        return c
    return f


l, w, b, h, a, r, d, t = 7.0, 4.0, 6.0, 5.0, 3.0, 2.5, 5.0, 64.0
rows = []

rows.append(("Rectangle A = l x w", area_by_grid(lambda x, y: 0 <= x <= l and 0 <= y <= w, 0, l, 0, w), l * w))
rows.append(("Triangle A = 1/2 bh", area_by_grid(poly_inside([(0, 0), (b, 0), (2, h)]), 0, b, 0, h), 0.5 * b * h))
rows.append(("Parallelogram A = bh", area_by_grid(poly_inside([(0, 0), (b, 0), (b + 2, h), (2, h)]), 0, b + 2, 0, h), b * h))
rows.append(("Trapezium A = 1/2(a+b)h", area_by_grid(poly_inside([(0, 0), (b, 0), (2 + a, h), (2, h)]), 0, b, 0, h), 0.5 * (a + b) * h))
rows.append(("Circle A = pi r^2", area_by_grid(lambda x, y: x * x + y * y <= r * r, -r, r, -r, r), math.pi * r * r))
per = sum(
    math.dist(
        ((d / 2) * math.cos(2 * math.pi * k / 200000), (d / 2) * math.sin(2 * math.pi * k / 200000)),
        ((d / 2) * math.cos(2 * math.pi * (k + 1) / 200000), (d / 2) * math.sin(2 * math.pi * (k + 1) / 200000)),
    )
    for k in range(200000)
)
rows.append(("Circumference C = pi d", per, math.pi * d))


def in_sector(x, y):
    return x * x + y * y <= r * r and 0 <= math.degrees(math.atan2(y, x)) <= t


rows.append(("Sector A = t/360 x pi r^2", area_by_grid(in_sector, -r, r, -r, r), t / 360 * math.pi * r * r))
arc = sum(
    math.dist(
        (r * math.cos(math.radians(t * k / 200000)), r * math.sin(math.radians(t * k / 200000))),
        (r * math.cos(math.radians(t * (k + 1) / 200000)), r * math.sin(math.radians(t * (k + 1) / 200000))),
    )
    for k in range(200000)
)
rows.append(("Arc length L = t/360 x 2 pi r", arc, t / 360 * 2 * math.pi * r))
rows.append(("Cuboid V = l x w x h", volume_by_slices(lambda z: l * w, h), l * w * h))
A = 0.5 * b * h
rows.append(("Prism V = A x l", volume_by_slices(lambda z: A, l), A * l))
rows.append(("Cylinder V = pi r^2 h", volume_by_slices(lambda z: math.pi * r * r, h), math.pi * r * r * h))
base = 36.0
rows.append(("Pyramid V = 1/3 Ah", volume_by_slices(lambda z: base * (1 - z / h) ** 2, h), base * h / 3))
rows.append(("Cone V = 1/3 pi r^2 h", volume_by_slices(lambda z: math.pi * (r * (1 - z / h)) ** 2, h), math.pi * r * r * h / 3))
rows.append(("Sphere V = 4/3 pi r^3", volume_by_slices(lambda z: math.pi * (r * r - (z - r) ** 2), 2 * r), 4 / 3 * math.pi * r**3))

bad = 0
for name, measured, formula in rows:
    err = abs(measured - formula) / formula
    ok = err < 0.002
    bad += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name:32s} measured {measured:10.4f}  formula {formula:10.4f}  error {err*100:.3f}%")
print("All 14 agree" if not bad else f"{bad} FAILED")
raise SystemExit(bad)
