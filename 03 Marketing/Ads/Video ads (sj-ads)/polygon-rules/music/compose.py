#!/usr/bin/env python3
"""Original synth track for the 6 polygon rules reel, written to the reel's beat map.
Key: A minor (Am, F, C, G), 150 BPM (matching the fast, driving tempo and groove of the reference track).
Ending: Cuts straight from recap to the black neon follow end card at V_END (60).
Run: /tmp/sj-audio/bin/python music/compose.py && python3 music/normalise.py
"""
import sys
from pathlib import Path

import numpy as np
import scipy.signal as sg
from scipy.io import wavfile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from build import BEAT, SCENE_BEATS, V_END, V_RECAP, V_STOP  # noqa: E402

SR = 48000
RNG = np.random.default_rng(4024)
V_LIFT = 24
LENGTH = V_STOP * BEAT + 3.0
N = int(LENGTH * SR)


def tb(b):
    return b * BEAT


def midi_hz(m):
    return 440.0 * 2 ** ((np.asarray(m, dtype=float) - 69) / 12)


# ---------- oscillators and helpers ----------
def poly_blep(t, dt):
    out = np.zeros_like(t)
    a = t < dt
    x = t[a] / dt[a]
    out[a] = x + x - x * x - 1
    b = t > 1 - dt
    x = (t[b] - 1) / dt[b]
    out[b] = x * x + x + x + 1
    return out


def saw(freq, phase0=0.0):
    dt = freq / SR
    t = (phase0 + np.cumsum(dt)) % 1.0
    return 2 * t - 1 - poly_blep(t, dt)


def lp(x, hz, order=2):
    return sg.sosfilt(sg.butter(order, min(hz, SR * 0.45), "low", fs=SR, output="sos"), x)


def hp(x, hz, order=2):
    return sg.sosfilt(sg.butter(order, hz, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi, order=2):
    return sg.sosfilt(sg.butter(order, [lo, hi], "band", fs=SR, output="sos"), x)


def place(bus, sig, t0, gain=1.0):
    i = int(round(t0 * SR))
    if i >= N:
        return
    if sig.ndim == 1:
        sig = np.stack([sig, sig])
    n = min(sig.shape[1], N - i)
    bus[:, i:i + n] += gain * sig[:, :n]


def pan(sig, p):
    a = (p + 1) * np.pi / 4
    return np.stack([sig * np.cos(a), sig * np.sin(a)])


# ---------- instruments ----------
def kick(vel=1.0):
    n = int(0.42 * SR)
    t = np.arange(n) / SR
    f = 48 + 115 * np.exp(-t * 36)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7.5)
    click = hp(RNG.standard_normal(n), 2600) * np.exp(-t * 380) * 0.14
    return np.tanh(2.4 * (body + click)) * 0.62 * vel


def clap(vel=1.0):
    n = int(0.38 * SR)
    t = np.arange(n) / SR
    noise = bp(RNG.standard_normal(n), 950, 4400)
    env = np.zeros(n)
    for k, d in enumerate((0.0, 0.008, 0.016)):
        tt = np.clip(t - d, 0, None)
        env += (t >= d) * np.exp(-tt * (150 if k < 2 else 18)) * (0.8 if k < 2 else 1.0)
    s = noise * env * 0.34 * vel
    return np.stack([s, np.roll(s, 75)])


def hat(open_=False, vel=1.0):
    n = int((0.38 if open_ else 0.06) * SR)
    t = np.arange(n) / SR
    s = hp(RNG.standard_normal(n), 7500, 4) * np.exp(-t * (10 if open_ else 75)) * 0.22 * vel
    return pan(s, 0.22 if open_ else -0.18)


def crash(vel=1.0):
    n = int(2.4 * SR)
    t = np.arange(n) / SR
    s = hp(RNG.standard_normal(n), 4500, 2) * np.exp(-t * 1.8) * 0.28 * vel
    return np.stack([s, hp(RNG.standard_normal(n), 4500, 2) * np.exp(-t * 1.8) * 0.28 * vel])


def supersaw(midis, dur, voices=5, spread=0.12):
    n = int(dur * SR)
    out = np.zeros((2, n))
    for m in midis:
        for v in range(voices):
            det = (v - (voices - 1) / 2) / ((voices - 1) / 2)
            f = np.full(n, midi_hz(m + det * spread))
            out += pan(saw(f, RNG.random()), det * 0.7)
    return out / (len(midis) * voices) * 2.2


