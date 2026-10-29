"""assets/audio/mix.wav: funk breakbeat (125 BPM, cut so beats fall on 0.48s steps), desk sounds from the brand kit, sonic logo on the end card.  python3 build/mix.py"""
import subprocess
from pathlib import Path
root = Path(__file__).parent.parent
DUR = 20.5
MUSIC_IN = 1.948          # a beat in the track; video beats then sit at k * 0.48s
MUSIC_OUT = 18.24         # music stops for the sonic logo
F = 1 / 30
FX = [  # (time, file, gain dB): each starts on the first frame of its move
    (0.84, "sj-sfx-pen-circle", -4),        # pen circles LUMS
    (2.44, "sj-sfx-highlighter-swipe", -4), # "after"
    (3.84, "sj-sfx-paper-slide", -8), (5.76, "sj-sfx-paper-slide", -8), (7.68, "sj-sfx-paper-slide", -8),
    (9.60, "sj-sfx-paper-slide", -8),       # phone
    (13.44 + 4 * F, "sj-sfx-stamp", -1),    # CHECKED touches down
    (14.48, "sj-sfx-paper-slide", -9),      # tickets
    (15.30, "sj-sfx-highlighter-swipe", -6),
    (16.56 + 4 * F, "sj-sfx-stamp", -6),    # UNI
    (17.20, "sj-sfx-pen-circle", -5),       # arrow
    (18.27, "sj-sonic-logo-full", 0),
]
inputs = ["-ss", str(MUSIC_IN), "-i", str(root / "assets/audio/music.mp3")]
fx = []
for i, (t, f, g) in enumerate(FX):
    inputs += ["-i", str(root / "assets/sfx" / (f + ".wav"))]
    fx.append(f"[{i + 1}]aresample=48000,aformat=channel_layouts=stereo,volume={g}dB,adelay={int(t * 1000)}:all=1[f{i}]")
n = len(FX)
graph = (f"[0]atrim=0:{MUSIC_OUT},afade=t=in:d=0.02,afade=t=out:st={MUSIC_OUT - 0.35}:d=0.35,aresample=48000,aformat=channel_layouts=stereo,volume=-7dB[mus];"
         + ";".join(fx) + ";" + "".join(f"[f{i}]" for i in range(n)) + f"amix=inputs={n}:normalize=0[fxs];"
         f"[mus][fxs]amix=inputs=2:normalize=0,apad=whole_dur={DUR},atrim=0:{DUR},loudnorm=I=-14:TP=-1.5:LRA=11[o]")
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs, "-filter_complex", graph, "-map", "[o]", "-ar", "48000", "-ac", "2", str(root / "assets/audio/mix.wav")], check=True)
print("mixed", DUR)
