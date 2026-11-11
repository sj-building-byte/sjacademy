#!/usr/bin/env python3
"""Ranks the tracks in 03 Marketing/Music Folder for a draw reel and maps the winner.

It measures: tempo, how clearly the beats land, where bars start, where the sections
change and the key. It then finds the scene length (whole bars) and the start point
that put the music's lifts on scene changes and its thin-out under the end card.
It cannot hear mood. A person must listen to the audition clips before a track is final.

Setup (once):
  python3 -m venv /tmp/sj-audio && /tmp/sj-audio/bin/pip install numpy scipy

Run:
  /tmp/sj-audio/bin/python music_pick.py --scenes 9 --scene-seconds 4.3 \
      --mood calm,focused --out /tmp/picks

--scene-seconds  the hold each scene needs: 1 s + 0.3 s per word of its longest text, and 3.2 s at least
--scenes         number of content scenes
--recap / --pitch / --end  beats for the closing sections (defaults 12, 20, 12)
--avoid          text in file names to skip, comma separated
--max-seconds    longest film allowed, default 66 (the format runs 55 to 65 s)
--allow-all      include genres that usually do not suit this format (horror, funny, trailer and so on)
--mood           words to prefer in file names, as a tie-break only
--only           only analyse files containing this text
--out            folder for results.json, results.md and audition clips of the top 3
"""
import argparse
import csv
import json
import subprocess
from pathlib import Path

import numpy as np
import scipy.signal as sg
from scipy.ndimage import maximum_filter1d

SR = 22050
HOP = 128
FF = SR / HOP
KR_MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
KR_MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
NAMES = "C C# D D# E F F# G G# A A# B".split()
NOT_MUSIC = ("sfx", "whoosh", "stadium", "crowd", "growl", "logo")
# Genres that do not suit a calm teaching reel. --allow-all turns this off.
WRONG_FOR_FORMAT = ("horror", "funny", "cartoon", "comedy", "mischief", "trailer", "epic", "tension", "suspense", "dark", "brain-damage")


def load(path):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                       capture_output=True, check=True)
    return np.frombuffer(p.stdout, dtype=np.int16).astype(float) / 32768


def hf_tempo(path):
    """Beat length from HyperFrames' own beat detector, or None if it is unavailable."""
    try:
        p = subprocess.run(["npx", "hyperframes", "beats", str(path), "--json"], capture_output=True, text=True, timeout=120)
        d = json.loads(p.stdout[p.stdout.index("{"):])
        return 60 / float(d["bpm"]) if d.get("bpm") else None
    except Exception:
        return None


def refine(flux, c, span=0.015):
    """Fine search around a beat length: the grid that sits on the strongest onsets."""
    best = (0.0, c, 0.0)
    end = len(flux) / FF - 0.2
    for T in np.linspace(c * (1 - span), c * (1 + span), 61):
        for ph in np.arange(0, T, 0.006):
            idx = (np.arange(ph, end, T) * FF).round().astype(int)
            v = flux[idx].mean()
            if v > best[0]:
                best = (float(v), float(T), float(ph))
    return best[1], best[2]


def own_tempo(flux):
    """Second opinion: the beat length whose grid points most consistently land on hits.
    Tested on 18 tracks (9 November 2026): right on 13; the rest are 3:2 or 4:3 mix-ups,
    which is why HyperFrames' detector is used first and a disagreement is flagged."""
    end = len(flux) / FF - 0.2
    loc = maximum_filter1d(flux, size=2 * int(0.03 * FF) + 1)
    best = (-1.0, 0.5)
    for T in np.arange(0.375, 0.75, 0.001):
        for ph in np.arange(0, T, 0.012):
            idx = (np.arange(ph, end, T) * FF).round().astype(int)
            v = np.percentile(loc[idx], 35)
            if v > best[0]:
                best = (float(v), float(T))
    return best[1]


