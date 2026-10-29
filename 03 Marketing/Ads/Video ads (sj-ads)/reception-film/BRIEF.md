# Reception film: "A day at SJ Academy"

- workflow: general-video
- What: a 131s 16:9 loop for the 32 inch TV at reception, for visiting parents and students. 1920x1080, 30fps, with a soft music bed, designed to work on mute.
- Direction (chosen 20 Oct 2026): a clock is the spine. Each chapter opens with a giant time from the real timetable, which shrinks onto its stop on a day rail at the bottom of the frame. The film ends on a fade to black, so the loop restarts cleanly.
- Decisions from Sunyyan (20 Oct): direction "A day at SJ"; soft music bed; testimonial footage included; every teacher on the website gets a tile; no outside building shots (the exterior isn't presentable); the Google reviews go on a review wall; the schedule matches the live website.

## v2 (20 Oct 2026), after Sunyyan's review of v1
Feedback on v1, and what changed:
- "The tick and cross cards clip (IMG_5724) is for a fun entertainment reel." It's out of the film. The method now plays over IMG_6926 (a teacher at a student's desk, slow motion) and IMG_8689 (marking).
- "Classes don't start at 1 PM, they start at 4 PM. Only labs start early." The 1 PM chapter is gone. The lab chapter says "Lab practicals from 11 AM", and the 4 PM chapter says "Classes start at 4 PM."
- "Add Sir Sunyyan's, Sir Salman's and Sir Riza's video like the other teachers." They now appear on video twice: in full-screen features (name behind the cutout, as in the brand film) and as moving tiles on the faculty wall. The clips are IMG_1593 (Salman), IMG_7161 (Sunyyan) and IMG_7262 (Riza), the roster confirmed for the brand film. Sir Abdullah's tile is video too (IMG_1603).
- "More reviews, especially for Sir Sunyyan and Business." The wall grows from 10 to 16 reviews, five of them about Sir Sunyyan's Business classes, on three pages of paper cards.
- "The timetable is off brand." It's now a printed timetable on the canvas ground: level tabs with a yellow marker that slides between them, ink type, and the time of each class highlighted.
- "More fun videos like FIFA." After hours is now two FIFA shots (IMG_5552, IMG_5656) and three candid panels (IMG_6869, IMG_5485, IMG_5411) under "Not on the timetable. Still compulsory."
- "More polished, better animations, more footage, longer." Words rise out of masks, the highlighter swipes after each line lands, cards drop in like paper, the pen circles the flame test and ticks the method steps, and two highlighter wipes mark the faculty and timetable chapters. The day rail ties the chapters together. The film runs 118s to 131s on the full music track with its own ending, and uses 40 shots instead of 26.

## Chapters (v2)
| Time | Chapter | Footage | Copy |
|---|---|---|---|
| 0:00 | Welcome | IMG_6861 | Welcome to SJ Academy. Here's a day with us. |
| 0:06 | 11:00 AM lab | IMG_5817; flame, flask and microscope panels; IMG_8206 | Weekends · Fully equipped practical lab. / Saturdays and Sundays. Lab practicals from 11 AM. |
| 0:18 | 4:00 PM classes | SJ Academy.MOV, IMG_7398, IMG_6925, IMG_5683; five subject panels | Classes start at 4 PM. In class at DHA Phase 7, or live online. / O Level, AS and A2. |
| 0:30 | 5:00 PM method (canvas) | IMG_6926, IMG_8689 | Three steps to better marks (the three steps from the May/June 2027 ad) |
| 0:39 | 6:00 PM faculty | features: Salman, Sunyyan, Riza, Kashaan, Tayyaba; then the 14-tile wall | Meet the faculty. Teachers from LUMS, IBA, and ex-KGS. / The full faculty. |
| 1:03 | 7:00 PM results | stats, 16 reviews, Hadi (IMG_3560) | 4,500+ students taught · 226+ five-star Google reviews · In their words. · two lines from Hadi |
| 1:29 | 8:00 PM online | IMG_6516; Abdullah, Khawar, Umair, Saifullah panels | Live online classes. Not recordings. / Study from anywhere in Pakistan. + Ghazifa's review line |
| 1:37 | 10:30 PM after hours | FIFA (IMG_5552, IMG_5656); IMG_6869, IMG_5485, IMG_5411 | Last class of the day: AS Law. / Post-study FIFA. Beat the teachers. If you can. / Not on the timetable. Still compulsory. |
| 1:48 | Timetable (canvas) | 4 pages: O Level, AS, A2, Lab practicals | the live timetable |
| 2:04 | Close | IMG_7184 under a dark scrim | Your first class is on us. Ask at the front desk for a free demo class. QR to WhatsApp. |

