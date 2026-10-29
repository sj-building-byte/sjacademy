"""HISTORICAL: already run on 2026-09-30 against the pre-reorganisation layout. Do not re-run."""
"""Stage SEO fixes for the O/A Level past-paper hub widgets.

Reads originals from A_Level_Hubs/ and O_Level_Hubs/, writes fixed copies to
SEO_Fixes_2026_09_30/staged/<same path>. Originals are never modified.

Fixes applied:
1. Strip document wrappers (doctype, html, head, meta, title, body) so the file
   is a valid Elementor HTML-widget fragment. This removes the nested <head> and
   duplicate <title> Google sees on the live hub pages.
2. H1 gains the qualification and "Mark Schemes" ("A Level Business (9609)
   Past Papers & Mark Schemes").
3. The one-line FAQ becomes an H2 section with study guidance and internal links
   (mark-scheme guide, grade thresholds, subject tuition page).
4. Non-www internal links are switched to https://www. to skip a redirect.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "SEO_Fixes_2026_09_30" / "staged"

A_TUITION = {
    "9700": "/a-level-biology-tuition/",
    "9609": "/a-level-business-tuition/",
    "9701": "/a-level-chemistry/",
    "9618": "/a-level-computer-science-tuition/",
    "9708": "/a-level-economics-tuition/",
    "9709": "/a-level-maths/",
    "9702": "/a-level-physics-tuition/",
}
O_TUITION = {
    "7707": "/o-level-accounting-tuition/",
    "5090": "/o-level-biology-sj-academy/",
    "7115": "/business7081/",
    "5070": "/o-level-chemistry-tuitions/",
    "2281": "/economics/",
    "2058": "/o-level-islamiat-tuition/",
    "4024": "/o-level-math-tuition/",
    "2059": "/o-level-pakistan-studies-tuition/",
    "5054": "/o-level-physics-tuition/",
}

FAQ_TEMPLATE = """    <div class="seo-faq">
        <h2>About {level} {subject} ({code}) Past Papers</h2>
{syllabus_block}
        <h3>How do I read a {code} past paper file name?</h3>
        <p>Every file follows the Cambridge pattern <strong>{code}_s25_qp_12</strong>. The letter is the session (s = May/June, w = Oct/Nov), the two digits are the year, qp is the question paper and ms is the mark scheme. The last two digits are the paper number followed by the variant, so 12 means Paper 1, Variant 2.</p>

        <h3>Which variant should I practise?</h3>
        <p>Cambridge sets different variants of the same paper for different time zones. They test the same syllabus to the same standard, so practise every variant from a session. It doubles your question bank for each topic.</p>

        <h3>How should I use the mark schemes?</h3>
        <p>Attempt the paper under timed conditions first, then mark it yourself against the mark scheme. Note where you lost marks for missing keywords or structure, not only for wrong answers. Our guide on <a href="https://www.sjacademy.pk/blog/how-to-use-mark-scheme/">how to use a Cambridge mark scheme</a> walks through the method, and our <a href="https://www.sjacademy.pk{threshold_url}">{threshold_label}</a> explains how raw marks convert to grades.</p>

{help_block}    </div>"""

HELP_TAUGHT = """        <h3>Want help with {level} {subject}?</h3>
        <p>SJ Academy teaches {level} {subject} in DHA Phase 7, Karachi, and live online across Pakistan. <a href="https://www.sjacademy.pk{tuition_url}">See our {level} {subject} classes</a> or book a free demo class.</p>
"""
HELP_GENERIC = """        <h3>Want structured help for your {level}s?</h3>
        <p>SJ Academy runs {level} classes in DHA Phase 7, Karachi, and live online across Pakistan. <a href="https://www.sjacademy.pk{tuition_url}">See which {level} subjects we currently teach</a> or book a free demo class.</p>
