#!/usr/bin/env python3
"""Second solve of the ranking. This is a separate Python version of rank() in source.html, written from the
rules in BRIEF.md (not by translating line by line). It runs 5,000 random answer sets through both and compares
the three route ids. Needs node. Run: python3 ref_check.py"""
import json, os, random, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "source.html"), encoding="utf-8").read()
def grab(n): return re.search(r"var %s=(.*?);\n" % n, src, re.S).group(1)
DATA = ["SUBJ", "OL_GROUPS", "OL2A", "HAS_OL", "STYLES", "DIRS", "BAN_GROUPS", "ROUTES"]
prelude = "".join("var %s=%s;\n" % (n, grab(n)) for n in DATA)
fn = re.search(r"(  var names=.*?\n  var has=.*?\n)", src, re.S).group(1)
rank_js = re.search(r"(  function rank\(s\)\{.*?\n  \}\n)", src, re.S).group(1)
rng = random.Random(7)
OL = [i[0] for g in json.loads(subprocess.run(["node", "-e", prelude + "console.log(JSON.stringify(OL_GROUPS))"], capture_output=True, text=True, check=True).stdout) for i in g["items"]]
STY = ["logic", "essays", "science", "systems", "projects"]
DIR = ["medicine", "engineering", "cs", "business", "law", "creative"]
BAN = ["biology", "chemistry", "physics", "math", "cs", "econ", "accounting", "essay"]
states = []
for _ in range(5000):
    d = ["undecided"] if rng.random() < .15 else rng.sample(DIR, rng.choice([1, 2]))
    states.append({"strong": rng.sample(OL, rng.randint(1, 8)), "style": rng.choice(STY), "dirs": d,
                   "bans": rng.sample(BAN, rng.choice([0, 0, 0, 1, 1, 2, 3]))})
js = prelude + fn + rank_js + "var S=%s;console.log(JSON.stringify(S.map(function(s){var r=rank(s);return {t:r.top.map(function(x){return x.r.id}),d:r.removed.map(function(x){return x.r.id}),f:r.fallback}})))" % json.dumps(states)
open(os.path.join(HERE, ".rank_tmp.js"), "w").write(js)
js_out = json.loads(subprocess.run(["node", os.path.join(HERE, ".rank_tmp.js")], capture_output=True, text=True, check=True).stdout)
os.remove(os.path.join(HERE, ".rank_tmp.js"))

# ---- independent Python version ----
R = json.loads(subprocess.run(["node", "-e", prelude + "console.log(JSON.stringify({r:ROUTES,o:OL2A,h:HAS_OL,b:BAN_GROUPS}))"], capture_output=True, text=True, check=True).stdout)
ROUTES, OL2A, HAS, BANG = R["r"], R["o"], R["h"], R["b"]
def solve(s):
    banned = set()
    for g in BANG:
        for b in g["items"]:
            if b["id"] in s["bans"]: banned.update(b["keys"])
    liked = {a for o in s["strong"] for a in OL2A.get(o, [])}
    und = "undecided" in s["dirs"]
    cand, removed = [], []
    for idx, r in enumerate(ROUTES):
        pool = [k for k in r.get("choose", {}).get("from", []) if k not in banned]
        dead = any(k in banned for k in r["core"]) or ("choose" in r and len(pool) < r["choose"]["n"])
        dirs = [t for t in r["tags"] if t in s["dirs"]]
        if dead:
            if dirs: removed.append(r["id"])
            continue
        score = len(r["tags"]) * 2 if und else (10 * len(dirs) if dirs else -20)
        if r["style"] == s["style"]: score += 5
        have = [k for k in r["core"] if k in liked]
        weak = [k for k in r["core"] if k not in liked and HAS.get(k)]
        need = len(r["core"]); got = len(have)
        if "choose" in r:
            need += r["choose"]["n"]; got += min(r["choose"]["n"], len([k for k in pool if k in liked]))
        score += int(10 * got / need + 0.5) - 2 * len(weak) if need else -2 * len(weak)
        cand.append((-score, idx, r["id"], bool(dirs)))
    cand.sort()
    top = []
    for d in s["dirs"]:
        for c in cand:
            if d in ROUTES[c[1]]["tags"]:
                if c not in top: top.append(c)
                break
    for c in cand:
        if len(top) >= 3: break
        if c not in top: top.append(c)
    top.sort()
    return {"t": [c[2] for c in top], "d": removed, "f": (not und) and bool(top) and not top[0][3]}
bad = [(i, s, js_out[i], solve(s)) for i, s in enumerate(states) if solve(s) != js_out[i]]
print("states:", len(states), "differences:", len(bad))
for b in bad[:3]: print(b)
raise SystemExit(1 if bad else 0)
