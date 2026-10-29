import json, gt_data as D

def a_star(A, B, mx):
    return min(2 * A - B, (A + mx) / 2.0)

import math
def rnd(x):
    return math.floor(x + 0.5)

def totals(asv, a2v, tot):
    """Cambridge rule, checked against every row: A, B, E are summed and rounded; C and D sit
    one third and two thirds of the way from B down to E (rounded down); A* is A plus the
    A-to-B gap, but never more than halfway from A to full marks."""
    A = rnd(asv[0] + a2v[0]); B = rnd(asv[1] + a2v[1]); E = rnd(asv[4] + a2v[4])
    C = math.floor(B - (B - E) / 3.0 + 1e-9); Dd = math.floor(B - 2 * (B - E) / 3.0 + 1e-9)
    S = rnd(min(2 * A - B, (A + tot) / 2.0))
    return [S, A, B, C, Dd, E]

def build():
    out, problems = [], []
    keys = [s[0] for s in D.SESSIONS]
    for sub in D.SUBJECTS:
        P = sub["papers"]
        for r in sub["routes"]:
            comps = r.get("comps") or sub["comps_all"]
            as_rows = r.get("as_rows") or sub["as_rows_all"][r["as_key"]]
            as_max = round(sum(P[p][1] * P[p][2] for p in r["as"]), 3)
            a2_max = round(sum(P[p][1] * P[p][2] for p in r["a2"]), 3)
            tot = as_max + a2_max
            sess = {}
            for k in keys:
                rows = as_rows[k]
                asv = [sum(row[i] for row in rows) / len(rows) for i in range(5)]
                a2v = [sum(comps[k][p][i] * P[p][2] for p in r["a2"]) for i in range(5)]
                sess[k] = {"as": [round(x, 2) for x in asv], "a2": [round(x, 2) for x in a2v]}
                # verify against Cambridge linear rows (average of rows given)
                chk = r["check"][k]
                if isinstance(chk[0], list):
                    chk = [sum(c[i] for c in chk) / len(chk) for i in range(6)]
                mine = totals(asv, a2v, tot)
                diff = max(abs(mine[i] - chk[i]) for i in range(6))
                tag = "%s %s %s" % (sub["code"], r["id"], k)
                if __name__ == "__main__": print("%-22s mine=%s cambridge=%s maxdiff=%.2f" % (tag, [round(x, 1) for x in mine], chk, diff))
                if diff > 1.01:
                    problems.append(tag)
            out.append({
                "code": sub["code"], "name": sub["name"], "route": r["id"], "label": r["label"],
                "asMax": as_max, "a2Max": a2_max,
                "asPapers": [[p if len(p) > 1 else "Paper " + p, P[p][0], P[p][1]] for p in r["as"]],
                "a2Papers": [[p if len(p) > 1 else "Paper " + p, P[p][0], P[p][1], P[p][2]] for p in r["a2"]],
                "s": sess,
            })
    return out, problems

if __name__ == "__main__":
    data, problems = build()
    print("PROBLEMS:", problems)
