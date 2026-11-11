# Natural habitat: general A Level film

Status: draft v4 (field journal), 9 November 2026, 64.6s, 9:16. Waiting for Sunyyan's review. File: `renders/sj_ad_natural-habitat_9x16_v4_2026-11-09.mp4`. v4 adds an epilogue before the end card at his request: Day 275 (IMG_7076) Exam day. A question is asked. Nobody freezes. Day 276 (IMG_2533 crop) It survives Paper 1. Revision for Paper 2 starts next week. Final entry (IMG_4002) Every year, a new herd arrives. End of field notes. Music crossfades at Day 276 into the track's closing section from 115s. Measured, not heard. Caption: `CAPTION.txt`. Earlier versions: `Archive/v1/`, `Archive/v2/`, `Archive/v3/`. Style frames: `phase-1/style-frames/`. The sections after "Build" describe older versions.

## Sunyyan's notes on v2 (9 November 2026)
- The music stopped mid-film. It now runs as one continuous track.
- The film ended abruptly with only one teacher. It now has seven named teachers.
- The opening clip had to change. It is now a wide shot of a real class (IMG_2533).
- IMG_6504 is a teacher fixing his hat, not a student clutching his head. It is out of the film.
- The narration did not flow, and "Next week has arrived" on Day 213 made no sense. Rewritten so each line follows the last.
- The end card was stacked. It now uses the full height with space around every element.

## Script
| Stamp | Clip | Text |
|---|---|---|
| Day 1 | IMG_2533 at 11s | A Level students in their natural habitat. This one plans to start revising next week. |
| Day 8 | IMG_2533 at 39s | It is now next week. Revision now starts next week. |
| Day 47 | IMG_7427 | It opens one past paper. Uses this for 7 × 8. |
| Day 96 | IMG_7179 | A question is asked. The group freezes. Threat. No eye contact. |
| Day 131 | IMG_6869 | Two specimens compare progress. Has not started. Also has not started. Both feel better. |
| Day 240 | IMG_5552, IMG_5411 | Exams are close. The herd gathers around a glowing green field. Scientists have no explanation. |
| Day 268 | IMG_2246 cropped | The exam is next week. It has stopped saying next week. |
| Day 269 | journal page | It has one natural predator: the mark scheme. |
| Day 270 | IMG_6926 | Luckily, this habitat has trackers. |
| Trackers 1 to 7 | brand-film-v2 clips | Sir Sunyyan, Business. Sir Khawar, Economics. Sir Saifullah, Accounts. Sir Salman, Maths and Physics. Sir Abdullah, Chemistry. Sir Riza, Computer Science. Miss Tayyaba, English and Sociology. |
| | IMG_8689, IMG_2532 | They know how it hunts. They teach the young to survive it. |
| End | journal page | Logo. Suitable habitat found. Class photo. A Level classes at DHA Phase 7, Karachi, or live online across Pakistan. Free demo class. WhatsApp, website, Instagram. |

## Build notes
Joke shots play briefly or start on a held frame while grain and gate weave keep moving, so pen marks land accurately. Other brands' logos are removed in `build/shots.py`: club crest on IMG_6869, bag logos on IMG_7179 and IMG_2533. The foreground shoe on IMG_7179 is darkened. No logo until the end card.
`python3 build/shots.py`, `PYTHONPATH=build python3 build/mix.py`, `python3 build/build.py`, then render with `npx hyperframes@0.9.19 render` and compress to about 18 Mbps.

## Open
- Sunyyan to judge the music by ear. It was chosen from its loudness curve and has not been heard.
- Sunyyan to confirm every teacher name matches the face. Names come from the brand film and reception film clip lists; subjects from the reception film's website list.
- Written consent from identifiable students.
- Before paid ads: music licence certificate, the game on screen, the Cambridge mark scheme extract, and the Mac system fonts (local only, so this project renders on this Mac).
- The website line on the end card sits low, where Instagram's caption may overlap it. The WhatsApp number sits above that area.
- No sonic logo on the end card. His call.

