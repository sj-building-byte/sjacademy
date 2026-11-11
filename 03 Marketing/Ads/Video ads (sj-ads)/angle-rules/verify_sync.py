# Measures the rendered reel against the music. Needs numpy. Run: python verify_sync.py "renders/<file>.mp4"
import subprocess, sys
import numpy as np
f = sys.argv[1]; sr = 44100; B = 60 / 112; M = 15.045
def load(p, ss=None, t=None, af=None):
    c = ["ffmpeg", "-v", "error"] + (["-ss", str(ss)] if ss is not None else []) + (["-t", str(t)] if t is not None else []) + ["-i", p, "-ac", "1", "-ar", str(sr)] + (["-af", af] if af else [])
    return np.frombuffer(subprocess.run(c + ["-f", "f32le", "-"], capture_output=True).stdout, dtype=np.float32)
r = load(f); s = load("assets/music/fresh.mp3", M, 60)
print("Render audio against the track from 15.045 s:")
for a in (2, 18, 30, 45):
    w = r[int(a * sr):int((a + 3) * sr)]; m = int(.2 * sr); q = s[int(a * sr) - m:int((a + 3) * sr) + m]
    c = np.fft.irfft(np.fft.rfft(q, len(q) + len(w)) * np.conj(np.fft.rfft(w, len(q) + len(w))))
    print(f"  at {a:2d} s: {(int(np.argmax(c[:2 * m])) - m) / sr * 1000:+.1f} ms")
hop = 44; fps = sr / hop
for name, af in (("sub 20-100 Hz", "highpass=f=20,lowpass=f=100"), ("click 2-6 kHz", "highpass=f=2000,lowpass=f=6000")):
    x = load(f, af=af); n = len(x) // hop; e = np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1)); e = np.convolve(e, np.hanning(9) / np.hanning(9).sum(), "same")
    w = int(B * fps); p = np.zeros(w)
    for k in range(100):
        i = int(k * B * fps); p += e[i:i + w]
    print(f"Average beat, {name}: peak at +{int(np.argmax(p)) / fps * 1000:.0f} ms from the grid")
W, H = 108, 192
v = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-vf", f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout, dtype=np.uint8).reshape(-1, H, W).astype(float)
d = np.abs(np.diff(v, axis=0)).mean((1, 2))
beats = [6 * i + 3.5 for i in range(12)]
lag = []
for b in beats:
    t = b * B; c = int(round(t * 30)); i, j = c - 3, c + 4
    lag.append((i + int(np.argmax(d[i:j])) + 1) / 30 - t)
lag = np.array(lag)
print(f"First angle or number of each rule: median {np.median(lag) * 1000:+.0f} ms from its beat, within 2 frames {(np.abs(lag) <= 2 / 30 + .001).mean() * 100:.0f}%")