## Faculty wall (14, from sjacademy.pk/meet-the-teachers on 20 Oct 2026)
- Video, reframed on the face: Salman, Sunyyan, Riza, Kashaan, Tayyaba (half speed), Khawar, Abdullah, Saifullah.
- Photos: Umair (his clip shows the back of his head), Aaliyan.
- No photo on the website, so initials on brown: Shaibaz, Basharat, Asmat, Muzna. Swap in photos when they exist.

## Sources and accuracy
- Schedule: the live classes schedule on sjacademy.pk (published sheet, May/June 2027 tabs), read 20 Oct 2026. It matches the "27" tabs of the SJA Class Timetable sheet. The board shows the first in-class batch per subject and marks online classes. Note: the sheet lists O Level Physics on Sat Sun at 1 PM and AS Chemistry on Fri Sat at 3 PM, earlier than "Classes start at 4 PM". Confirm with Sunyyan. Edit `BOARD` in `build/build.py` when the timetable changes, then rebuild and re-render.
- Numbers: only FACTS.md claims (4,500+ students, 226+ five-star Google reviews, LUMS, IBA and ex-KGS faculty, a fully equipped practical lab, a free demo class, in class at DHA Phase 7 or live online). 950+ A*s is not used.
- Reviews: 16 five-star Google reviews read from the Google Maps listing on 20 Oct 2026 (review search for "Sunyyan", "business" and "A*" added to the first read). Quotes are verbatim, trimmed with an ellipsis; first names only. One review's display name isn't a name, so it's credited "AS and A Level Business student". Reviews that praise teachers not on the current faculty list were left out. Reviewers' own words such as "best" stay as their opinion, not our claim; none of the chosen quotes use them.
- Hadi's lines are transcribed from IMG_3560 (whisper small.en) and shown as captions, since the film's sound is music only.
- Teacher subjects are from the website's teacher list.
- Footage left out on purpose: IMG_5724 (fun reel), and the skit and interview clips (IMG_6157, IMG_6159, IMG_5529, IMG_5530, IMG_5406, IMG_6504) in case they belong to unreleased reels.

## Sound
- Music: `03 Marketing/Music Folder/tunetank-inspiring-cinematic-music-409347.mp3`, from 1.0s for 131s, so the track's own ending lands on the close card. 1.2s fade in, 2.5s fade out as a safety, loudness normalised to -16 LUFS. Licence: logged in `01 Brand/Sound/licence-log.csv` as "to confirm".

## Build
- `bash build/prep_clips.sh` cuts every shot (HLG converted to SDR) and copies the five teacher features and cutouts from `brand-film-v2-landscape`. `python3 build/build.py` writes `index.html` from `build/style.css` and `build/timeline.js`.
- v1 clips and music are in `archive/v1/`.
- The loop file for TVs that can't repeat a single video is the film repeated to about 30 minutes.

## Status
- 20 Oct 2026: v1 rendered and reviewed (feedback above).
- 20 Oct 2026: v2 rendered, awaiting review: `renders/sj_reception-film_16x9_v2_2026-10-20.mp4` and the 30-minute loop. Once approved, the final goes to `✅ Finished/Videos/Brand film/SJ Academy reception film.mp4`.

- 20 Oct 2026: Sunyyan said v2 was fine overall, but the clock and day timeline didn't work. Directions were explored (parent questions, enrolment checklist, review headlines, a TV frame). A v3 checklist motion test was built in `../reception-film-v3/` and rejected (he didn't like the "Choosing an academy?" opening). **The project was cancelled the same day.** Renders are kept; nothing went to ✅ Finished.
