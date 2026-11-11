# Measures the rendered reel against the track. Needs numpy. Run: python verify-sync.py "renders/12 angle rules (draft v2).mp4"
import json, subprocess, sys
import numpy as np
f = sys.argv[1]
d = json.load(open("sync-events.json")); B = 60 / d["bpm"]; M = d["media_start"]; ev = d["events"]; sr = 22050
def load(p, ss=None, t=None, af=None):
    c = ["ffmpeg", "-v", "error"] + (["-ss", str(ss)] if ss is not None else []) + (["-t", str(t)] if t is not None else []) + ["-i", p, "-ac", "1", "-ar", str(sr)] + (["-af", af] if af else [])
    return np.frombuffer(subprocess.run(c + ["-f", "f32le", "-"], capture_output=True).stdout, dtype=np.float32)
r = load(f); s = load("assets/music/track.mp3", M, 70)
print("A. render audio against the track")
for a in (2, 15, 30, 45, 58):
    w = r[int(a * sr):int((a + 4) * sr)]; m = int(0.3 * sr); q = s[int(a * sr) - m:int((a + 4) * sr) + m]
    c = np.fft.irfft(np.fft.rfft(q, len(q) + len(w)) * np.conj(np.fft.rfft(w, len(q) + len(w))))
    print(f"   at {a:2d} s: {(int(np.argmax(c[:2 * m])) - m) / sr * 1000:+.1f} ms")
hop = 16; fps = sr / hop
l = load(f, af="lowpass=f=150"); n = len(l) // hop; e = np.sqrt((l[:n * hop].reshape(n, hop) ** 2).mean(1)); e = np.convolve(e, np.hanning(21) / np.hanning(21).sum(), "same")
a = np.convolve(np.maximum(0, np.diff(e)), np.hanning(11), "same")
print("B. kick attack strength around the scheduled whole-beat events")
whole = [v for v in ev if abs(v["t"] / B - round(v["t"] / B)) < 2e-3 and v["t"] < 60]
win = int(0.2 * fps); prof = np.zeros(2 * win)
for v in whole:
    c = int(v["t"] * fps)
    if c - win >= 0 and c + win < len(a): prof += a[c - win:c + win]
prof /= prof.max(); pk = (int(np.argmax(prof)) - win) / fps
print(f"   {len(whole)} events: the attack peaks {pk * 1000:+.0f} ms from the event; strength at the event {prof[win - 12:win + 12].max():.2f}, median elsewhere {np.median(prof):.2f}")
print("C. rendered picture against the schedule")
W, H = 108, 192
v = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-vf", f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout, dtype=np.uint8).reshape(-1, H, W).astype(float)
df = np.abs(np.diff(v, axis=0)).mean((1, 2))
for kind in ("cut", "angle", "sum-result"):
    lag = []
    for x in [e_ for e_ in ev if e_["kind"] == kind]:
        c = int(round(x["t"] * 30)); i, j = max(0, c - 3), min(len(df), c + 4)
        if j > i: lag.append((i + int(np.argmax(df[i:j])) + 1) / 30 - x["t"])
    lag = np.array(lag); print(f"   {kind:10s} n={len(lag):3d} median {np.median(lag) * 1000:+.0f} ms, within 2 frames {(np.abs(lag) <= 2 / 30 + .001).mean() * 100:.0f}%")
