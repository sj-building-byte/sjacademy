# 14 area and volume formulas (O Level Maths reel)

Rebuilt from a reference reel Sunyyan dropped in on 9 November 2026 (`SJ Academy Media/All 14 area and volume formulas you need for GCSE...mp4`, a GCSE reel for another maths brand). The format is borrowed. The copy, drawings, music, colours and closing are SJ Academy's own.

## Five-line brief
1. **Who and when:** O Level Maths (4024) students scrolling in the evening, a few weeks before a test or mock.
2. **The one thing:** every shape formula they need for area and volume in one saveable reel, and SJ Academy is where it came from.
3. **The idea:** a pen draws each shape on the beat while its formula lands, then all 14 draw at once on one screen they can screenshot. A student would send it to a friend the night before a paper.
4. **The proof:** the formulas themselves, checked twice, and the real past papers page on a real phone.
5. **Format and level:** teacher reel, 9:16, 64.3 s, Clear (level 2), on the beat. Ink ground.

## What was taken from the reference, and what changed
| Reference | This reel |
|---|---|
| Ghost outline, pen dot traces it, labels land, fill, fade | Same system and timing, built from scratch (`build.py`) |
| New shape every 3.2 s (2 bars at 150 BPM) | New shape every 3.21 s (6 beats at 112 BPM), so every shape lands on a beat |
| Formula box changes on the beat | Box morphs its size and colour into the next formula on the beat |
| All shapes draw together in a two-column recap | Same, plus "screenshot this one" |
| Dimmed recap, phone rises, word-by-word caption | Same, with SJ's live O Level Maths past papers page in the phone |
| Music build under the shapes | "Fresh" trimmed so its bass lift lands on the first volume shape |
| "Every area and volume formula" | "14 area and volume formulas": the set leaves out surface area, so "every" would be false |
| Voiceover over the pitch | No voice (Sunyyan's rule: no AI voice unless he asks). The words are on screen |
| Rainbow colours, serif maths font, mascot, app pitch | Yellow and orange strokes, brown fills, Poppins, no mascot, free demo |
| "Comment VERSUS" | Screenshot note, then a WhatsApp end card |

## Timing (all multiples of one beat, 60/112 s)
- Beats 0 to 84: the 14 shapes, 6 beats each. Volumes start at beat 48 (25.7 s), on the music's bass lift.
- Beats 84 to 94: recap. Beats 94 to 112: phone and captions. Beats 112 to 120: end card, music fading from beat 117.
- Inside a shape: formula on beat 0, ghost on 0.5, pen beats 1 to 3, helper lines on 3, labels on 3.5, 4 and 4.5, fill on 4.5, fade ending just before beat 6.

## Music
- "Fresh" (`bransboynd-fresh-457883.mp3`, `03 Marketing/Music Folder`), starting at its beat 16 (8.616 s) and ending on its beat 136, a bar line, as the track thins out by itself.
- Chosen by measurement against the reference: tempo fit and tone (spectral distance 3.9, second closest of all tracks tried; the closest, a lo-fi loop at 86 BPM, cannot hit a 3.2 s shape on a bar or beat grid as neatly).
- The reference's own track was not used: it is not licensed to SJ. Licence for "Fresh" is still "to confirm" in `01 Brand/Sound/licence-log.csv`, so get the certificate before running this as a paid ad.
- No sound effects and no sonic logo: the kit is still synthesised prototype audio, which Sunyyan has rejected in earlier films.

## Rebuild
- `python3 build.py` writes `index.html` and `compositions/`. Copy, shapes and timing all live in `build.py`; do not hand-edit the generated files.
- `python3 verify_formulas.py` re-runs the second solve.
- `npx hyperframes check`, then `npx hyperframes render --quality delivery --fps 30 -o renders/<name>.mp4`.
- `assets/page/maths-past-papers.png` is a capture of the live page (9 November 2026, 390 px wide). Recapture it if the page changes.

## Deliberate departures to confirm
- **Highlighter on the title:** the full letter height, not the lower half, because canvas letters on a yellow band are unreadable on an ink ground. A two-tone test cut the letters in half and read like a strikethrough.
- **Custom letter l:** a small drawn tail, because Poppins' l slanted reads as a slash in "A = l × w".
- **Custom θ:** Poppins has no θ, so it is drawn to match, keeping the piece to one typeface.

## Accuracy check (9 November 2026)
- **Solved twice:** every formula checked against a numeric measurement with no formula in it (grid counting, thin slices, arc segments). `verify_formulas.py`: all 14 agree, largest error 0.018%.
- **Question complete:** every letter on screen is defined under its box. Conditions are stated: perpendicular height (triangle, parallelogram, trapezium, pyramid, cone), parallel sides (trapezium), angle at the centre in degrees (sector, arc length), area of the cross-section (prism), area of the base (pyramid). The box label says what A, C, L or V measures.
- **Diagram honest:** no numbers to mislead. Right-angle marks on every perpendicular height, parallel arrows on the parallelogram and trapezium, hidden edges dashed, apex over the centre of the base on the pyramid and cone. The review caught a base curve that did not meet the cone's sides; fixed before this render.
- **Notation:** ×, π, ², ³ and θ used throughout, in the same form in the diagram, the box, the definition and the recap. Terms follow CAIE use: cross-section, perpendicular height, sector, arc.
- **Title:** "14", not "every". Surface area formulas are not in this set, so "every area and volume formula" would be false.
- **Claims:** "Free" and "No sign-up" are shown on the live page in the phone (checked 9 November 2026). "One class free" is in `FACTS.md`. WhatsApp number from `CLAUDE.md`. No results or class-size claims.
- **Watched as a student:** frame 0, each of the 14 finished shapes, mid-draw and mid-transition frames, the recap, all three captions, the wipe and the end card. Each makes sense alone and nothing overlaps. Smallest reading text is 28 px.
- **Sound:** measured, not heard. -14.0 LUFS, peak -1.2 dBFS, music within 2 ms of the visual beat grid. Sunyyan approved the final after review.
- **Result:** pass. Sunyyan approved it on 9 November 2026. Final: `✅ Finished/Videos/Reels & teaching/14 area and volume formulas.mp4`.

## New end card (11 November 2026)
At Sunyyan's request, the phone scene (the past papers page and its captions) and the yellow demo end card are removed. The recap now cuts straight to the black neon follow end card used in every video (`draw-reel-kit/HANDOVER.md` section 9). `V_END = 94`, `V_STOP = 108`, 57.9 s (was 64.3 s). The music is still "Fresh", so the end card's beats follow its grid, with a 3-beat fade at the end. -14.0 LUFS. The items are unchanged; their sync is still the older timing (median 33 ms, 68% within 50 ms on this render, against the newer reels' 20 ms target). Replaced `✅ Finished/Videos/Reels & teaching/14 area and volume formulas.mp4`. The caption no longer mentions past papers or the demo. The "Fresh" licence is still to confirm before any paid use.
