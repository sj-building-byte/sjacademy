#!/usr/bin/env python3
"""Checks a reel's music by measurement. Nobody can hear it for you: this is a guard, not an ear.

Run:
  /tmp/sj-audio/bin/python music_check.py assets/music/track.wav --bpm 112 --scenes 9 \
      --scene-beats 8 --accents 0,4,5 --reference path/to/reference_audio.wav

It reports:
- loudness and peak (target -14 LUFS, peak -1 dBFS or lower)
- how much a phone speaker keeps (above 250 Hz)
- energy by band: under 150 Hz, 150-600, 600-2,500, over 2,500
- lead tone: 2nd and 3rd harmonic against the note (round lead: about -18 and -26 dB)
- repetition: similarity to 4 bars earlier (0.5 or less = the melody develops; 0.9 = one loop)
- offbeat bass share (a bouncy groove has plenty)
- the loudness jump at every accent, in the phone range (each should rise above the moment before)
- whether hits sit on the beat grid
With --reference, the same numbers for the reference, to compare.
Benchmarks: circle theorems v4 track and the GCSE reference, in HANDOVER.md section 5b.
"""
import argparse
import subprocess

import numpy as np
import scipy.signal as sg

SR = 22050


def load(path):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                       capture_output=True, check=True)
    return np.frombuffer(p.stdout, dtype=np.int16).astype(float) / 32768


def loudness(path):
    p = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    i = [ln for ln in p.stderr.splitlines() if ln.strip().startswith("I:")]
    pk = [ln for ln in p.stderr.splitlines() if ln.strip().startswith("Peak:")]
    return (i[-1].split()[1] if i else "?"), (pk[-1].split()[1] if pk else "?")


