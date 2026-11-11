# Every circle theorem (O Level Maths reel)

Second reel in the same style as `../area-volume-formulas/`, rebuilt from a GCSE reference Sunyyan supplied on 9 November 2026 (`SJ Academy Media/Every circle theorem for GCSE...mp4`). The format is borrowed. The theorems, wording, drawings, music, colours and closing are SJ Academy's own.

## Five-line brief
1. **Who and when:** O Level Maths (4024) students scrolling in the evening, a few weeks before a test or mock.
2. **The one thing:** every circle theorem on the syllabus, and the exact words to write as the reason.
3. **The idea:** a pen draws each theorem on the beat, angle values stamp in on the drums, and all nine draw on one screen they can screenshot. A student would send it to a friend before a geometry test.
4. **The proof:** Cambridge's own syllabus wording, and the real past papers page on a real phone.
5. **Format and level:** teacher reel, 9:16, 62.1 s, Clear (level 2), locked to the music. Ink ground. v2 music is an original synth track written to the picture.

## Syllabus basis
The list and wording come from the Cambridge O Level Mathematics 4024 syllabus for 2025, 2026 and 2027, sections 4.7 and 4.8 (page 28). It lists exactly nine properties and says candidates are expected to use the properties listed in the syllabus when giving reasons. That is why "Every" is true here, and why each box shows the syllabus wording exactly. (v3 and earlier also labelled every box "Write this as your reason"; Sunyyan had it removed on 10 November 2026, because it repeated on all nine slides and is not in the reference.)

| # | On screen | Section |
|---|---|---|
| 1 | Angle at the centre is twice the angle at the circumference | 4.7 |
| 2 | Angle in a semicircle = 90° | 4.7 |
| 3 | Angles in the same segment are equal | 4.7 |
| 4 | Opposite angles of a cyclic quadrilateral sum to 180° | 4.7 |
| 5 | Angle between tangent and radius = 90° | 4.7 |
| 6 | Alternate segment theorem | 4.7 |
| 7 | Equal chords are equidistant from the centre | 4.8 |
| 8 | The perpendicular bisector of a chord passes through the centre | 4.8 |
| 9 | Tangents from an external point are equal in length | 4.8 |

The GCSE reference has eight: it says "the perpendicular from the centre bisects the chord" (not the syllabus wording) and leaves out equal chords. Check this list against the new syllabus before reusing the reel for 2028 exams.

## Music sync (what changed from the formula reel)
Sunyyan asked for better synced music. Track: "Fresh" again, because it has clear bar starts and its sections fall on exact multiples of 8 beats.

| | Formula reel | This reel |
|---|---|---|
| Scene length | 6 beats (1.5 bars), so every second shape starts mid-bar | 8 beats (2 bars), so every theorem starts on a bar start |
| Music sections | Lift on the first volume shape | Lifts on theorems 2 and 6, thinning under the end card |
| Key values | Fade in near the beat | Stamp in on the drum |
| Scene change | Fades finish before the beat | Everything starts on the bar and glides after it |
| Strong visual moments near an audio hit | Median 44 ms, 63% within 50 ms | Median 14 ms, 79% within 50 ms |

The rule that made the difference: the eye catches the moment something changes, so a move's first visible frame sits one frame ahead of the hit (`land()` in `build.py`) and the settling comes after it. Moves that start early and finish on the hit look early, even when they are technically "on the beat".

### Beat map (one beat = 60/112 s; video beat 0 = track beat 24, 12.902 s into the file)
- Beats 0 to 72: nine theorems, 8 beats each. Track lifts at video beats 8 (theorem 2) and 40 (theorem 6).
- Inside a theorem: statement on 0, ghost on 0.5, pen beats 1 to 3, angle arcs and marks on 3, first value or tick on 4, second on 5, exit on 8.
- Beats 72 to 84: recap. Beats 84 to 104: phone, one caption word per beat. Beats 104 to 116: end card, contact details landing on beat 108 as the track thins out, music fading from beat 112.

## v2 music: SJ's own synth track (10 November 2026)
Sunyyan asked to replace "Fresh" with synth music like the reference's. `music/compose.py` composes an original track in code, written to this reel's beat map, so it needs no licence and every hit is placed on purpose.

**What was taken from the reference, and what was not:** the palette only. Measured from the reference:
- a low A drone held under everything
- a gliding synth lead in the low-mid range
- short paired chord stabs
- four-on-the-floor drums
- A minor

The chords (Am, F, C, G over the A drone), the lead lines, the drum parts and the arrangement are new. No melody was copied. The tempo stays at 112 BPM, so the visuals did not change: each theorem keeps its 4.3 s.

**Written to the picture:**

| Video beats | Music |
|---|---|
| Each theorem, beat 0 | Chord stab and kick as the statement lands |
| Beats 1 to 3 | The lead glides upward while the pen draws, landing on beat 3 with the angle arcs |
| Beats 4 and 5 | Strong chord stabs on the kick and clap as the values stamp in; the lead lifts off just before each one |
| Beats 6 to 8 | The lead falls back |
| 0 | Full groove from frame 0 (no quiet intro) |
| 40 | Lift for the alternate segment theorem: pads, brighter lead, extra hats, a cymbal |
| 72 to 84 | Peak under the recap |
| 84 to 104 | Lighter under the phone captions: a soft pluck for each word as it lights |
| 104 to 116 | Cymbal on the wipe, a stab for each line of the end card, a final A minor chord ringing out |

**Measured, not heard:**

