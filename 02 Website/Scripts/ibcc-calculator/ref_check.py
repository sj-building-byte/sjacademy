"""Independent second solve for the IBCC engine (ACCURACY.md step 1).
1. Parses IBCC's own A* PDFs (text) and compares every value with engine.js.
2. Re-implements the rules in Python from the sources and compares thousands of random cases with engine.js.
3. Checks IBCC's and Cambridge's published worked examples."""
import json, os, random, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "sources")
problems = []

# ---------- 1. A* tables from the official text ----------
NAMES = {"physics": "phy", "chemistry": "chem", "biology": "bio", "computer studies": "cs", "computer science": "cs",
         "computer": "cs", "mathematics": "math", "english": "eng", "urdu": "urdu", "pakistan studies": "pst",
         "pak studies": "pst", "islamiyat": "isl"}
official = {"O": {}, "A": {}}
for f in sorted(os.listdir(SRC)):
    m = re.match(r"(\d{4})-([oa])\.txt", f)
    if not m:
        continue
    year, lvl = int(m.group(1)), m.group(2).upper()
    text = re.sub(r"\s+", " ", open(os.path.join(SRC, f)).read())
    body = text.split("Pak. Marks", 1)[1]
    t = {}
    for name, val in re.findall(r"([A-Za-z][A-Za-z .]*?)\s+(\d{2}|NA)\b", body):
        n = name.strip().lower()
        if "other" in n:
            t["_"] = int(val)
        elif val != "NA":
            t[NAMES[n]] = int(val)
    official[lvl][year] = t

node = subprocess.run(["node", "-e", "const S=require('%s/engine.js');console.log(JSON.stringify(S.ASTAR))" % HERE],
                      capture_output=True, text=True, check=True)
eng = json.loads(node.stdout)
subjects = ["phy", "chem", "bio", "cs", "math", "eng", "urdu", "pst", "isl", "acc"]
checked = 0
for lvl in "OA":
    for year, t in official[lvl].items():
        e = eng[lvl][str(year)]
        for s in subjects:
            want = t.get(s, t["_"])
            got = e.get(s, e["_"])
            checked += 1
            if want != got:
                problems.append("A* %s %d %s: official %s, engine %s" % (lvl, year, s, want, got))
print("A* values compared with IBCC text:", checked)

# ---------- 2. Python re-implementation ----------
LET = {"A": 85, "B": 75, "C": 65, "D": 55, "E": 45}
NUM = {"8": 87, "7": 82, "6": 77, "5": 70, "4": 60, "3": 50, "2": 40}


def star(lvl, year, subj):
    y = 2026 if year == 2027 else (2020 if year <= 2020 else year)
    if y == 2020:
        return 90
    t = official[lvl][y]
    if subj == "ethics" or (lvl == "A" and subj in ("eng", "englit", "urdu", "isl", "pst")):
        return t["_"]
    return t.get(subj, t["_"])


def mk(lvl, year, subj, g):
    if g in LET:
        return LET[g]
    if g in NUM:
        return NUM[g]
    return star(lvl, year, subj)  # A* or 9


def ref(case):
    """case: target, route, group, rows list of (level, kind, subj, grade, year)."""
    rows = case["rows"]
    O = [r for r in rows if r[0] == "O"]
    A = [r for r in rows if r[0] == "A"]
    o_total = sum(mk(*([r[0], r[4], r[2], r[3]])) for r in O)
    ssc = round(o_total / (len(O) * 100) * 900 + 1e-9)
    if case["target"] == "ssc":
        return {"marks": ssc, "max": len(O) * 100}
    science = case["group"] != "hum"
    finish = max(r[4] for r in O)
    new = science and finish >= 2026
    counted = [r for r in O if (r[1] == "comp" or not new)] + A
    tot = sum(mk(r[0], r[4], r[2], r[3]) for r in counted)
    mx = len(counted) * 100
    return {"marks": round(tot / mx * 1100 + 1e-9), "max": mx, "ssc": ssc, "new": new}


