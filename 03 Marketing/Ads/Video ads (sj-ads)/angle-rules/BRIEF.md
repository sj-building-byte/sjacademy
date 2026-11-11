# 12 angle rules for O Level Maths

Second reel in the maths series with "14 area and volume formulas". Rebuilt from a reference reel Sunyyan dropped in on 9 November 2026 (`SJ Academy Media/All 12 angle rules for GCSE...mp4`, a GCSE reel for another maths brand). The format is borrowed. The copy, drawings, music, colours and closing are SJ Academy's own.

## Five-line brief
1. **Who and when:** O Level Maths (4024) students scrolling in the evening, a few weeks before a test or mock.
2. **The one thing:** the 12 core angle rules in one saveable reel, and SJ Academy is where to use them on past papers.
3. **The idea:** a pen draws each rule on the beat while its sum lands, then all 12 draw at once on one screen they can screenshot.
4. **The proof:** every diagram drawn to its real angles and checked twice, and the real past papers page on a real phone.
5. **Format and level:** teacher reel, 9:16, 57.9 s, Clear (level 2), on the beat. Ink ground.

## Versions
- **v1 (`archive/v1/`):** rejected. Weak music, only the cuts on the beat, amateur look.
- **v2 (`archive/v2/`):** "fine", but over-designed: flashing wedges, pulsing grid, progress bar, stamps, club track.
- **v3 (this):** Sunyyan pointed to the 14 formulas reel as what he expected. Rebuilt on that reel's `build.py`, so the two read as one series.

## Same as the 14 formulas reel
Title with highlighter, centred logo, ghost outline, pen dot at constant speed, formula box that morphs size and colour on the beat, definition under the box, alternating yellow and orange, screenshot recap in two columns, phone with the live 4024 past papers page, word-by-word captions, yellow end card, "Fresh".

## What is different here
- **Angles:** each arc and orange wedge draws into place and lands on the beat with its label. Enclosed shapes fill brown on beat 3.
- **Z, F and C:** on the parallel-line rules, the base lines are a neutral hairline and the shape draws over them in colour on beat 3.
- **The box** holds the rule's name and its worked sum. The rule in words sits underneath.
- **Recap** shows each rule's name and result. Each drawing is fitted to its cell.
- **End card** says "Knowing the rule is the easy part. Join our Maths classes. One class free. Then decide." The chip reads "O LEVEL AND A LEVEL MATHS", as Sunyyan chose.
- **Title:** "12", not "every". Syllabus topics 4.7 and 4.8 (circle theorems) are not in this set.

## Timing (all multiples of one beat, 60/112 s)
- Beats 0 to 72: the 12 rules, 6 beats each (3.21 s; the reference is 3.18 s). Triangles start at beat 36 (19.3 s), on the music's bass lift.
- Beats 72 to 82: recap. Beats 82 to 100: phone and captions. Beats 100 to 108: end card, music fading from beat 105.
- Inside a rule: sum on beat 0, ghost on 0.5, pen beats 1 to 3, highlight, marks and fill on 3, angles on 3.5, 4 and 4.5 (quarter beats when there are four or more), fade ending just before beat 6.

## Music
- "Fresh" (`bransboynd-fresh-457883.mp3`), the same track as the 14 formulas reel, for the series. It starts at its beat 28 (15.045 s) and ends on its beat 136, a bar line.
- Three gain steps even out the track, as on the 14 formulas reel.
- The reference's own track was not used: it is not licensed to SJ. Licence is "to confirm" in `01 Brand/Sound/licence-log.csv`, so get the certificate before a paid ad.
- No sound effects and no sonic logo.

## Sync check (`verify_sync.py`)
- Render audio against the track: 0.0 ms offset at four points.
- Grid against the music, on the rendered audio averaged over 100 beats: the click peaks 12 ms after the beat, the sub 39 ms after.
- Bass lift confirmed on beat 36: the level steps from -13 to -8 dB.
- First angle or number of each rule, in the rendered picture: median +32 ms from its beat. 10 of 12 are within 2 frames.
- Sound measured, not heard. Sunyyan judges by ear.

