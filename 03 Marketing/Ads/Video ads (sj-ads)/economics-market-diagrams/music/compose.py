#!/usr/bin/env python3
"""Original synth track for the A Level Economics market diagrams reel, 128 BPM, D minor.

Same structure as the circle theorems track (v3), new key, new progression and new hook:
- a round, almost pure lead tone (2nd harmonic about -18 dB, 3rd about -26 dB), no echo
- one hook that develops over four items (8 bars)
- a bouncy half-time groove with offbeat bass in the opening, four-on-the-floor from the lift
  (beat 40, the indirect tax item)
Sync: video beat 0 is music beat 0. Each item is 8 beats: stab on 0, call on 1-3, stabs on 4 and 5
with the lead silent, answer on 6-7.5.
Run: /tmp/sj-audio/bin/python music/compose.py, then python3 music/normalise.py
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
RNG = np.random.default_rng(9708)
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


# ---------- arrangement (v3) ----------
CHORDS = {  # voicings above the D pedal
    "Dm": [57, 62, 65, 69], "Bb": [58, 62, 65, 70], "F": [57, 60, 65, 69], "C": [55, 60, 64, 67],
}
LOOP = ["Dm", "Bb", "F", "C"]  # one chord per bar


def chord_at(vb):
    if vb >= V_END + 8:
        return "Dm"
    return LOOP[int(vb // 4) % 4]


def section(vb):
    if vb < V_LIFT:
        return "A"  # bouncy half-time groove, offbeat bass
    if vb < V_RECAP:
        return "B"  # four-on-the-floor lift
    if vb < V_PITCH:
        return "R"
    if vb < V_END:
        return "P"
    return "E"


# The melody: one hook that develops over four theorems (8 bars), then repeats with the lift.
# Each note: (beat in theorem, midi, swoop start in semitones below or None for legato, glide s, length in beats)
# Beats 1-3: the call, swooping up while the pen draws, landing on beat 3 with the angle arcs.
# Beats 4-5: silence in the lead so the stamps' chord stabs speak. Beats 6-7.5: the answer.
PHRASES = [
    [(1.0, 69, 7, 0.11, 0.7), (1.75, 72, None, 0.04, 0.25), (2.0, 74, None, 0.04, 0.5), (2.5, 72, None, 0.04, 0.5),
     (3.0, 69, None, 0.07, 0.4), (6.0, 70, 5, 0.09, 0.5), (6.5, 69, None, 0.04, 0.5), (7.0, 65, None, 0.13, 0.35)],
    [(1.0, 72, 7, 0.11, 0.7), (1.75, 77, None, 0.05, 0.25), (2.0, 81, None, 0.08, 0.5), (2.5, 79, None, 0.04, 0.5),
     (3.0, 77, None, 0.07, 0.4), (6.0, 76, 5, 0.09, 0.5), (6.5, 79, None, 0.04, 0.5), (7.0, 72, None, 0.13, 0.35)],
    [(1.0, 74, 7, 0.11, 0.7), (1.75, 77, None, 0.04, 0.25), (2.0, 81, None, 0.06, 0.5), (2.5, 77, None, 0.04, 0.5),
     (3.0, 74, None, 0.07, 0.4), (6.0, 77, 5, 0.1, 0.5), (6.5, 74, None, 0.04, 0.5), (7.0, 70, None, 0.13, 0.35)],
    [(1.0, 69, 7, 0.11, 0.7), (1.75, 72, None, 0.05, 0.25), (2.0, 77, None, 0.06, 0.5), (2.5, 81, None, 0.09, 0.5),
     (3.0, 79, None, 0.07, 0.4), (6.0, 76, 3, 0.09, 0.5), (6.5, 72, None, 0.04, 0.5), (7.0, 67, None, 0.13, 0.35)],
]


def lead_events():
    ev = []
    n_scenes = int(V_RECAP // SCENE_BEATS)
    for s in range(n_scenes):
        base = s * SCENE_BEATS
        for b, m, sw, g, L in PHRASES[s % 4]:
            ev.append((base + b, m, sw, g, L))
    # recap: the hook once more, call on the pens (73-74), landing with the stamps (75)
    for b, m, sw, g, L in PHRASES[0]:
        ev.append((V_RECAP + b, m, sw, g, L))
    for b, m, sw, g, L in PHRASES[2][:5]:
        ev.append((V_RECAP + 8 + b - 1, m, sw, g, L))
    return sorted(ev)


def render_lead(events):
    """A round, almost pure tone (like the reference's lead) that swoops into notes."""
    pitch = np.full(N, 57.0)
    gate = np.zeros(N)
    note_on = np.full(N, -1.0)
    cur = 57.0
    for (b, m, sw, g, L) in events:
        i0, i1 = int(tb(b) * SR), int(tb(b + L) * SR)
        start = m - sw if sw is not None else cur
        ramp = np.arange(i1 - i0)
        pitch[i0:i1] = start + (m - start) * (1 - np.exp(-ramp / max(g * SR / 3, 1)))
        if i1 < N:
            pitch[i1:] = m
        gate[i0:i1] = 1
        note_on[i0:i1] = i0
        cur = m
    t = np.arange(N) / SR
    age = np.where(note_on >= 0, (np.arange(N) - note_on) / SR, 0)
    vib = 0.13 * np.sin(2 * np.pi * 5.2 * t) * np.clip((age - 0.18) / 0.15, 0, 1)
    f = midi_hz(pitch + vib)
    ph = 2 * np.pi * np.cumsum(f) / SR
    # harmonics set to the reference's measured tone: 2nd about -18 dB, 3rd about -26 dB
    tone = np.sin(ph) + 0.126 * np.sin(2 * ph) + 0.05 * np.sin(3 * ph)
    ph2 = 2 * np.pi * np.cumsum(f * 1.0035) / SR  # a second voice a few cents up, for width
    tone2 = np.sin(ph2) + 0.126 * np.sin(2 * ph2) + 0.05 * np.sin(3 * ph2)
    k_att, k_rel = 1 - np.exp(-1 / (0.012 * SR)), 1 - np.exp(-1 / (0.12 * SR))
    env = np.zeros(N)
    e = 0.0
    for i in range(0, N, 32):
        target = gate[i]
        k = k_att if target > e else k_rel
        e += (target - e) * (1 - (1 - k) ** 32)
        env[i:i + 32] = e
    return np.stack([tone * 0.8 + tone2 * 0.2, tone * 0.2 + tone2 * 0.8]) * env


def bass_pluck(m, vel=1.0, dur=0.22):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = midi_hz(m)
    s = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)
    s = np.tanh(2.0 * s) * np.exp(-t * 11) * np.minimum(t / 0.004, 1)
    return s * 0.5 * vel