def find_grid(flux, path):
    """Returns beat length, phase and a note when the two tempo readings disagree."""
    hint = hf_tempo(path)
    own = own_tempo(flux)
    note = ""
    if hint is None:
        hint = own
        note = "tempo from own estimate only: listen to confirm"
    elif abs(own - hint) / hint > 0.02 and abs(own - 2 * hint) / hint > 0.03 and abs(own - hint / 2) / hint > 0.02:
        note = f"tempo readings disagree ({60 / hint:.1f} vs {60 / own:.1f} BPM): listen and tap along before using"
    T, ph = refine(flux, hint)
    return T, ph, note


def key_of(x):
    f, _, Z = sg.stft(x, SR, nperseg=8192, noverlap=4096)
    M = np.abs(Z) ** 2
    ch = np.zeros(12)
    for i, fq in enumerate(f):
        if 60 < fq < 2000:
            ch[int(round(12 * np.log2(fq / 261.63))) % 12] += M[i].sum()
    options = [(np.corrcoef(np.roll(KR_MAJ, k), ch)[0, 1], NAMES[k] + " major") for k in range(12)]
    options += [(np.corrcoef(np.roll(KR_MIN, k), ch)[0, 1], NAMES[k] + " minor") for k in range(12)]
    return max(options)[1]


def analyse(path):
    x = load(path)
    dur = len(x) / SR
    fr, _, Z = sg.stft(x, SR, nperseg=1024, noverlap=1024 - HOP)
    M = np.abs(Z)
    fl = np.maximum(0, np.diff(np.log1p(50 * M), axis=1))
    flux = fl.sum(0)
    T, ph, tempo_note = find_grid(flux, path)
    idx = (np.arange(ph, dur - 0.2, T) * FF).round().astype(int)
    idx = idx[idx < len(flux)]
    w = int(0.035 * FF)
    strength = np.array([flux[max(i - w, 0):i + w + 1].max() for i in idx])
    clarity = float(flux[idx].mean() / flux.mean())
    hits = float((strength > np.percentile(flux, 80)).mean())
    low = fl[fr < 180].sum(0)
    weight = np.array([low[max(i - w, 0):i + w + 1].max() for i in idx]) * 2 + strength
    by_phase = [float(weight[k::4].mean()) for k in range(4)]
    down = int(np.argmax(by_phase))
    bar_conf = float(max(by_phase) / np.mean(by_phase))
    # loudness per bar, from the first bar start
    samples = (ph + np.arange(len(idx) + 1) * T) * SR
    bars = []
    for b in range(down, len(idx) - 4, 4):
        seg = x[int(samples[b]):int(samples[b + 4])]
        bars.append((b, float(20 * np.log10(np.sqrt((seg ** 2).mean()) + 1e-9))))
    lifts, thins = [], []
    for k in range(2, len(bars) - 1):
        before = np.mean([bars[k - 1][1], bars[k - 2][1]])
        # the change must already be there in this bar and hold into the next
        if min(bars[k][1], bars[k + 1][1]) - before >= 2.5:
            lifts.append(bars[k][0])
        elif before - max(bars[k][1], bars[k + 1][1]) >= 2.5:
            thins.append(bars[k][0])
    lifts = [b for i, b in enumerate(lifts) if i == 0 or b - lifts[i - 1] > 8]
    thins = [b for i, b in enumerate(thins) if i == 0 or b - thins[i - 1] > 8]
    bass_share = float((M[fr < 150] ** 2).sum() / ((M ** 2).sum() + 1e-9))
    return dict(file=Path(path).name, duration=round(dur, 1), bpm=round(60 / T, 2), beat=round(T, 5), first_beat=round(ph, 3),
                clarity=round(clarity, 2), hits=round(hits, 2), bar_start_offset=down, bar_confidence=round(bar_conf, 2),
                lifts=lifts, thins=thins, key=key_of(x), bass_share=round(bass_share, 2), tempo_note=tempo_note)


