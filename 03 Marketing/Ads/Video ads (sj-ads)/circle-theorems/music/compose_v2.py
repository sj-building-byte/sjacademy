#!/usr/bin/env python3
"""Original synth track for the circle theorems reel, written to the reel's beat map.

The palette follows the reference reel (a low A drone, a gliding synth lead, short paired
chord stabs, four-on-the-floor drums, A minor) but every note and part here is SJ Academy's
own. Owned outright, so no licence is needed.

Sync: video beat 0 is music beat 0. Each theorem is 8 beats:
  beat 0      chord stab with the kick as the statement lands
  beats 1-3   the lead glides upward while the pen draws
  beat 3      the lead lands as the angle arcs appear
  beats 4, 5  chord stabs on the kick and clap as the values stamp in
  beats 6-8   the lead falls back, ready for the next theorem
The track lifts at beat 40 (alternate segment theorem), peaks under the recap, thins under
the phone captions (a soft pluck for each word), and resolves on the end card.

Needs numpy and scipy:  /tmp/sj-audio/bin/python music/compose.py
Writes assets/music/sj-circle-synth.wav, then normalise with the ffmpeg command in BRIEF.md.
"""
import sys
from pathlib import Path

import numpy as np
import scipy.signal as sg
from scipy.io import wavfile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from build import BEAT, SCENE_BEATS, V_END, V_PITCH, V_RECAP, V_STOP  # noqa: E402

SR = 48000
RNG = np.random.default_rng(4024)
V_LIFT = 40
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
    """Band-limited sawtooth for a per-sample frequency array."""
    dt = freq / SR
    t = (phase0 + np.cumsum(dt)) % 1.0
    return 2 * t - 1 - poly_blep(t, dt)


def square(freq, phase0=0.0):
    dt = freq / SR
    t = (phase0 + np.cumsum(dt)) % 1.0
    t2 = (t + 0.5) % 1.0
    return (np.where(t < 0.5, 1.0, -1.0) + poly_blep(t, dt) - poly_blep(t2, dt))


def lp(x, hz, order=2):
    return sg.sosfilt(sg.butter(order, min(hz, SR * 0.45), "low", fs=SR, output="sos"), x)


def hp(x, hz, order=2):
    return sg.sosfilt(sg.butter(order, hz, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi, order=2):
    return sg.sosfilt(sg.butter(order, [lo, hi], "band", fs=SR, output="sos"), x)


def place(bus, sig, t0, gain=1.0):
    """Adds a mono or stereo signal into a stereo bus at time t0."""
    i = int(round(t0 * SR))
    if i >= N:
        return
    if sig.ndim == 1:
        sig = np.stack([sig, sig])
    n = min(sig.shape[1], N - i)
    bus[:, i:i + n] += gain * sig[:, :n]


def pan(sig, p):
    """p from -1 (left) to 1 (right), constant power."""
    a = (p + 1) * np.pi / 4
    return np.stack([sig * np.cos(a), sig * np.sin(a)])


# ---------- instruments ----------
def kick(vel=1.0):
    n = int(0.5 * SR)
    t = np.arange(n) / SR
    f = 46 + 104 * np.exp(-t * 32)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 6.5)
    click = hp(RNG.standard_normal(n), 2500) * np.exp(-t * 350) * 0.12
    return np.tanh(2.2 * (body + click)) * 0.6 * vel


def clap(vel=1.0):
    n = int(0.45 * SR)
    t = np.arange(n) / SR
    noise = bp(RNG.standard_normal(n), 900, 4200)
    env = np.zeros(n)
    for k, d in enumerate((0.0, 0.009, 0.019)):
        tt = np.clip(t - d, 0, None)
        env += (t >= d) * np.exp(-tt * (140 if k < 2 else 16)) * (0.8 if k < 2 else 1.0)
    s = noise * env * 0.32 * vel
    return np.stack([s, np.roll(s, 90)])


def hat(open_=False, vel=1.0):
    n = int((0.45 if open_ else 0.07) * SR)
    t = np.arange(n) / SR
    s = hp(RNG.standard_normal(n), 7200, 4) * np.exp(-t * (9 if open_ else 70)) * 0.2 * vel
    return pan(s, 0.25 if open_ else -0.2)


def crash(vel=1.0):
    n = int(2.6 * SR)
    t = np.arange(n) / SR
    s = hp(RNG.standard_normal(n), 4200, 2) * np.exp(-t * 1.6) * 0.26 * vel
    return np.stack([s, hp(RNG.standard_normal(n), 4200, 2) * np.exp(-t * 1.6) * 0.26 * vel])


