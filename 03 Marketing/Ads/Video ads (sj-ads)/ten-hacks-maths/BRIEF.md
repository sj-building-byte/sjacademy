# 10 Hacks: Maths (episode 1 of the "10 Hacks" series)

## Five-line brief
1. **Who and when:** O Level and A Level maths students scrolling Instagram in the evening, a few weeks before a test.
2. **The one thing:** ten mental shortcuts they can use in their next maths test, and SJ Academy is where they came from.
3. **The idea:** a countdown from 01 to 10 where the numbers do the trick themselves: digits split, drop in and stamp the answer. Worth saving as a cheat sheet.
4. **The proof:** every hack is worked through on screen, and every one has been checked (below).
5. **Format and level:** teacher reel, 9:16, 96 s, Teach speed with a fast opening.

## Design (final v4, 26 Oct 2026; older looks in archive/: v1-brown, v2-busy, v3-calm. v4 = v3 calm + flat brand yellow + brand orange accents)
- Sunyyan rejected v1: boring brown background, logo crammed against the counter, basic type, no real transitions, no excitement. He asked for colour, gradients and a creative maths background (a deliberate departure from the playbook's no-gradient rule).
- Ground: navy radial gradient, two soft glows that change to each hack's accent colour, a faint masked grid, and a drifting chalk layer (Caveat formulas, parabola, sine wave, unit circle, number line, big operators) moving up with parallax.
- One accent per hack (ACC in build.py): notes, arrows, glows, rail segment and the transition panel. Brand yellow-to-orange gradient for the counter, highlights and answer stamps.
- Layout: logo at y 280, counter at y 440 (about 100 px gap), title and "HACK / 10" to its right, gradient divider, rule, then the worked example in a frosted card (y 880 to 1390). Captions centred below at y about 1460 to 1580.
- Transitions: a full-screen hit before every hack (0.6 s): accent panel sweeps in diagonally, giant number slams in with the hack name, burst lines, whoosh plus impact, then the number flies into the counter as the panel sweeps off. Same hit into the recap ("Cheat sheet").
- Motion: masked title rise, items pop in with blur and overshoot, digits drop with a bounce, answer stamp with a gold box, glow and an expanding ring.
- Voice, music and timing unchanged from v1; the hits add 6.6 s (102.7 s total).

## How to make the next episode
1. Copy this folder (for example `ten-hacks-chemistry`) and delete `voice/*.wav`, `renders/`, `.review/`.
2. Write the new lines in `voice/lines.txt` (i1, h1a/h1b ... h10a/h10b, o1, o2) and run `./make-voice.sh`.
3. Edit `episode.py` (titles, rules, board items and events; see the comments at the top) and run `python3 build.py`.
4. `npx --yes hyperframes@0.8.167 check`, snapshot, render (command in REVIEW.md).

## The ten hacks, answers and checks
Each was solved twice: by the hack and by direct calculation (Python), and each general rule was tested over a full range.

| # | Example | Hack working | Direct check | Rule tested |
|---|---|---|---|---|
| 1 | 34 × 11 | 3 \| 3+4 \| 4 = 374 | 374 | every two-digit number (carry case 78 × 11 = 858 shown) |
| 2 | 68 × 5 | 680 ÷ 2 = 340 | 340 | always true (× 5 = × 10 ÷ 2) |
| 3 | 37 × 99 | 3700 − 37 = 3663 | 3663 | always true (× 99 = × 100 − × 1) |
| 4 | 8% of 50 | 50% of 8 = 4 | 4 | x% of y = xy/100 = y% of x |
| 5 | 5247 | 5+2+4+7 = 18, divisible by 9 and 3 | 5247 = 9 × 583 | n from 1 to 100 000, for 3 and 9 |
| 6 | 49 × 51 | 50² − 1² = 2499 | 2499 | (m − g)(m + g) = m² − g² |
| 7 | 52² | 25+2 = 27, 2² = 04, 2704 | 2704 | (50 + d)² = 100(25 + d) + d², d from −9 to 9 (41² to 59²) |
| 8 | 1/3 + 1/5 | (3+5)/(3×5) = 8/15 | 8/15 | a, b from 1 to 29 with exact fractions |
| 9 | 100, +10%, −10% | 110, then 99 | 100 × 1.1 × 0.9 = 99 | always × 0.99 |
| 10 | legs 6 and 8 | 3, 4, 5 × 2 gives 10 | √(36 + 64) = 10 | 3-4-5, 5-12-13, 8-15-17, 7-24-25 all satisfy a² + b² = c² |

## Accuracy check (24 October 2026)
- Solved twice: done for all ten (table above). All agree.
- Question complete: every condition is on screen ("two-digit" for × 11, "right-angled" for triples, "(50 + d)²" and "41² to 59²" for near-50 squares, "one on top" for fractions).
- Diagram honest: the triangle is drawn to scale (6 : 8 : 10 at 40 px a unit) with a right-angle mark.
- Tips true in general: the recap rows are full identities or state their condition.
- Frames reviewed as a student: each hack's question, working and answer, the recap and the end card (`.review/`). Nothing overlaps; all reading text is 36 px or more.
- Result: pass. To do before posting: Sunyyan watches on his phone with sound.

## Instagram caption
10 maths hacks your calculator would rather you didn't know.

From × 11 in your head to the percentage trap hiding in exam questions. Save this for your next maths test, then tell us which one was new to you.

#OLevelMaths #ALevelMaths #MentalMaths #MathsTricks #CAIE #Karachi