YEARS = [2019, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
ELEC = ["phy", "chem", "bio", "cs", "acc", "econ", "bus", "addm"]
ASUB = ["phy", "chem", "bio", "math", "cs", "econ", "bus", "psy", "eng", "urdu"]
GA = {"pm": ["phy", "chem", "bio"], "pe": ["phy", "chem", "math"], "cs": ["phy", "math", "cs"]}


def rand_case(rng):
    target = rng.choice(["ssc", "hssc"])
    route = rng.choice(["pk", "abroad", "foreign"] + (["mixed"] if target == "hssc" else []))
    group = rng.choice(["pm", "pe", "cs", "hum"]) if target == "hssc" else None
    ex = route in ("abroad", "foreign")
    numeric = rng.random() < 0.25
    og = (["9", "8", "7", "6", "5", "4", "3", "2"] if numeric else ["A*", "A", "B", "C", "D", "E"])
    oyear = rng.choice(YEARS)
    ayear = rng.choice(YEARS)
    st = {"target": target, "route": route, "group": group, "oYear": oyear, "aYear": ayear, "rows": {}}
    rows = []

    def add(rid, lvl, kind, subj, fixed):
        y = rng.choice(YEARS) if rng.random() < 0.2 else (oyear if lvl == "O" else ayear)
        g = rng.choice(og if lvl == "O" else ["A*", "A", "B", "C", "D", "E"])
        st["rows"][rid] = {"grade": g}
        if y != (oyear if lvl == "O" else ayear):
            st["rows"][rid]["year"] = y
        if not fixed:
            st["rows"][rid]["subj"] = subj
        rows.append((lvl, kind, subj, g, y))

    add("o-eng", "O", "comp", "eng", True)
    add("o-math", "O", "comp", "math", True)
    if not ex:
        add("o-urdu", "O", "comp", "urdu", True)
        isl = rng.choice(["isl", "ethics"])
        add("o-isl", "O", "comp", isl, isl == "isl")
        if isl == "ethics":
            st["rows"]["o-isl"]["subj"] = "ethics"
        add("o-pst", "O", "comp", "pst", True)
    if target == "hssc" and group != "hum":
        add("o-e1", "O", "elec", "phy", True)
        add("o-e2", "O", "elec", "chem", True)
        if group == "pm":
            add("o-e3", "O", "elec", "bio", True)
        else:
            add("o-e3", "O", "elec", rng.choice(["bio", "cs", "addm"]), False)
        for i, s in enumerate(GA[group]):
            add("a-%d" % (i + 1), "A", "a", s, True)
    else:
        for i, s in enumerate(rng.sample(ELEC, 3)):
            add("o-e%d" % (i + 1), "O", "elec", s, False)
        if target == "hssc":
            for i, s in enumerate(rng.sample(ASUB, 3)):
                add("a-%d" % (i + 1), "A", "a", s, False)
    return st, {"target": target, "route": route, "group": group, "rows": rows}


rng = random.Random(2026)
cases = [rand_case(rng) for _ in range(5000)]
js = subprocess.run(["node", "-e", """
const S=require('%s/engine.js');let d='';process.stdin.on('data',c=>d+=c).on('end',()=>{
const out=JSON.parse(d).map(s=>{const r=S.compute(s);return {status:r.status,marks:r.marks,max:r.max,ssc:r.ssc&&r.ssc.marks,newRule:!!r.newRule,errors:r.errors,missing:r.missing};});
console.log(JSON.stringify(out));});""" % HERE], input=json.dumps([c[0] for c in cases]), capture_output=True, text=True, check=True)
outs = json.loads(js.stdout)
bad = 0
for (st, case), got in zip(cases, outs):
    want = ref(case)
    ok = got["status"] == "ok" and got["marks"] == want["marks"] and got["max"] == want["max"]
    if case["target"] == "hssc":
        ok = ok and got["ssc"] == want["ssc"] and got["newRule"] == want["new"]
    if not ok:
        bad += 1
        if bad <= 5:
            problems.append("random case differs: %s\n   engine %s\n   python %s" % (json.dumps(st), got, want))
print("random cases compared:", len(cases), "differences:", bad)

# ---------- 3. Published worked examples ----------
FIX = []
all_star = lambda ids: {i: {"grade": "A*"} for i in ids}
O8 = ["o-eng", "o-math", "o-urdu", "o-isl", "o-pst", "o-e1", "o-e2", "o-e3"]
O5 = ["o-eng", "o-math", "o-e1", "o-e2", "o-e3"]
# IBCC O Level example (2021 A* values, Pakistan): 750/800 -> 844/900. Electives Physics, Chemistry, Biology.
r = all_star(O8); r["o-e1"]["subj"] = "phy"; r["o-e2"]["subj"] = "chem"; r["o-e3"]["subj"] = "bio"
FIX.append(("IBCC O Level example, Pakistan", {"target": "ssc", "route": "pk", "oYear": 2021, "rows": r}, 750, 844))
r = all_star(O5); r["o-e1"]["subj"] = "phy"; r["o-e2"]["subj"] = "chem"; r["o-e3"]["subj"] = "bio"
FIX.append(("IBCC O Level example, abroad", {"target": "ssc", "route": "foreign", "oYear": 2021, "rows": r}, 470, 846))
# IBCC A Level example (2021 values): Pakistan 1030/1100; overseas 750/800 -> 1031
FIX.append(("IBCC A Level example, Pakistan", {"target": "hssc", "route": "pk", "group": "pm", "oYear": 2021, "aYear": 2021,
            "rows": all_star(O8 + ["a-1", "a-2", "a-3"])}, 1030, 1030))
FIX.append(("IBCC A Level example, abroad", {"target": "hssc", "route": "abroad", "group": "pm", "oYear": 2021, "aYear": 2021,
            "rows": all_star(O5 + ["a-1", "a-2", "a-3"])}, 750, 1031))
# Cambridge Destination Pakistan SSC example (2023 values): 629/800 x 900 = 707.6 -> 708
r = {"o-eng": {"grade": "A*"}, "o-urdu": {"grade": "B"}, "o-isl": {"grade": "A"}, "o-pst": {"grade": "B"},
     "o-e1": {"subj": "phy", "grade": "A"}, "o-e2": {"subj": "chem", "grade": "C"}, "o-e3": {"subj": "bio", "grade": "D"},
     "o-math": {"grade": "A*"}}
FIX.append(("Cambridge brochure SSC example", {"target": "ssc", "route": "pk", "oYear": 2023, "rows": r}, 629, 708))
# Audit fixtures: eight O Level As = 680/800; eleven As = 935/1100
r = {i: {"grade": "A"} for i in O8}; r["o-e1"]["subj"] = "phy"; r["o-e2"]["subj"] = "chem"; r["o-e3"]["subj"] = "bio"
FIX.append(("Eight O Level As", {"target": "ssc", "route": "pk", "oYear": 2025, "rows": r}, 680, 765))
FIX.append(("Legacy HSSC, eleven As", {"target": "hssc", "route": "pk", "group": "pm", "oYear": 2025, "aYear": 2026,
            "rows": {i: {"grade": "A"} for i in O8 + ["a-1", "a-2", "a-3"]}}, 935, 935))
# New rule (O Levels 2026): 5 compulsory As + 3 A Level Bs = 650/800 -> 893.75 -> 894
r = {i: {"grade": "A"} for i in O8}; r.update({i: {"grade": "B"} for i in ["a-1", "a-2", "a-3"]})
FIX.append(("New 2026 rule, 5 As + 3 Bs", {"target": "hssc", "route": "pk", "group": "pe", "oYear": 2026, "aYear": 2027,
            "rows": dict(r, **{"o-e3": {"grade": "A", "subj": "cs"}})}, 650, 894))
js = subprocess.run(["node", "-e", """
const S=require('%s/engine.js');let d='';process.stdin.on('data',c=>d+=c).on('end',()=>{
console.log(JSON.stringify(JSON.parse(d).map(s=>{const r=S.compute(s);return [r.status,r.raw,r.marks,r.pct,r.errors,r.missing];})));});""" % HERE],
                    input=json.dumps([f[1] for f in FIX]), capture_output=True, text=True, check=True)
for (name, _, raw, marks), got in zip(FIX, json.loads(js.stdout)):
    line = "%-34s raw %s (want %s)  marks %s (want %s)  %s%%  %s" % (name, got[1], raw, got[2], marks, got[3], got[0])
    print(line)
    if got[1] != raw or got[2] != marks:
        problems.append(line + " " + json.dumps(got[4:]))

print("\nPROBLEMS:" if problems else "\nPROBLEMS: none")
for p in problems:
    print(" -", p)
sys.exit(1 if problems else 0)