## Rebuild
- `python3 build.py` writes `index.html` and `compositions/`, and stops if the maths check fails. Do not hand-edit generated files.
- `npx --yes hyperframes@0.9.26 check`, then `npx --yes hyperframes@0.9.26 render --quality delivery --fps 30 -o "renders/<name>.mp4"`.

## Known trade-offs
- Five rules with long wording (co-interior, isosceles, exterior angle, polygon exterior and interior) are on screen for about 3.1 s, under the 3.5 to 4 s reading floor. Strict 6-beat cycles are the format, and all 12 return in the recap to screenshot.
- `check` passes with no errors. Lint reports 73 warnings, not all reviewed one by one. The ones read were these reading holds and a hidden-dash note on the phone's circle, which the frames show is not visible.

## The rules, answers and checks
Solved twice: by the rule, and by `check_maths()` in `build.py`, which stops the build if a label, a total, or a corner measured from the drawn coordinates disagrees.

| # | Rule on screen | Example | Check |
|---|---|---|---|
| 1 | Angles on a straight line add up to 180° | 130° + 50° | 180 |
| 2 | Angles at a point add up to 360° | 140° + 100° + 120° | 360 |
| 3 | Vertically opposite angles are equal | 70° = 70° | lines drawn at ±35° |
| 4 | Alternate angles on parallel lines are equal | 60° = 60° | transversal drawn at 60° |
| 5 | Corresponding angles on parallel lines are equal | 60° = 60° | transversal drawn at 60° |
| 6 | Co-interior angles on parallel lines add up to 180° | 120° + 60° | 180 |
| 7 | Angles in a triangle add up to 180° | 60° + 45° + 75° | corners measured 60, 45, 75 |
| 8 | Base angles of an isosceles triangle are equal | 70° = 70° | corners measured 70, 70; equal sides ticked |
| 9 | The exterior angle of a triangle equals the sum of the two opposite interior angles | 50° + 70° = 120° | corners measured 50, 70, 60; 180 − 60 = 120 |
| 10 | Angles in a quadrilateral add up to 360° | 70° + 100° + 80° + 110° | corners measured 70, 100, 80, 110 |
| 11 | The exterior angles of a convex polygon add up to 360° | Regular pentagon: 5 × 72° | 360; each side turns 72° at each corner |
| 12 | Interior angles of an n-sided polygon add up to (n − 2) × 180° | Hexagon: (6 − 2) × 180° | 720; 4 numbered triangles × 180 |

## Accuracy check (9 November 2026, repeated on v3)
- **Syllabus:** wording compared with Cambridge O Level Mathematics 4024 syllabus 2025 to 2027, topic 4.6, page 28. Rules 1 to 7 and 10 are named there, and polygons (11, 12) are covered by "exterior and interior angles, and angle sum". Rules 8 and 9 are not listed by name. They are true in general and were kept from the reference.
- **Solved twice:** done for all 12 (table above). All agree.
- **Complete:** "on parallel lines", "convex", "n-sided" and "Regular pentagon" are on screen. Parallel arrows and equal-side ticks are drawn.
- **Diagrams honest:** all drawn to the proportions labelled. The hexagon's diagonals give 4 triangles.
- **Terms:** Cambridge's terms in every rule. Z, F and C appear only as "Look for the Z shape", because the syllabus expects correct terminology in reasons.
- **Claims:** "Free" and "No sign-up" are on the live page in the phone. "One class free" and the WhatsApp number match the 14 formulas reel, `FACTS.md` and the playbook.
- **Frames reviewed as a student:** frame 0, each landed rule, mid-draw frames, recap, end card. Nothing overlaps.
- **Result:** pass on visuals and maths. **Not done:** sound measured, not heard. Sunyyan to approve before it moves to `✅ Finished/Videos/Reels & teaching/`.

## Instagram caption
12 angle rules. One reel. Screenshot the recap, because your next geometry question will not wait for you to find it again.

Each rule uses the wording Cambridge expects in your reasons.

Free demo class for O Level and A Level Maths: WhatsApp +92-336-2144454

#OLevelMaths #4024 #CAIE #Geometry #Karachi