def plan(t, a):
    """Best whole-bar scene length and start beat for this track."""
    best = None
    T = t["beat"]
    down = t["bar_start_offset"]
    total_beats = int((t["duration"] - t["first_beat"]) / T) - 1
    for bars in (1, 2, 3, 4):
        sb = bars * 4
        secs = sb * T
        if secs < max(3.2, a.scene_seconds - 0.45) or secs > a.scene_seconds + 1.6:
            continue
        film = a.scenes * sb + a.recap + a.pitch + a.end
        if film * T > a.max_seconds:
            continue
        for start in range(down, total_beats - film, 4):
            content = a.scenes * sb
            v_end = content + a.recap + a.pitch
            on_scene = [b - start for b in t["lifts"] if 0 < b - start < content and (b - start) % sb == 0]
            off_scene = [b - start for b in t["lifts"] if 0 < b - start < content and (b - start) % sb != 0]
            thin_in_film = [b - start for b in t["thins"] if 0 < b - start < v_end - 4]
            thin_end = [b - start for b in t["thins"] if v_end - 4 <= b - start <= v_end + a.end - 2]
            score = len(on_scene) * 3 - len(off_scene) * 2 - len(thin_in_film) * 2 + (2 if thin_end else 0)
            if on_scene and on_scene[0] <= sb * 2:
                score += 2  # the music moves early, while the viewer is deciding
            score -= abs(secs - a.scene_seconds) * 1.5
            score -= start / 400
            if best is None or score > best["fit"]:
                best = dict(fit=round(score, 2), scene_beats=sb, scene_seconds=round(secs, 2), start_beat=start,
                            media_start=round(t["first_beat"] + start * T, 3), film_seconds=round(film * T, 1),
                            v_lifts=on_scene, v_lifts_off_scene=off_scene, v_thin_end=thin_end, v_thin_early=thin_in_film)
    return best


def explain_no_fit(a):
    """Why nothing fits, and the tempo range that would."""
    closing = a.recap + a.pitch + a.end
    lines = [f"\nNo track fits {a.scenes} scenes of at least {a.scene_seconds} s in {a.max_seconds:.0f} s or less.",
             "Scenes must be whole bars. Tempo windows that would fit:"]
    for bars in (1, 2, 3):
        sb = bars * 4
        slow = 60 * sb / max(3.2, a.scene_seconds - 0.45)  # scenes long enough to read
        fast = 60 * (a.scenes * sb + closing) / a.max_seconds  # film short enough
        fast, slow = max(fast, 80), min(slow, 160)  # tempo is only measured from 80 to 160 BPM
        if fast <= slow:
            lines.append(f"  {sb}-beat scenes: tracks between {fast:.0f} and {slow:.0f} BPM")
        else:
            lines.append(f"  {sb}-beat scenes: none (scenes would be too short, or the film too long)")
    lines += ["Options: split the list into two reels (best for 12 or more items), find a track in a window above,",
              "or raise --max-seconds if a longer film is acceptable."]
    return "\n".join(lines)


