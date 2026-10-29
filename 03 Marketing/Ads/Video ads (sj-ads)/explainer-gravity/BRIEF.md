# Explainer: Gravity

- workflow: general-video (voiced explainer)
- Voice: Sunyyan's own recording (`03 Marketing/Voiceovers/Gravity/Gravity.m4a`). Three slips cut (a doubled "up", two false starts on the hammer line, a repeated "So next time"), then denoised, compressed and levelled. Original untouched. Edited voice: `assets/audio/vo.wav` (75.3s).
- Visuals: 13 illustrated scenes timed to the voice, word-by-word captions. Bolder look than usual by request (space scenes, cartoon Earth with a face, the Moon); brand fonts, logo and end card.
- Sound (v2): warmer voice processing (EQ, de-ess, light room), about 60 effects (own synthesised pop/boing/twinkle/thud/chime in assets/sfx/fx-*.wav plus the brand desk sounds), slow music ('Dreamy Soothing Mellow', licence to confirm) mixed after render with sidechain ducking: about 16 dB under the voice on average. The sonic logo is on the end card. Sunyyan asked for music here, against the playbook's no-music-under-lessons rule.
- Source: edit `source/index.template` and `source/captions.json`, then `python3 source/build.py` writes `index.html`.
- Status: v2 rendered, awaiting review. `renders/sj_explainer_gravity_9x16_v2_2026-10-17.mp4` (79.4s, -13.9 LUFS). v1 had voice only.
- Final mix command (render first, then mix in the music): see the v2 notes in the series memory, or re-run the ffmpeg sidechain mix with assets/audio/mellow.mp3 at -9 dB, threshold 0.025, ratio 5, then loudnorm to -14.

## Accuracy check (00 Start Here/ACCURACY.md)
- Facts checked in SCRIPT.md:
  - Earth's mass ≈ 6 × 10^24 kg, shown as 6 followed by 24 zeros
  - g = 9.8 m/s²
  - Apollo 15, David Scott, 1971
  - Moon gravity ≈ 1/6 of Earth's
  - mass vs weight
- Diagrams honest:
  - falling-ball strobe drawn to scale (20 px per metre); speeds 9.8, 19.6, 29.4 m/s
  - Earth and Moon drawn to true relative size (Moon radius 0.27 × Earth's)
  - weights for a 60 kg person: 60 × 9.8 ≈ 590 N, 60 × 1.62 ≈ 97 N, shown in newtons so mass and weight aren't mixed up
- Captions checked against the voice: British spellings (centre, metres), "Moon" capitalised.
- Frame review as a student: passed 2026-10-17 after fixes (yellow highlight leaks, pen off-screen, stamp over helmet, label on arrows).
