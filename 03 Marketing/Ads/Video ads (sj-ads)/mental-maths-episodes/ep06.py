# "Solve it in your head" #6. Loaded by ../mental-maths-build.py, which provides path, FR, FR2, INK, YEL, PEN and math.
EPISODE = {
    "slug": "mental-maths-ep06", "reviewed": "2026-10-17", "num": 6,
    "question": "Find the shaded area.",
    "hint": "Hint: does the<br>top point matter?",
    "trick": ["The top point", "doesn't matter."],
    "svg": "\n".join([
        '<path id="shade" d="M 270 570 L 390 210 L 810 570 Z" fill="#c9c4b5" opacity="0"/>',
        path("q1", "M 270 210 L 810 210 L 810 570 L 270 570 Z"),
        path("q2", "M 270 570 L 390 210 L 810 570", w=7),
        path("r1", "M 390 210 L 390 570", w=6, color=PEN),
    ]),
    "labels": [("lrect", "Rectangle", 270, 700, 50, "pt"), ("l12", "12 cm", 474, 1146, 52, ""), ("l8", "8 cm", 830, 923, 52, ""),
               ("lA", "Area = ?", 414, 982, 52, "x")],
    "reveal_labels": [],
    "answer_at": ("lA", "48 cm²", 404, 984, 50),
    "steps": ["Same base, same height.", "So it's exactly half the rectangle.", "12 × 8 ÷ 2 = <b>48 cm²</b>"],
    "reveal": [("fill", "shade", 1.0), ("pen", "r1", 13.3, 0.4)],
    "answer": "48 cm²",
    "tip_title": "Triangle area facts",
    "tips": ["Area = ½ × base × height", "Same base and height: equal area", "Same base and height as a rectangle: half its area"], "tipsize": 32,
    "verify": lambda: 12 * 8 / 2, "expect": 48, "must_show": ["rectangle", "12 cm", "8 cm", "shaded"],
    "caption": "A 12 cm by 8 cm rectangle and a shaded triangle. Find the shaded area in 10 seconds.\n\nThe top point looks important. It isn't.\n\n#OLevelMaths #ALevelMaths #Geometry #CAIE #Karachi",
}
