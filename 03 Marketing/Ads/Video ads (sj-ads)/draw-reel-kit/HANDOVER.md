# Draw reel: full handover

How to build SJ Academy's "pen draws it on the beat" teaching reels, on any topic. Written so another AI agent can do it with no other context. The `draw-reel` skill is the short version; this file has the detail. Last updated 10 November 2026.

**Finished examples**
- `✅ Finished/Videos/Reels & teaching/Every circle theorem.mp4`: the current standard. Copy `../circle-theorems/`.
- `✅ Finished/Videos/Reels & teaching/14 area and volume formulas.mp4`: the first in the series (older timing, folder music).

**What Sunyyan wants next (10 November 2026):** faster-paced music than the circle theorems reel. See section 5.

## 1. What the format is
A 9:16 reel on an ink ground, 45 to 55 s, music only. One topic in a countable list (formulas, theorems, definitions, graphs). It rebuilds a reference reel's format cleanly; do not add extra design on top.
1. **Each item:** a faint outline appears, a white pen dot traces it while the music's lead rises, values stamp in on chord hits, it clears on a bar start, and the text box morphs into the next item. The box holds the statement only, with no label above it.
2. **Recap:** every item draws at once on one screen ("screenshot this one").
3. **End card:** the recap cuts straight to the black neon follow card (section 9). Since 11 November 2026 there is no phone scene and no past papers mention anywhere in the reel or its caption.

## 2. Read first
`CLAUDE.md` at the root, `00 Start Here/FACTS.md`, `00 Start Here/ACCURACY.md`, `01 Brand/SJ-ACADEMY-BRAND-BOOK.md`, then the Video and Sound playbooks in `01 Brand/`.

## 3. Hard rules from Sunyyan
- No AI voiceover unless he asks. No sound effects; music only. No sonic logo until the final one is recorded.
- Music stays continuous, with no mid-film stops. Never use a reference video's track. Composed music (section 5) is approved; it must not copy the reference's melody.
- Every animated element syncs to the music, not just the cuts.
- Frame 1 names the audience and the topic. Logo at the top.
- Poppins and Caveat only. Yellow #FCE004, orange #FE6100 (strokes only, never text), brown #453516, ink #151515, canvas #F7F5EF.
- No em dashes, active voice, sentence case, no buzzwords. Claims only from `FACTS.md` or the live page shown.
- No repeated labels on every slide. He had "Write this as your reason" removed from all nine boxes.
- Finals go to `✅ Finished` only after he approves on his phone. You can measure sound but not hear it: always say so.
- A reference video lends only its format. Never copy its name, brand, mascot, art or music.

## 4. Steps
1. **Set up.** `cp -R "../circle-theorems" "../<topic>"`, then delete `renders/`, `compositions/*`, `.hyperframes/`, `.thumbnails/`, `music/compose_v2.py` and `assets/music/fresh.mp3`. Rewrite `BRIEF.md` and `CAPTION.txt`.
2. **Get the content from the syllabus, not memory.** Fetch the official Cambridge syllabus PDF for the subject and exam years. If WebFetch returns raw PDF bytes, extract the text with `pypdf` from the saved file. Quote its list and wording, and save section numbers and years in `BRIEF.md`.
3. **Test the title claim.** "Every" only if the set is the full syllabus list; otherwise use the number. GCSE references often differ from CAIE (the circle reference had 8 theorems, the 4024 syllabus has 9), so never copy their list.
4. **Set the tempo and scene length** (section 5), and put `BEAT` in `build.py`.
5. **Edit the scenes in `build.py`** (sections 6 to 8), then write the second-solve script (section 10).
6. **Compose the music** (section 5): edit `music/compose.py`, run it, then `music/normalise.py`.
7. **Check:** `python3 build.py`, `npx hyperframes check --json`. Fix every error. The `svg_round_cap_hidden_dash` warnings are safe, because paths stay at opacity 0 until they draw.
8. **Look:** `npx hyperframes snapshot --at <times> --no-end -o <dir>` and read the contact sheets.
9. **Render:** `npx hyperframes render --quality delivery --fps 30 --crf 15 --skill hyperframes -o renders/<name>_v1.mp4`
10. **Measure** music, sync and loudness (section 11), then fix and re-render.
11. **Audit every slide as a student** (section 10), then **file** it (section 12).

## 5. Music
**Default: compose it in code.** `music/compose.py` writes an original track to the reel's beat map, which gives the best sync (median 11 ms, 93% within 50 ms on circle theorems v4). SJ owns it, so it needs no licence. All parts are in beats, and `BEAT` comes from `build.py`, so changing the tempo there changes the music too.

**Faster pace next (his request, 10 November 2026).** Circle theorems ran at 112 BPM, 8 beats (4.3 s) per item. At 8 beats per item:

