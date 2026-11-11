# 12 angle rules for O Level Maths

## Five-line brief
1. **Who and when:** O Level Maths (4024) students scrolling Instagram, revising geometry before a test.
2. **The one thing:** the 12 core angle rules in one saveable reel, and SJ Academy is where to use them on past papers.
3. **The idea:** each rule draws itself on the beat of a club track, the angles land on the hits, and all 12 finish on one cheat sheet.
4. **The proof:** every diagram is computed from its real angles and re-measured by the build script.
5. **Format and level:** teacher reel, 9:16, 67.5 s, Hype speed, music only.

## Where it came from
Sunyyan asked for an SJ Academy version of a MathsGenie reel ("All 12 angle rules for GCSE", in `SJ Academy Media/`). Same idea and order of rules, redrawn from scratch. Nothing is taken from the original: no art, mascot, app screens or audio.

## Decisions (Sunyyan, 9 Nov 2026)
- Ink ground, yellow lines, orange angles, canvas text. The end card switches to yellow.
- Title "12 angle rules for O Level Maths", not "Every angle rule". Syllabus topics 4.7 and 4.8 (circle theorems) are not in these 12, so "every" would be untrue.
- End card offers O Level and A Level Maths with a free demo. No teacher named: `FACTS.md` lists Sir Salman for A Level only.
- Music only. No voice.

## v1 rejected (9 Nov 2026)
Sunyyan: the music was not good and did not sync, and the video looked like an amateur edit. v1 only cut on the beat, so strokes and labels landed at arbitrary times. It started on a quiet part of the track, and the look was static (boxed captions, thin arcs, a big fixed title). v1 is in `archive/v1/`.

## How the original syncs (measured)
Each rule in the MathsGenie reel is a strict 3.18 s, 8-beat cycle: the drawing runs over the first 4 beats, each angle pops on beats 5 to 8, it fades on the last half beat, and the cut hits the next downbeat.

## How v2 syncs
- **Track:** Miromax "Club" (`miromaxmusic-club-no-copyright-618622.mp3`), 128 BPM (127.995 fitted to the kick attacks). The reel starts at 75.626 s, the first kick of the drop, so frame 1 opens on full energy.
- **Everything is in beats.** `build.py` schedules every stroke, angle, sum term, highlighted word, recap cell and end card element in beats. `sync-events.json` lists them all.
- **The cycle:** one 8-beat rule is 3.75 s. Shape on beats 0 to 3, angles land from beat 3, the result and highlighted word on beat 5, the exit finishes on the next downbeat.
- **Longer rules:** 9 and 11 run 12 beats and 12 runs 16, because they have more to read. Every cut still falls on a bar line.
- **End card** starts on beat 128, where the track's own level steps down (-5.5 to -8.6 dB), so the contact details sit on a calmer section.
- **Measured, not heard.** See "Sync check" below. Sunyyan judges the music by ear.

## Sync check (draft v2, `verify-sync.py`)
- Render audio against the track: 0.0 ms offset at five points across the reel.
- Grid against the music, averaged over 128 beats: the punch of the kick (150 to 500 Hz) peaks 1 ms after the beat, its click about 15 ms before it, and its sub body 60 to 100 ms after. All three lock to the same beat.
- Grid confirmed by structure: the level jumps on beat 0 (-9.8 to -5.5 dB) and steps down on beat 128.
- Rendered picture against the schedule, within 2 frames: cuts 100%, angles 93%, sum results 83%. Stamps ease in, so the biggest frame change can sit a frame or two from the start.
- A first grid (75.374 s) was about a quarter-second off, nearly on the off-beat, because its detector read low-level noise. A render check caught it before delivery. If this method is reused, fit the grid to envelope attacks and confirm it by band.
- Output: 1080 x 1920, 30 fps, 67.5 s, 7.7 MB, -14.1 LUFS. `check` passes; its one contrast warning is a mid-fade sample at a cut.

## Design changes in v2
- Angles are shaded wedges with a clean arc, so nothing pokes past the lines. Wedge and arc flash on the hit, then settle.
- Sums build term by term under the diagram, and the result stamps in yellow.
- Caption without a box, larger, words blur in, key word highlighted on a hit.
- Header: logo, rule counter and a 12-part progress bar. The big title holds for rule 1, then shrinks to one line.
- Faint graph-paper grid that drifts and pulses on each bar.
- Diagrams 25% larger, with parallel lines running to the frame edges.
- Yellow highlighter wipe into the recap and the end card.
- Recap lands one cell every half beat. "Save this." stamps on beat 8.

## Choices made while building
- **No sonic logo.** The prototype is synthesized, he has rejected synthesized sound, and it clashed with music on brand film v2. His call.
- **Bounce on stamps and labels:** `back.out` is used on angle labels and sum results. The playbook reserves it for stamps; these act as stamps, and he asked for more excitement.
- **Layout:** uses more height than the playbook's safe area, following his repeated note. Every word stays above y 1450, except the end card's "One class free" note.
- **Grid vignette:** a soft radial fade on the grid. The brand book allows gradients only for photo scrims, but he asked for gradients and a maths background on 10 Hacks. Remove it if he prefers.
- **Z, F and C** appear only as small handwritten memory notes. The captions use Cambridge's terms, because the syllabus expects correct terminology in reasons.
- **Licence:** "Club" was already logged for the uni-checker reel as "to confirm". Get the certificate before paid ads.

## Timing
See `timing.txt`. Rebuild with `python3 build.py`, then `npx --yes hyperframes@0.9.26 check`.

Render: `npx --yes hyperframes@0.9.26 render -o renders/raw.mp4`, then
`ffmpeg -i renders/raw.mp4 -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k "renders/12 angle rules (draft v2).mp4"`

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
| 12 | Interior angles of an n-sided polygon add up to (n − 2) × 180° | n = 6: (6 − 2) × 180° = 720° | 720; 4 numbered triangles × 180 |

## Accuracy check (9 November 2026, repeated on v2)
- **Syllabus:** wording compared with Cambridge O Level Mathematics 4024 syllabus 2025 to 2027, topic 4.6, page 28. Rules 1 to 7 and 10 are named there, and polygons (11, 12) are covered by "exterior and interior angles, and angle sum". Rules 8 and 9 are not listed by name. They are true in general and were kept from the reference.
- **Solved twice:** done for all 12 (table above). All agree.
- **Complete:** "on parallel lines", "convex" and "n-sided" are on screen. "Regular pentagon" is stated in the sum. Parallel arrows and equal-side ticks are drawn.
- **Diagrams honest:** all drawn to the proportions labelled.
- **Frames reviewed as a student:** every rule landed, recap, end card. Nothing overlaps. All reading text is 28 px or more.
- **Facts:** end card uses only `FACTS.md` claims: past-paper practice marked to the mark scheme, in class at DHA Phase 7 or online, free demo class, WhatsApp number.
- **Result:** pass on visuals and maths. **Not done:** the music was measured, not heard. Sunyyan to watch on his phone with sound before it moves to `✅ Finished/Videos/Reels & teaching/`.

## Instagram caption
12 angle rules. One reel. Save it, because your next geometry question will not wait for you to find it again.

Each rule uses the wording Cambridge expects in your reasons.

Free demo class for O Level and A Level Maths: WhatsApp +92-336-2144454

#OLevelMaths #4024 #CAIE #Geometry #Karachi
