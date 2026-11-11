# Lab practicals launch trailer

Status: finished 8 November 2026. Three files in `✅ Finished/Videos/Practicals/`: `LabPractical_Trailer_9x16.mp4` (50.4s, approved), `LabPractical_Trailer_38s_9x16.mp4` (38.1s, starts on the "essential" quote, no horror section) and `LabPractical_Trailer_16x9.mp4` (50.4s). All -14 LUFS. Draft previews stay in `renders/`. v2 files are in `Archive/v2/`.
Phase 1 deck: `phase-1/index.html` (published as a private artifact). It shows the earlier concept, not the final film.

## Five-line brief
1. Who and when: an A Level science student in Karachi, scrolling at night, private candidates especially.
2. The one thing: "I can't sit my practical exam without doing this." No dates or class times: the film only tells students SJ exists, so they message when they need it.
3. The idea: a horror trailer built from real lines in A Level examiner reports, answered by SJ's lab and real students.
4. The proof: examiner reports word for word, real SJ lab footage, real Google reviews.
5. Format and level: film trailer. Full freedom on fonts, colour and motion. Copy rules, sentence case and logo at the top of the end card still apply.

## The final film
- 0 to 2.3: "A Level" in large yellow, Physics, Chemistry, Biology with icons, a caution sign, "Every year, Cambridge examiners write down your practical mistakes." with "mistakes." in red. "Based on real Cambridge examiner reports." from 1.0.
- 2.3 to 14.2: five examiner lines over cold lab footage (burette, heating, drawing, robotic arm, limited experience), then "It is essential…" on black.
- 14.2 to 17.0: "So where do A Level students get hands-on practical experience?", "At" and the logo pop in at 14.7, "Duh." at 15.7.
- 17.0 to 35.9: colour returns. "A fully equipped practical lab." then Physics, Chemistry, Biology and "Your own hands on real apparatus. No robotic arm required." Text moves at each cut to keep faces and the action clear.
- 35.9 to 45.2: Hania Shaikh and Mustafa khan, highlighted sentence only, word for word.
- 45.2 to 50.4: end card, centred: logo, "A Level Lab Practicals", subjects, WhatsApp +92 336 2144454, sjacademy.pk, @sjacademypk, sources line.
- Sound: "Dark Horror Opener" to 14.2, crossfading from 12.3 into "jonasblakewood synthwave upbeat", whose drop lands at 17.0. Each shot's own lab sound sits low underneath. No voice and no synthesized sound.

## Decisions from Sunyyan
- 7 Nov: no O Level practicals; no class times; faces and Cambridge quotes approved; use existing footage.
- 8 Nov, on preview v2: no voiceover, no synthesized sound effects, no basic transitions; frame 1 must say A Level science and mistakes; cut the limewater, phone and "Some candidates" ideas; whole reviews.
- 8 Nov, on cut 3: colour back by 15s; reviews smaller with clear footage and highlighted sentence only; centred end card; subject icons; synthwave for act 2; longer lab section; crossfade music; question card with "At" logo and "Duh."; text placed per shot; red "mistakes." and a caution sign. The ink drip and red crosses were tried and rejected.

## Other versions
- 38s version (8 Nov, at Sunyyan's request): the 9:16 final from 12.3 to the end, starting on "It is essential…". Same picture and mix, 0.25s fade-in, -14 LUFS.
- The 15s cutdown (`build/cut15.py`) was rejected by Sunyyan. The file is in `Archive/rejected/`.
- 16:9 (`../lab-practical-trailer-landscape/`: `build/shots.py`, `build/mix.py`, `build/build.py` there): same edit, timing, copy and music, full-frame landscape footage (8 Nov, at Sunyyan's request). Landscape clips IMG_5816, 5817, 6880, 6881 and 8206 from `Footage & assets`. No landscape footage exists of the burette, burner, microscopes, drawing, the circuit close-up or the flexing student, so those are 16:9 bands cropped from the vertical clips (the circuit from the 4K IMG_0407). Text sits in a top or bottom band per shot. The earlier panel layout is in that project's `Archive/`.

## Build
- `python3 build/shots.py` cuts and grades the clips and pulls each shot's sound, `python3 build/mix.py` builds `assets/audio/mix.wav`, `python3 build/build.py` writes the composition. Render with `npx hyperframes@0.9.19 render --quality delivery`.

## Open
- Verify the report lines against Cambridge's own PDFs. They were checked against copies on dynamicpapers.com.
- Music licences are logged in `01 Brand/Sound/licence-log.csv` as "to confirm". Get the Pixabay certificates before any paid ad.

## Accuracy check
- 7 Nov 2026: every on-screen examiner line matched to extracted report text, then read in context.
- 8 Nov 2026: the six report lines rechecked word for word. Three end in "…" because the sentence continues in the report (balance, limited experience, essential). Tags give subject, series and year.
- 8 Nov 2026: both review sentences matched word for word to Sunyyan's screenshots.
- 8 Nov 2026: lab section copy describes only what each shot shows. "A fully equipped practical lab" is approved in FACTS.md. No free demo is offered (practical students join directly).
- 8 Nov 2026: final file reviewed at one frame per second and at each cut: spelling, safe zones, faces clear of text, end card. Loudness -14.2 LUFS, peak -2.1 dBFS.
