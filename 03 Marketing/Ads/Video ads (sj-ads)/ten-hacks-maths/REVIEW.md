# Review: 10 Maths Hacks (draft, 24 Oct 2026)

- Render: `npx --yes hyperframes@0.8.167 render -o renders/raw.mp4`, then loudnorm to -14 LUFS (command in build notes below). Draft: `renders/10 Maths Hacks (draft).mp4`, 96.1 s.
- Measured: -14.1 LUFS, true peak -1.4 dB, no clipping, sound present from start to end. Not heard: the mix was measured, not listened to.
- Looked at: every hack's question, working and answer frame, recap and end card (`.review/s1` to `s4`). Fixed: counter digits, caption fragments, fraction spacing, a clipped note in hack 9.
- Kept on purpose: `check` contrast warnings on the rule highlights are mid-swipe frames (brown text on yellow once landed). Captions file is dense (53 clips) by design.
- Weakest shot: the intro's lower half is empty under the title; with more time, put the first example (34 × 11) on screen there as a teaser.
- Length: 96 s, longer than the 75 s planned, because each hack needs both voice lines and a beat to read the answer.

Loudness step: ffmpeg -i renders/raw.mp4 -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k "renders/10 Maths Hacks (draft).mp4"

# Review: v2 redesign (26 Oct 2026)
- Render: `renders/10 Maths Hacks (v2).mp4`, 102.7 s, -14.1 LUFS, peak -1.4 dB. `check` passes; remaining warnings are mid-animation contrast samples.
- Looked at: intro, every hack's working and answer, the hit transitions (render frames 11.2 to 12.3 s), recap, end card (`.review/v2`, `v2b`, `v2c`).
- Fixed during review: see-through transition panel (now opaque), counter digit gap, chalk showing through the card (card now more solid).
- Not heard: the mix was measured, not listened to.

# Final: v4 (26 Oct 2026)
- Changes from v3: flat brand yellow everywhere (no gradient), brand orange on dividers, stamp rings, intro strip and CTA; solid transition panels.
- Fixed clipping: notes lost their last character under the reveal wipe (59², "of 110"); hack 8 fraction touched the card top (card now 540 tall, fraction moved down); answer boxes crowding the "="; "1 0" gap in the counter; intro strip now separated with •.
- Render: 102.7 s, -14.1 LUFS, peak -1.4 dB, check passes. Filed as `✅ Finished/Videos/Reels & teaching/10 Maths Hacks.mp4`.

# End card rebuilt (26 Oct 2026, after Sunyyan called the old one "AI slop")
- Flat brand yellow, horizontal logo centred on top, "Which one was new to you?" in brand brown with a brand orange underline, an outlined "Comment below" button, then a brown panel with youtube.com/@sjacademypk and sjacademy.pk. No grid, symbols or stacked logo. No captions on the end card (the text is on screen).
- Old draft renders (draft, v2, v3 calm) moved to archive/old-renders so they aren't confused with the final. Final replaced in ✅ Finished.
