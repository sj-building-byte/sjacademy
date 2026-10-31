#!/usr/bin/env python3
"""Refreshes only the paper tables in a hand-edited past papers page, from the checked file list.

For pages whose copy was written by hand (A Level Business, Economics, Maths), so nothing outside the
paper tables changes: headings, copy, keywords, FAQs and structured data stay byte for byte.
Inside each series table it:
  - keeps the page's own paper rows and paper names
  - links only files that exist in storage, and adds files that exist but were missing (extra variants)
  - adds a "Side by side" link to the past paper viewer for each paper with a mark scheme
It also updates the file count in the hero and makes the page script skip the Side by side links.

Run: python3 refresh-tables.py   (all pages in PAGES below)
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.normpath(os.path.join(HERE, "..", ".."))
VIEWER = os.path.join(WEB, "Tools", "Past Paper Viewer", "past-paper-viewer-elementor-widget.html")
SITE = "https://www.sjacademy.pk"
STORE = "https://sjacademy.pk/file/Past-papers-storage/A+Level"
LBL = {"qp": "QP", "ms": "MS", "in": "IN", "ci": "CI"}
SESS = {"s": ("May+June", "mj"), "w": ("October+November", "on")}

# page file, file list key, code, storage folder, viewer subject slug, wrapper class
PAGES = [
    ("a-level-business-past-papers-elementor-widget.html", "A Level/Business", "9609", "Business+%289609%29", "business", "sj-p-pp-business"),
    ("a-level-economics-past-papers-elementor-widget.html", "A Level/Economics", "9708", "Economics+%289708%29", "economics", "sj-p-pp-economics"),
]

# Maths: every series in storage, labelled by the numbering of its year. 9709 was renumbered in 2020
# (checked on 9709_w19 and 9709_s20 cover pages): up to 2019 Paper 4 M1, 5 M2, 6 S1, 7 S2; from 2020 Paper 4 M1, 5 S1, 6 S2.
MATHS = ("a-level-maths-past-papers-elementor-widget.html", "A Level/Mathematics", "9709", "Mathematics+%289709%29", "mathematics", "sj-p-pp-maths")
MATHS_OLD = {1: ("P1", "Pure Mathematics 1 (P1)"), 2: ("P2", "Pure Mathematics 2 (P2)"), 3: ("P3", "Pure Mathematics 3 (P3)"), 4: ("M1", "Mechanics 1 (M1)"),
             5: ("M2", "Mechanics 2 (M2)"), 6: ("S1", "Probability &amp; Statistics 1 (S1)"), 7: ("S2", "Probability &amp; Statistics 2 (S2)")}
MATHS_NEW = {1: ("P1", "Pure Mathematics 1 (P1)"), 2: ("P2", "Pure Mathematics 2 (P2)"), 3: ("P3", "Pure Mathematics 3 (P3)"), 4: ("M1", "Mechanics (M1)"),
             5: ("S1", "Probability &amp; Statistics 1 (S1)"), 6: ("S2", "Probability &amp; Statistics 2 (S2)")}
MATHS_FILTER = [("P1", "Pure 1 (P1)"), ("P2", "Pure 2 (P2)"), ("P3", "Pure 3 (P3)"), ("M1", "Mechanics (M1)"), ("M2", "Mechanics 2 (M2)"), ("S1", "Statistics 1 (S1)"), ("S2", "Statistics 2 (S2)")]


def files_by_series(key):
    F = json.loads(re.search(r"var FILES = (.*);\n", open(VIEWER, encoding="ascii").read()).group(1))[key]
    out = {}
    for ser, toks in F["s"].items():
        for tok in toks.split():
            t, c = tok.split("_")
            out.setdefault(ser, {}).setdefault(int(c[0]), {}).setdefault(c[1:], {})[t] = tok
    return out


def refresh(page, key, code, folder, vsub, wrapper):
    path = os.path.join(WEB, "Pages", page)
    w = open(path, encoding="utf-8").read()
    data = files_by_series(key)
    a, b = w.index("<!-- 2. PAPERS -->"), w.index("<!-- 3. HOW TO USE THEM -->")
    papers = w[a:b]
    count = 0

    def table(m):
        nonlocal count
        block = m.group(0)
        sers = set(re.findall(r"/%s_([sw]\d\d)_" % code, block))
        assert len(sers) == 1, sers
        ser = sers.pop()
        se, yy = ser[0], int(ser[1:])
        y = 2000 + yy
        have = data.get(ser, {})
        # the page's own rows: paper number and its label cell, kept exactly
        rows = re.findall(r'<tr data-paper="(\d)">\s*(<td data-label="Paper">.*?</td>)', block, re.S)
        variants = sorted({v for p, _ in rows for v in have.get(int(p), {})}, key=int)
        head = "".join('<th scope="col">Variant %s</th>' % v for v in variants)
        body = []
        for p, label in rows:
            tds = []
            for v in variants:
                cell = have.get(int(p), {}).get(v)
                if not cell or "qp" not in cell:
                    tds.append('<td data-label="Variant %s"><span><span class="sj-muted">Not set</span></span></td>' % v)
                    continue
                links = []
                for t in ("qp", "ms", "in", "ci"):
                    if t in cell:
                        count += 1
                        links.append('<a href="%s/%s/%s+%d/%s_%s_%s.pdf">%s %s%s</a>' % (STORE, folder, SESS[se][0], y, code, ser, cell[t], LBL[t], p, v))
                if "ms" in cell:
                    links.append('<a class="sjp-side" href="%s/past-paper-viewer/?level=a-level&amp;subject=%s&amp;series=%d-%s&amp;paper=%s%s" data-event="viewer_click" data-loc="papers">Side by side</a>' % (SITE, vsub, y, SESS[se][1], p, v))
                tds.append('<td data-label="Variant %s"><span>%s</span></td>' % (v, " ".join(links)))
            body.append('<tr data-paper="%s">%s%s</tr>' % (p, re.sub(r"\s*\n\s*", " ", label), "".join(tds)))
        return ('<div class="sj-table-wrap"><table class="sj-table sj-table-stack"><thead><tr><th scope="col">Paper</th>%s</tr></thead><tbody>\n%s\n</tbody></table></div>'
                % (head, "\n".join(body)))

    new_papers = re.sub(r'<div class="sj-table-wrap">\s*<table class="sj-table sj-table-stack">.*?</table>\s*</div>', table, papers, flags=re.S)
    note_old = re.search(r'(<p class="sjp-top">[^<]*?)(</p>)', new_papers)
    if 'Side by side' not in note_old.group(1):
        new_papers = new_papers.replace(note_old.group(0), note_old.group(1) + ' "Side by side" opens the paper next to its mark scheme.' + note_old.group(2), 1)
    w = w[:a] + new_papers + w[b:]
    # hero file count and variant wording
    w = re.sub(r"(all three variants|every variant), \d+ files", "every variant, %d files" % count, w, count=1)
    # page script must not turn Side by side links into downloads
    w = w.replace("querySelectorAll('.sjp-year td a')", "querySelectorAll('.sjp-year td a:not(.sjp-side)')")
    # style for the Side by side link, added once after the page's own link style
    side_css = "#sj.%s .sjp-year td a.sjp-side{border-style:dashed;font-weight:400}" % wrapper
    if side_css not in w:
        w = w.replace("</style>", side_css + "\n</style>", 1)
    w = w.replace("–", "-")
    w.encode("ascii")
    open(path, "w", encoding="ascii", newline="\n").write(w)
    print("%s: %d file links, %d side by side links" % (page, count, w.count('class="sjp-side"')))


def maths(page, key, code, folder, vsub, wrapper):
    path = os.path.join(WEB, "Pages", page)
    w = open(path, encoding="utf-8").read()
    data = files_by_series(key)
    years = sorted({2000 + int(k[1:]) for k in data}, reverse=True)
    count = 0
    used = set()

    def table(ser):
        nonlocal count
        se, y = ser[0], 2000 + int(ser[1:])
        names = MATHS_OLD if y < 2020 else MATHS_NEW
        have = data[ser]
        variants = sorted({v for p in have.values() for v in p}, key=int)
        rows = []
        for p in sorted(have):
            comp, label = names[p]
            used.add(comp)
            tds = []
            for v in variants:
                cell = have[p].get(v)
                if not cell or "qp" not in cell:
                    tds.append('<td data-label="Variant %s"><span><span class="sj-muted">Not set</span></span></td>' % v)
                    continue
                links = []
                for t in ("qp", "ms", "in", "ci"):
                    if t in cell:
                        count += 1
                        links.append('<a href="%s/%s/%s+%d/%s_%s_%s.pdf">%s %d%s</a>' % (STORE, folder, SESS[se][0], y, code, ser, cell[t], LBL[t], p, v))
                if "ms" in cell:
                    links.append('<a class="sjp-side" href="%s/past-paper-viewer/?level=a-level&amp;subject=%s&amp;series=%d-%s&amp;paper=%d%s" data-event="viewer_click" data-loc="papers">Side by side</a>' % (SITE, vsub, y, SESS[se][1], p, v))
                tds.append('<td data-label="Variant %s"><span>%s</span></td>' % (v, " ".join(links)))
            rows.append('<tr data-paper="%s"><td data-label="Paper"><span><b>Paper %d</b> <span class="sj-muted">%s</span></span></td>%s</tr>' % (comp, p, label, "".join(tds)))
        return ('<h3 class="sj-h3">%s %d</h3>\n<div class="sj-table-wrap"><table class="sj-table sj-table-stack"><thead><tr><th scope="col">Paper</th>%s</tr></thead><tbody>\n%s\n</tbody></table></div>'
                % ("May/June" if se == "s" else "Oct/Nov", y, "".join('<th scope="col">Variant %s</th>' % v for v in variants), "\n".join(rows)))

    panels = []
    for y in years:
        sers = [s_ for s_ in ("s%02d" % (y % 100), "w%02d" % (y % 100)) if s_ in data]
        note = '\n<p class="sj-small sj-muted">Old numbering before 2020: Paper 4 Mechanics 1, Paper 5 Mechanics 2, Paper 6 Statistics 1, Paper 7 Statistics 2.</p>' if y < 2020 else ""
        panels.append('<div class="sj-tabpanel sj-stack sjp-year" role="tabpanel" id="sjp-y%d" aria-labelledby="sjp-t%d">\n<h3 class="sj-h4 sjp-yh">A Level Maths past papers %d</h3>%s\n%s\n</div>' % (y, y, y, note, "\n".join(table(s_) for s_ in sers)))
    tabs = "\n".join('<button role="tab" id="sjp-t%d" aria-controls="sjp-y%d" aria-selected="%s"%s>%d</button>' % (y, y, "true" if i == 0 else "false", "" if i == 0 else ' tabindex="-1"', y) for i, y in enumerate(years))
    a, b = w.index("<!-- 2. PAPERS -->"), w.index("<!-- 3. HOW TO USE THEM -->")
    papers = w[a:b]
    t0 = papers.index('<div class="sj-tabs"')
    t1 = papers.index('<p class="sj-small sj-muted sj-measure">Past papers and mark schemes are the copyright')
    papers = papers[:t0] + '<div class="sj-tabs" role="tablist" aria-label="Year" id="sjp-tabs" hidden>\n' + tabs + '\n</div>\n' + "\n".join(panels) + "\n</div>\n" + papers[t1:]
    f0 = papers.index('<div class="sj-choices" role="group" aria-labelledby="sjp-fl">')
    f1 = papers.index("</div>", f0)
    radios = '<label class="sj-choice"><input type="radio" name="sjp-p" value="" checked><span>All papers</span></label> ' + " ".join(
        '<label class="sj-choice"><input type="radio" name="sjp-p" value="%s"><span>%s</span></label>' % (c, l) for c, l in MATHS_FILTER if c in used)
    papers = papers[:f0] + '<div class="sj-choices" role="group" aria-labelledby="sjp-fl"> ' + radios + " " + papers[f1:]
    note_old = re.search(r'(<p class="sjp-top">[^<]*?)(</p>)', papers)
    if "Side by side" not in note_old.group(1):
        papers = papers.replace(note_old.group(0), note_old.group(1) + ' "Side by side" opens the paper next to its mark scheme.' + note_old.group(2), 1)
    w = w[:a] + papers + w[b:]
    jump = "".join('<a class="sj-btn sj-btn-ghost" href="#sjp-y%d" data-sjp-year="%d" data-loc="hero">%d</a>' % (y, y, y) for y in years)
    w = re.sub(r'<div class="sjp-years">.*?</div>', '<div class="sjp-years">' + jump + "</div>", w, count=1, flags=re.S)
    w = re.sub(r"(all three variants|every variant), \d+ files", "every variant, %d files" % count, w, count=1)
    w = w.replace("querySelectorAll('.sjp-year td a')", "querySelectorAll('.sjp-year td a:not(.sjp-side)')")
    side_css = "#sj.%s .sjp-year td a.sjp-side{border-style:dashed;font-weight:400}" % wrapper
    if side_css not in w:
        w = w.replace("</style>", side_css + "\n</style>", 1)
    w.encode("ascii")
    open(path, "w", encoding="ascii", newline="\n").write(w)
    print("%s: %d years (%d to %d), %d file links, %d side by side links, filter %s" % (page, len(years), years[-1], years[0], count, w.count('class="sjp-side"'), sorted(used)))


if __name__ == "__main__":
    for args in PAGES:
        refresh(*args)
    maths(*MATHS)
