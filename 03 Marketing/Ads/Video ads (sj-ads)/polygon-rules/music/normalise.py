#!/usr/bin/env python3
"""Two-pass loudness normalisation of the composed track to -14 LUFS, -1.5 dBTP.
Run after compose.py:  python3 music/normalise.py"""
import json
import subprocess
from pathlib import Path

music = Path(__file__).resolve().parent.parent / "assets" / "music"
raw, out = music / "sj-polygon-synth-raw.wav", music / "sj-polygon-synth.wav"
target = "I=-14:TP=-1.5:LRA=7"
p = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(raw), "-af", f"loudnorm={target}:print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True)
d = json.loads(p.stderr[p.stderr.rindex("{"):p.stderr.rindex("}") + 1])
af = (f"loudnorm={target}:measured_I={d['input_i']}:measured_TP={d['input_tp']}:measured_LRA={d['input_lra']}:"
      f"measured_thresh={d['input_thresh']}:offset={d['target_offset']}:linear=true,aresample=48000")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-af", af, "-c:a", "pcm_s16le", str(out)], check=True)
print(f"{raw.name}: {d['input_i']} LUFS -> {out.name}")
