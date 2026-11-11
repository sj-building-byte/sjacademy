# 8 angle rules for O Level Maths (Reel)

Third reel in the series after `../area-volume-formulas/` and `../circle-theorems/`. Built to the faster 128 BPM tempo (requested 10 November 2026), with 8 beats (3.75 s) per rule, whole bars only, composed synth music in D minor, and no repeated labels on the rule box.
Updated on 11 November 2026 (v2) with:
1. Centered 2x4 recap grid (equidistant 200px margins, midpoint x = 540).
2. Generous breathing space below logo (logo ends at 287px, note begins at 350px).
3. 16px angle labels along exact bisectors with >= 10px line/arc clearance across all 8 diagrams.
4. Pure black neon follow end card cutting straight from recap (no phone scene, no past papers mention).

## Five-line brief
1. **Who and when:** O Level Maths (4024) and IGCSE (0580) students scrolling in the evening, a few weeks before a test or mock exam.
2. **The one thing:** the 8 core angle rules examiners test, and the exact geometric reasons Cambridge requires (no informal "Z-angles", "F-angles" or "C-angles").
3. **The idea:** a pen traces each shape on the beat, angle arcs and labels land on the hits, and all eight draw on a 2x4 recap grid students can screenshot.
4. **The proof:** exact Cambridge syllabus wording, diagrams drawn to true coordinates, and the black neon follow end card.
5. **Format and level:** teacher reel, 9:16, 42.2 s, Clear (level 2), locked to the music. Ink ground. Original synth music composed in Python.

## Syllabus basis
The list and wording come from the Cambridge O Level Mathematics 4024 syllabus for 2025 to 2027, section 4.6 (page 28):
"calculate unknown angles using the following geometrical properties:
– angles at a point
– angles at a point on a straight line and intersecting straight lines
– vertically opposite angles
– alternate angles
– corresponding angles
– allied (co-interior) angles
– angle sum of a triangle, quadrilateral and polygons
– exterior and interior angles of a polygon"

Cambridge mark schemes explicitly require correct geometric reasons and reject colloquial names ("Z-angles", "F-angles", "C-angles"). Polygon properties are reserved for a separate polygon reel; this reel focuses on lines and triangles (the 8 deduction reasons).

| # | Rule Name | On-Screen Statement | Highlighted Key |
|---|---|---|---|
| 1 | Straight line | Angles on a straight line add up to 180° | 180° |
| 2 | At a point | Angles at a point add up to 360° | 360° |
| 3 | Vertically opposite | Vertically opposite angles are equal | equal |
| 4 | Alternate angles | Alternate angles on parallel lines are equal | equal |
| 5 | Corresponding angles | Corresponding angles on parallel lines are equal | equal |
| 6 | Allied angles | Allied angles on parallel lines add up to 180° | 180° |
| 7 | Triangle angle sum | Angles in a triangle add up to 180° | 180° |
| 8 | Triangle exterior | Exterior angle of a triangle equals the sum of opposite interior angles | opposite interior angles |

## Music and Beat Map
- **Tempo:** 128 BPM (`BEAT = 60 / 128 = 0.46875 s`).
- **Scene length:** 8 beats (3.75 s) per rule (2 full bars of 4/4).
- **Structure:**
  - Beats 0 to 64: 8 rules (8 beats each, 30.0 s).
  - Beat 24 (`V_LIFT`): Music lifts to 4-on-the-floor as parallel lines start (rule 4).
  - Beats 64 to 76: Recap (2x4 grid, 12 beats, 5.625 s).
  - Beats 76 to 90: Black neon follow end card (14 beats, 6.5625 s). Total: 42.188 s.
- **Inside each rule:**
  - Beat 0: Statement lands in box with kick and chord stab.
  - Beat 0.5: Faint ghost outline appears.
  - Beats 1 to 3: Pen dot traces the shape along its strokes.
  - Beat 3: Shape finishes; angle wedges pop and highlight strokes (Z, F, C) draw.
  - Beat 4: First angle value stamps in (scale 1.3 -> 1.0) on chord stab.
  - Beat 5: Second angle value stamps in on chord stab.
  - Beats 6 to 7.5: Synth lead answers, leading smoothly into the next rule.
  - Beat 8 (0 of next): Next rule box morphs seamlessly.

## Original Synth Music (D minor)
Composed procedurally in Python (`music/compose.py`) and normalised to -14 LUFS (`music/normalise.py`). Owned entirely by SJ Academy; no licensing required.
- **Harmony:** Dm, Bb, F, C over a low D drone (73.4 Hz).
- **Lead tone:** Round, gliding whistle-lead with 2nd harmonic at -15.9 dB and 3rd at -26.3 dB.
- **End card stabs:** Chord stabs timed to the neon tube flickers on beats 0, 1, 2.5, 3, 4, 5, 6, 7 and final chord pad on 8.
- **Measurements:**
  - Integrated Loudness: **-13.8 LUFS** (target: -14.0 LUFS).
  - True Peak: **-1.5 dBTP** (target: -1.0 dBFS or lower).

## Sync Benchmark
Measured using `../draw-reel-kit/tools/measure_sync.py`:
- **Median distance from audio hit:** **19 ms** (target: $\le 20$ ms).
- **Hits within 50 ms:** **71%** (target: $\ge 70\%$).

## Accuracy and Mathematical Verification
Script: `verify_rules.py` (run `python3 verify_rules.py`):
1. **Drawn coordinates:** Every angle, sum, and relation is measured directly from the on-screen coordinate geometry:
   - Straight line: 130° + 50° = 180° (PASS)
   - At a point: 140° + 100° + 120° = 360° (PASS)
   - Vertically opposite: 70° = 70° (PASS)
   - Alternate angles: 60° = 60° (PASS)
   - Corresponding angles: 60° = 60° (PASS)
   - Allied angles: 120° + 60° = 180° (PASS)
   - Triangle sum: 60° + 45° + 75° = 180° (PASS)
   - Triangle exterior: 50° + 70° = 120° (PASS)
2. **Randomised re-test:** Each of the 8 rules re-derived at 2,000 random configurations (seed 4024). All passed with zero mathematical gap ($< 10^{-13}$).

## Student-Perspective Audit
- **Honest diagrams:** All shapes drawn to true geometric proportion. Parallel arrows (chevrons) drawn on both parallel lines.
- **No repeated label:** The rule box contains only the statement and the highlighted key term.
- **Clear conditions:** Notes clarify parallel lines, transversal, adjacent straight line angles, and opposite interior angles.
- **2x4 Recap layout:** Fits all 8 rules in two symmetrically centered columns (col_x = [295, 785]), 16px angle values on bisectors with >= 10px clear margin to all lines and arcs.
- **End card:** Pure black neon follow card with tube flickers, Gilroy 800/500 typography, glowing rule, Poppins CTA, and PT Mono contact pills (`sjacademy.pk`, `+92-336-2144454`). No phone scene and no past papers mention anywhere.

## Render File
`renders/8_angle_rules_v2.mp4` (42.2 s, 2.9 MB, 1080x1920, 30 fps).
Approved by Sunyyan on 11 November 2026 and published to `✅ Finished/Videos/Reels & teaching/8 angle rules.mp4`. Caption in `CAPTION.txt`. Original synth music in D minor owned by SJ Academy.
