# "Solve it in your head" #7. Loaded by ../mental-maths-build.py, which provides path, FR, FR2, INK, YEL, PEN and math.
EPISODE = {
    # simple trick (Sunyyan, 23 Oct 2026). Replaced the unposted 58² − 42² (now in mental-maths-episodes/shelved).
    # Redone 24 Oct 2026 (Sunyyan): no diagram, ask 45² directly, 5-second countdown, a cleaner tile reveal.
    # Own template and timing: 21 s, countdown 2.2-7.2 s, reveal 7.6-17 s, end card 17-21 s.
    "slug": "mental-maths-ep07", "reviewed": "2026-10-24", "num": 7, "hide_answer": True,
    "template": "mental-maths-template-ep07.html", "seconds": 5,
    "question": "What is 45 × 45?",
    "hint": "Hint: look at<br>the last digit.",
    "trick": ["Squaring a number", "that ends in 5."],
    "svg": "", "labels": [("lhero", "45²", 0, 0, 0, "")], "reveal_labels": [("lnl", "4 × (4 + 1)", 0, 0, 0, ""), ("lnr", "always 25", 0, 0, 0, ""), ("ltl", "4 × 5", 0, 0, 0, ""), ("ltr", "25", 0, 0, 0, "")],
    "unknown": None,
    "steps": ["Times the 4 by the next number up.", "Write 25 on the end.", "Now finish it in your head."],
    "reveal": [],
    "answer": "2025",
    "tip_title": "Works for any whole number ending in 5",
    "tips": ["25²: 2 × 3 = 6, then 25: 625", "65²: 6 × 7 = 42, then 25: 4225", "115²: 11 × 12 = 132, then 25: 13225"],
    "tip_rows": [("25²", "2 × 3", "625"), ("65²", "6 × 7", "4225"), ("115²", "11 × 12", "13225")],
    # the trick vs the long way, checked for every whole number ending in 5 up to 995 and for each tip row
    "verify": lambda: (4 * 5 * 100 + 25) if all((n // 10) * (n // 10 + 1) * 100 + 25 == n * n for n in range(5, 1000, 10))
              and all(int(s) * int(s) == int(r) for s, r in (("25", "625"), ("65", "4225"), ("115", "13225"))) else -1,
    "expect": 45 ** 2,
    "must_show": ["45²", "45 × 45"],
    "caption": "Find 45² in 5 seconds. No pen, no calculator.\n\nThere's a trick for every number that ends in 5. Learn it once and you'll never multiply 45 × 45 the long way again.\n\nComment your answer.\n\n#OLevelMaths #MentalMaths #MathsTricks #CAIE #Karachi",
}
