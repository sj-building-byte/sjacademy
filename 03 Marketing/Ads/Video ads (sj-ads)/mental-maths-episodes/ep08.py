# "Solve it in your head" #8. Loaded by ../mental-maths-build.py, which provides path, FR, FR2, INK, YEL, PEN and math.
EPISODE = {
    # simple angle question (Sunyyan, 23 Oct 2026). To scale: O (520, 400), r 280; A at 145°, B at 35°, C at 250°, so angle AOB = 110°
    "slug": "mental-maths-ep08", "reviewed": "2026-10-23", "num": 8, "hide_answer": True,
    "question": "O is the centre. Find x.",
    "hint": "Hint: look<br>at O.",
    "trick": ["The centre angle", "is double."],
    "svg": "\n".join([
        path("q1", "M 520 120 A 280 280 0 1 1 519.9 120", w=7),
        path("q2", "M 290.6 560.6 L 520 400 L 749.4 560.6", w=7),
        path("q3", "M 290.6 560.6 L 424.2 136.9 L 749.4 560.6"),
        path("q4", "M 569.1 434.4 A 60 60 0 0 1 470.9 434.4", w=6),
        path("q5", "M 466.8 192.4 A 70 70 0 0 1 403.2 203.6", w=6),
        '<circle id="q6" cx="520" cy="400" r="9" fill="#151515"/>',
        path("r1", "M 569.1 434.4 A 60 60 0 0 1 470.9 434.4", w=8, color=PEN),
        path("r2", "M 466.8 192.4 A 70 70 0 0 1 403.2 203.6", w=8, color=PEN),
    ]),
    "labels": [("lA", "A", 232, 1110, 52, "pt"), ("lB", "B", 776, 1110, 52, "pt"), ("lC", "C", 384, 628, 52, "pt"),
               ("lO", "O", 536, 898, 44, "pt"), ("l110", "110°", 476, 1028, 44, ""), ("lx", "x", 426, 776, 64, "x")],
    "reveal_labels": [("l2x", "= 2x", 478, 1074, 54, "red")],
    "unknown": "lx",
    "steps": ["x and 110° both stand on arc AB.", "Centre angle = 2 × edge angle.", "Now finish it in your head."],
    "reveal": [("pen", "r1", 13.3, 0.3), ("pen", "r2", 13.6, 0.3), ("pop", "l2x", 13.9)],
    "answer": "x = 55°",
    "tip_title": "Circle theorems worth knowing",
    "tips": ["Same arc: centre angle = 2 × edge angle", "Angle in a semicircle = 90°", "Tangent and radius meet at 90°"], "tipsize": 32,
    # angle at C measured from the drawn points vs half the centre angle
    "verify": lambda: round(math.degrees(math.atan2(560.6 - 136.9, 290.6 - 424.2) - math.atan2(560.6 - 136.9, 749.4 - 424.2)), 1),
    "expect": 110 // 2,
    "must_show": ["centre", "110°", "x"],
    "caption": "O is the centre of the circle. Find x in 10 seconds. No pen, no calculator.\n\nOne circle theorem does all the work. Comment your answer, then count how many people overthought it.\n\n#OLevelMaths #CircleTheorems #Geometry #CAIE #Karachi",
}