## Accuracy check
9 Nov 2026: Day numbers and specimen labels are jokes, not claims. The mark scheme page is real and unaltered apart from a pen circle: `04 Teaching/Past Papers (all subjects)/Economics/Oct Nov 21/9708_w21_ms_42.pdf`, page 7. End card facts match FACTS.md. Rendered file reviewed at one frame per second: spelling, faces clear of notes, stamps clear of words, no student names, no religious text, no brand logos. -14.3 LUFS, peak -1.1 dBFS, 1080x1920, 30fps, SDR, 16 Mbps.

---

# Older notes

## v2 plan: field journal
Sunyyan's decisions, 9 November 2026:
- Look: field journal. Text alone tells the story, with no narrator. Existing clips only.
- Poppins is dropped for this film. Handwriting (Bradley Hand Bold) and typewriter (American Typewriter) in the frames. Colour: film grade with warm highlights, grain and halation.
- His notes on v1: each frame looked like lazy effort, the jokes did not land, the clips had no film grade, and frame 1 must show this is not an average ad.

| Stamp | Clip | Text |
|---|---|---|
| Day 1 | IMG_2246 | A Level students in their natural habitat. Says revision starts next week. |
| Day 47 | IMG_7427 | Still next week. (arrow to the calculator) Uses this for 7 x 8. |
| Day 96 | IMG_7179 | A question is asked. The group freezes. (no eye contact; Threat.) |
| Day 131 | IMG_4002 | Two specimens compare progress. Neither has started. Both feel better. |
| Day 163 | IMG_5482 | It has spotted us. Do not move. |
| Day 190 | IMG_5552, IMG_5411 | Exams are close. The herd gathers around a glowing green field. Scientists have no explanation. |
| Day 213 | IMG_6504 | Next week has arrived. |
| Day 214 | journal page | It has one natural predator: the mark scheme. |
| Day 215 | IMG_6926, IMG_8689 | Here, it learns how the predator hunts. |
| End | campus | Logo, free demo class, WhatsApp, website. |

How v2 is built: each joke shot plays briefly and holds on one frame while grain and gate weave keep moving, so pen marks land accurately on handheld footage. IMG_6869 holds from its first frame. Other brands' logos are removed in `build/shots.py` (club crest on IMG_6869 with a soft patch, bag logo on IMG_7179 with delogo). The foreground shoe on IMG_7179 is darkened. IMG_6869 was previously on the avoid list for the crest; the patch clears it for this film. No logo until the end card. The music stops on Day 213, leaving room sound through the mark scheme page, and returns on Day 215.

Build: `python3 build/shots.py`, `PYTHONPATH=build python3 build/mix.py`, `python3 build/build.py`, then render with `npx hyperframes@0.9.19 render` and compress to about 18 Mbps (the grain makes the raw render about 44 Mbps).

Open for v2: Sunyyan to clear IMG_6504 and judge the music by ear; written student consent; confirm the Cambridge mark scheme extract and the Mac system fonts (local only, so this project renders on this Mac) before paid ads; music licence certificate and the game on screen before paid ads; no sonic logo on the end card, his call.

Accuracy check, 9 Nov 2026: Day numbers and specimen labels are jokes, not claims. The mark scheme page is real: `04 Teaching/Past Papers (all subjects)/Economics/Oct Nov 21/9708_w21_ms_42.pdf`, page 7, unaltered apart from a pen circle. End card facts match FACTS.md: DHA Phase 7, live online across Pakistan, free demo class, WhatsApp. Rendered file reviewed at one frame per second: spelling, faces clear of notes, stamps clear of words, no student names, no religious text. Loudness -14.7 LUFS, peak -1.4 dBFS, 1080x1920, 30fps, SDR, 15 Mbps. Music not judged by ear.

## Five-line brief
1. Who and when: an A Level student in Karachi or elsewhere in Pakistan, scrolling at night, avoiding revision. Parents may see it when the student sends it.
2. The one thing: "This place gets A Level students. I can try one class free."
3. The idea: a straight-faced nature documentary about A Level students, told in on-screen narration over real campus footage. Students send it to the friend it describes.
4. The proof: real SJ classes, teachers and marking; past-paper practice marked to the mark scheme; in class at DHA Phase 7 or live online; free demo class (all in FACTS.md).
5. Format and level: footage-led 9:16 film, documentary pace (a genre exception to Hype speed, as agreed for the concept). Poppins and Caveat only. Logo at the top. No voiceover. Hard cuts only.