def used_counts(folder):
    log = folder.parents[1] / "01 Brand" / "Sound" / "licence-log.csv"
    out = {}
    if log.exists():
        with open(log, newline="") as f:
            for row in csv.DictReader(f):
                out[row["Track"]] = (row.get("Used in", ""), row.get("Covers organic", ""))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", default=str(Path(__file__).resolve().parents[4] / "Music Folder"))
    ap.add_argument("--scenes", type=int, required=True)
    ap.add_argument("--scene-seconds", type=float, required=True)
    ap.add_argument("--recap", type=int, default=12)
    ap.add_argument("--pitch", type=int, default=20)
    ap.add_argument("--end", type=int, default=12)
    ap.add_argument("--avoid", default="")
    ap.add_argument("--mood", default="")
    ap.add_argument("--only", default="")
    ap.add_argument("--max-seconds", type=float, default=66, help="longest film allowed (format: 55 to 65 s)")
    ap.add_argument("--allow-all", action="store_true", help="include genres that usually do not suit this format")
    ap.add_argument("--out", default="/tmp/picks")
    a = ap.parse_args()
    folder = Path(a.folder)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    avoid = [w for w in a.avoid.split(",") if w]
    mood = [w for w in a.mood.split(",") if w]
    log = used_counts(folder)
    rows = []
    for f in sorted(folder.glob("*.mp3")):
        n = f.name.lower()
        if any(k in n for k in NOT_MUSIC) or any(k in n for k in avoid) or (a.only and a.only not in n):
            continue
        if not a.allow_all and not a.only and any(k in n for k in WRONG_FOR_FORMAT):
            continue
        t = analyse(f)
        film_min = (a.scenes * 4 + a.recap + a.pitch + a.end) * t["beat"]
        if t["duration"] < film_min:
            continue
        p = plan(t, a)
        if not p:
            t.update(note="no whole-bar scene length fits")
            continue
        used = next((v for k, v in log.items() if f.name in k), ("", ""))
        t.update(plan=p, used_in=used[0], licence_organic=used[1] or "not logged")
        quality = t["clarity"] * 1.2 + t["hits"] * 3 + (t["bar_confidence"] - 1) * 6
        if t["bar_confidence"] < 1.1:
            quality -= 3  # flat bars: nothing to land a scene change on
        if t["hits"] < 0.7:
            quality -= 3  # too many beats with no audible hit
        if t["tempo_note"]:
            quality -= 2
        repeat = used[0].count(";") + 1 if used[0] else 0
        t["score"] = round(quality + p["fit"] - repeat * 0.5 + sum(w in n for w in mood) * 1.0, 2)
        rows.append(t)
        print(f"{f.name[:44]:44s} {t['bpm']:6.1f} bpm score {t['score']:5.1f}", flush=True)
    if not rows:
        print(explain_no_fit(a))
        return
    rows.sort(key=lambda r: (bool(r["tempo_note"]), -r["score"]))  # a flagged tempo never outranks a clean one
    (out / "results.json").write_text(json.dumps(rows, indent=1))
    lines = ["| Rank | Track | BPM | Key | Beats land | Bars clear | Scene | Start beat | Lifts on scenes | Thin-out under end card | Used in | Check |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        p = r["plan"]
        lines.append(f"| {i} | {r['file'][:42]} | {r['bpm']} | {r['key']} | {r['hits']:.0%} | {r['bar_confidence']:.2f} | "
                     f"{p['scene_beats']} beats, {p['scene_seconds']} s | {p['start_beat']} | {p['v_lifts'] or 'none'} | "
                     f"{'yes' if p['v_thin_end'] else 'no'} | {r['used_in'] or 'not used yet'} | {r['tempo_note'] or 'ok'} |")
    (out / "results.md").write_text("\n".join(lines) + "\n")
    print("\n" + "\n".join(lines))
    print("\nFor build.py (top 3):")
    for r in rows[:3]:
        p = r["plan"]
        print(f"\n{r['file']}\n  BEAT = 60 / {r['bpm']}\n  FIRST_BEAT = {r['first_beat']}\n  START_BEAT = {p['start_beat']}\n"
              f"  SCENE_BEATS = {p['scene_beats']}\n  MEDIA_START = {p['media_start']}\n  lifts at video beats {p['v_lifts']}, off-scene {p['v_lifts_off_scene']}\n"
              f"  thin-out at video beats {p['v_thin_end'] or 'none'}")
        clip = out / f"audition-{rows.index(r) + 1}-{Path(r['file']).stem[:30]}.mp3"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(p["media_start"]), "-t", str(p["film_seconds"]),
                        "-i", str(folder / r["file"]), "-af", f"afade=t=out:st={max(p['film_seconds'] - 2, 0)}:d=2", "-q:a", "3", str(clip)], check=True)
        print(f"  listen: {clip}")
        if r["tempo_note"]:
            print(f"  CHECK: {r['tempo_note']}")


if __name__ == "__main__":
    main()
