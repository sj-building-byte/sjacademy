# Flags isolated single-frame changes (pops) in a rendered video from ffmpeg scene scores.
import re, subprocess, sys
video, tmp = sys.argv[1], sys.argv[2]
subprocess.run(["ffmpeg", "-loglevel", "error", "-i", video, "-vf",
    f"scale=270:480,select='gte(scene,0)',metadata=print:key=lavfi.scene_score:file={tmp}", "-f", "null", "-"], check=True)
v = [float(x) for x in re.findall(r"scene_score=([\d.]+)", open(tmp).read())]
fps = 60
for i in range(1, len(v)):
    ctx = v[max(0, i - 4):i] + v[i + 1:i + 5]
    base = max(sum(ctx) / len(ctx), 0.002)
    if v[i] > 0.01 and v[i] > 4 * base:
        print(f"POP t={i / fps:.3f} score={v[i]:.4f} ctx={base:.4f}")
print("frames", len(v))
