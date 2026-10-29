"""Builds "Solve it in your head" episodes from one template.

Usage: python3 mental-maths-build.py
Each episode spec is one file, mental-maths-episodes/epNN.py; output goes to mental-maths-epNN/. Assets are copied from mental-maths-ep01.
To add an episode, add mental-maths-episodes/epNN.py (copy a similar one) and run the script.
Timing is fixed: question 0-1.9s, 10s countdown 2.2-12.2s, reveal 12.6-20s, end card 20-24s.
An episode can set "template" to use its own page and timing instead (#7: 5s countdown, 21s).
"""
import json, shutil
from pathlib import Path

HERE = Path(__file__).parent
BASE = HERE / "mental-maths-ep01"

INK, YEL, PEN = "#151515", "#FCE004", "#D63A2F"

def path(id_, d, w=9, color=INK, extra=""):
    return (f'<path id="{id_}" d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-linejoin="round" pathLength="1" stroke-dasharray="1" {extra}/>')

import math
# stacked fractions, so "x + 1/x" can't be misread as (x + 1)/x
FR = '<span class="fr"><span>1</span><span>x</span></span>'
FR2 = '<span class="fr"><span>1</span><span>x²</span></span>'

EPISODES_DIR = HERE / "mental-maths-episodes"

def load_episode(f):
    """Each episode is one small file defining EPISODE. Shelved (built, never posted) ones live in episodes/shelved and are not built."""
    ns = {"path": path, "FR": FR, "FR2": FR2, "INK": INK, "YEL": YEL, "PEN": PEN, "math": math}
    exec(compile(f.read_text(), str(f), "exec"), ns)
    return ns["EPISODE"]

EPISODES = [load_episode(f) for f in sorted(EPISODES_DIR.glob("ep*.py"))]

TEMPLATE = (HERE / "mental-maths-template.html").read_text()

def lbl_html(id_, text, left, top, size, cls, hidden=False):
    return f'<div class="lbl {cls}" id="{id_}" style="left:{left}px;top:{top}px;font-size:{size}px">{text}</div>'

def accuracy_check(ep):
    """Mechanical part of 00 Start Here/ACCURACY.md. The frame-by-frame student read still has to be done by eye."""
    got = ep["verify"]()
    assert abs(got - ep["expect"]) < 1e-9, f'{ep["slug"]}: computed {got}, expected {ep["expect"]}'
    assert str(ep["expect"]) in ep["answer"], f'{ep["slug"]}: answer card "{ep["answer"]}" does not show {ep["expect"]}'
    on_screen = " ".join([ep["question"]] + [l[1] for l in ep["labels"]]).lower()
    missing = [w for w in ep["must_show"] if w.lower() not in on_screen]
    assert not missing, f'{ep["slug"]}: question is incomplete, missing on screen: {missing}'
    if ep.get("hide_answer"):
        shown = [ep["question"], ep["hint"], ep["caption"], *ep["trick"], *ep["steps"], *ep["tips"], ep["tip_title"]] + [l[1] for l in ep["labels"] + ep["reveal_labels"]]
        leaks = [t for t in shown if str(ep["expect"]) in t]
        assert not leaks, f'{ep["slug"]}: answer is hidden but shows up in: {leaks}'
    else:
        assert str(ep["expect"]) in ep["answer_at"][1], f'{ep["slug"]}: diagram answer label disagrees with the answer'
    print(f'{ep["slug"]}: answer {got:g} verified; conditions on screen: {", ".join(ep["must_show"])}')

for ep in EPISODES:
    accuracy_check(ep)

import re
def visible_text(html):
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S)
    return re.sub(r"<[^>]+>", " ", html)