## Script (on-screen narration)
| Time | Shot | Line |
|---|---|---|
| 0.0 | IMG_1967 wide class | A Level students in their natural habitat. |
| 3.2 | IMG_7076 group writing | The A Level student. (note: Stressus maximus) |
| 5.6 | IMG_2246 chin on hand | It believes revision starts next week. |
| 8.4 | IMG_6504 stretching | It has believed this since August. |
| 11.2 | IMG_5482 into the lens | Careful. It has noticed the camera. |
| 13.8 | IMG_7161 Sir Sunyyan, marketing mix on the projector | An older specimen arrives. |
| 16.0 | IMG_1806 teacher gesturing | It makes loud calls to protect the group's marks. |
| 19.7 | IMG_6926 at a student's desk | It finds the weak answer. It does not attack. It explains. |
| 24.0 | IMG_7427 then IMG_8689 | Diet: past papers, marked to the mark scheme. |
| 27.6 | IMG_5552 FIFA silhouettes | After dark, the herd gathers around a glowing green field. |
| 31.6 | IMG_5411 the pitch | Scientists have no explanation. |
| 33.8 | IMG_1603 online teacher, cropped | Others live far away. The class reaches them live online. |
| 38.1 | IMG_4002 student in the lab room | Every A Level student needs the right habitat. |
| 41.5 | end card | Find yours. Free demo class. WhatsApp, website, Instagram. |

## Footage left out on purpose
- IMG_7399, IMG_7398, IMG_7018: the whiteboard shows Islamiat content with prophets' names. Never put a joke caption over it. It is also not an A Level class.
- IMG_1272: the people in shot look like adults, not students.
- IMG_6869: a student's hoodie shows a football club crest.
- IMG_7179: a foot and shoe point at the camera in the foreground.
- IMG_1603 uncropped: the projector shows real student names in a participant list. The crop removes it.

## Sound
"Inspiring Cinematic" (tunetank) from 0s, quiet for the first 15s, building from about 35s. Each shot's own room sound sits low underneath. No voice, no synthesized sound.

## Build
`python3 build/shots.py` cuts and grades clips and pulls their sound, `python3 build/mix.py` writes `assets/audio/mix.wav`, `python3 build/build.py` writes the composition. Render with `npx hyperframes@0.9.19 render`.

## Open before this goes out
- Written consent from every identifiable student, as the Video playbook requires. Clearest cases: IMG_5482 (close-up), IMG_2246, IMG_6504, IMG_4002.
- IMG_6504: the reception film left it out in case it belonged to an unreleased reel. Sunyyan to confirm it is free to use.
- Sir Sunyyan is on screen as "An older specimen" (IMG_7161). His call.
- No sonic logo on the end card. The Sound playbook asks for one; the lab practicals trailer was approved without one and Sunyyan rejected synthesized sound. His call.
- Music licence is "to confirm" in `01 Brand/Sound/licence-log.csv`. Get the certificate before any paid ad. Same check for the game on screen in the FIFA shots.
- Music was chosen by name and measured loudness over time. It has not been judged by ear.

## Accuracy check
- 9 Nov 2026: every claim checked against `00 Start Here/FACTS.md` and CLAUDE.md: past papers marked to the mark scheme, DHA Phase 7, live online across Pakistan, free demo class, WhatsApp number. The film does not sell lab practicals, which have no free demo. No class times, no A* numbers.
- 9 Nov 2026: the lines "It believes revision starts next week" and "Scientists have no explanation" are jokes, not claims. "Stressus maximus" is an invented name, written as a joke.
- 9 Nov 2026: rendered file reviewed at one frame per second and at each changed shot: spelling, safe zones, faces clear of text, no student names on screen, no prophets' names on screen, end card. Loudness -14.5 LUFS, peak -1.2 dBFS, 1080x1920, 30fps, SDR.
