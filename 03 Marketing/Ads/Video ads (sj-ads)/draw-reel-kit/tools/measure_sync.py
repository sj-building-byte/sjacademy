#!/usr/bin/env python3
"""Measures how close a rendered reel's strong visual moments are to real audio hits.

Run: /tmp/sj-audio/bin/python measure_sync.py renders/name.mp4 --end 45
--end   last second of the content scenes and recap (leave out the phone and end card)

Targets: median 20 ms or less, and at least 75% within 50 ms.
Benchmarks: 14 formulas reel 44 ms and 63%; circle theorems reel 14 ms and 79%.
"""
import argparse
import subprocess

import numpy as np
import scipy.signal as sg

ap = argparse.ArgumentParser()
ap.add_argument("video")
ap.add_argument("--end", type=float, required=True)
a = ap.parse_args()

p = subprocess.run(["ffmpeg", "-v", "error", "-i", a.video, "-vf", "crop=1080:1160:0:260,scale=108:116,format=gray",
                    "-f", "rawvideo", "-"], capture_output=True, check=True)
frames = np.frombuffer(p.stdout, dtype=np.uint8).reshape(-1, 116, 108).astype(float)
change = np.abs(np.diff(frames, axis=0)).mean((1, 2))
times = (np.arange(len(change)) + 1) / 30
peaks, _ = sg.find_peaks(change, height=np.percentile(change, 92), distance=4)
visual = times[peaks]
visual = visual[visual < a.end]

p = subprocess.run(["ffmpeg", "-v", "error", "-i", a.video, "-ac", "1", "-ar", "22050", "-f", "s16le", "-"],
                   capture_output=True, check=True)
x = np.frombuffer(p.stdout, dtype=np.int16).astype(float) / 32768
_, t, Z = sg.stft(x, 22050, nperseg=1024, noverlap=896)
flux = np.maximum(0, np.diff(np.log1p(50 * np.abs(Z)), axis=1)).sum(0)
t = t[1:]
ap_, _ = sg.find_peaks(flux, height=np.percentile(flux, 90), distance=int(0.12 * 22050 / 128))
audio = t[ap_]

err = np.array([np.min(np.abs(audio - v)) for v in visual])
median, within = float(np.median(err) * 1000), float(np.mean(err < 0.05) * 100)
print(f"Strong visual moments: {len(visual)}")
print(f"Median distance from an audio hit: {median:.0f} ms (target 20 or less)")
print(f"Within 50 ms of a hit: {within:.0f}% (target 75 or more)")
print("PASS" if median <= 20 and within >= 75 else "NOT YET: look for moves that finish on the hit instead of starting on it")