def stab(midis, vel=1.0, dur=0.24, bright=1.0):
    raw = supersaw(midis, dur)
    n = raw.shape[1]
    t = np.arange(n) / SR
    env_f = np.exp(-t * 15)
    amp = np.minimum(t / 0.003, 1) * np.exp(-t * 10.5)
    bright_sig = np.stack([lp(c, 4000 * bright) for c in raw])
    dark_sig = np.stack([lp(c, 700) for c in raw])
    return (bright_sig * env_f + dark_sig * (1 - env_f)) * amp * vel


def pad(midis, dur, vel=1.0):
    raw = supersaw(midis, dur, voices=4, spread=0.08)
    n = raw.shape[1]
    t = np.arange(n) / SR
    amp = np.minimum(t / 0.3, 1) * np.minimum((dur - t) / 0.35, 1).clip(0, 1)
    return np.stack([lp(c, 1200) for c in raw]) * amp * 0.55 * vel


# ---------- arrangement in A minor (Am, F, C, G) ----------
CHORDS = {
    "Am": [57, 60, 64, 69],  # A3, C4, E4, A4
    "F":  [53, 57, 60, 65],  # F3, A3, C4, F4
    "C":  [48, 55, 60, 64],  # C3, G3, C4, E4
    "G":  [55, 59, 62, 67],  # G3, B3, D4, G4
}
LOOP = ["Am", "F", "C", "G"]


