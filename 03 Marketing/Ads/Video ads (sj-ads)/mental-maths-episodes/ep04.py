# "Solve it in your head" #4. Loaded by ../mental-maths-build.py, which provides path, FR, FR2, INK, YEL, PEN and math.
EPISODE = {
    "slug": "mental-maths-ep04", "reviewed": "2026-10-17", "num": 4,
    "question": "Diagonal = 10 cm. Find the area.", "qsize": 56,
    "hint": "Hint: you never<br>need the side.",
    "trick": ["It's half", "of a 10 × 10 box."], "trick_hl": 1,
    "svg": "\n".join([
        '<path id="fill" d="M 540 100 L 820 380 L 540 660 L 260 380 Z" fill="#FCE004" opacity="0"/>',
        path("q1", "M 540 100 L 820 380 L 540 660 L 260 380 Z"),
        path("q2", "M 260 380 L 820 380", w=6),
        path("q3", "M 512 128 L 540 156 L 568 128", w=6),
        path("r1", "M 260 100 L 820 100 L 820 660 L 260 660 Z", w=6, color=PEN),
    ]),
    "labels": [("l10", "10 cm", 470, 870, 54, ""), ("lA", "Area = ?", 410, 1010, 60, "x"), ("lsq", "Square", 120, 596, 50, "pt")],
    "reveal_labels": [("lbox", "10 × 10 = 100", 610, 590, 50, "red")],
    "answer_at": ("lA", "50 cm²", 420, 1010, 60),
    "steps": ["The box around it is 10 × 10 = 100.", "The square fills exactly half.", "Area = 100 ÷ 2 = <b>50 cm²</b>"],
    "reveal": [("pen", "r1", 13.3, 0.5), ("pop", "lbox", 13.8), ("fill", "fill", 14.6)],
    "answer": "50 cm²",
    "tip_title": "Shortcut: area from diagonals",
    "tips": ["Square: d² ÷ 2", "Rhombus: d₁ × d₂ ÷ 2", "Kite: d₁ × d₂ ÷ 2"],
    "verify": lambda: 10 ** 2 / 2, "expect": 50, "must_show": ["square", "10 cm", "area"],
    "caption": "A square has a 10 cm diagonal. Find its area. 10 seconds.\n\nIf you just reached for √2, watch the trick.\n\n#ALevelMaths #OLevelMaths #Geometry #CAIE #Karachi",
}
