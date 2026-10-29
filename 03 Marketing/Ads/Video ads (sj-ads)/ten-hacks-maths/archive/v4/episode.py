# "10 Hacks" series, episode: maths. Built by build.py (python3 build.py).
# Voice lines live in voice/lines.txt; every timing below is anchored to a voice clip:
#   ("a", 0.5) = halfway through the hack's first clip, ("b", 0.9) = near the end of the second, 0.3 = 0.3 s into the scene.
# Board coordinates are frame pixels (1080 x 1920). Text, words and the brief: BRIEF.md.
from build import row, frac, note, arrow, path, text

SUBJECT = "Maths"
INTRO = {
    "voice": "i1",
    "big": "10",
    "title": ["maths ", "hacks"],          # second word gets the highlighter
    "sub": "No calculator. No long working.",
    "ticker": "34 × 11 = 374   •   68 × 5 = 340   •   37 × 99 = 3663   •   8% of 50 = 4   •   49 × 51 = 2499   •   52² = 2704   •   ",
}

# ---------------------------------------------------------------- the ten hacks
H = []

# 1. × 11
A = row(790, 112, [("a3", "3"), ("a4", "4"), ("ax", " × 11")])
B = row(925, 128, [("b3", "3"), ("b7", "7"), ("b4", "4")])
H.append(dict(
    title="× 11", rule=[("Two-digit numbers: the digit sum goes ", 0), ("in the middle", 1)],
    items=A + B + [
        note("n7", "← 3 + 4", B[-1]["x1"] + 36, 925),
        text("c1", "Sum 10 or more? Carry the 1:  78 × 11 = 858", 90, 1062, 38, 500, "dim"),
    ],
    events=[
        (0.35, "in", ["a3", "a4", "ax"]),
        (("a", 0.25), "hl_rule"),
        (("a", 0.5), "from", "b3", "a3"), (("a", 0.5), "from", "b4", "a4"),
        (("a", 0.5), "dim", ["a3", "a4", "ax"]),
        (("a", 0.78), "drop", "b7"), (("a", 0.82), "note", "n7"),
        (("b", 0.62), "stamp", ["b3", "b7", "b4"]),
        (("b", 1.0), "in", ["c1"]),
    ]))

# 2. × 5
A = row(790, 112, [("a68", "68"), ("ax", " × 5")])
B = row(925, 120, [("b68", "68"), ("b0", "0"), ("bd", " ÷ 2")])
C = row(1060, 120, [("ce", "= "), ("cr", "340")])
H.append(dict(
    title="× 5", rule=[("Multiply by 10, ", 0), ("then halve it", 1)],
    items=A + B + C + [note("n0", "← × 10", B[-1]["x1"] + 36, 925)],
    events=[
        (0.35, "in", ["a68", "ax"]),
        (("a", 0.2), "hl_rule"),
        (("a", 0.45), "from", "b68", "a68"), (("a", 0.45), "dim", ["a68", "ax"]),
        (("a", 0.6), "drop", "b0"), (("a", 0.64), "note", "n0"),
        (("a", 0.85), "in", ["bd"]),
        (("b", 0.55), "in", ["ce"]), (("b", 0.8), "stamp", ["cr"]),
    ]))

# 3. × 99
A = row(790, 112, [("a37", "37"), ("ax", " × 99")])
B = row(925, 120, [("b37", "37"), ("b00", "00"), ("bm", " − "), ("b37b", "37")])
C = row(1060, 120, [("ce", "= "), ("cr", "3663")])
H.append(dict(
    title="× 99", rule=[("Multiply by 100, then ", 0), ("take the number away once", 1)],
    items=A + B + C,
    events=[
        (0.35, "in", ["a37", "ax"]),
        (("a", 0.2), "hl_rule"),
        (("a", 0.4), "from", "b37", "a37"), (("a", 0.52), "drop", "b00"),
        (("a", 0.8), "in", ["bm"]), (("a", 0.84), "from", "b37b", "a37"),
        (("a", 0.84), "dim", ["a37", "ax"]),
        (("b", 0.58), "in", ["ce"]), (("b", 0.82), "stamp", ["cr"]),
    ]))

# 4. percentages swap
A = row(790, 112, [("a8", "8%"), ("aof", " of "), ("a50", "50")])
S = row(790, 112, [("s50", "50%"), ("sof", " of "), ("s8", "8")])
B = row(940, 120, [("be", "= "), ("b4", "4")])
H.append(dict(
    title="% swap", rule=[("x% of y ", 0), ("= y% of x", 1)],
    items=A + S + B + [note("nh", "50% is just half", B[-1]["x1"] + 50, 940)],
    events=[
        (0.35, "in", ["a8", "aof", "a50"]),
        (("a", 0.35), "hl_rule"),
        (("b", 0.08), "swap", {"s50": "a50", "sof": "aof", "s8": "a8"}),
        (("b", 0.45), "in", ["be"]), (("b", 0.55), "note", "nh"),
        (("b", 0.85), "stamp", ["b4"]),
    ]))

