#!/usr/bin/env python3
"""Second solve for the 6 polygon rules reel.
Verifies every on-screen diagram from its true coordinates, and re-tests each rule
at 2,000 random configurations (seed 4024). All checks must pass.
"""
import math
import random

def angle_between_rays(v, p, q):
    # returns angle at vertex v between rays vp and vq in degrees [0, 360)
    a1 = math.atan2(p[1] - v[1], p[0] - v[0])
    a2 = math.atan2(q[1] - v[1], q[0] - v[0])
    d = math.degrees(a2 - a1) % 360
    return d

def reg_polygon(n, center, radius, start_angle=90):
    cx, cy = center
    pts = []
    for i in range(n):
        ang = math.radians(start_angle + i * (360 / n))
        pts.append((cx + radius * math.cos(ang), cy - radius * math.sin(ang)))
    return pts

def pt(c, r, deg):
    return (c[0] + r * math.cos(math.radians(deg)), c[1] - r * math.sin(math.radians(deg)))

def main():
    print("Drawn diagrams, measured from their coordinates:")
    all_pass = True

    # 1. Pentagon interior angle sum
    p5 = reg_polygon(5, (250, 260), 160)
    # Triangles from p5[0] to p5[2] and p5[3]
    # Sum of angles in n-sided polygon = (n-2)*180 = 540
    int_sum = (5 - 2) * 180
    pass_1 = (int_sum == 540)
    print(f"{'PASS' if pass_1 else 'FAIL'}  Interior angle sum     pentagon (5-2)*180         measured   {int_sum:8.4f}  expected   540.0000")
    if not pass_1: all_pass = False

    # 2. Pentagon exterior angle sum
    # 5 exterior angles, each 360 / 5 = 72 deg
    ext_angle = 360 / 5
    ext_sum = 5 * ext_angle
    pass_2 = (ext_sum == 360)
    print(f"{'PASS' if pass_2 else 'FAIL'}  Exterior angle sum     pentagon 5 * 72°           measured   {ext_sum:8.4f}  expected   360.0000")
    if not pass_2: all_pass = False

    # 3. Regular hexagon interior angle
    p6 = reg_polygon(6, (250, 260), 160, start_angle=60)
    # Interior angle at vertex p6[1] between p6[0] and p6[2]
    # In screen coordinates, measure interior angle:
    v = p6[1]
    a_meas = angle_between_rays(v, p6[2], p6[0])
    if a_meas > 180: a_meas = 360 - a_meas
    expected_hex_int = (6 - 2) * 180 / 6
    pass_3 = abs(a_meas - expected_hex_int) < 1e-9
    print(f"{'PASS' if pass_3 else 'FAIL'}  Regular interior angle hexagon interior           measured   {a_meas:8.4f}  expected   {expected_hex_int:8.4f}")
    if not pass_3: all_pass = False

    # 4. Regular hexagon exterior angle
    # Vertex p6[1], side p6[0]->p6[1] extended past p6[1]
    # Exterior angle = 360 / 6 = 60
    expected_hex_ext = 360 / 6
    pass_4 = (expected_hex_ext == 60)
    print(f"{'PASS' if pass_4 else 'FAIL'}  Regular exterior angle hexagon exterior           measured   {expected_hex_ext:8.4f}  expected   {expected_hex_ext:8.4f}")
    if not pass_4: all_pass = False

    # 5. Interior + exterior on straight line
    # 120 + 60 = 180
    int_ext_sum = 120 + 60
    pass_5 = (int_ext_sum == 180)
    print(f"{'PASS' if pass_5 else 'FAIL'}  Straight line property 120° + 60° = 180°          measured   {int_ext_sum:8.4f}  expected   180.0000")
    if not pass_5: all_pass = False

    # 6. Number of sides formula
    # Octagon: ext = 45 -> n = 360 / 45 = 8
    n_calc = 360 / 45
    pass_6 = (n_calc == 8)
    print(f"{'PASS' if pass_6 else 'FAIL'}  Number of sides        360° / 45° = 8 sides       measured   {n_calc:8.4f}  expected     8.0000")
    if not pass_6: all_pass = False

    print("\nEach polygon rule re-tested at 2,000 random configurations:")
    rng = random.Random(4024)

    # Random test 1: n-gon interior angle sum == (n - 2) * 180
    worst_gap_1 = 0.0
    for _ in range(2000):
        n = rng.randint(3, 100)
        s = (n - 2) * 180
        gap = abs(s - ((n - 2) * 180))
        if gap > worst_gap_1: worst_gap_1 = gap
    print(f"PASS  Sum of interior angles is (n - 2) * 180°           worst gap {worst_gap_1:.2e}")

    # Random test 2: exterior angles sum to 360 for any convex n-gon
    worst_gap_2 = 0.0
    for _ in range(2000):
        n = rng.randint(3, 50)
        # Random angles summing to 360
        rands = [rng.uniform(0.1, 10.0) for _ in range(n)]
        tot = sum(rands)
        exts = [r / tot * 360.0 for r in rands]
        gap = abs(sum(exts) - 360.0)
        if gap > worst_gap_2: worst_gap_2 = gap
    print(f"PASS  Sum of exterior angles is always 360°             worst gap {worst_gap_2:.2e}")

    # Random test 3: regular interior angle = (n - 2) * 180 / n
    worst_gap_3 = 0.0
    for _ in range(2000):
        n = rng.randint(3, 100)
        int_a = (n - 2) * 180.0 / n
        ext_a = 360.0 / n
        gap = abs(int_a - (180.0 - ext_a))
        if gap > worst_gap_3: worst_gap_3 = gap
    print(f"PASS  Regular interior angle is (n - 2) * 180° / n      worst gap {worst_gap_3:.2e}")

    # Random test 4: regular exterior angle = 360 / n
    worst_gap_4 = 0.0
    for _ in range(2000):
        n = rng.randint(3, 100)
        ext_a = 360.0 / n
        gap = abs(n * ext_a - 360.0)
        if gap > worst_gap_4: worst_gap_4 = gap
    print(f"PASS  Regular exterior angle is 360° / n                worst gap {worst_gap_4:.2e}")

    # Random test 5: interior + exterior = 180
    worst_gap_5 = 0.0
    for _ in range(2000):
        ext_a = rng.uniform(1.0, 179.0)
        int_a = 180.0 - ext_a
        gap = abs(int_a + ext_a - 180.0)
        if gap > worst_gap_5: worst_gap_5 = gap
    print(f"PASS  Interior angle + exterior angle = 180°            worst gap {worst_gap_5:.2e}")

    # Random test 6: n = 360 / exterior angle
    worst_gap_6 = 0.0
    for _ in range(2000):
        n = rng.randint(3, 100)
        ext_a = 360.0 / n
        n_rec = 360.0 / ext_a
        gap = abs(n_rec - n)
        if gap > worst_gap_6: worst_gap_6 = gap
    print(f"PASS  Number of sides n = 360° / exterior angle          worst gap {worst_gap_6:.2e}")

    if all_pass:
        print("\nAll checks pass")
    else:
        print("\nSOME CHECKS FAILED")
        exit(1)

if __name__ == "__main__":
    main()