def soft_pluck(m, vel=1.0, dur=0.5):
    n = int(dur * SR)
    t = np.arange(n) / SR
    ph = 2 * np.pi * midi_hz(m) * t
    s = (np.sin(ph) + 0.15 * np.sin(2 * ph)) * np.exp(-t * 8) * np.minimum(t / 0.003, 1)
    return pan(s * vel, 0.15)


def main():
    drums = np.zeros((2, N))
    music = np.zeros((2, N))  # pads and drone: ducked under the kick
    stabs = np.zeros((2, N))  # the hits: not ducked
    plucks = np.zeros((2, N))
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
        if sec == "A":
            # half-time bounce: kick on 1, a pickup kick on the "and" of 2 in the first bar,
            # clap on 3; in the second bar a clap on 2 under the second stamp
            if in_bar == 0:
                k(t0)
            if bar_in_scene == 0 and in_bar == 1:
                k(t0 + tb(0.5), 0.7)
            if in_bar == 2:
                place(drums, clap(0.95), t0)
            if bar_in_scene == 1 and in_bar == 1:
                place(drums, clap(0.6), t0)
            place(drums, hat(False, 0.5), t0 + tb(0.5))
            if in_bar == 1:  # ghost hat, kept clear of the sixteenth before each accent
                place(drums, hat(False, 0.2), t0 + tb(0.75))
            # offbeat bass on every "and", the bounce the reference has in its opening
            place(bass, bass_pluck(38 if in_bar % 2 == 0 else 50, 0.9 if in_bar != 3 else 0.3, 0.22 if in_bar != 3 else 0.1), t0 + tb(0.5))
        elif sec in "BR":
            k(t0, 1.0 if in_bar == 0 else 0.8)
            if in_bar in (1, 3):
                place(drums, clap(0.95), t0)
            place(drums, hat(in_bar != 3, 0.32), t0 + tb(0.5))
            place(drums, hat(False, 0.16), t0 + tb(0.25))
            if in_bar in (1, 2):
                place(drums, hat(False, 0.12), t0 + tb(0.75))
            place(bass, bass_pluck(38, 0.75 if in_bar != 3 else 0.3, 0.22 if in_bar != 3 else 0.1), t0 + tb(0.5))
        elif sec == "P":
            if in_bar == 0:
                k(t0, 0.8)
            if in_bar == 2:
                place(drums, clap(0.5), t0)
            place(drums, hat(False, 0.35), t0 + tb(0.5))
            place(bass, bass_pluck(38, 0.6), t0 + tb(0.5))
        elif sec == "E":
            if vb in (V_END, V_END + 4):
                k(t0)
            if vb < V_END + 8:
                place(drums, hat(False, 0.25), t0 + tb(0.5))

    for vb, v in ((V_LIFT, 0.7), (V_RECAP, 0.8), (V_END, 0.9)):
        place(drums, crash(v), tb(vb))

    # chord stabs on the sync points: landing (0), marks (2.5, 3), stamps (4, 5)
    for s in range(int(V_RECAP // SCENE_BEATS)):
        base = s * SCENE_BEATS
        for b, vel in ((0, 1.6), (2.5, 0.3), (3.0, 0.25), (4, 2.1), (5, 1.45)):
            vb = base + b
            br = (0.95 if base < V_LIFT else 1.1) * (1.2 if b in (0, 4, 5) else 1.0)
            place(stabs, stab(CHORDS[chord_at(vb)], vel * (1.25 if b in (0, 4, 5) else 1.0), bright=br), tb(vb), 0.85)
    for b, vel in ((0, 1.5), (1, 0.6), (3, 1.6), (4, 0.6), (6.5, 0.5), (7, 0.6), (8, 1.2), (10.5, 0.5), (11, 0.6)):
        vb = V_RECAP + b
        place(stabs, stab(CHORDS[chord_at(vb)], vel, bright=1.05), tb(vb), 0.85)
    for vb in range(V_PITCH, V_END, 4):
        place(stabs, stab(CHORDS[chord_at(vb)], 0.5, bright=0.55), tb(vb), 0.85)
    # end card: logo on 0, "Save this reel" on 1, "a friend" on 2.5, rule on 3, follow line on 4,
    # subline on 5, the two contact rows on 6 and 7, light sweep and final chord on 8
    for b, vel in ((0, 1.4), (1, 1.1), (2.5, 0.6), (3, 0.6), (4, 1.4), (5, 0.8), (6, 1.0), (7, 1.0)):
        place(stabs, stab(CHORDS["Dm" if b < 4 else "Bb"], vel, bright=0.8), tb(V_END + b), 0.85)
    final = CHORDS["Dm"] + [77]
    place(music, pad(final, tb(8) + 1.5, 1.2), tb(V_END + 8))
    place(stabs, stab(final, 0.9, dur=1.2, bright=0.7), tb(V_END + 8), 0.8)

    for vb in range(V_LIFT, V_END, 4):
        place(music, pad(CHORDS[chord_at(vb)], tb(4) + 0.3, 0.38 if section(vb) != "P" else 0.9), tb(vb))
    for vb in range(0, V_LIFT, 8):
        place(music, pad(CHORDS[chord_at(vb)], tb(8) + 0.3, 0.35), tb(vb))

    # a soft round pluck for each caption word
    for vb in range(V_PITCH + 1, V_END):
        tones = CHORDS[chord_at(vb)]
        place(plucks, soft_pluck(tones[(vb * 3) % len(tones)] + 12, 0.7), tb(vb))

    # the D drone (quieter than v2; it carries the low end with the offbeat bass)
    t = np.arange(N) / SR
    sub = np.tanh(1.8 * (np.sin(2 * np.pi * 73.42 * t) + 0.35 * np.sin(2 * np.pi * 146.83 * t))) * 0.09
    tail = t > tb(V_STOP) + 0.5
    sub[tail] *= np.exp(-(t[tail] - tb(V_STOP) - 0.5) * 3)
    sub = lp(sub, 240)
    music += np.stack([sub, sub])

    # lead, no echo; lifts off just before each accent so the hit has room
    events = lead_events()
    lead = render_lead(events) * 0.55
    high = render_lead([(b, m + 12, sw, g, L) for b, m, sw, g, L in events]) * 0.16
    lift_zone = (t >= tb(V_LIFT)) & (t < tb(V_PITCH))
    lead = lead * (1 + 0.1 * lift_zone) + high * lift_zone
    accents = [tb(s * SCENE_BEATS + b) for s in range(int(V_RECAP // SCENE_BEATS)) for b in (0, 4, 5)]
    accents += [tb(V_RECAP + b) for b in (0, 3)]
    dip = np.ones(N)
    for ta in accents:
        i0, i1 = int((ta - 0.25) * SR), int((ta + 0.03) * SR)
        if i0 < 0:
            continue
        w = np.linspace(0, np.pi, i1 - i0)
        dip[i0:i1] = np.minimum(dip[i0:i1], 1 - 0.85 * np.sin(w) ** 0.6)
    lead *= dip

    duck = np.ones(N)
    for kt in kick_times:
        i0 = int(kt * SR)
        n = min(int(0.35 * SR), N - i0)
        tt = np.arange(n) / SR
        duck[i0:i0 + n] = np.minimum(duck[i0:i0 + n], 1 - 0.32 * np.exp(-tt * 10))
    music *= duck

    # a short, soft room: no echo
    ir_n = int(1.3 * SR)
    ti = np.arange(ir_n) / SR
    irs = [np.concatenate([np.zeros(int(0.012 * SR)), lp(RNG.standard_normal(ir_n), 5000) * np.exp(-ti / 0.28)]) for _ in range(2)]
    send = 0.18 * lead + 0.12 * stabs + 0.1 * music + 0.08 * drums + 0.2 * plucks
    send = np.stack([hp(c, 300) for c in send])
    wet = np.stack([sg.fftconvolve(send[c], irs[c])[:N] for c in range(2)]) * 0.09

    mix = drums * 0.75 + music + stabs + lead + plucks + bass + wet
    mix = np.stack([hp(c, 28) for c in mix])
    mix = np.tanh(1.1 * mix) / np.tanh(1.1)
    mix /= np.abs(mix).max() / 0.89
    out = HERE.parent / "assets" / "music" / "sj-market-synth-raw.wav"
    wavfile.write(out, SR, mix.T.astype(np.float32))
    print(f"wrote {out} ({LENGTH:.1f} s)")


if __name__ == "__main__":
    main()
