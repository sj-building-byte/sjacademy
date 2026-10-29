# Explainer: Price elasticity of demand (PED), 16:9 cut

- workflow: talking-head-recut (16:9 port of `../explainer-ped`, asked for by Sunyyan on 20 Oct 2026)
- Same edit, voice, captions, timings, sound effects and numbers as the vertical final (v4). Only the layout changes. Script, voice clean-up and the accuracy check are in `../explainer-ped/BRIEF.md`.
- Framing: the take is vertical (1080x1920), so he never fills the frame. While he talks (opening and "Ask one question"), he is a sharp 540x960 panel in the centre, with the petrol and burger cards either side. During graphics he moves to a 400x711 yellow-ringed window on the right, and the graphics fill the left. This matches the brand film's 16:9 "Mix" choice: people stay sharp vertical panels, and nothing is cropped to fill.
- Captions sit along the bottom, centred under him while he talks and under the graphics column otherwise.
- Charts keep the vertical version's coordinates (same axes, +10% price = 100 px on both), shifted as a group. The petrol "Demand" label moved 25 px left so it no longer touches the curve.
- End card: same content as the vertical, laid out in one column for 1080 tall, with the curves below the text.
- Source: edit `source/index.template`, then `python3 source/build.py` (writes `index.html`). `assets/` is a clone of the vertical project's. Do not re-run `edit.py` here; if the cut changes, change it in the vertical project and copy `assets/video/ped.mp4` and `assets/audio/vo.wav` across.
- Sound: render the picture (`npx hyperframes@0.8.174 render -o renders/ped_landscape_nomusic.mp4`), then copy the audio across with `ffmpeg -i renders/ped_landscape_nomusic.mp4 -i <vertical final> -map 0:v -map 1:a -c copy`. The final takes its audio track straight from the vertical final (`✅ Finished/Videos/Reels & teaching/Price elasticity of demand explained.mp4`). Both run on the same 55.5s timeline, so the mix is identical: voice, effects, Fresh with its drop and swell, and the sonic logo.
- CLI pinned at hyperframes 0.8.174, the same as the vertical project, so both cuts render with the same version (latest is 0.8.181).

## Status
- FINAL, approved 20 Oct 2026: v1 (1920x1080, 55.5s, -14.1 LUFS, peak -1.0 dB), moved to `✅ Finished/Videos/Reels & teaching/Price elasticity of demand explained (YouTube).mp4`.

## Accuracy check
- Content unchanged from the vertical final, which passed the check on 19 Oct (see `../explainer-ped/BRIEF.md`).
- Frame review of the new layout at 2.8, 5.6, 10, 12.5, 18.6, 21, 26.9, 29.5, 32.5, 36, 38, 41.5, 44.8, 48.5 and 53.8s. Every line is readable. Nothing overlaps him, the charts or the captions. Both stamps sit clear of the window.
