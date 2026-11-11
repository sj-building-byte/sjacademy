# 6 polygon rules for O Level Maths (Reel)

Fourth reel in the series after `../area-volume-formulas/`, `../circle-theorems/`, and `../angle-reasons/`.
Built to the driving 150 BPM tempo requested by Sunyyan on 11 November 2026, matching the reference track's groove (Am -> F -> C -> G, 4-on-the-floor kick, bouncy off-beat bass, soaring lead harmonics) with 8 beats (3.20 s) per rule, whole bars only, composed synth music, symmetrical 2x3 recap grid, clear angle/formula values with halos, and black neon follow end card.

## Five-line brief
1. **Who and when:** O Level Maths (4024) and IGCSE (0580) students revising geometry before paper 1 and paper 2.
2. **The one thing:** the 6 core polygon rules examiners test, covering interior angles, exterior angles, regular polygons, straight-line supplementary angles, and the number-of-sides formula.
3. **The idea:** a pen traces each polygon on the beat, angle wedges pop, values stamp on the chord hits, and all 6 draw simultaneously on a 2x3 recap grid students can screenshot.
4. **The proof:** verified mathematical geometry from true coordinates (error < 10⁻¹³), exact Cambridge syllabus formulas, and black neon follow end card.
5. **Format and level:** teacher reel, 9:16, 29.6 s, Clear (level 2), locked to the 150 BPM music. Ink ground. Original synth music composed in Python.

## Syllabus basis
Cambridge O Level Mathematics 4024 (and IGCSE 0580), section 4.6 (Geometrical terms and relationships):
"calculate unknown angles using the following geometrical properties:
– angle sum of a triangle, quadrilateral and polygons
– exterior and interior angles of a polygon"

| # | Rule Name | On-Screen Statement | Highlighted Key |
|---|---|---|---|
| 1 | Interior angle sum | Sum of interior angles equals (n - 2) × 180° | (n - 2) × 180° |
| 2 | Exterior angle sum | Sum of exterior angles is always 360° | 360° |
| 3 | Regular interior angle | Interior angle of regular polygon equals (n - 2) × 180° / n | (n - 2) × 180° / n |
| 4 | Regular exterior angle | Exterior angle of regular polygon equals 360° / n | 360° / n |
| 5 | Interior + exterior | Interior + exterior angle always add up to 180° | 180° |
| 6 | Number of sides | Number of sides of regular polygon n = 360° / exterior angle | 360° / exterior angle |

## Music and Beat Map
- **Tempo:** 150 BPM (`BEAT = 60 / 150.0 = 0.400 s`).
- **Scene length:** 8 beats (3.200 s) per rule (2 full bars of 4/4).
- **Structure:**
  - Beats 0 to 48: 6 polygon rules (8 beats each, 19.20 s).
  - Beat 24 (`V_LIFT`): Music lifts to 4-on-the-floor driving beat on scene 4 (regular exterior angle).
  - Beats 48 to 60: Recap (2x3 symmetrical grid, 12 beats, 4.80 s).
  - Beats 60 to 74: Black neon follow end card (14 beats, 5.60 s). Total: 29.60 s.
- **Inside each rule:**
  - Beat 0: Statement lands in box with kick and chord stab.
  - Beat 0.5: Faint ghost outline appears.
  - Beats 1 to 3: Pen dot traces the polygon strokes.
  - Beat 3: Polygon completes; angle wedges pop and highlight lines draw.
  - Beat 4: First angle value stamps in (scale 1.3 -> 1.0) on chord stab.
  - Beat 5: Second angle/side value stamps in on chord stab.
  - Beats 6 to 7.5: Synth lead answers, carrying forward into the next rule.
  - Beat 8 (0 of next): Next rule box morphs seamlessly.

## Original Synth Music (A minor)
Composed by `music/compose.py` and loudness normalized by `music/normalise.py`:
- Key: A minor (Am -> F -> C -> G), 150 BPM.
- Harmonic spectrum: lead 2nd harmonic at -16.0 dB, 3rd at -29.4 dB (reference: -17.7 dB, -25.1 dB).
- Bass: 28% offbeat onsets with tight 4-on-the-floor kick in lift zone.
- Loudness: -14.22 LUFS (target -14 LUFS), -8.49 dBTP peak.
- 100% original, fully owned by SJ Academy.

## Quality Checks
- `verify_polygons.py`: All 6 rules passed on drawn coordinates and 2,000 randomized configurations (worst gap < 10⁻¹³).
- `hyperframes check`: 0 errors across runtime, layout, contrast (28/28 passed), motion, craft, and audio.
- Audio sync: Median error 6 ms (target ≤ 20 ms), tested with `measure_sync.py`.
- Render: `renders/polygon_rules_v1.mp4` (29.6 s, 1080x1920, 30 fps, 2.2 MB).
