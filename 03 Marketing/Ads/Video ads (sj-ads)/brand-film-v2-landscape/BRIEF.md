---
workflow: general-video
flow: companion
storyboard: no
message: "Named teachers for your subjects, in class or live online. First class free."
destination: youtube (16:9 cut of brand-film-v2)
aspect: 1920x1080
language: en
audience: Cambridge O Level and A Level students in Karachi and online, and their parents
length: 43.0s (16 bars at 96.65 BPM plus a 3.27s end card)
angle: brand film, premium tech-launch style ("The 2027 edition")
fps: 30
---

## Intent

v2 of the SJ Academy brand film, rethought from the ground up (2026-10-14). Sunyyan asked for "more of an Apple style video with cool animations on top of the videos to show what subjects we offer, how it's like to be at SJ Academy, and the amazing teachers you get to study with, and both physical and online classes", with completely different music. Approved script and round 1 answers: `../brand-film/STORYBOARD.md`, section v2. v1 stays in `../brand-film/`.

## Assets

- `assets/clips/*.mp4`: cut by `build/prep_clips.sh` from `../../../../SJ Academy Media/Footage & assets/` and the clips one level up (1080x1920, 30fps, SDR; HLG clips converted and lightly graded). Re-run after changing an in-point.
- `assets/cutouts/*.webm`: teacher cutouts from `npx hyperframes remove-background` on salman, kashaan, tayyaba, riza and sunyyan. Redo a cutout whenever its clip is re-cut.
- `assets/audio/music.wav` + `sfx.wav`: built by `build/audio.sh` from `assets/audio/src/` (the stomp track from `03 Marketing/Music Folder`, the SJ desk sounds and the sonic logo). Mix measured at -14.8 LUFS, -1.2 dBTP. Re-run after any timing change.

## Customizations

- Motion moves approved for this film: type window, window fly, bento grid, word behind (teacher cutout in front of a yellow name over 50% dimmed footage), spec swap.
- Highlighted words fade from canvas to ink as the yellow band draws.
- Teacher roster as confirmed for v1 on 2026-10-11; Sir Salman is IMG_1593.

## 16:9 cut (2026-10-14)

Landscape version for YouTube of the round 4 vertical edit. Framing: "Mix" (Sunyyan) — full-screen crops for wide shots only, people as sharp 608x1080 vertical panels. See STORYBOARD.md.
