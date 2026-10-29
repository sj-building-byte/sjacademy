---
workflow: general-video
flow: companion
storyboard: no
message: "POV: you just joined SJ Academy. Meet the squad."
destination: instagram (pinned reel)
aspect: 1080x1920
language: en
audience: Cambridge O Level, A Level and IGCSE students in Karachi and online
length: 44.0s (99 beats at 135 BPM)
angle: brand film
fps: 30
---

## Intent

Pinned Instagram brand film. Style test first: POV walk-in hook, "Meet the squad" drop,
three FIFA/FC-walkout-style teacher cards (freeze frame cuts itself into a card, syllabus code
circled in red pen), lineup + CTA. Brand v3 rules; facts register only (no A* or student counts).

## Assets

- assets/clips/*: cut from ~/Documents/sj-ads/Academy videos (1966 hook, 7399 Kashaan, 7161 Sunyyan with green-cast fix, 1603 Abdullah) + freeze stills.
- assets/audio/music.wav: synthesized 135 BPM hype bed; sfx.wav from window.__sfxEvents. Regenerate with `node build/audio.mjs` after any timing change.

## v2 (2026-10-14): "The 2027 edition"

Requested by Sunyyan: "rethink the brand-film from the ground up, work up a completely different music and create a video that's completely different. More of an Apple style video with cool animations on top of the videos to show what subjects we offer, how it's like to be at SJ Academy, and the amazing teachers you get to study with, and both physical and online classes."

- message: "Named teachers for your subjects, in class or live online. First class free."
- aspect 1080x1920, 42.74s (16 bars at 96.65 BPM plus a 3s end card), 30fps, Instagram.
- Concept, script and music plan: `STORYBOARD.md`, section v2. Status: approved for build on 2026-10-14 (round 1 answers recorded there). Built in `../brand-film-v2/`; v1 above stays as it is.
