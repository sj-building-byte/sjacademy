# Study websites speedrun

- workflow: general-video
- What: a 9:16 reel (1080x1920, about 55s) of seven websites every O and A Level student should know. Each one solves a real exam problem on screen against a speedrun timer.
- Voice: Sunyyan's voiceover (script: `03 Marketing/Voiceovers/Study websites/Study websites script.md`), with music under it. Captions on everything, so it works on mute.
- Decisions from Sunyyan (21 Oct 2026):
  - Concept: "Speedrun".
  - Four outside tools: Desmos, PhET, Anki, Cambridge's own syllabus pages.
  - Then an SJ finale, "And three we built at SJ Academy": the A Level grade strategy tool, the subject combinations tool and past papers.
  - No Physics & Maths Tutor or ZNotes (competitors).
  - Add a voiceover.
- Process: style frames first for approval (lesson from the cancelled reception film), then motion.

## Tools and the problem each one solves
| # | Tool | Problem on screen | Proof shown |
|---|---|---|---|
| 1 | Desmos (desmos.com/calculator) | 9709 P1: where does y = x − 1 meet y = x² − 4x + 3? | Both graphs, the crossing points (1, 0) and (4, 3) |
| 2 | PhET Circuit Construction Kit: DC | O Level Physics: add a second bulb in parallel | The ammeter reading doubles |
| 3 | Anki (ankiweb.net) | 9609: forty definitions before Paper 1 | A card flips; the next review is days away |
| 4 | Cambridge syllabus (cambridgeinternational.org) | Lost marks on "evaluate" | The command words table: "judge or calculate the quality, importance, amount, or value of something" (9708 2026 to 2028, p37) |
| 5 | SJ A Level grade strategy tool | B at AS, want an A | Three paths with the score each needs |
| 6 | SJ subject combinations tool | Which A Levels fit your degree? | The four steps, then suggested combinations |
| 7 | SJ past papers | Papers 2019 to 2025 | The subject list, free, no sign-up |

## Accuracy
See the accuracy check in the script file. Every tool claim was checked on its live site on 21 Oct 2026.

## Build (21 Oct 2026)
- Direction A (speedrun HUD), pitched at O and A Level students: live stopwatch, speedrun splits that fill with a ding, slams and stamps with a shake, stickers in Caveat.
- Voice: Sunyyan's Chatterbox clone (he couldn't record). `build/vo/`: `lines.txt` (what the clone reads), `gen.py` + `run.sh` (memory-safe, resumable; one take per process keeps it under 8 GB), `assemble.py` (trims, 1.13x, gaps) writes `assets/audio/vo.wav` and `timing.json`. Every picked take was checked with Whisper. PhET is named on screen only (the clone says "fit"). Line 14 uses the tool's own name, "Grade Comeback Calculator".
- Speedrun time: 59.44s from "Let's go!" to "Time!".
- Music: synthwave (jonasblakewood, already in the licence log as "to confirm"), ducked under the voice; 39 sound effects. `python3 build/mix.py` writes `assets/audio/mix.wav` (-14 LUFS).
- `python3 build/build.py` writes `index.html`; render with `--video-bitrate 16M`, then mux `mix.wav` onto the picture.
- The grade tool's "Examiner Verdict" box is cropped out of the capture.

## Status
- 21 Oct 2026: v1 rendered, awaiting review: `renders/sj_reel_study-websites-speedrun_9x16_v1_2026-10-21.mp4` (71.4s, -14.2 LUFS).

## v2 (21 Oct 2026), after Sunyyan rejected v1
His notes on v1: "Shit video." He wants full-screen video of every tool, no voiceover ("so unnatural"), no black background, 20 to 25 seconds, lively, real value per tool, creative use of brand elements. Some sites can sit on a Mac screen. The subject combinations tool has a new look.
- 24s, no voice. Real screen recordings made in headless Chrome (`build/rec/`: `lib.mjs` has the full-resolution DevTools recorder, a stop-motion recorder for canvas apps, a yellow tap marker, and hides floating widgets). Phone recordings at 1080x1920 for Anki, Grade Comeback Calculator, subject combinations (new look) and past papers; desktop recordings on a CSS MacBook for Desmos and PhET; the Cambridge syllabus screenshot on the Mac with a highlighter swipe and a red pen circle.
- Grounds: SJ yellow and canvas on a graph-paper grid. Ink tool tags, white paper one-liners with hard ink shadows, Caveat notes, a "MADE BY SJ ACADEMY" stamp before the three SJ tools, and the seven sites fanning out in the opening. Scenes deal in from the right like cards.
- `python3 build/v2.py` writes `index.html`; `python3 build/mix2.py` writes the sound (synthwave from its 7.6s drop, plus effects); render with `--video-bitrate 16M`, then mux `mix2.wav`.
- v1 files are in `archive/v1/`.
- Status: v2 rendered, awaiting review: `renders/sj_reel_7-free-websites_9x16_v2_2026-10-21.mp4` (24.0s, -14 LUFS).