def supersaw(midis, dur, voices=5, spread=0.13):
    """Detuned saw chord, stereo, no envelope."""
    n = int(dur * SR)
    out = np.zeros((2, n))
    for m in midis:
        for v in range(voices):
            det = (v - (voices - 1) / 2) / ((voices - 1) / 2)
            f = np.full(n, midi_hz(m + det * spread))
            out += pan(saw(f, RNG.random()), det * 0.7)
    return out / (len(midis) * voices) * 2.2


def stab(midis, vel=1.0, dur=0.26, bright=1.0):
    """Short chord stab: bright attack closing to dark, like a filter envelope."""
    raw = supersaw(midis, dur)
    n = raw.shape[1]
    t = np.arange(n) / SR
    env_f = np.exp(-t * 14)
    amp = np.minimum(t / 0.003, 1) * np.exp(-t * 9.5)
    bright_sig = np.stack([lp(c, 3800 * bright) for c in raw])
    dark_sig = np.stack([lp(c, 650) for c in raw])
    return (bright_sig * env_f + dark_sig * (1 - env_f)) * amp * vel


def pluck(m, vel=1.0, dur=0.5):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = np.full(n, midi_hz(m))
    s = 0.6 * saw(f) + 0.4 * np.sin(2 * np.pi * f * t)
    env_f = np.exp(-t * 20)
    s = lp(s, 4500) * env_f + lp(s, 900) * (1 - env_f)
    return pan(s * np.exp(-t * 7) * np.minimum(t / 0.002, 1) * vel, 0.15)


def pad(midis, dur, vel=1.0):
    raw = supersaw(midis, dur, voices=4, spread=0.09)
    n = raw.shape[1]
    t = np.arange(n) / SR
    amp = np.minimum(t / 0.35, 1) * np.minimum((dur - t) / 0.4, 1).clip(0, 1)
    return np.stack([lp(c, 1100) for c in raw]) * amp * 0.55 * vel


# ---------- arrangement ----------
CHORDS = {  # voicings above the A pedal
    "Am": [57, 60, 64, 69], "F": [57, 60, 65, 69], "C": [55, 60, 64, 67], "G": [55, 59, 62, 67], "Em": [55, 59, 64, 67],
}
LOOP = ["Am", "F", "C", "G"]  # one chord per bar


