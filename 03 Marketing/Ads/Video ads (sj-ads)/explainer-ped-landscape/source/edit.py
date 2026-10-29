"""Cuts and speeds up Sunyyan's take, and cleans the voice.

Inputs:  assets/video/ped-sdr-master.mp4 (SDR copy of PED.mov), assets/audio/vo-raw.wav (its audio)
Outputs: assets/video/ped.mp4 (edited, sped up, silent), assets/audio/vo.wav (cleaned, edited, sped up)

KEEP and SPEED are shared with build.py, which maps every source time in the template onto the edit.
"""
import subprocess
from pathlib import Path

root = Path(__file__).parent.parent

# source seconds to keep: drops the false start (0-5.4), trims three pauses and one "you know"
KEEP = [(5.4, 12.33), (12.62, 22.42), (22.72, 39.25), (39.45, 56.92), (57.07, 61.85)]
SPEED = 1.1

# handling rumble below 100 Hz, boom at 150-500 Hz and weak presence were the problems
VOICE = ",".join([
    "highpass=f=100:poles=2", "highpass=f=100:poles=2",
    "adeclick",
    "arnndn=m=assets/models/sh.rnnn:mix=0.9",
    "equalizer=f=140:t=q:w=1.2:g=-3",
    "equalizer=f=320:t=q:w=1.0:g=-4.5",
    "equalizer=f=3800:t=q:w=1.0:g=3.5",
    "highshelf=f=9000:g=2.5",
    "deesser=i=0.4",
    "acompressor=threshold=-24dB:ratio=3.5:attack=5:release=90:makeup=5",
    "alimiter=limit=0.89",
])


def run(args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True, cwd=root)


def main():
    run(["-i", "assets/audio/vo-raw.wav", "-af", VOICE, "-ar", "48000", "assets/audio/vo-clean-full.wav"])

    parts, labels = [], []
    for i, (a, b) in enumerate(KEEP):
        fade = f"afade=t=in:d=0.012,afade=t=out:st={b - a - 0.012:.3f}:d=0.012"
        parts.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}]")
        parts.append(f"[1:a]atrim={a}:{b},asetpts=PTS-STARTPTS,{fade}[a{i}]")
        labels.append(f"[v{i}][a{i}]")
    parts.append("".join(labels) + f"concat=n={len(KEEP)}:v=1:a=1[vc][ac]")
    parts.append(f"[vc]setpts=PTS/{SPEED},fps=30[v]")
    parts.append(f"[ac]atempo={SPEED},loudnorm=I=-16:TP=-1.5:LRA=7[a]")
    run([
        "-i", "assets/video/ped-sdr-master.mp4", "-i", "assets/audio/vo-clean-full.wav",
        "-filter_complex", ";".join(parts),
        "-map", "[v]", "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-g", "30", "-keyint_min", "30",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", "assets/video/ped.mp4",
        "-map", "[a]", "-ar", "48000", "assets/audio/vo.wav",
    ])
    kept = sum(b - a for a, b in KEEP)
    print(f"kept {kept:.2f}s of source, {kept / SPEED:.2f}s after speed-up")


if __name__ == "__main__":
    main()
