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
    ("a-level-maths-past-papers-elementor-widget.html", "A Level/Mathematics", "9709", "Mathematics+%289709%29", "mathematics", "sj-p-pp-maths"),
]


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


if __name__ == "__main__":
    for args in PAGES:
        refresh(*args)
