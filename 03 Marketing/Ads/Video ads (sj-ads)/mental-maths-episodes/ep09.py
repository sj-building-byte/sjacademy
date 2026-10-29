# "Solve it in your head" #9. Loaded by ../mental-maths-build.py, which provides path, FR, FR2, INK, YEL, PEN and math.
EPISODE = {
    # approved bank (Sunyyan, 23 Oct 2026): × 25 trick. Answer hidden; layout follows the shelved x + 1/x card, arrow and box
    "slug": "mental-maths-ep09", "reviewed": "2026-10-24", "num": 9, "hide_answer": True,
    "question": "Work out 25 × 36.",
    "hint": "Hint: four 25s<br>make 100.",
    "trick": ["Don't multiply by 25.", "Use 100 ÷ 4."],
    "svg": "\n".join([
        path("q1", "M 290 220 L 790 220 Q 830 220 830 260 L 830 360 Q 830 400 790 400 L 290 400 Q 250 400 250 360 L 250 260 Q 250 220 290 220 Z", w=7),
        path("q2", "M 540 410 L 540 500", w=7),
        path("q3", "M 515 475 L 540 500 L 565 475", w=7),
        path("q4", "M 440 520 L 640 520 L 640 660 L 440 660 Z", w=7),
        path("r1", "M 540 410 L 540 500", w=9, color=PEN),
    ]),
    "labels": [("leq", "25 × 36", 352, 800, 110, ""), ("lx", "?", 513, 1100, 96, "x")],
    "reveal_labels": [("l25", "25 = 100 ÷ 4", 140, 980, 62, "red"), ("lhow", "÷ 4, then × 100", 596, 980, 62, "red")],
    "unknown": "lx",
    "steps": ["25 = 100 ÷ 4", "So × 25 means ÷ 4, then × 100.", "Now finish it in your head."],
    "reveal": [("pen", "r1", 13.3, 0.3), ("pop", "l25", 13.6), ("pop", "lhow", 14.4)],
    "answer": "900",
    "tip_title": "Worth knowing",
    "tips": ["× 25: ÷ 4, then × 100", "× 50: ÷ 2, then × 100", "× 5: ÷ 2, then × 10", "× 125: ÷ 8, then × 1000"], "tipsize": 38,
    # long multiplication vs the trick
    "verify": lambda: 36 / 4 * 100, "expect": 25 * 36,
    "must_show": ["25", "36", "×"],
    "caption": "Work out 25 × 36 in 10 seconds. No pen, no calculator.\n\nThere's a trick that turns this into one easy division. Comment your answer. Counting on your fingers is allowed, but we will know.\n\n#OLevelMaths #MentalMaths #MathsTricks #CAIE #Karachi",
}