def profile(x, beat, first=0.0):
    out = {}
    f, P = sg.welch(x, SR, nperseg=8192)
    tot = P.sum()
    out["bands"] = [round(float(P[(f >= lo) & (f < hi)].sum() / tot * 100), 1)
                    for lo, hi in ((20, 150), (150, 600), (600, 2500), (2500, 11000))]
    ph = sg.sosfilt(sg.butter(4, 250, "high", fs=SR, output="sos"), x)
    out["phone_db"] = round(float(20 * np.log10(np.sqrt((ph ** 2).mean()) / np.sqrt((x ** 2).mean()))), 1)
    fr, _, Z = sg.stft(x, SR, nperseg=4096, noverlap=4096 - 512)
    M = np.abs(Z)
    band = (fr > 180) & (fr < 900)
    B = M[band]
    idx = np.argmax(B, axis=0)
    peak = B[idx, np.arange(B.shape[1])]
    keep = peak > np.percentile(M, 99)
    f0 = fr[band][idx][keep]
    cols = np.arange(M.shape[1])[keep]
    ratios = []
    for c, f_ in zip(cols, f0):
        h = [M[np.argmin(np.abs(fr - k * f_)), c] for k in (1, 2, 3)]
        ratios.append([20 * np.log10(h[1] / h[0] + 1e-9), 20 * np.log10(h[2] / h[0] + 1e-9)])
    out["lead_harmonics_db"] = [round(float(v), 1) for v in np.median(ratios, axis=0)] if ratios else None
    fr2, _, Z2 = sg.stft(x, SR, nperseg=8192, noverlap=8192 - 1024)
    P2 = np.abs(Z2) ** 2
    ch = np.zeros((12, P2.shape[1]))
    for i, q in enumerate(fr2):
        if 100 < q < 2000:
            ch[int(round(12 * np.log2(q / 261.63))) % 12] += P2[i]
    ch /= ch.sum(0) + 1e-12
    L = int(16 * beat / (1024 / SR))
    a, b = ch[:, :-L], ch[:, L:]
    out["repeat_4_bars"] = round(float(np.mean(np.sum(a * b, 0) / (np.linalg.norm(a, axis=0) * np.linalg.norm(b, axis=0) + 1e-9))), 2)
    fl_low = np.maximum(0, np.diff(np.log1p(50 * M[fr < 150]), axis=1)).sum(0)
    t = (np.arange(M.shape[1] - 1) + 1) * 512 / SR
    pk, _ = sg.find_peaks(fl_low, height=np.percentile(fl_low, 85), distance=int(0.08 * SR / 512) or 1)
    phase = ((t[pk] - first) / beat) % 1
    out["offbeat_bass_pct"] = round(float(np.mean((phase > 0.375) & (phase < 0.625)) * 100))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("track")
    ap.add_argument("--bpm", type=float, required=True)
    ap.add_argument("--scenes", type=int, required=True)
    ap.add_argument("--scene-beats", type=int, default=8)
    ap.add_argument("--accents", default="0,4,5", help="beats inside each scene where something lands")
    ap.add_argument("--reference", help="the reference reel's audio, to compare")
    ap.add_argument("--ref-bpm", type=float, help="the reference's tempo")
    a = ap.parse_args()
    beat = 60 / a.bpm
    x = load(a.track)
    I, pk = loudness(a.track)
    print(f"Loudness {I} LUFS, peak {pk} dBFS (targets -14 and -1 or lower)")
    rows = [("this track", profile(x, beat))]
    if a.reference:
        rb = 60 / (a.ref_bpm or a.bpm)
        rows.append(("reference", profile(load(a.reference), rb)))
    for name, p in rows:
        print(f"\n{name}:")
        print(f"  energy by band (<150 | 150-600 | 600-2.5k | >2.5k Hz): {p['bands']} %")
        print(f"  a phone speaker keeps all but {abs(p['phone_db'])} dB")
        print(f"  lead tone, 2nd and 3rd harmonic vs the note: {p['lead_harmonics_db']} dB (round lead about -18, -26)")
        print(f"  similarity to 4 bars earlier: {p['repeat_4_bars']} (0.5 or less: the melody develops)")
        print(f"  bass onsets on the offbeat: {p['offbeat_bass_pct']}%")
    hp = sg.sosfilt(sg.butter(2, 200, "high", fs=SR, output="sos"), x)
    print("\nAccents (loudness jump at the hit vs the 150 ms before, phone range):")
    weak = 0
    for b in [float(v) for v in a.accents.split(",")]:
        jumps = []
        for s in range(a.scenes):
            i = int((s * a.scene_beats + b) * beat * SR)
            if i - int(0.15 * SR) < 0:
                continue
            pre = hp[i - int(0.15 * SR):i - int(0.01 * SR)]
            post = hp[i:i + int(0.06 * SR)]
            jumps.append(20 * np.log10(np.sqrt((post ** 2).mean()) / np.sqrt((pre ** 2).mean()) + 1e-12))
        weak += sum(j < 0.5 for j in jumps)
        print(f"  scene beat {b:g}: median {np.median(jumps):+.1f} dB, weakest {min(jumps):+.1f} dB, "
              f"{sum(j >= 0.5 for j in jumps)} of {len(jumps)} rise clearly")
    fr, t, Z = sg.stft(x, SR, nperseg=1024, noverlap=896)
    fl = np.maximum(0, np.diff(np.log1p(50 * np.abs(Z)), axis=1)).sum(0)
    t = t[1:]
    pk_, _ = sg.find_peaks(fl, height=np.percentile(fl, 90), distance=int(0.1 * SR / 128))
    on = t[pk_]
    grid = np.arange(0, int(len(x) / SR / beat * 2) + 4) * beat / 2
    err = np.array([np.min(np.abs(grid - o)) for o in on])
    print(f"\nHits on the grid: median {np.median(err) * 1000:.1f} ms from the half-beat grid, {np.mean(err < 0.02) * 100:.0f}% within 20 ms")
    print(f"\n{'Every accent rises' if weak == 0 else f'{weak} accents do not rise: look at what plays in the 150 ms before them'}")


if __name__ == "__main__":
    main()
