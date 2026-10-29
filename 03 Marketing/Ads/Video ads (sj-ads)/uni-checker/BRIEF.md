# University admission checker reel

- What: 9:16 Instagram Reel (1080x1920, 30fps, 20.5s) promoting the free checker at sjacademy.pk/university-admission-criteria-tool/. Ask: comment UNI for the link.
- Audience: Pakistani A Level students and parents about to apply. No voice; music and desk sounds; every line is on-screen text, so it works on mute.
- Brief from Sunyyan, 29 Oct 2026 (scenes, copy, safe zones and facts rules as given).

## Build
- `index.html` is the whole composition (HyperFrames 0.8.174). Cuts sit on the music's beat (125 BPM, 0.48s): 1.92, 3.84, 5.76, 7.68, 9.60, 14.40, 16.32, end card 18.24. 20.5s so the sonic logo rings out.
- Screen recording: `node build/rec/rec_uni.mjs` (headless Chrome, phone viewport) writes `assets/rec/uni.mp4`; `--shots` saves stills instead. The 5s phone clip `assets/rec/phone.mp4` is cut from it with ffmpeg: LUMS picked (0.4 to 1.6s), grade entry at 2.5x (5.0 to 8.2s), the result "13" (12.45 to 13.0s), the Qualify (13) tab (13.75s to end). Step 4 (exam session dates) is left out.
- Dates scrubbed on the page before recording, so the reel stays true next month: "Your Fall 2027 university map" shows as "Your university map", and the "Next date / days left" rows are hidden. Criteria text is untouched.
- Sound: `python3 build/mix.py` writes `assets/audio/mix.wav` (funk breakbeat from 1.948s so beats land on the cuts; brand desk sounds on each move; music stops at 18.24 for the full sonic logo). -13.5 LUFS, peak -1.5 dB.
- Render: `npx hyperframes@0.8.174 render -o renders/draft.mp4 --fps 30 --video-bitrate 16M`, then mux `mix.wav` as AAC 320k. The encoder settles near 3 Mbps because the picture is mostly flat colour; phone text checked sharp at 13.0s.
- Cover: frame at 1.85s, title in the middle 1080x1440.

## Accuracy check (29 Oct 2026)
Checked against the live tool page and its comparison table:
- LUMS: "BBB average across your best three A Levels" -> on screen "B average across your best three A Levels". Matches.
- IBA Karachi BBA: "BBC for BBA" -> "At least 2 Bs and a C". Matches; the tool's own card says "At least B, B, C".
- NUST: "NET 75% + O Level equivalence 25% while you are still in A Level" -> "The entry test is 75% of your merit". True for A Level students applying before results, the reel's audience.
- "16 universities. Pakistan and abroad. Free." The page lists 16 and says "Free" and "16 universities, Pakistan and abroad".
- "Deadlines" and "Merit calculator": the tool has a deadlines list with reminders and an aggregate (merit) calculator.
- No dates, grade promises, A* totals or student numbers on screen. No em dashes.
- Frames read as a student: hook, catch, each card, the phone at pick, grades and Qualify (13), stamp, tickets, CTA, end card. Nothing overlaps or clips (pen circle spacing and the Merit calculator ticket fixed before render).
- Safe zones: text between y 290 and 1250; nothing in the right 230px below y 960 except the pen arrow and the phone's bezel edge.
- Result: pass. If the tool's data changes (new admission cycle), re-check the three cards.

## Status
- 29 Oct 2026: v1 rendered, awaiting review: `renders/sj_reel_uni-checker_9x16_v1_2026-10-29.mp4` and `renders/sj_reel_uni-checker_cover_v1_2026-10-29.png`.

## v2 (29 Oct 2026), after Sunyyan rejected v1
His notes on v1: "too slow... too tame... too lame... too basic", no hook, empty frames, no exciting motion, no sticky CTA, no 3D, no voice, the same sound effects every time. v1 files are in `archive/v1/`.
- Look: flat brand yellow with an ink graph-paper floor and ceiling running to the horizon in perspective. The camera (`#world`, CSS 3D, perspective 1300px) flies through every scene. There are no hard cuts on empty grounds.
- Hook: 14 university names stream past the camera, and LUMS slams to a stop on the music's drop with a sub boom, a flash and a shake. Then "Will / take your / A Levels?" slams in and the pen circles LUMS.
- Sticky CTA: "Comment UNI for the free checker link", pinned from 0.5s and pulsing every two beats until the comment scene.
- Catch: the application form flies in, gets SUBMITTED, then a red X, with "bad idea." in Caveat.
- Criteria: the camera flies down a corridor of three cards: B tile and average for LUMS; B B C tiles for IBA BBA; a 75% ring counting up for NUST.
- Tool: "So check first." slams in. A 3D phone (CSS slab with thickness) flies in spinning, with the real recording on its screen. A/B/B grade tiles drop into it, the camera pushes in on Qualify (13), and the CHECKED stamp lands.
- 16 universities: a giant 16 with all 16 tool universities orbiting it, then a FREE stamp.
- Comment: the CTA turns into a comment box. "UNI" types itself, a heart pops and "Free checker link sent to your DMs" appears. End card with the sonic logo.
- Sound: club track (miromaxmusic, 128 BPM), its drop at 15.58s in the file placed on the LUMS slam (musicIn 14.96). New synthesised effects in `assets/sfx2/` (`build/sfx.sh`): whoosh, zip, riser, boom, hit, pop, tick, chime, scratch. `python3 build/mix.py` reads the timings from the `T` object in index.html and ducks the music under `assets/audio/vo.wav` when it exists.
- Voice: Sunyyan records this script (29 Oct):
  "Will LUMS take your A Levels? Most students find out after they apply. Bad idea. LUMS wants a B average. IBA BBA, two Bs and a C. NUST? The entry test is 75% of your merit. So check first. Enter your grades, see every programme you qualify for. 16 universities. Free. Comment UNI and we'll DM you the link."
  When it arrives: clean it, place it at 0s, and set each T time from the word timings. Rerun mix.py, then render.