"""


def strip_wrappers(html: str) -> str:
    html = re.sub(r"<!DOCTYPE[^>]*>\s*", "", html, flags=re.I)
    html = re.sub(r"</?html[^>]*>\s*", "", html, flags=re.I)
    html = re.sub(r"</?head>\s*", "", html, flags=re.I)
    html = re.sub(r"</?body[^>]*>\s*", "", html, flags=re.I)
    html = re.sub(r"[ \t]*<meta [^>]*>\s*", "", html, flags=re.I)
    html = re.sub(r"[ \t]*<title>.*?</title>\s*", "", html, flags=re.I | re.S)
    return html.strip() + "\n"


def fix_hub(src: Path, level: str) -> list[str]:
    html = src.read_text(encoding="utf-8")
    notes = []

    m = re.search(r'<h1 class="hub-title"><span class="highlight">(.+?) \((\w+)\)</span> Past Papers</h1>', html)
    if not m:
        return [f"SKIPPED {src.name}: H1 pattern not found"]
    subject, code = m.group(1), m.group(2)
    html = html.replace(
        m.group(0),
        f'<h1 class="hub-title">{level} <span class="highlight">{subject} ({code})</span> Past Papers &amp; Mark Schemes</h1>',
    )
    notes.append(f'H1 -> "{level} {subject} ({code}) Past Papers & Mark Schemes"')

    faq = re.search(r'    <div class="seo-faq">\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>\s*</div>', html, flags=re.S)
    if not faq:
        return [f"SKIPPED {src.name}: FAQ block not found"]
    syllabus_block = f"        <h3>{faq.group(1)}</h3>\n        <p>{faq.group(2)}</p>\n"
    mapped = (A_TUITION if level == "A Level" else O_TUITION).get(code)
    tuition = mapped or ("/a-level-tuition-center-karachi/" if level == "A Level" else "/o-level-tuition-center-karachi/")
    help_block = (HELP_TAUGHT if mapped else HELP_GENERIC).format(level=level, subject=subject, tuition_url=tuition)
    threshold_url, threshold_label = (
        ("/blog/a-level-thresholds-guide/", "A Level grade thresholds guide")
        if level == "A Level"
        else ("/o-level-grade-thresholds/", "O Level grade thresholds page")
    )
    html = html.replace(
        faq.group(0),
        FAQ_TEMPLATE.format(
            level=level, subject=subject, code=code, syllabus_block=syllabus_block,
            threshold_url=threshold_url, threshold_label=threshold_label, help_block=help_block,
        ),
    )
    html = html.replace("#sj-pastpaper-hub .seo-faq h3 {", "#sj-pastpaper-hub .seo-faq h2 { font-size: 1.6rem; font-weight: 800; margin-bottom: 20px; }\n        #sj-pastpaper-hub .seo-faq h3 {")
    notes.append(f"FAQ -> H2 section, 4 new H3 Q&As, links: mark-scheme guide, thresholds, {tuition}")

    n = html.count('href="https://sjacademy.pk/')
    html = html.replace('href="https://sjacademy.pk/', 'href="https://www.sjacademy.pk/')
    if n:
        notes.append(f"{n} internal link(s) -> www")

    html = strip_wrappers(html)
    notes.append("removed doctype/html/head/meta/title/body wrappers")

    dst = OUT / src.relative_to(ROOT)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(html, encoding="utf-8")
    return notes


def fix_directory(src: Path) -> list[str]:
    html = src.read_text(encoding="utf-8")
    notes = []
    n = html.count('href="https://sjacademy.pk/')
    html = html.replace('href="https://sjacademy.pk/', 'href="https://www.sjacademy.pk/')
    if n:
        notes.append(f"{n} internal link(s) -> www")
    if 'class="directory-title"><span class="highlight">A Level</span> Past Papers</h1>' in html:
        html = html.replace(
            'class="directory-title"><span class="highlight">A Level</span> Past Papers</h1>',
            'class="directory-title"><span class="highlight">A Level</span> Past Papers &amp; Mark Schemes</h1>',
        )
        notes.append('H1 -> "A Level Past Papers & Mark Schemes"')
    html = strip_wrappers(html)
    notes.append("removed doctype/html/head/meta/title/body wrappers")
    dst = OUT / src.relative_to(ROOT)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(html, encoding="utf-8")
    return notes


if __name__ == "__main__":
    for folder, level in (("A_Level_Hubs", "A Level"), ("O_Level_Hubs", "O Level")):
        for f in sorted((ROOT / folder).glob("*.html")):
            notes = fix_directory(f) if f.name.startswith("main_") else fix_hub(f, level)
            print(f"{folder}/{f.name}: " + "; ".join(notes))
    sys.exit(0)