def write_brief(ep, out, hide):
    brief = out / "BRIEF.md"
    old_brief = brief.read_text() if brief.exists() else ""
    notes = old_brief[old_brief.index("\n## Notes"):] if "\n## Notes" in old_brief else ""
    (out / "BRIEF.md").write_text(
        f"# Solve it in your head, #{ep['num']}\n\n- workflow: general-video\n- Built by ../mental-maths-build.py from ../{ep.get('template', 'mental-maths-template.html')}. Edit the episode there, not here.\n"
        f"- Question: {ep['question']}\n- Answer: {ep['answer']}" + (" (hidden: never shown on screen or in the caption; viewers comment it)" if hide else "") + "\n"
        f"- Status: final, in ✅ Finished/Videos/Solve it in your head/Solve it in your head {ep['num']}.mp4\n\n"
        f"## Accuracy check (00 Start Here/ACCURACY.md)\n"
        f"- Solved twice: worked by hand and computed by the build script (answer {ep['expect']}).\n"
        f"- Conditions shown on screen: {', '.join(ep['must_show'])}.\n"
        + ("- Answer hidden: the build checks it appears nowhere on screen or in the caption.\n" if hide else "- Answer card and diagram label agree.\n")
        + (f"- Frame review as a student (question, mid-countdown, each reveal step, answer, tip, end card): passed {ep['reviewed']}.\n"
           if ep.get("reviewed") else "- Frame review as a student: NOT DONE YET. Do it, then set \"reviewed\" in the spec.\n")
        + notes)

def build_custom(ep, out):
    """Episodes with their own template (no diagram, own timing). The page holds its own layout and motion."""
    hide = ep.get("hide_answer", False)
    steps = "\n          ".join(f'<div class="mask stp"><span id="st{i}">{s}</span></div>' for i, s in enumerate(ep["steps"]))
    rows = "".join(f'<div class="r"><b>{n}</b><i class="tl">{m}</i><i class="tr">25</i><em>= {r}</em></div>' for n, m, r in ep["tip_rows"])
    t1, t2 = ep["trick"]
    html = ((HERE / ep["template"]).read_text()
            .replace("{{NUM}}", str(ep["num"]))
            .replace("{{QUESTION}}", ep["question"])
            .replace("{{HINT}}", ep["hint"])
            .replace("{{TRICK1}}", t1)
            .replace("{{TRICK2}}", f'<span class="hlw">{t2}<i class="mk" id="mk-r"></i></span>')
            .replace("{{STEPS}}", steps)
            .replace("{{CARD}}", "Your turn." if hide else ep["answer"])
            .replace("{{END1}}", "What did" if hide else "How long did")
            .replace("{{END2}}", "you get?" if hide else "it take you?")
            .replace("{{PILL}}", "Comment your answer." if hide else "Comment your time.")
            .replace("{{ENDV}}", "?" if hide else ep["answer"])
            .replace("{{TIPTITLE}}", ep["tip_title"])
            .replace("{{TIPROWS}}", rows))
    assert "{{" not in html, f'{ep["slug"]}: unfilled placeholder in {ep["template"]}'
    if hide:
        assert str(ep["expect"]) not in visible_text(html), f'{ep["slug"]}: answer is hidden but appears on the page'
    (out / "index.html").write_text(html)
    (out / "CAPTION.txt").write_text(ep["caption"] + "\n")
    write_brief(ep, out, hide)
    print("built", ep["slug"], "(own template)")