# 5. divisible by 3 or 9
A = row(790, 112, [("a5", "5"), ("a2", "2"), ("a4", "4"), ("a7", "7")])
B = row(925, 96, [("b5", "5"), ("p1", " + "), ("b2", "2"), ("p2", " + "), ("b4", "4"), ("p3", " + "), ("b7", "7")])
C = row(1060, 120, [("ce", "= "), ("cr", "18")])
H.append(dict(
    title="÷ 3 or ÷ 9?", rule=[("Add the digits. If the total divides, ", 0), ("so does the number", 1)],
    items=A + B + C + [note("nd", "divides by 9 and by 3", A[-1]["x1"] + 50, 790)],
    events=[
        (0.35, "in", ["a5", "a2", "a4", "a7"]),
        (("a", 0.25), "hl_rule"),
        (("a", 0.6), "from", "b5", "a5"), (("a", 0.64), "from", "b2", "a2"),
        (("a", 0.68), "from", "b4", "a4"), (("a", 0.72), "from", "b7", "a7"),
        (("a", 0.75), "in", ["p1", "p2", "p3"]),
        (("b", 0.3), "in", ["ce"]), (("b", 0.38), "stamp", ["cr"]),
        (("b", 0.7), "stamp", ["a5", "a2", "a4", "a7"]), (("b", 0.78), "note", "nd"),
    ]))

# 6. either side of a round number
A = row(790, 112, [("a49", "49"), ("ax", " × "), ("a51", "51")])
B = row(925, 120, [("b50", "50²"), ("bm", " − "), ("b1", "1²")])
C = row(1060, 120, [("ce", "= "), ("cr", "2499")])
H.append(dict(
    title="Either side", rule=[("Square the middle, then ", 0), ("take away the gap squared", 1)],
    items=A + B + C + [note("ng", "50 − 1 and 50 + 1", A[-1]["x1"] + 50, 790)],
    events=[
        (0.35, "in", ["a49", "ax", "a51"]),
        (("a", 0.15), "note", "ng"),
        (("a", 0.35), "hl_rule"),
        (("a", 0.5), "in", ["b50"]), (("a", 0.8), "in", ["bm", "b1"]),
        (("b", 0.45), "in", ["ce"]), (("b", 0.8), "stamp", ["cr"]),
    ]))

# 7. squares near 50
A = row(790, 112, [("a52", "52²")])
B = row(925, 112, [("bl", "25 + 2"), ("bb", "  |  "), ("br", "2²")])
C = row(1060, 120, [("ce", "= "), ("c27", "27"), ("c04", "04")])
H.append(dict(
    title="Near 50²", rule=[("For (50 + d)², write ", 0), ("25 + d, then d²", 1), (" as two digits", 0)],
    items=A + B + C + [
        note("nd", "d = 2", A[-1]["x1"] + 50, 790),
        note("nr", "works for 41² to 59²", 520, 1060, 44),
    ],
    events=[
        (0.35, "in", ["a52"]),
        (("a", 0.2), "note", "nd"),
        (("a", 0.4), "hl_rule"),
        (("a", 0.45), "in", ["bl"]), (("a", 0.82), "in", ["bb", "br"]),
        (("b", 0.15), "in", ["ce"]),
        (("b", 0.22), "from", "c27", "bl"), (("b", 0.42), "from", "c04", "br"),
        (("b", 0.78), "stamp", ["c27", "c04"]),
        (("b", 1.0), "note", "nr"),
    ]))

# 8. adding unit fractions
FA = frac("a", "1", "3", 90, 835, 96) + [text("ap", " + ", None, 860, 96, 700)]
FA[-1]["x"] = FA[2]["x1"] + 4
FA[-1]["x1"] = FA[-1]["x"] + FA[-1]["w"]
FA += frac("c", "1", "5", FA[-1]["x1"] + 4, 835, 96)
EQ = text("be", "= ", 90, 1080, 96, 700)
FB = frac("b", "3 + 5", "3 × 5", EQ["x1"], 1080, 84)
EQ2 = text("ce", " = ", FB[2]["x1"] + 8, 1080, 96, 700)
FC = frac("r", "8", "15", EQ2["x1"], 1080, 96)
H.append(dict(
    title="1/a + 1/b", rule=[("New top: add the bottoms. ", 0), ("New bottom: multiply them", 1)],
    items=FA + [EQ] + FB + [EQ2] + FC,
    events=[
        (0.35, "in", ["an", "abar", "ad", "ap", "cn", "cbar", "cd"]),
        (("a", 0.3), "in", ["be", "bbar"]),
        (("a", 0.45), "from", "bn", "ad"), (("a", 0.55), "hl_rule"),
        (("a", 0.78), "from", "bd", "cd"),
        (("b", 0.3), "in", ["ce", "rbar"]), (("b", 0.4), "in", ["rn", "rd"]),
        (("b", 0.75), "stamp", ["rn", "rbar", "rd"]),
    ]))