| | Circle v1 (Fresh) | Circle v2 (synth) |
|---|---|---|
| Strong visual moments: median distance from an audio hit | 14 ms | 12 ms |
| Within 50 ms of a hit | 79% | 93% |
| Loudness jump at the statement, stamp 1, stamp 2 (phone range) | +3.9, +3.4, +0.5 dB | +2.7, +1.7, +5.3 dB |
| Left on a phone speaker (above 250 Hz) | | -2.9 dB (reference -3.3) |
| Loudness, peak | -14.0 LUFS, -1.7 dBFS | -13.9 LUFS, -5.1 dBFS |

Tonal balance by section is close to the reference's. The weakest hit is the statement landing on the alternate segment theorem (no jump). Nobody has listened to the track yet: it was checked by measurement only. Synthesised music can sound cheap, so judge it on a phone before posting.

**Regenerate:** `/tmp/sj-audio/bin/python music/compose.py`, then `python3 music/normalise.py` (-14 LUFS, -1.5 dBTP), then `python3 build.py` and render. v1 (Fresh), v2 (first synth) and v3 (current) are in `renders/`.

## v3 music and slide fixes (10 November 2026)
Sunyyan said v2 was not as addictive as the reference: it felt like v1's base music, perhaps the echo. Measuring both tracks found three differences:

| | Reference | v2 | v3 |
|---|---|---|---|
| Lead tone: 2nd and 3rd harmonics against the note | -18, -26 dB (round, near whistle) | -12, -19 dB (buzzy, plus echo) | -20, -27 dB, no echo |
| Similarity to 4 bars earlier | 0.35 to 0.54 (the melody develops) | 0.93 to 0.95 (one loop) | 0.42 to 0.48 |
| Opening groove | Syncopated half-time, 42% of bass notes on the offbeat | Kick on every beat, 0% | Half-time bounce, 82% offbeat bass, then four-on-the-floor at the lift |
| Lead range | G#3 to G5, swoops of up to an octave | B3 to C5 | Up to G5, with swoops of 5 to 7 semitones into each call |
| Mid-range (600 to 2,500 Hz) | 11 to 21% | not measured | 9 to 16% |

v3 keeps every sync point:
- Statements land on a stab.
- The pen draws under the lead's rising call.
- The stamps land on strong stabs, and the lead stays silent there.

Measured, not heard:
- **Sync:** median 11 ms, 93% within 50 ms.
- **Loudness:** -13.9 LUFS, peak -4.2 dBFS.
- **Phone speaker:** loses 1.9 dB above 250 Hz (reference 3.3 dB).
- **Hits:** 23 of 26 rise clearly above the moment before (median +4.7, +2.5 and +7.8 dB). The statement on equal chords and the first stamp on the chord bisector are slightly flat.

v2's script is kept as `music/compose_v2.py`.

**Slide audit fixes (every slide checked as a student):**
- **Same segment:** the note now says "on the same side of it". Without that, two angles on the same chord but on opposite sides (which add to 180°) would wrongly look equal.
- **Angle at the centre:** the note now gives the condition, "Both angles stand on the same arc".
- **Equal chords and chord bisector:** the notes now say O is the centre, so each slide stands on its own.
- **Recap, tangent and radius:** "90°" moved off the tangent line.

All other values, all nine statements (checked word for word against the syllabus), the phone page, the captions and the end card were correct. `verify_theorems.py` still passes.

## Rebuild
- `python3 build.py` writes `index.html` and `compositions/`. Do not hand-edit the generated files.
- `python3 verify_theorems.py` re-runs the second solve.
- `npx hyperframes check`, then `npx hyperframes render --quality delivery --fps 30 --crf 15 -o renders/<name>.mp4`.

## Accuracy check (9 November 2026)
- **Solved twice:** every value and marking is measured from the coordinates actually drawn, and each theorem is re-tested at 2,000 random positions (`verify_theorems.py`). All pass. Largest gap 2e-10.
- **Question complete:** every property is stated with its condition. O is defined wherever it is labelled; cyclic, tangent point of contact and the alternate segment are explained under the box.
- **Diagram honest:** every drawing is exact, not approximate: the 50° shown is a true 50° on screen. Right-angle marks and equal-length ticks match the text.
- **Notation:** °, × and = used throughout. Wording follows the syllabus.
- **Claims:** "Every" is backed by sections 4.7 and 4.8. "Free" and "No sign-up" appear on the live page in the phone (checked 9 November 2026). "One class free" is in `FACTS.md`.
- **Watched as a student:** frame 0, all nine finished theorems, a scene change, the recap, captions, the wipe and the end card. Each makes sense alone. Labels moved clear of lines, and "chord" on the alternate segment diagram now sits beside the chord it means. Smallest reading text is 28 px.
- **Sound:** measured, not heard. v1 -14.0 LUFS, peak -1.7 dBFS. v2 -13.9 LUFS, peak -5.1 dBFS.
- **Result:** pass after the 10 November fixes (see v3 above). Sunyyan approved v4 on 10 November 2026. Final: `✅ Finished/Videos/Reels & teaching/Every circle theorem.mp4` (v4: v3 music, no "Write this as your reason" label). Earlier drafts v1 to v3 stay in `renders/`.

Music licence: v2 uses SJ's own composed track, so no licence is needed. v1 used "Fresh", which is still "to confirm" in `01 Brand/Sound/licence-log.csv`.

## v5: new end card (11 November 2026)
At Sunyyan's request, the phone scene (past papers page and captions) and the yellow demo end card are removed. The recap now cuts straight to the black neon follow end card used in every draw reel (see `draw-reel-kit/HANDOVER.md` section 9). Timing: `V_RECAP, V_END, V_STOP = 72, 84, 98` (52.5 s). The music's ending stabs moved to the end card beats. Sync is a median 17 ms, with 79% within 50 ms; -14.0 LUFS. Replaced `✅ Finished/Videos/Reels & teaching/Every circle theorem.mp4`. The caption no longer mentions past papers or the demo.