for ep in EPISODES:
    out = HERE / ep["slug"]
    if not out.exists():
        shutil.copytree(BASE, out, ignore=shutil.ignore_patterns("renders", ".hyperframes", "index.html", "BRIEF.md", "snapshots", "CLAUDE.md", "AGENTS.md"))
        (out / "renders").mkdir(exist_ok=True)
        (out / "meta.json").write_text(json.dumps({"id": ep["slug"], "name": ep["slug"], "createdAt": "2026-10-17T13:00:00.000Z"}, indent=2) + "\n")
        pkg = (BASE / "package.json").read_text().replace("mental-maths-ep01", ep["slug"])
        (out / "package.json").write_text(pkg)

    if ep.get("template"):
        build_custom(ep, out)
        continue
    labels = "\n        ".join(lbl_html(*l) for l in ep["labels"] + ep["reveal_labels"])
    hide = ep.get("hide_answer", False)
    if hide:
        aid = ep["unknown"]
    else:
        aid, atext, aleft, atop, asize = ep["answer_at"]
        labels += f'\n        <div class="lbl ans" id="lans" style="left:{aleft}px;top:{atop}px;font-size:{asize}px"><span>{atext}</span></div>'
    steps = "\n          ".join(f'<div class="mask stp"><span id="st{i}">{s}</span></div>' for i, s in enumerate(ep["steps"]))
    tips = "".join(f"<span>{t}</span>" for t in ep["tips"])
    t1, t2 = ep["trick"]
    trick2 = f'<span class="hlw">{t2}<i class="mk" id="mk-r"></i></span>'

    js = []
    for l in ep["labels"]:
        js.append(f'pop("#{l[0]}", 1.25);')
    for kind, id_, t, *rest in ep["reveal"]:
        if kind == "pen":
            js.append(f'pen("#{id_}", {t}, {rest[0]});')
        elif kind == "pop":
            js.append(f'pop("#{id_}", {t});')
        elif kind == "fill":
            js.append(f'tl.fromTo("#{id_}", {{ opacity: 0 }}, {{ opacity: 0.55, duration: 0.4, ease: "none" }}, {t});')
    js.append(f'tl.fromTo("#{aid}", {{ rotation: -6 }}, {{ rotation: 6, duration: 0.5, repeat: 9, yoyo: true, ease: "sine.inOut" }}, 2.2);')
    js.append(f'tl.to("#{aid}", {{ rotation: 0, duration: 0.2 }}, 12.2);')
    if not hide:
        js.append(f'tl.to("#{aid}", {{ opacity: 0, scale: 0.6, duration: 0.15 }}, 15.85);')

    svg_paths_question = [p for p in ("q1", "q2", "q3", "q4", "q5") if f'id="{p}"' in ep["svg"]]
    for i, p in enumerate(svg_paths_question):
        js.append(f'pen("#{p}", {0.3 + i * 0.22:.2f}, 0.35);')
    for d in ("dl", "dr"):
        if f'id="{d}"' in ep["svg"]:
            js.append(f'tl.fromTo("#{d}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3, ease: "none" }}, 0.75);')
    if 'id="q6"' in ep["svg"]:
        js.append('pop("#q6", 1.1);')

    html = (TEMPLATE
            .replace("{{NUM}}", str(ep["num"]))
            .replace("{{SVG}}", ep["svg"])
            .replace("{{LABELS}}", labels)
            .replace("{{QUESTION}}", ep["question"])
            .replace("{{QSIZE}}", str(ep.get("qsize", 66)))
            .replace("{{HINT}}", ep["hint"])
            .replace("{{TRICK1}}", t1)
            .replace("{{TRICK2}}", trick2)
            .replace("{{STEPS}}", steps)
            .replace("{{CARD}}", "Your turn." if hide else ep["answer"])
            .replace("{{ANSJS}}", "" if hide else '      stamp("#lans", 16.0, -8);\n')
            .replace("{{END1}}", "What did" if hide else "How long did")
            .replace("{{END2}}", "you get?" if hide else "it take you?")
            .replace("{{PILL}}", "Comment your answer." if hide else "Comment your time.")
            .replace("{{ENDV}}", "?" if hide else ep["answer"])
            .replace("{{TIPTITLE}}", ep["tip_title"])
            .replace("{{TIPS}}", tips)
            .replace("{{TIPSIZE}}", str(ep.get("tipsize", 38)))
            .replace("{{EPJS}}", "\n      ".join(js)))
    (out / "index.html").write_text(html)
    (out / "CAPTION.txt").write_text(ep["caption"] + "\n")
    brief = out / "BRIEF.md"
    old_brief = brief.read_text() if brief.exists() else ""
    notes = old_brief[old_brief.index("\n## Notes"):] if "\n## Notes" in old_brief else ""
    (out / "BRIEF.md").write_text(
        f"# Solve it in your head, #{ep['num']}\n\n- workflow: general-video\n- Built by ../mental-maths-build.py from ../mental-maths-template.html. Edit the episode there, not here.\n"
        f"- Question: {ep['question']}\n- Answer: {ep['answer']}" + (" (hidden: never shown on screen or in the caption; viewers comment it)" if hide else "") + "\n"
        f"- Status: final, in ✅ Finished/Videos/Solve it in your head/Solve it in your head {ep['num']}.mp4\n\n"
        f"## Accuracy check (00 Start Here/ACCURACY.md)\n"
        f"- Solved twice: worked by hand and computed by the build script (answer {ep['expect']}).\n"
        f"- Conditions shown on screen: {', '.join(ep['must_show'])}.\n"
        + ("- Answer hidden: the build checks it appears nowhere on screen or in the caption.\n" if hide else "- Answer card and diagram label agree.\n")
        + (f"- Frame review as a student (question, mid-countdown, each reveal step, answer, tip, end card): passed {ep['reviewed']}.\n"
           if ep.get("reviewed") else "- Frame review as a student: NOT DONE YET. Do it, then set \"reviewed\" in the spec.\n")
        + notes)
    print("built", ep["slug"])
