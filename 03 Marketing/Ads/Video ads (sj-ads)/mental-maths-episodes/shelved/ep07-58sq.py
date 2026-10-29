# "Solve it in your head" #7. Loaded by ../mental-maths-build.py, which provides path, FR, FR2, INK, YEL, PEN and math.
EPISODE = {
    # to scale: 58 square = 480 px, 42 square = 347.6 px, strip 16 = 132.4 px
    "slug": "mental-maths-ep07", "reviewed": "2026-10-22", "num": 7,
    "question": "Find 58² − 42².",
    "hint": "Hint: don't square<br>anything.",
    "trick": ["Difference of", "two squares."],
    "svg": "\n".join([
        '<path id="shade" d="M 300 210 L 780 210 L 780 690 L 647.6 690 L 647.6 342.4 L 300 342.4 Z" fill="#c9c4b5" opacity="0"/>',
        path("q1", "M 300 210 L 780 210 L 780 690 L 300 690 Z"),
        path("q2", "M 300 342.4 L 647.6 342.4 L 647.6 690", w=7),
        path("r1", "M 255 210 L 285 210 M 270 210 L 270 342.4 M 255 342.4 L 285 342.4", w=6, color=PEN),
    ]),
    "labels": [("lsq", "Squares", 100, 1040, 44, "pt"), ("l58", "58", 806, 984, 52, ""), ("l42", "42", 452, 918, 48, ""),
               ("lx", "?", 524, 798, 72, "x")],
    "reveal_labels": [("l16", "16", 196, 806, 60, "red")],
    "answer_at": ("lx", "1600", 466, 806, 56),
    "steps": ["a² − b² = (a + b)(a − b)", "58 + 42 = 100 and 58 − 42 = 16.", "100 × 16 = <b>1600</b>"],
    "reveal": [("fill", "shade", 1.0), ("pen", "r1", 13.3, 0.3), ("pop", "l16", 13.6)],
    "answer": "1600",
    "tip_title": "Difference of two squares",
    "tips": ["a² − b² = (a + b)(a − b)", "If a + b = 100: a² − b² = 100(a − b)", "99 × 101 = 100² − 1² = 9999"], "tipsize": 32,
    "verify": lambda: 58 ** 2 - 42 ** 2, "expect": 1600, "must_show": ["58²", "42²", "58", "42"],
    "caption": "Find 58² − 42² in 10 seconds. No pen, no calculator.\n\nIf you're squaring 58 right now, put it down. There's a one-line trick.\n\n#OLevelMaths #ALevelMaths #Algebra #CAIE #Karachi",
}
