# "Solve it in your head" #3. Loaded by ../mental-maths-build.py, which provides path, FR, FR2, INK, YEL, PEN and math.
EPISODE = {
    "slug": "mental-maths-ep03", "reviewed": "2026-10-17", "num": 3,
    "question": "Interior angle = 160°. Find n.", "qsize": 54,
    "hint": "Hint: step<br>outside.",
    "trick": ["Use the", "exterior angle."], "trick_hl": 1,
    "svg": None,  # filled below (regular 18-gon)
    "labels": [("l160", "160°", 486, 1110, 54, ""), ("ln", "n = ?", 440, 780, 84, "x"), ("lnd", "Regular polygon with n sides", 170, 890, 48, "pt")],
    "reveal_labels": [("l20", "20°", 672, 1236, 54, "red")],
    "answer_at": ("ln", "n = 18", 410, 780, 84),
    "steps": ["Exterior = 180 − 160 = 20°.", "Exterior angles add to 360°.", "n = 360 ÷ 20 = <b>18</b>"],
    "reveal": [("pen", "r1", 13.3, 0.35), ("pen", "r2", 13.6, 0.25), ("pop", "l20", 13.8)],
    "answer": "n = 18",
    "tip_title": "Exterior angles worth knowing",
    "tips": ["n = 360 ÷ exterior angle", "Hexagon: 60°", "Octagon: 45°", "Decagon: 36°"],
    "verify": lambda: 360 / (180 - 160), "expect": 18, "must_show": ["regular", "interior", "160°", "n sides"],
    "caption": "A regular polygon has interior angles of 160°. Find n, the number of sides. 10 seconds, no calculator.\n\nMost people start with the interior angle formula. Don't.\n\n#ALevelMaths #OLevelMaths #Polygons #CAIE #Karachi",
}

# episode 3: part of a regular 18-gon (centre (540, 200), r 480) so the sides can't be counted; bottom vertex at (540, 680)
def vtx(deg):
    return 540 + 480 * math.cos(math.radians(deg)), 200 + 480 * math.sin(math.radians(deg))
arc = [vtx(a) for a in range(30, 151, 20)]
edge = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in arc)
rx, ry = vtx(10); lx, ly = vtx(170)
EPISODE["svg"] = "\n".join([
    path("q1", edge, w=7),
    f'<path id="dl" d="M {arc[-1][0]:.1f} {arc[-1][1]:.1f} L {lx:.1f} {ly:.1f}" fill="none" stroke="#9b9b9b" stroke-width="6" stroke-linecap="round" stroke-dasharray="4 18" opacity="0"/>',
    f'<path id="dr" d="M {arc[0][0]:.1f} {arc[0][1]:.1f} L {rx:.1f} {ry:.1f}" fill="none" stroke="#9b9b9b" stroke-width="6" stroke-linecap="round" stroke-dasharray="4 18" opacity="0"/>',
    # interior angle at the bottom vertex (540, 680)
    path("q2", "M 589.2 671.3 A 50 50 0 0 0 490.8 671.3", w=6),
    # extend the side through the bottom vertex, then the exterior angle
    path("r1", "M 540 680 L 658.2 700.9", w=6, color=PEN),
    path("r2", "M 608.9 692.2 A 70 70 0 0 0 608.9 667.8", w=6, color=PEN),
])