- Status: motion preview with provisional timing and no voice: `renders/preview_motion_v2.mp4`, style frames in `renders/styleframes/`.

## v2 final cut with Sunyyan's voice (29 Oct 2026)
- Voice: `Lane 11 8.m4a` (from Downloads) copied to `assets/audio/vo/raw.m4a`. He read script 1, "Your cousin is wrong", in his own words. The false start "Comment UNI and we will eat..." (25.0 to 27.76s in the raw file) is cut. Cleaned (highpass, denoise, presence EQ, compression), sped up to 1.1x, written to `assets/audio/vo.wav` (24.5s). Word times come from Whisper small.en (`assets/audio/vo/vo.json`) and drive every value in `T`.
- Spoken: "Your cousin says LUMS needs straight As, but your cousin is wrong, because LUMS requires a B average across your best three A Levels. IBA BBA requires two Bs and a C. As for NUST, the entry test is 75% of your merit. So yes, the test matters more than your grades. Stop guessing and put your grades in our free checker and see every programme you qualify for in these 16 universities. Comment UNI and we'll DM you the link straight away."
- New hook: the names tunnel, LUMS slams on the drop (0.92s, music in at 14.66s), "needs straight As" in a speech bubble, then a strike and a WRONG stamp on "wrong". The application-form scene is cut because it isn't in the voice.
- NUST: the ring fills to 75%, then the O Level 25% fills in. On "the test matters more than your grades", bars show NUST entry test 75% against O Level grades 25%.
- 27.2s total (24.5s voice plus end card and sonic logo). -14.2 LUFS, peak -1.4 dB.
- Accuracy: "the test matters more than your grades" holds for NUST (NET 75% + O Level equivalence 25% while in A Level), and it plays over the NUST bars. "We'll DM you the link straight away" is his promise. It assumes DMs go out quickly (automation or someone watching comments).
- Status: `renders/sj_reel_uni-checker_9x16_v2_2026-10-29.mp4` and cover `renders/sj_reel_uni-checker_cover_v2_2026-10-29.png` (the WRONG stamp frame), awaiting review. The preview and style frames are in `archive/v2-preview/`.

## v3 (29 Oct 2026): his own screen recording, full screen; voice above the music
- Notes on v2: use his new recording instead of the phone mock-up, show it full screen, and the music was drowning out the voice.
- Footage: `SJ Academy Media/ScreenRecording_10-29-2026 15-03-44_1.mov` (iPhone, 1206x2436, 32s) copied to `assets/rec/screen.mov`. `assets/rec/full.mp4` (5.77s, 30fps, 1080x1920, zoomed 1.1x and anchored top, so the bottom 20% with Safari's bar and the deadline line is cropped) is three cuts:
  grade entry, Business B / Computer Science A (11.4 to 17.7s at 2.86x); the LUMS programme list (6.35 to 8.3s at 1.08x); the comparison table scrolling through all 16 universities (20.0 to 23.7s at 2.11x).
  Left out because they show dates: the opening hero ("Fall 2027", "October 2026"), the LUMS deadline rows ("27 Jan 2027, 90 days left"), the "Fall 2027" university sections and the deadline calendar. The recording doesn't reach the Qualify results tab, so the CHECKED stamp is gone.
- Picture: "Stop guessing." slams in, then the footage flies in as a tilted card and opens to full bleed with a slow push. Captions sit on ink pills over the footage. Our small top logo hides while the site's own header shows. A yellow counter ticks 1 to 16 as the table scrolls, then FREE stamps down. The 3D phone and the 16-orbit scene are cut.
- Mix: the music bed went from -5 to -9 dB, and the sidechain duck under the voice was set to threshold 0.02, ratio 6. The voice is boosted 3 dB and the effects bus cut by 6 dB. Measured: voice -13.6 LUFS, ducked music -30.1 LUFS, so the music sits 16.5 dB under the voice (the sound playbook says 14 to 18 dB for ads). Final mix -14.1 LUFS, peak -1.5 dB.
- Status: `renders/sj_reel_uni-checker_9x16_v3_2026-10-29.mp4` and cover `..._cover_v3_...png`, awaiting review. v2 is in `archive/v2/`.
