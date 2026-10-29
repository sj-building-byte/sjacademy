"""Builds ../index.html from index.template.

The template is timed in SOURCE seconds (the raw take, PED.mov). edit.py cuts and speeds the take up,
so every data-start / data-duration here, and every tl position in the page (via T() in the script),
is mapped onto the edited timeline. Times past the end of the take run at normal speed (the end card).

Captions come from ../transcript.json, transcribed from the edited voice, so they are already in output time.
"""
import json
import re
from pathlib import Path

from edit import KEEP, SPEED

here = Path(__file__).parent
LAST = KEEP[-1][1]
END = sum(b - a for a, b in KEEP) / SPEED


def T(x):
    if x >= LAST:
        return END + (x - LAST)
    done = 0.0
    for a, b in KEEP:
        if x < a:
            return done / SPEED
        if x <= b:
            return (done + x - a) / SPEED
        done += b - a
    return END


def retime(html):
    """Maps each tag's data-start/data-duration. Sounds keep their own length; everything else stretches."""
    def tag(m):
        t = m.group(0)
        s = re.search(r'data-start="([\d.]+)"', t)
        d = re.search(r'data-duration="([\d.]+)"', t)
        if not (s and d):
            return t
        a, dur = float(s.group(1)), float(d.group(1))
        new_dur = dur if t.startswith("<audio") else T(a + dur) - T(a)
        t = t.replace(s.group(0), f'data-start="{T(a):.3f}"', 1)
        return t.replace(d.group(0), f'data-duration="{new_dur:.3f}"', 1)
    return re.sub(r"<(audio|video|div|section)\b[^>]*>", tag, html)


words = json.loads((here.parent / "transcript.json").read_text())
w = [[round(x["start"], 2), round(x["end"], 2), x["text"].strip()] for x in words]
# whisper pins the opening "So," to 0; the voice starts after the title beat. Keep it in the first phrase.
so_at = (6.25 - KEEP[0][0]) / SPEED  # "So" starts at 6.25s in the source
w[0] = [round(so_at, 2), round(so_at + 0.12, 2), w[0][2].rstrip(",")]
w[1][0] = max(w[1][0], w[0][1])

# whisper heard "that's a real pricing power"; he says "that's real pricing power"
w = [x for i, x in enumerate(w) if not (x[2] == "a" and i + 1 < len(w) and w[i + 1][2] == "real")]

# whisper split "inelastic" into two words
out = []
for x in w:
    if out and out[-1][2] == "in" and x[2].startswith("elastic"):
        out[-1] = [out[-1][0], x[1], "in" + x[2]]
    else:
        out.append(x)
w = out

MAX = 32
txt = lambda g: " ".join(y[2] for y in g)

# clauses end at punctuation; short clauses ("If they can,") join the next one when it fits
clauses, cur = [], []
for x in w:
    cur.append(x)
    if re.search(r"[.,?!]$", x[2]):
        clauses.append(cur)
        cur = []
if cur:
    clauses.append(cur)
merged = []
for c in clauses:
    if merged and len(txt(merged[-1])) < 12 and len(txt(merged[-1] + c)) <= MAX:
        merged[-1] = merged[-1] + c
    else:
        merged.append(c)

# long clauses split into balanced chunks
caps = []
for c in merged:
    n = -(-len(txt(c)) // MAX)
    target = len(txt(c)) / n
    chunk = []
    for x in c:
        if chunk and len(txt(chunk + [x])) > target + 4:
            caps.append(chunk)
            chunk = []
        chunk.append(x)
    caps.append(chunk)

(here / "captions.json").write_text(json.dumps(caps))
t = (here / "index.template").read_text()
t = t.replace("{{END}}", f"{END:.3f}").replace("{{CAPS}}", json.dumps(caps)).replace("{{KEEP}}", json.dumps(KEEP)).replace("{{SPEED}}", str(SPEED))
(here.parent / "index.html").write_text(retime(t))
print(f"built index.html: {len(caps)} caption phrases, voice ends {END:.2f}s, video ends {T(LAST + 5):.2f}s")
for c in caps:
    print(f"  {c[0][0]:6.2f}  " + txt(c))