| BPM | Seconds per item | Words that fit the reading rule (1 s + 0.3 s a word) |
|---|---|---|
| 112 (circle theorems) | 4.29 | 11 |
| 120 | 4.00 | 10 |
| 128 | 3.75 | 9 |
| 136 | 3.53 | 8 |
| 140 | 3.43 | 8 |

Start at 128 BPM. The reference reels ran at 150 BPM with 3.2 s per item, so viewers cope with fast. If the longest statement is over 9 words (syllabus wording can't be shortened), use 120 or 128 and say so. At higher tempos, shorten the lead's swoop times (seconds, not beats) by the same ratio, and keep scenes to whole bars.

**What makes it pleasing** (measured against the reference, 10 November 2026). v2 failed with Sunyyan because it lacked these:
- **Lead tone:** round, almost pure. The 2nd harmonic sits about 18 dB under the note and the 3rd about 26 dB under (`render_lead`). Buzzy saw or square leads sound cheap.
- **Echo:** none. A short soft room only.
- **Melody:** one hook that develops over four items (8 bars, `PHRASES`), not a 2-bar loop. Similarity to 4 bars earlier should be 0.5 or less.
- **Range:** swoops of 5 to 7 semitones into each call, with peaks up to G5.
- **Groove:** a bouncy half-time opening with offbeat bass, switching to four-on-the-floor at the lift. A kick on every beat from the start reads as "the same base music".
- **Key and palette:** a low A drone, chord stabs, A minor. Change the key and chords per reel for variety.

**Sync points written into the music:**

| Item beat | Music |
|---|---|
| 0 | Chord stab as the statement lands |
| 1 to 3 | The lead's call rises while the pen draws, landing on 3 with the arcs |
| 4 and 5 | Strong stabs as the values stamp; the lead is silent so they speak |
| 6 to 7.5 | The lead's answer |

Sections: the lift is on an important item, the peak is under the recap, it thins under the captions (a soft pluck per word), and it resolves on the end card.

**Keep the hits clear:**
- Stabs go on their own bus, not ducked by the kick.
- The lead lifts off for 0.2 s before each accent (`dip`).
- No ghost hi-hat on the sixteenth before an accent.
- Pads stay quiet after the lift.

**Folder music instead:** `tools/music_pick.py` ranks `03 Marketing/Music Folder` for a given item count and length (section 13). Folder tracks need a licence certificate before paid ads, and sync is looser (14 ms against 11 ms).

## 6. Layout (1080 x 1920, 30 fps)
| Element | Position and style |
|---|---|
| Ground | Ink #151515 |
| Logo | Horizontal on-brown, x 420, y 272, 240 wide, until the end card (which has its own logo) |
| Title | y 356, Poppins 700, 56/68 px, canvas, two lines. Audience in yellow highlight at full letter height with ink text |
| Diagram | 500 x 500 box at scale 1.1, offset x 265, y 505. Stroke 6 px |
| Text box | Centred at y 1200, rounded 22, 4 px stroke matching the scene. Width from `poppins-metrics.json`, height 56 px a line plus 52 |
| Statement | Poppins 600, 42/56 px, canvas, key word yellow, at most 2 lines, no label above |
| Note | y 1322, Poppins 400, 34 px, #D9D4C7, at most 2 lines |
| Limits | Text 28 px or larger. Nothing below about y 1410 except the end card. Keep text clear of the right edge in the lower half |

**Colours:** strokes alternate yellow and orange. Angle wedges and fills use solid brown. Labels are canvas with a dark halo (`paint-order: stroke`).

**Type gaps:** Poppins has no θ or ⅓. Draw θ as SVG, and build fractions as stacked spans. Poppins' slanted l looks like a slash, so use the drawn l with a tail in `../area-volume-formulas/build.py`.

## 7. Timing in beats
`BEAT = 60 / BPM`. With composed music, video beat 0 is music beat 0 (`MEDIA_START = 0`).

**The key rule: changes start on the hit.** The eye catches the moment something changes, so a move that finishes on the beat looks early. `land(b) = b × BEAT − 1/30` is the first visible frame of any move, one frame ahead of the sound, and moves settle after the hit. Only pen strokes finish on a hit.

**One item (8 beats):**

| Beat | What happens |
|---|---|
| 0 | Old lines fade over 0.17 s (power2.out), old text gone in 2 frames, new text in over 5 frames (expo.out), box morphs over 0.34 s (expo.out), all starting together |
| 0.5 | Ghost outline to 17% over 0.2 s |
| 1 to 3 | Pen dot traces at constant speed; position written per frame |
| 3 | Arcs, wedges, right angles, dashed lines |
| 3.5 | Word labels |
| 4 | First value or tick stamps: 130% to 100% in 4 frames, `back.out(1.7)` |
| 5 | Second value or tick stamps |
| 8 | Next item. Hosts run 0.22 s past their slot so exits finish |

**Closing (9 items, `V_RECAP, V_END, V_STOP = 72, 84, 98`; `V_PITCH = V_END` so the music has no phone section):**

| Beats | What happens |
|---|---|
| Recap, 12 beats | Rings draw, pens draw, values stamp on beat 3 |
| End card, 14 beats | Hard cut to black. Logo flickers on (0), "Save this reel" (1), "share it with" (2), "a friend" flickers on (2.5), rule draws (3), follow line and its glow (4), "for O/A Level Success" (5), website pill (6), WhatsApp pill (7), light sweep (8), then the glows pulse on every bar. Chord stabs in `compose.py` sit on the same beats |

The music fades over the last 4 beats. For other item counts, change `V_RECAP` and the rest by 8 beats an item.

## 8. Diagrams: draw them exactly
Compute every point from real geometry, never by eye, so a labelled 50° really measures 50°. Helpers in `build.py`: `P(deg)`, `wedge`, `bisect_point`, `square`, `tick`, `angle_at`. Each scene is a dict: `lines`, `line2`, `note`, `draw`, `thin`, `dash`, `marks`, `wedges`, `vals`, `ticks`, `dots`, `words`, `check` (`check` holds the values `verify` measures).

Every marking must match the text. Mark right angles and equal lengths, dash hidden edges, define every letter, and place labels beside what they name, away from lines. Check the recap too: values at small size can sit on a line.

**Other topics:** the engine draws any polyline. Graphs become axes then curves; processes become boxes and arrows. For 3D use oblique projection with hidden edges dashed.

## 9. Recap and end card
- **Recap:** 3 x 3 grid for 9 items (2 x 7 for 14). Reuse each scene at small scale, with short labels (curve names, letters) at 55% size. Caveat 60 px "screenshot this one" at y 338. Two-line names are fine on the bottom row only.
- **End card (every video, since 11 November 2026):** copy `write_end()`, `EC` and `flicker()` from the template's `build.py` unchanged, with `assets/brand/Gilroy-ExtraBold.ttf` and `Gilroy-Medium.ttf`. Sunyyan rejected the yellow demo card, the phone with the past papers page, and five colourful concepts before approving this one, so do not redesign it.

| Element | Style and position (glyph tops measured from the frame) |
|---|---|
| Ground | Pure black #000, no border, no grid, no haze |
| Logo | On-brown horizontal, 340 wide, top 296, drop-shadow glow |
| Line 1 | "Save this reel", Gilroy 800, 96 px, white |
| Line 2 | "and share it with a friend", Gilroy 500, 66 px, #cfcfcf; "a friend" neon yellow |
| Rule | 300 x 3 px, orange to yellow gradient with glow |
| Follow | "Follow SJ Academy", Poppins 700, 59 px, white with a yellow and orange glow layer underneath; the same width as the next line |
| Subline | "for O/A Level Success", Poppins 500, 52 px; "O/A Level" yellow |
| Pills | 640 x 108, radius 54, 3 px neon border (yellow for sjacademy.pk with a globe, orange for +92-336-2144454 with a chat icon), PT Mono 42 px |
| Spacing | Equal 130 px gaps between logo, message, rule, follow block and pills; 25 px between the pills |
| Safe zone | Content y 296 to 1452 and x 174 to 904, inside y 250 to 1500 and x 60 to 960 (Reels header, caption and right-hand buttons) |

**The neon is in the motion,** not in decoration: elements switch on like tubes (`flicker()`: on, dim, on, dim, on over 5 frames from the hit), a light sweep crosses the follow line on beat 8, and the glows brighten on every bar after that. Check with the measuring snippet in the economics `BRIEF.md` if any text changes: gaps equal within 2 px, nothing outside the safe zone.

**Caption:** end with "Save this reel and share it with a friend. Follow SJ Academy for O/A Level success." then "sjacademy.pk | WhatsApp +92-336-2144454". No past papers or demo lines.

## 10. Accuracy and the slide audit
Follow `00 Start Here/ACCURACY.md`. Write a second-solve script that measures every drawn value from its coordinates and re-tests each rule at random positions (see `../circle-theorems/verify_theorems.py`). Record the check in `BRIEF.md`.

**Audit every slide as a student,** from the render: frame 0, each finished item, the recap, each caption, the end card. Put two slides side by side per image. Check:
- **Conditions in every note:** a note that drops a condition teaches a wrong method. "Both angles stand on the same chord" was wrong without "on the same side of it", because angles on opposite sides add to 180°.
- **Letters defined on each slide:** a slide that labels O must say O is the centre; viewers land mid-reel.
- **Statements word for word:** check every statement against the syllabus.
- **Recap values clear of lines.**

## 11. Measuring
Setup once: `python3 -m venv /tmp/sj-audio && /tmp/sj-audio/bin/pip install numpy scipy pypdf`

| Check | Command | Target |
|---|---|---|
| Music | `/tmp/sj-audio/bin/python tools/music_check.py assets/music/<track>.wav --bpm <bpm> --scenes <n> --reference <reference audio> --ref-bpm <bpm>` | -14 LUFS; lead harmonics about -18 and -26 dB; similarity to 4 bars earlier 0.5 or less; every accent rising (positive median at each accent beat) |
| Sync | `/tmp/sj-audio/bin/python tools/measure_sync.py renders/<name>.mp4 --end <seconds where the recap starts>` | Median 20 ms or less, 75% or more within 50 ms |
| Loudness | `ffmpeg -hide_banner -i video.mp4 -af ebur128=peak=true -f null - 2>&1 \| tail -12` | -14 LUFS, peak -1 dBFS or lower |

Get the reference audio with `ffmpeg -i <reference video> -vn -ac 1 -ar 22050 ref.wav`; the original videos are in `SJ Academy Media/`.

**Benchmarks:**

| Reel | Music | Sync | Within 50 ms |
|---|---|---|---|
| 14 formulas | Folder music | 44 ms | 63% |
| Circle theorems v1 | Fresh | 14 ms | 79% |
| Circle theorems v4 | Composed | 11 ms | 93% |

## 12. Filing
- Drafts stay in the project's `renders/` as `_v1`, `_v2` and so on. After approval, move one file to `✅ Finished/Videos/Reels & teaching/` with a plain name.
- `CAPTION.txt`: plain text, with the "not affiliated with Cambridge" line.
- Log the music in `01 Brand/Sound/licence-log.csv` (composed tracks as "Owned"). Add a dated entry at the top of "Latest changes" in `03 Marketing/START-HERE.md`.

## 13. Folder music picker (when not composing)
`/tmp/sj-audio/bin/python tools/music_pick.py --scenes 9 --scene-seconds 4.3 --mood calm,focused --out /tmp/picks` ranks the folder by:
- beats that land
- clear bar starts
- section lifts on scene changes
- a thin-out under the end card

It also writes the `build.py` constants and audition clips of the top 3. The tempo comes from `npx hyperframes beats`, checked by a second reading. Tracks where they disagree are flagged "listen and tap along" and rank last (miromax, tunetank, lightstock, energysound, humanstudioed). It drops tracks that push the film past 66 s and skips horror, funny and trailer genres by default. For 12 or more items, split the list into two reels. Best unused fit as of 9 November: studiokolomna "Risk", 120 BPM, not yet auditioned.

## 14. Mistakes already made
| Mistake | Fix |
|---|---|
| "Every" on a list that left out surface area | Use the number, or include all |
| Copying the reference's list | Use the CAIE syllabus |
| 6-beat scenes | Whole bars only |
| Stamps and fades finishing on the beat looked early | Start every change on the hit |
| Canvas text over a half-height highlight on ink | Full-height band, ink text |
| Cone base curve did not meet its sides | Compute tangent points; review frames |
| Label could point to the wrong line | Place it beside the exact line |
| A note dropped a condition ("same chord" without "same side") | Audit every note for conditions |
| "Write this as your reason" on every box | No repeated labels |
| Buzzy lead with echo, 2-bar loop, kick on every beat | Section 5 |
| Stabs ducked by the kick, so the hits got quieter | Stabs on their own bus |
| Dotted-eighth echo put hits off the grid | No echo, or straight eighths |
| A checking script built its beat grid for 32 s only, so "off-grid" was false | Check the grid covers the whole track |
| Chrome headless will not go under 500 px | `capture_page.cjs` |
| zsh: no word splitting; `$VAR:l` is a modifier; ffmpeg rejects `-t .8` | Run multi-step shell logic from Python; write `0.8` |

## 15. Done means
- [ ] Title claim true, syllabus cited in `BRIEF.md`
- [ ] Second-solve script passes
- [ ] Every slide audited as a student (section 10)
- [ ] End card copied unchanged; no phone scene and no past papers mention in the reel or caption
- [ ] Music measured against the reference, every accent rising
- [ ] Every item starts on a bar start; sync and loudness on target
- [ ] Check shows 0 errors
- [ ] Caption, licence log and START-HERE updated
- [ ] Told Sunyyan the music was measured, not heard
- [ ] Sunyyan approved on his phone before moving to `✅ Finished`