def chord_at(vb):
    bar = int(vb // 4)
    if vb >= V_END + 8:
        return "Am"
    return LOOP[bar % 4]


def section(vb):
    if vb < V_LIFT:
        return "A"
    if vb < V_RECAP:
        return "B"
    if vb < V_PITCH:
        return "R"
    if vb < V_END:
        return "P"
    return "E"


# lead motifs: (beat in scene, midi, glide seconds, length in beats); my own lines in A minor
MOTIF_A = [(1.0, 69, 0.14, 0.9), (2.0, 72, 0.05, 0.45), (2.5, 74, 0.05, 0.45), (3.0, 76, 0.09, 0.55),
           (6.0, 72, 0.28, 0.9), (7.0, 69, 0.32, 0.55)]
MOTIF_B = [(1.0, 76, 0.14, 0.9), (2.0, 79, 0.06, 0.45), (2.5, 76, 0.05, 0.45), (3.0, 74, 0.09, 0.55),
           (6.0, 71, 0.28, 0.9), (7.0, 67, 0.32, 0.55)]


def lead_events():
    ev = []
    for s in range(int(V_RECAP // SCENE_BEATS)):
        base = s * SCENE_BEATS
        motif = MOTIF_A if s % 2 == 0 else MOTIF_B
        for b, m, g, L in motif:
            ev.append((base + b, m, g, L))
    # recap: pens draw on beats 73-74, values stamp on 75
    for b, m, g, L in MOTIF_A:
        ev.append((V_RECAP + b, m + 12 if b < 4 else m, g, L))
    for b, m, g, L in MOTIF_B[:4]:
        ev.append((V_RECAP + 8 + b - 1, m, g, L))
    # the lead sits an octave lower, in the reference's low-mid register
    return sorted((b, m - 12, g, L) for b, m, g, L in ev)


def render_lead(events, start_m=52):
    """One gliding voice: pitch slides into each note, vibrato settles in."""
    pitch = np.full(N, float(start_m))
    gate = np.zeros(N)
    cur = start_m
    for (b, m, g, L) in events:
        i0, i1 = int(tb(b) * SR), int(tb(b + L) * SR)
        gi = int(g * SR)
        ramp = np.arange(i1 - i0)
        curve = cur + (m - cur) * (1 - np.exp(-ramp / max(gi / 3, 1)))
        pitch[i0:i1] = curve
        if i1 < N:
            pitch[i1:] = m
        gate[i0:i1] = 1
        cur = m
    t = np.arange(N) / SR
    vib = 0.14 * np.sin(2 * np.pi * 5.4 * t)
    f = midi_hz(pitch + vib)
    sig = 0.62 * saw(f) + 0.38 * square(f)
    # smooth gate into an envelope (10 ms attack, 90 ms release)
    k_att, k_rel = 1 - np.exp(-1 / (0.01 * SR)), 1 - np.exp(-1 / (0.09 * SR))
    env = np.zeros(N)
    e = 0.0
    for i in range(0, N, 32):
        target = gate[i]
        k = k_att if target > e else k_rel
        e += (target - e) * (1 - (1 - k) ** 32)
        env[i:i + 32] = e
    return sig, env


def main():
    drums = np.zeros((2, N))
    music = np.zeros((2, N))  # gets the sidechain
    lead_bus = np.zeros((2, N))
    plucks = np.zeros((2, N))
    stabs = np.zeros((2, N))  # not ducked: the stabs are the hits
    kick_times = []

    total_beats = V_STOP
    for vb in range(total_beats):
        sec = section(vb)
        in_bar = vb % 4
        t0 = tb(vb)
        if sec in "ABR":
            v = 1.0 if in_bar == 0 else 0.78
            drums_k = kick(v)
            place(drums, drums_k, t0)
            kick_times.append(t0)
            if in_bar in (1, 3):
                place(drums, clap(0.55 if sec == "A" else 0.85), t0)
            place(drums, hat(False, 0.55 if sec == "A" else 0.75), t0 + tb(0.5))
            if sec != "A":
                place(drums, hat(False, 0.18), t0 + tb(0.25))
                place(drums, hat(False, 0.18), t0 + tb(0.75))
                place(drums, hat(True, 0.4), t0 + tb(0.5))
        elif sec == "P":
            if in_bar in (0, 2):
                place(drums, kick(0.8), t0)
                kick_times.append(t0)
            place(drums, hat(False, 0.4), t0 + tb(0.5))
        elif sec == "E":
            if vb in (V_END, V_END + 4):
                place(drums, kick(1.0), t0)
                kick_times.append(t0)
            if vb < V_END + 8:
                place(drums, hat(False, 0.3), t0 + tb(0.5))

    # crashes on the lift, the recap and the end card
    for vb, v in ((V_LIFT, 0.8), (V_RECAP, 0.9), (V_END, 1.0)):
        place(drums, crash(v), tb(vb))

    # chord stabs: on each theorem's landing (0), its marks (2.5, 3) and its two stamps (4, 5)
    for s in range(int(V_RECAP // SCENE_BEATS)):
        base = s * SCENE_BEATS
        for b, vel in ((0, 1.7), (2.5, 0.35), (3.0, 0.45), (4, 1.9), (5, 1.5)):
            vb = base + b
            br = 0.8 if base < V_LIFT else 1.15
            place(stabs, stab(CHORDS[chord_at(vb)], vel, bright=br * (1.25 if b in (0, 4, 5) else 1.0)), tb(vb), 0.95)
    for b, vel in ((0, 1.0), (1, 0.7), (3, 1.0), (4, 0.6), (6.5, 0.6), (7, 0.7), (8, 0.9), (10.5, 0.6), (11, 0.7)):
        vb = V_RECAP + b
        place(stabs, stab(CHORDS[chord_at(vb)], vel, bright=1.15), tb(vb), 0.95)
    for vb in range(V_PITCH, V_END, 4):
        place(stabs, stab(CHORDS[chord_at(vb)], 0.55, bright=0.7), tb(vb), 0.95)
    # end card: wipe, then chip, line, button, contact
    for b, vel in ((0, 1.1), (1, 0.55), (2, 0.6), (3, 0.65), (4, 0.95)):
        place(stabs, stab(CHORDS["Am" if b < 4 else "F"], vel, bright=1.0), tb(V_END + b), 0.95)
    final = CHORDS["Am"] + [76]
    place(music, pad(final, tb(8) + 1.5, 1.2), tb(V_END + 8))
    place(stabs, stab(final, 1.0, dur=1.2, bright=0.9), tb(V_END + 8), 0.45)

    # pads from the lift onwards
    for vb in range(V_LIFT, V_END, 4):
        place(music, pad(CHORDS[chord_at(vb)], tb(4) + 0.3, 0.6 if section(vb) != "P" else 1.0), tb(vb))
    for vb in range(0, V_LIFT, 8):
        place(music, pad(CHORDS[chord_at(vb)], tb(8) + 0.3, 0.45), tb(vb))

    # caption plucks: one per word, one per beat, from chord tones
    for vb in range(V_PITCH + 1, V_END):
        tones = CHORDS[chord_at(vb)]
        place(plucks, pluck(tones[(vb * 3) % len(tones)] + 12, 0.85), tb(vb))

    # the A drone, with harmonics so it carries on a phone
    t = np.arange(N) / SR
    sub = np.sin(2 * np.pi * 55 * t) + 0.35 * np.sin(2 * np.pi * 110 * t)
    sub = np.tanh(1.8 * sub) * 0.13
    sub_env = np.ones(N)
    sub_env[t > tb(V_STOP) + 0.5] = np.exp(-(t[t > tb(V_STOP) + 0.5] - tb(V_STOP) - 0.5) * 3)
    sub = lp(sub * sub_env, 240)
    music += np.stack([sub, sub])

    # lead
    sig, env = render_lead(lead_events())
    t_sec = np.arange(N) / SR
    bright = np.where(t_sec < tb(V_LIFT), 0.0, 1.0)
    dark = lp(sig, 2400)
    light = lp(sig, 5200)
    lead = (dark * (1 - 0.6 * bright) + light * 0.6 * bright) * env * 0.8
    octave_env = np.where((t_sec >= tb(V_LIFT)) & (t_sec < tb(V_PITCH)), 1.0, 0.0)
    lead_bus += pan(lead, -0.1)
    # eighth-note echo, alternating sides
    d = int(tb(0.5) * SR)  # straight eighth echo keeps every repeat on the grid
    echo = np.zeros((2, N))
    src = lead * 0.32
    for k in range(1, 4):
        side = k % 2
        echo[side, d * k:] += src[:N - d * k] * (0.45 ** (k - 1))
    lead_bus += np.stack([lp(echo[0], 3000), lp(echo[1], 3000)])
    lead_bus *= 1 + 0.25 * octave_env
    # lift off before every accent (statement landing and both stamps), so each hit has room
    accents = [tb(sc * SCENE_BEATS + b) for sc in range(int(V_RECAP // SCENE_BEATS)) for b in (0, 4, 5)]
    accents += [tb(V_RECAP + b) for b in (0, 3)]
    dip = np.ones(N)
    for ta in accents:
        i0, i1 = int((ta - 0.2) * SR), int((ta + 0.03) * SR)
        if i0 < 0:
            continue
        w = np.linspace(0, np.pi, i1 - i0)
        dip[i0:i1] = np.minimum(dip[i0:i1], 1 - 0.7 * np.sin(w) ** 0.6)
    lead_bus *= dip

    # sidechain: music ducks under every kick
    duck = np.ones(N)
    for kt in kick_times:
        i0 = int(kt * SR)
        n = min(int(0.35 * SR), N - i0)
        tt = np.arange(n) / SR
        duck[i0:i0 + n] = np.minimum(duck[i0:i0 + n], 1 - 0.32 * np.exp(-tt * 10))
    music *= duck
    lead_bus *= 0.85 + 0.15 * duck

    # reverb: decaying noise, different for each side
    ir_n = int(2.0 * SR)
    ti = np.arange(ir_n) / SR
    irs = [lp(RNG.standard_normal(ir_n), 6500) * np.exp(-ti / 0.42) for _ in range(2)]
    irs = [np.concatenate([np.zeros(int(0.018 * SR)), ir]) for ir in irs]
    send = 0.22 * lead_bus + 0.16 * music + 0.14 * stabs + 0.12 * drums + 0.25 * plucks
    send = np.stack([hp(c, 300) for c in send])
    wet = np.stack([sg.fftconvolve(send[c], irs[c])[:N] for c in range(2)]) * 0.11

    mix = drums * 0.75 + music + stabs + lead_bus + plucks + wet
    mix = np.stack([hp(c, 28) for c in mix])
    mix = np.tanh(1.15 * mix) / np.tanh(1.15)
    mix /= np.abs(mix).max() / 0.89
    out = HERE.parent / "assets" / "music" / "sj-circle-synth-raw.wav"
    wavfile.write(out, SR, mix.T.astype(np.float32))
    print(f"wrote {out} ({LENGTH:.1f} s)")


if __name__ == "__main__":
    main()
