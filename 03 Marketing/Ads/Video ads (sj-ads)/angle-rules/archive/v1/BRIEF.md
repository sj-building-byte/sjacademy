# 12 angle rules for O Level Maths

## Five-line brief
1. **Who and when:** O Level Maths (4024) students scrolling Instagram, revising geometry before a test.
2. **The one thing:** the 12 core angle rules in one saveable reel, and SJ Academy is where to use them on past papers.
3. **The idea:** each rule draws itself on a dark board, with the wording Cambridge uses, then all 12 land on one cheat sheet.
4. **The proof:** every diagram is computed from its real angles and re-measured by the build script.
5. **Format and level:** teacher reel, 9:16, 60.7 s, Teach speed, music only.

## Where it came from
Sunyyan asked for an SJ Academy version of a MathsGenie reel ("All 12 angle rules for GCSE", in `SJ Academy Media/`). Same idea and order of rules, redrawn from scratch. Nothing is taken from the original: no art, mascot, app screens or audio.

## Decisions (Sunyyan, 9 Nov 2026)
- Ink ground, yellow lines, orange angle arcs, canvas text. The end card switches to yellow.
- Title "12 angle rules for O Level Maths", not "Every angle rule". Syllabus topics 4.7 and 4.8 (circle theorems) are not in these 12, so "every" would be untrue.
- End card offers O Level and A Level Maths with a free demo. No teacher named: `FACTS.md` lists Sir Salman for A Level only.
- Music only. No voice.

## Choices made while building
- **No sonic logo.** The question to Sunyyan mentioned one. It was left out because the prototype is synthesized, he has rejected synthesized sound, and it clashed with music on brand film v2. Say if he wants it back.
- **Music:** Nastelbom, `nastelbom-no-copyright-music-602445.mp3`, measured at a steady 168 BPM. Every cut lands on a beat (0.714 s units). Not used in any earlier video. Logged in `01 Brand/Sound/licence-log.csv` as "to confirm".
- **Layout:** uses more height than the playbook's safe area, following his repeated note on full-page layouts. Every word stays above y 1450. Only the end card's "One class free" note and protractor sit lower, and neither carries needed information.
- **Z, F and C** appear only as small handwritten memory notes. The captions use Cambridge's terms, because the syllabus expects correct terminology in reasons.
- **Improvements on the original:** a sum line under each "add up to" rule; recap shows name and result instead of tiny labels, which overlapped in the original.

## Timing
See `timing.txt`. Rebuild with `python3 build.py`, then `npx --yes hyperframes@0.9.26 check`.

Render: `npx --yes hyperframes@0.9.26 render -o renders/raw.mp4`, then
`ffmpeg -i renders/raw.mp4 -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k "renders/12 angle rules (draft).mp4"`

Draft measured: 1080 x 1920, 30 fps, 60.8 s, 4.2 MB, -13.4 LUFS, peak -1.3 dB, no silent gaps. Check passes with no warnings.

## The rules, answers and checks
Solved twice: by the rule, and by `check_angles()` in `build.py`, which stops the build if a labelled value, a total, or a corner measured from the drawn coordinates disagrees.

| # | Rule on screen | Example | Check |
|---|---|---|---|
| 1 | Angles on a straight line add up to 180° | 130° + 50° | 180 |
| 2 | Angles at a point add up to 360° | 140° + 100° + 120° | 360 |
| 3 | Vertically opposite angles are equal | 70°, 70° | lines drawn at ±35° |
| 4 | Alternate angles on parallel lines are equal | 60°, 60° | transversal drawn at 60° |
| 5 | Corresponding angles on parallel lines are equal | 60°, 60° | transversal drawn at 60° |
| 6 | Co-interior angles on parallel lines add up to 180° | 120° + 60° | 180 |
| 7 | Angles in a triangle add up to 180° | 60° + 45° + 75° | corners measured 60, 45, 75 |
| 8 | Base angles of an isosceles triangle are equal | 70°, 70° | corners measured 70, 70; equal sides ticked |
| 9 | The exterior angle of a triangle equals the sum of the two opposite interior angles | 50° + 70° = 120° | corners measured 50, 70, 60; 180 − 60 = 120 |
| 10 | Angles in a quadrilateral add up to 360° | 70° + 100° + 80° + 110° | corners measured 70, 100, 80, 110 |
| 11 | The exterior angles of a convex polygon add up to 360° | Regular pentagon: 5 × 72° | 360; 360 ÷ 5 = 72 |
| 12 | Interior angles of an n-sided polygon add up to (n − 2) × 180° | Hexagon: n = 6, (6 − 2) × 180° | 720; 4 numbered triangles × 180 |

## Accuracy check (9 November 2026)
- **Syllabus:** wording compared with Cambridge O Level Mathematics 4024 syllabus 2025 to 2027, topic 4.6, page 28. Rules 1 to 7 and 10 are named there, and polygons (11, 12) are covered by "exterior and interior angles, and angle sum". Rules 8 and 9 are not listed by name. They are true in general and were kept from the reference.
- **Solved twice:** done for all 12 (table above). All agree.
- **Complete:** "on parallel lines", "convex" and "n-sided" are on screen. "Regular" is stated for the pentagon. Parallel arrows and equal-side ticks are drawn.
- **Diagrams honest:** all drawn to the proportions labelled. Review caught and fixed a wrong hexagon diagonal that did not give 4 triangles.
- **Frames reviewed as a student:** every rule landed and mid-draw samples, recap, end card. Nothing overlaps. All reading text is 28 px or more.
- **Facts:** end card uses only `FACTS.md` claims: past-paper practice marked to the mark scheme, in class at DHA Phase 7 or online, free demo class, WhatsApp number.
- **Result:** pass on visuals and maths. **Not done:** the mix was measured, not heard. Sunyyan to watch on his phone with sound before it moves to `✅ Finished/Videos/Reels & teaching/`.

## Before paid ads
Get the Pixabay licence certificate for the track.

## Instagram caption
12 angle rules. One reel. Save it, because your next geometry question will not wait for you to find it again.

Each rule uses the wording Cambridge expects in your reasons. 
Free demo class for O Level and A Level Maths: WhatsApp +92-336-2144454

#OLevelMaths #4024 #CAIE #Geometry #Karachi