def chord_at(vb):
    if vb >= V_END + 8:
        return "Am"
    return LOOP[int(vb // 4) % 4]


def section(vb):
    if vb < V_LIFT:
        return "A"  # bouncy four-on-the-floor groove
    if vb < V_RECAP:
        return "B"  # energetic lift
    if vb < V_END:
        return "R"  # recap
    return "E"      # end card


# Melodic phrases in A minor (each tuple: beat_offset, midi_pitch, swoop_semitones, swoop_dur, note_dur)
PHRASES = [
    # Phrase 1 (Rule 1, Am): Call rising E5 -> A5, silence 4-5, answer
    [(1.0, 69, 7, 0.09, 0.65), (1.75, 72, 3, 0.07, 0.55), (2.5, 76, 5, 0.08, 0.8),
     (6.0, 74, 4, 0.08, 0.5), (6.75, 72, 3, 0.07, 0.5), (7.5, 69, 5, 0.08, 0.7)],

    # Phrase 2 (Rule 2, F -> G): Call from F5 -> G5, answer
    [(1.0, 72, 5, 0.09, 0.65), (1.75, 76, 4, 0.07, 0.55), (2.5, 77, 4, 0.08, 0.8),
     (6.0, 76, 3, 0.08, 0.5), (6.75, 74, 3, 0.07, 0.5), (7.5, 72, 4, 0.08, 0.7)],

    # Phrase 3 (Rule 3, C -> G): High soaring call
    [(1.0, 76, 7, 0.09, 0.65), (1.75, 79, 4, 0.07, 0.55), (2.5, 81, 5, 0.08, 0.8),
     (6.0, 79, 4, 0.08, 0.5), (6.75, 76, 3, 0.07, 0.5), (7.5, 72, 5, 0.08, 0.7)],

    # Phrase 4 (Rule 4, Am, LIFT): Driving high resolution
    [(1.0, 69, 5, 0.08, 0.65), (1.75, 72, 4, 0.07, 0.55), (2.5, 76, 5, 0.08, 0.8),
     (6.0, 77, 4, 0.08, 0.5), (6.75, 76, 3, 0.07, 0.5), (7.5, 72, 4, 0.08, 0.7)],

    # Phrase 5 (Rule 5, F -> C):
    [(1.0, 72, 5, 0.08, 0.65), (1.75, 76, 4, 0.07, 0.55), (2.5, 79, 5, 0.08, 0.8),
     (6.0, 76, 4, 0.08, 0.5), (6.75, 74, 3, 0.07, 0.5), (7.5, 72, 4, 0.08, 0.7)],

    # Phrase 6 (Rule 6, G -> Am): Climactic run into recap
    [(1.0, 74, 5, 0.08, 0.65), (1.75, 76, 3, 0.07, 0.55), (2.5, 81, 5, 0.08, 0.8),
     (6.0, 79, 4, 0.08, 0.5), (6.75, 76, 3, 0.07, 0.5), (7.5, 69, 5, 0.08, 0.7)],
]


def lead_events():
    events = []
    for s in range(len(PHRASES)):
        base = s * SCENE_BEATS
        for b_off, m, sw, g, dur in PHRASES[s]:
            events.append((base + b_off, m, sw, g, dur))
    # Recap melody (beats 48 to 60)
    recap_notes = [
        (48.5, 76, 5, 0.08, 0.6), (49.5, 79, 4, 0.07, 0.6), (50.5, 81, 5, 0.08, 0.9),
        (52.5, 79, 4, 0.08, 0.6), (53.5, 76, 3, 0.07, 0.6), (54.5, 72, 5, 0.08, 0.9),
        (56.5, 74, 4, 0.08, 0.6), (57.5, 76, 3, 0.07, 0.6), (58.5, 69, 5, 0.08, 1.2),
    ]
    events.extend(recap_notes)
    return events


def render_lead(events):
    sig = np.zeros(N)
    for b_start, midi_note, swoop_semi, swoop_dur, dur in events:
        i0 = int(tb(b_start) * SR)
        n = int(dur * SR)
        if i0 >= N:
            continue
        n = min(n, N - i0)
        t = np.arange(n) / SR
        f_target = midi_hz(midi_note)
        f_start = midi_hz(midi_note - swoop_semi)
        sw_n = min(int(swoop_dur * SR), n)
        freqs = np.full(n, f_target)
        if sw_n > 0:
            freqs[:sw_n] = np.linspace(f_start, f_target, sw_n)
        phase = np.cumsum(freqs) / SR * 2 * np.pi
        tone = np.sin(phase) + 0.13 * np.sin(2 * phase) + 0.05 * np.sin(3 * phase)
        env = np.minimum(t / 0.012, 1) * np.minimum((dur - t) / 0.03, 1).clip(0, 1)
        sig[i0:i0 + n] += tone * env
    return pan(sig, 0.0)


def bass_pluck(m, vel=1.0, dur=0.20):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = midi_hz(m)
    s = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)
    s = np.tanh(2.2 * s) * np.exp(-t * 12) * np.minimum(t / 0.003, 1)
    return s * 0.52 * vel


def main():
    drums = np.zeros((2, N))
    music = np.zeros((2, N))
    stabs = np.zeros((2, N))
    bass = np.zeros((2, N))
    kick_times = []

    def k(t0, v=1.0):
        place(drums, kick(v), t0)
        kick_times.append(t0)

    for vb in range(V_STOP):
        sec = section(vb)
        in_bar = vb % 4
        bar_in_scene = (vb % SCENE_BEATS) // 4
        t0 = tb(vb)
        if sec in ("A", "B", "R"):
            # Driving four-on-the-floor kick
            k(t0, 1.0 if in_bar == 0 else 0.85)
            # Snare / clap on beats 1 and 3 (the 2 and 4 of bar)
            if in_bar in (1, 3):
                place(drums, clap(0.95), t0)
            # Upbeat open hi-hat on the offbeat (& of beat)
            place(drums, hat(True, 0.32), t0 + tb(0.5))
            place(drums, hat(False, 0.16), t0 + tb(0.25))
            if in_bar in (1, 2):
                place(drums, hat(False, 0.12), t0 + tb(0.75))
            # Bouncy offbeat bassline in A minor (A1 = 33, A2 = 45)
            root_midi = 33 if chord_at(vb) == "Am" else (29 if chord_at(vb) == "F" else (36 if chord_at(vb) == "C" else 31))
            place(bass, bass_pluck(root_midi, 0.8), t0 + tb(0.5))
        elif sec == "E":
            if vb in (V_END, V_END + 4):
                k(t0)
            if vb < V_END + 8:
                place(drums, hat(False, 0.25), t0 + tb(0.5))

    for vb, v in ((V_LIFT, 0.7), (V_RECAP, 0.85), (V_END, 0.9)):
        place(drums, crash(v), tb(vb))

    # chord stabs for scenes
    for s in range(int(V_RECAP // SCENE_BEATS)):
        base = s * SCENE_BEATS
        for b, vel in ((0, 1.6), (3.0, 1.2), (4, 2.0), (5, 1.6)):
            vb = base + b
            br = (0.95 if base < V_LIFT else 1.1) * (1.2 if b in (0, 4, 5) else 1.0)
            place(stabs, stab(CHORDS[chord_at(vb)], vel * (1.25 if b in (0, 4, 5) else 1.0), bright=br), tb(vb), 0.85)

    # chord stabs for recap
    for b, vel in ((0, 1.5), (1, 0.6), (3, 1.6), (4, 0.6), (6.5, 0.5), (7, 0.6), (8, 1.2), (10.5, 0.5), (11, 0.6)):
        vb = V_RECAP + b
        place(stabs, stab(CHORDS[chord_at(vb)], vel, bright=1.05), tb(vb), 0.85)

    # end card (11 November 2026): logo on 0, "Save this reel" on 1, "a friend" on 2.5, rule on 3,
    # follow line on 4, subline on 5, the two contact rows on 6 and 7, light sweep and final chord on 8
    for b, vel in ((0, 1.4), (1, 1.1), (2.5, 0.6), (3, 0.6), (4, 1.4), (5, 0.8), (6, 1.0), (7, 1.0)):
        place(stabs, stab(CHORDS["Am" if b < 4 else "F"], vel, bright=0.8), tb(V_END + b), 0.85)
    final = CHORDS["Am"] + [76]
    place(music, pad(final, tb(8) + 1.5, 1.2), tb(V_END + 8))
    place(stabs, stab(final, 0.9, dur=1.2, bright=0.7), tb(V_END + 8), 0.8)

    for vb in range(V_LIFT, V_END, 4):
        place(music, pad(CHORDS[chord_at(vb)], tb(4) + 0.3, 0.38), tb(vb))
    for vb in range(0, V_LIFT, 8):
        place(music, pad(CHORDS[chord_at(vb)], tb(8) + 0.3, 0.35), tb(vb))

    # Low A drone (55 Hz)
    t = np.arange(N) / SR
    sub = np.tanh(1.8 * (np.sin(2 * np.pi * 55.0 * t) + 0.35 * np.sin(2 * np.pi * 110.0 * t))) * 0.09
    tail = t > tb(V_STOP) + 0.5
    sub[tail] *= np.exp(-(t[tail] - tb(V_STOP) - 0.5) * 3)
    sub = lp(sub, 240)
    music += np.stack([sub, sub])

    events = lead_events()
    lead = render_lead(events) * 0.55
    high = render_lead([(b, m + 12, sw, g, L) for b, m, sw, g, L in events]) * 0.16
    lift_zone = (t >= tb(V_LIFT)) & (t < tb(V_END))
    lead = lead * (1 + 0.1 * lift_zone) + high * lift_zone
    accents = [tb(s * SCENE_BEATS + b) for s in range(int(V_RECAP // SCENE_BEATS)) for b in (0, 3, 4, 5)]
    accents += [tb(V_RECAP + b) for b in (0, 3)]
    dip = np.ones(N)
    for ta in accents:
        i0, i1 = int((ta - 0.18) * SR), int((ta + 0.03) * SR)
        if i0 < 0:
            continue
        w = np.linspace(0, np.pi, i1 - i0)
        dip[i0:i1] = np.minimum(dip[i0:i1], 1 - 0.7 * np.sin(w) ** 0.6)
    lead *= dip

    duck = np.ones(N)
    for kt in kick_times:
        i0 = int(kt * SR)
        n = min(int(0.32 * SR), N - i0)
        tt = np.arange(n) / SR
        duck[i0:i0 + n] = np.minimum(duck[i0:i0 + n], 1 - 0.32 * np.exp(-tt * 10))
    music *= duck

    ir_n = int(1.3 * SR)
    ti = np.arange(ir_n) / SR
    irs = [np.concatenate([np.zeros(int(0.012 * SR)), lp(RNG.standard_normal(ir_n), 5000) * np.exp(-ti / 0.28)]) for _ in range(2)]
    send = 0.18 * lead + 0.12 * stabs + 0.1 * music + 0.08 * drums
    send = np.stack([hp(c, 300) for c in send])
    wet = np.stack([sg.fftconvolve(send[c], irs[c])[:N] for c in range(2)]) * 0.09

    mix = drums * 0.75 + music + stabs + lead + bass + wet
    mix = np.stack([hp(c, 28) for c in mix])
    mix = np.tanh(1.1 * mix) / np.tanh(1.1)
    mix /= np.abs(mix).max() / 0.89
    out = HERE.parent / "assets" / "music" / "sj-polygon-synth-raw.wav"
    out.parent.mkdir(parents=True, exist_ok=True)
    wavfile.write(out, SR, mix.T.astype(np.float32))
    print(f"wrote {out} ({LENGTH:.1f} s)")


if __name__ == "__main__":
    main()
