# "Solve it in your head" #8. Loaded by ../mental-maths-build.py, which provides path, FR, FR2, INK, YEL, PEN and math.
EPISODE = {
    # answer hidden (Sunyyan, 22 Oct 2026): trick and method shown, the viewer finishes it and comments
    "slug": "mental-maths-ep08", "reviewed": "2026-10-22", "num": 8, "hide_answer": True,
    "question": f"Find x² + {FR2}.",
    "hint": "Hint: don't<br>solve for x.",
    "trick": ["Don't solve for x.", "Square it."],
    "svg": "\n".join([
        path("q1", "M 290 220 L 790 220 Q 830 220 830 260 L 830 360 Q 830 400 790 400 L 290 400 Q 250 400 250 360 L 250 260 Q 250 220 290 220 Z", w=7),
        path("q2", "M 540 410 L 540 500", w=7),
        path("q3", "M 515 475 L 540 500 L 565 475", w=7),
        path("q4", "M 440 520 L 640 520 L 640 660 L 440 660 Z", w=7),
        path("r1", "M 540 410 L 540 500", w=9, color=PEN),
    ]),
    "labels": [("lgiven", "Given", 250, 722, 40, "pt"), ("leq", f"x + {FR} = 5", 340, 808, 96, ""), ("lx", "?", 513, 1100, 96, "x")],
    "reveal_labels": [("lsq2", "square both sides", 580, 985, 52, "red"), ("lmid", "middle term = 2", 662, 1120, 54, "red")],
    "unknown": "lx",
    "steps": [f"Square it: (x + {FR})² = 25", f"x² + 2 + {FR2} = 25", "Now finish it in your head."],
    "reveal": [("pen", "r1", 13.3, 0.3), ("pop", "lsq2", 13.6), ("pop", "lmid", 14.4)],
    "answer": "23",
    "tip_title": "Worth knowing",
    "tips": [f"(x + {FR})² = x² + 2 + {FR2}", f"(x − {FR})² = x² − 2 + {FR2}", f"For x ≠ 0: x × {FR} = 1"], "tipsize": 40,
    "verify": lambda: ((5 + math.sqrt(21)) / 2) ** 2 + 1 / ((5 + math.sqrt(21)) / 2) ** 2, "expect": 23,
    "must_show": ["x + ", "= 5", "find x² + "],
    "caption": "x + 1/x = 5. Find x² + 1/x² in 10 seconds, without finding x.\n\nComment your answer. If you reached for the quadratic formula, we can tell.\n\n#ALevelMaths #OLevelMaths #Algebra #CAIE #Karachi",
}
