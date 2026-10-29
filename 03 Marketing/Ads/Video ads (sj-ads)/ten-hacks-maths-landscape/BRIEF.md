# 10 Maths Hacks: 16:9 YouTube cut (26 Oct 2026)

Landscape version of `../ten-hacks-maths` (final v4 + rebuilt end card). The episode.py, voice, music, timing (102.7 s), colours and transitions are identical. The hacks, answers and accuracy check are in `../ten-hacks-maths/BRIEF.md`.

Layout (1920 x 1080):
- logo top-left (x 96, y 60), rail top-right
- left column: counter, "HACK / 10" + title, orange divider, rule
- right: the working card (x 900, y 215, 924 x 600); the portrait board coordinates are shifted by BOARD_DX/DY = 850/-445
- captions centred at the bottom
- recap in two columns of five
- end card: horizontal logo on top, the question on one line, then "Comment below", with the YouTube and website links side by side in a brown panel

Build: `python3 build.py`, `npx --yes hyperframes@0.8.167 check`, render, then loudnorm to -14 LUFS (command in ../ten-hacks-maths/REVIEW.md).
Render: `renders/10 Maths Hacks (YouTube).mp4`, 102.7 s, -14.1 LUFS, peak -1.4 dB.