# 9. the percentage trap
A = row(790, 112, [("a100", "100"), ("gap1", "            "), ("a110", "110")])
B = row(940, 112, [("b110", "110"), ("gap2", "            "), ("b99", "99")])
H.append(dict(
    title="The % trap", rule=[("Up 10% then down 10% is ", 0), ("not back to the start", 1)],
    items=[i for i in A + B if not i["id"].startswith("gap")] + [
        arrow("ar1", A[0]["x1"] + 40, 800, A[2]["x"] - A[0]["x1"] - 80),
        arrow("ar2", B[0]["x1"] + 40, 950, B[2]["x"] - B[0]["x1"] - 80),
        note("l1", "+10%", A[0]["x1"] + 70, 725, 46),
        note("l2", "−10% of 110", B[0]["x1"] + 24, 872, 42),
        text("c1", "Overall: × 1.1 × 0.9 = × 0.99", 90, 1068, 44, 500, "dim"),
    ],
    events=[
        (0.35, "in", ["a100"]),
        (("a", 0.25), "draw", "ar1"), (("a", 0.3), "note", "l1"), (("a", 0.45), "in", ["a110"]),
        (("a", 0.55), "hl_rule"),
        (("b", 0.15), "from", "b110", "a110"),
        (("b", 0.45), "draw", "ar2"), (("b", 0.5), "note", "l2"),
        (("b", 0.8), "in", ["b99"]), (("b", 0.86), "stamp", ["b99"]),
        (("b", 1.0), "in", ["c1"]),
    ]))

# 10. Pythagorean triples. Triangle to scale: legs 6 and 8, 40 px a unit.
Ox, Oy = 130, 1050
H.append(dict(
    title="Triples", rule=[("In a right-angled triangle, ", 0), ("learn these by heart", 1)],
    items=[
        path("tri", f"M{Ox} {Oy - 240} L{Ox} {Oy} L{Ox + 320} {Oy} Z", 960),
        path("sq", f"M{Ox} {Oy - 34} L{Ox + 34} {Oy - 34} L{Ox + 34} {Oy}", 68, width=5),
        text("l6", "6", Ox - 62, Oy - 120, 64, 700),
        text("l8", "8", Ox + 145, Oy + 50, 64, 700),
        text("lq", "?", Ox + 175, Oy - 175, 72, 700),
        text("l10", "10", Ox + 168, Oy - 175, 72, 700),
        text("t1", "3, 4, 5", 590, 760, 54, 600),
        text("t2", "5, 12, 13", 590, 845, 54, 600),
        text("t3", "8, 15, 17", 590, 930, 54, 600),
        text("t4", "7, 24, 25", 590, 1015, 54, 600),
        note("nx", "3, 4, 5 × 2", 590, 1092, 46),
    ],
    events=[
        (0.3, "draw", "tri"), (0.6, "draw", "sq"), (0.7, "in", ["l6", "l8", "lq"]),
        (("a", 0.3), "hl_rule"),
        (("a", 0.62), "in", ["t1"]), (("a", 0.86), "in", ["t2"]), (("a", 0.97), "in", ["t3", "t4"]),
        (("b", 0.3), "stamp", ["t1"]), (("b", 0.36), "note", "nx"),
        (("b", 0.6), "out", ["lq"]), (("b", 0.7), "stamp", ["l10"]),
    ]))

HACKS = H

RECAP = {
    "voice": "o1",
    "title": "Your cheat sheet",
    "rows": [
        "× 11 (two digits): digit sum in the middle",
        "× 5: × 10, then halve",
        "× 99: × 100, then take the number away",
        "x% of y = y% of x",
        "÷ 3 or ÷ 9: check the digit sum",
        "(m − g)(m + g) = m² − g²",
        "(50 + d)² = 100(25 + d) + d²",
        "1/a + 1/b = (a + b)/ab",
        "+10% then −10% = 1% less",
        "3, 4, 5 · 5, 12, 13 · 8, 15, 17",
    ],
}
END = {
    "voice": "o2",
    "lines": ["Which one was", "new to you?"],
    "cta": "Comment below",
    "handle": "@sjacademypk",
}
