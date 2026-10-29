"""Mixes assets/audio/mix.wav: voice + synthwave bed (ducked under the voice) + sound effects from build/sfx.json.
python3 build/mix.py"""
import json, subprocess
from pathlib import Path
root = Path(__file__).parent.parent
S = json.loads((root / "build/sfx.json").read_text()); DUR = S["dur"]
A = root / "assets/audio"
# the 60s track is shorter than the film: play 0-57s, then cross into its 8-23.5s section for the end
music = (f"[1]atrim=0:57.5,afade=t=out:st=55.5:d=2[m1];"
         f"[1]atrim=8:23.5,asetpts=PTS-STARTPTS,afade=t=in:d=1.5,adelay=56000:all=1[m2];"
         f"[m1][m2]amix=inputs=2:normalize=0,afade=t=out:st={DUR - 1.8}:d=1.8,loudnorm=I=-16,volume=-9dB[mus];")
inputs = ["-i", str(A / "vo.wav"), "-i", str(A / "synthwave.mp3")]
fx = []
for i, c in enumerate(S["fx"]):
    inputs += ["-i", str(root / "assets/sfx" / c["f"])]
    fx.append(f"[{i + 2}]aresample=48000,aformat=channel_layouts=stereo,volume={c['g']},adelay={int(c['t'] * 1000)}:all=1[f{i}]")
n = len(S["fx"])
graph = (music + ";".join(fx) + ";" +
         "[0]aformat=channel_layouts=stereo,asplit=2[v][vk];"
         "[mus][vk]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=300[duck];"
         + "".join(f"[f{i}]" for i in range(n)) + f"amix=inputs={n}:normalize=0,volume=-6dB[fxs];"
         f"[v][duck][fxs]amix=inputs=3:normalize=0,apad=whole_dur={DUR},atrim=0:{DUR},loudnorm=I=-14:TP=-1.5[o]")
subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs, "-filter_complex", graph, "-map", "[o]", "-ar", "48000", str(A / "mix.wav")], check=True)
print("mixed", DUR, "s")
