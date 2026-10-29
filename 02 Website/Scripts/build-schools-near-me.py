#!/usr/bin/env python3
"""
Builds the SJ Academy "Schools near me" Elementor HTML widget (schools-near-me-elementor-widget.html).

Why a script: Google and AI crawlers need the school list inside the page HTML. The old page loaded the
list with JavaScript, so a crawler saw "0 schools found". This script bakes every school into the HTML.
Run it again whenever the Google Sheet changes, then paste the new file into the Elementor HTML widget.

Usage:
  python3 build-schools-near-me.py                      # downloads the published Google Sheet CSV
  python3 build-schools-near-me.py schools.csv          # uses a CSV file you exported from the sheet
  python3 build-schools-near-me.py schools.csv out.html # custom output path

Expected CSV columns: Area, School, Board(s), Sector, Address, Phone, SJ Review
Needs only the Python 3 standard library.
"""
import csv
import datetime
import html
import io
import json
import os
import re
import sys
import urllib.parse
import urllib.request

SHEET_CSV = "https://docs.google.com/spreadsheets/d/1JeL1ixggGTh60pFQAk8KgnKNTDLh1DZxBi66Tl_D2L8/export?format=csv&gid=0"
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT_JS = os.path.join(HERE, "sj-page-script.js")
DEFAULT_OUT = os.path.join(HERE, "..", "Pages", "schools-near-me-elementor-widget.html")

SITE = "https://www.sjacademy.pk"
PAGE_URL = SITE + "/schools-near-me-karachi/"
WA_NUMBER = "923362144454"
POPUP = "#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D"
VERSION = "2.0"

# Areas written two ways in the sheet are merged under one name.
AREA_FIX = {"gulshan": "Gulshan-e-Iqbal", "fb area": "Federal B Area"}
AREA_FIRST = ["DHA", "Clifton"]  # shown first in chips and in the list; everything else by school count

BOARD_LABELS = [
    ("cambridge", "Cambridge"),
    ("matric", "Matric"),
    ("intermediate", "Intermediate"),
    ("ib", "IB"),
    ("agakhan", "Aga Khan Board"),
    ("early", "Early years and primary"),
    ("technical", "Technical"),
    ("other", "Other"),
]


def esc(s):
    """HTML-escape and keep the file plain ASCII (non-ASCII becomes numeric entities)."""
    return html.escape(str(s), quote=True).encode("ascii", "xmlcharrefreplace").decode("ascii")


def clean(s):
    s = (s or "").strip()
    if s.lower() in ("information missing", "n/a", "na", "-"):
        return ""
    return s


def board_tags(b):
    low = b.lower()
    tags = []
    if "cambridge" in low or "igcse" in low:
        tags.append("cambridge")
    if "matric" in low:
        tags.append("matric")
    if "inter" in low:
        tags.append("intermediate")
    if re.search(r"\bib\b", low):
        tags.append("ib")
    if "khan" in low:
        tags.append("agakhan")
    if any(w in low for w in ("early years", "primary", "montessori", "prep", "pg to")):
        tags.append("early")
    if "technical" in low:
        tags.append("technical")
    return tags or ["other"]


def sector_key(s):
    return "government" if s.lower().startswith("gov") else "private"


def phone_parts(raw):
    """Returns a list of (display, tel_digits_or_None)."""
    raw = clean(raw)
    if not raw:
        return []
    out = []
    for seg in re.split(r"\s*[/|]\s*", raw):
        seg = seg.strip()
        if not seg:
            continue
        digits = re.sub(r"\D", "", seg)
        nat = digits
        if nat.startswith("0092"):
            nat = nat[4:]
        elif nat.startswith("92") and len(nat) >= 11:
            nat = nat[2:]
        if nat.startswith("0"):
            nat = nat[1:]
        disp, tel = seg, None
        if len(nat) == 10 and nat.startswith("21"):
            disp, tel = "021-" + nat[2:], "92" + nat
        elif len(nat) == 10 and nat.startswith("3"):
            disp, tel = "0" + nat[:3] + "-" + nat[3:], "92" + nat
        elif len(nat) == 9 and nat.startswith("111"):
            disp, tel = "111-" + nat[3:6] + "-" + nat[6:], "92" + nat
        elif len(nat) == 11 and nat.startswith("21111"):
            disp, tel = "021-111-" + nat[5:8] + "-" + nat[8:], None
        elif len(nat) == 8:
            disp, tel = "021-" + nat, "9221" + nat
        elif len(nat) > 10 and nat.startswith("21"):
            disp, tel = seg.strip(), "92" + nat[:10]  # extension range such as 35251414-44
        out.append((disp, tel))
    return out[:3]


def load_rows(path):
    if path:
        with open(path, newline="", encoding="utf-8-sig") as f:
            text = f.read()
    else:
        with urllib.request.urlopen(SHEET_CSV, timeout=60) as r:
            text = r.read().decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    rows = []
    for r in reader:
        name = clean(r.get("School"))
        if not name:
            continue
        area = clean(r.get("Area")) or "Karachi"
        area = AREA_FIX.get(area.lower(), area)
        board = clean(r.get("Board(s)")).replace("Agha Khan", "Aga Khan")
        sector = clean(r.get("Sector")) or "Private"
        rows.append({
            "area": area,
            "name": name,
            "board": board,
            "sector": sector,
            "address": clean(r.get("Address")),
            "phone": r.get("Phone"),
            "review": clean(r.get("SJ Review")),
        })
    return rows


def wa_link(lines):
    return "https://wa.me/%s?text=%s" % (WA_NUMBER, urllib.parse.quote("\n".join(lines), safe=""))


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else None
    out_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUT
    rows = load_rows(csv_path)
    # Drop rows that repeat the same school, address and area exactly. They look like copy-paste errors in the sheet.
    seen, unique, dropped = set(), [], []
    for r in rows:
        key = (r["name"].lower(), r["address"].lower(), r["area"].lower())
        if key in seen:
            dropped.append("%s (%s)" % (r["name"], r["area"]))
            continue
        seen.add(key)
        unique.append(r)
    rows = unique
    if dropped:
        print("Skipped %d exact duplicate rows: %s" % (len(dropped), "; ".join(dropped)))
    today = datetime.date.today()
    refreshed = "%d %s %d" % (today.day, today.strftime("%B"), today.year)

    counts = {}
    for r in rows:
        counts[r["area"]] = counts.get(r["area"], 0) + 1
    order = sorted(counts, key=lambda a: (AREA_FIRST.index(a) if a in AREA_FIRST else 99, -counts[a], a))
    rank = {a: i for i, a in enumerate(order)}
    rows.sort(key=lambda r: (rank[r["area"]], r["name"].lower()))

    n_total = len(rows)
    n_areas = len(counts)
    n_gov = sum(1 for r in rows if sector_key(r["sector"]) == "government")
    n_priv = n_total - n_gov
    tag_counts = {}
    for r in rows:
        for t in board_tags(r["board"]):
            tag_counts[t] = tag_counts.get(t, 0) + 1

    # ---------- cards ----------
    cards = []
    for r in rows:
        tags = board_tags(r["board"])
        maps = "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote_plus(
            re.sub(r"\s+", " ", ("%s %s" % (r["name"], r["address"] or "Karachi")).replace("\u2013", " ")), safe="")
        phones = phone_parts(r["phone"])
        ph = []
        for disp, tel in phones:
            if tel:
                ph.append('<a class="sj-link" href="tel:+%s">%s</a>' % (tel, esc(disp)))
            else:
                ph.append(esc(disp))
        review = ""
        if r["review"].startswith("http"):
            review = '<a class="sj-link" href="%s">Read our review</a>' % esc(r["review"])
        cards.append(
            '<li class="sj-card sjs-card" data-area="%s" data-boards="%s" data-sector="%s">'
            '<h3 class="sj-h3">%s</h3>'
            '<p class="sj-caption">%s &middot; %s</p>'
            '<p class="sj-row"><span class="sj-chip">%s</span></p>'
            '<p class="sj-small">%s</p>'
            '%s'
            '<div class="sjs-act"><a class="sj-btn sj-btn-ghost sj-btn-sm" href="%s" target="_blank" rel="noopener">View on map</a>%s</div>'
            '</li>' % (
                esc(r["area"]), " ".join(tags), sector_key(r["sector"]),
                esc(r["name"]),
                esc(r["area"]), esc(r["sector"]),
                esc(r["board"] or "Board not listed"),
                esc(r["address"] or "Address not listed"),
                ('<p class="sj-small">Phone: %s</p>' % " / ".join(ph)) if ph else "",
                esc(maps), review))

    area_opts = "".join('<option value="%s">%s (%d)</option>' % (esc(a), esc(a), counts[a]) for a in sorted(counts))
    board_opts = "".join('<option value="%s">%s (%d)</option>' % (k, esc(l), tag_counts[k])
                         for k, l in BOARD_LABELS if k in tag_counts)
    chips = "".join('<a class="sj-chip" href="?area=%s#sjs-results" data-area="%s">%s <span class="sj-num sj-muted">%d</span></a>'
                    % (urllib.parse.quote(a), esc(a), esc(a), counts[a]) for a in order[:8])
    label_js = json.dumps({k: l for k, l in BOARD_LABELS})

    wa_demo = wa_link(["Hi SJ Academy, I'd like to book a free demo class.", "Level: ", "Subject: ",
                       "Session: May/June 2027", "Mode (in class or online): ", "(Ref: SNM-DEMO)", "My name is "])
    wa_fix = wa_link(["Hi SJ Academy, I'd like to correct or add a school on your Schools near me list.",
                      "School name: ", "What is wrong or missing: ", "(Ref: SNM-FIX)", "My name is "])

    top_areas = [a for a in order if a in ("DHA", "Clifton", "PECHS", "Gulshan-e-Iqbal", "North Nazimabad",
                                           "Gulistan-e-Jauhar", "Korangi", "Malir", "Bahria Town") and a in counts]

    # ---------- FAQ (one source for the page and the FAQPage data) ----------
    def L(url, text):
        return "{link:%s|%s}" % (url, text)

    faqs = [
        ("How do I find schools near me in Karachi?",
         "Pick your area in the finder at the top of this page, then narrow it by board (Cambridge, Matric, Intermediate or IB) and sector (private or government). Every school shows its address, a phone number and a Google Maps link. If you already know the name, type it into the search box."),
        ("How many schools are on the list, and which areas does it cover?",
         "The list has %d schools across %d Karachi areas, including %s. %d are private schools and %d are government schools." % (
             n_total, n_areas, ", ".join(top_areas[:-1]) + " and " + top_areas[-1], n_priv, n_gov)),
        ("What is the difference between Cambridge, Matric and IB schools?",
         "Cambridge schools prepare students for IGCSE, O Level and A Level exams. Matric schools follow the Sindh board syllabus and lead to the SSC exam. IB schools teach the International Baccalaureate (PYP, MYP and the Diploma Programme). Some schools offer more than one, and the Board line on each card shows what is listed for that school."),
        ("Is the information up to date?",
         "The list was last refreshed on %s. Phone numbers, addresses and programmes change, so confirm admissions, fees and the board with the school before you visit." % refreshed),
        ("How do I report a mistake or add a school?",
         "Send us the school name and what is wrong or missing on %s." % L(wa_fix, "WhatsApp")),
        ("Do you rank or recommend these schools?",
         "No. This is a directory, not a ranking. We do not score schools here. A few schools have a written review on our blog, and the card links to it."),
        ("Is SJ Academy a school?",
         "No. SJ Academy is a tuition academy for Cambridge O Level and A Level students. Students stay at their own school and join our classes in person at DHA Phase 7 or live online. See our %s and %s pages for details." % (
             L(SITE + "/o-level-tuition-center-karachi/", "O Level tuition"), L(SITE + "/a-level-tuition-center-karachi/", "A Level tuition"))),
        ("Can I try a class before I register?",
         "Yes. Every class has a free demo class, except lab practicals, where students join directly. Send us your level and subject on %s and we will book you in. Fees are on the %s." % (
             L(wa_demo, "WhatsApp"), L(SITE + "/fee-structure/", "fee structure page"))),
    ]

    def _faq_html(t):
        out, pos = [], 0
        for m in re.finditer(r"\{link:([^|]+)\|([^}]+)\}", t):
            out.append(esc(t[pos:m.start()]))
            extra = ' target="_blank" rel="noopener"' if "wa.me" in m.group(1) else ""
            out.append('<a class="sj-link" href="%s"%s>%s</a>' % (esc(m.group(1)), extra, esc(m.group(2))))
            pos = m.end()
        out.append(esc(t[pos:]))
        return "".join(out)

    def faq_text(t):
        return re.sub(r"\{link:([^|]+)\|([^}]+)\}",
                      lambda m: m.group(2) + (" at " + m.group(1) if not m.group(1).startswith("https://wa.me") else ""), t)

    faq_items = []
    for i, (q, a) in enumerate(faqs):
        faq_items.append('<details%s><summary>%s</summary><div class="sj-faq-a"><p>%s</p></div></details>' % (
            " open" if i == 0 else "", esc(q), _faq_html(a)))

    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": faq_text(a)}} for q, a in faqs]}
    ld_crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Schools near me in Karachi", "item": PAGE_URL}]}
    ld_page = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Schools near me in Karachi",
               "description": "A directory of %d Karachi schools by area, board and sector, with address, phone number and map link." % n_total,
               "url": PAGE_URL, "inLanguage": "en", "dateModified": today.isoformat(),
               "publisher": {"@type": "EducationalOrganization", "name": "SJ Academy", "url": SITE + "/"}}

    with open(SCRIPT_JS, encoding="utf-8") as f:
        std_script = f.read().strip()

    page = TEMPLATE
    repl = {
        "__VERSION__": VERSION,
        "__REFRESHED__": refreshed,
        "__N__": str(n_total),
        "__A__": str(n_areas),
        "__AREA_OPTS__": area_opts,
        "__BOARD_OPTS__": board_opts,
        "__CHIPS__": chips,
        "__CARDS__": "\n".join(cards),
        "__FAQ__": "\n        ".join(faq_items),
        "__WA_DEMO__": esc(wa_demo),
        "__POPUP__": POPUP,
        "__STD_SCRIPT__": std_script,
        "__LABELS__": label_js,
        "__LD_FAQ__": json.dumps(ld_faq, ensure_ascii=True),
        "__LD_CRUMB__": json.dumps(ld_crumb, ensure_ascii=True),
        "__LD_PAGE__": json.dumps(ld_page, ensure_ascii=True),
        "__SITE__": SITE,
    }
    for k, v in repl.items():
        page = page.replace(k, v)

    left = re.findall(r"__[A-Z_]+__", page)
    if left:
        sys.exit("Unfilled placeholders: %s" % sorted(set(left)))
    bad = [c for c in page if ord(c) > 127]
    if bad:
        sys.exit("Non-ASCII characters in output: %r" % sorted(set(bad))[:10])
    if "gtag" in page:
        sys.exit("Literal 'gtag' found; Flying Scripts would delay the page.")

    with open(out_path, "w", encoding="ascii", newline="\n") as f:
        f.write(page)
    print("Wrote %s (%d bytes): %d schools, %d areas, %d private, %d government" % (
        os.path.abspath(out_path), len(page.encode("ascii")), n_total, n_areas, n_priv, n_gov))


TEMPLATE = r'''<!-- SJ Academy "Schools near me in Karachi" page, Elementor HTML widget. Version __VERSION__, generated __REFRESHED__.
     Family: Tool. Uses the shared stylesheet sj-brand.css 3.1.1 (already in Additional CSS).
     Paste this whole file into one HTML widget, replacing the old finder. Section: full width, zero padding, no entrance animation.
     Page layout: Elementor Full Width. Hide Title: Yes. Address stays /schools-near-me-karachi/ (no redirect needed).
     Take a Cloudways backup first. After pasting, purge WP-Optimize, Cloudways and Cloudflare.
     Every school is written into this HTML (no data fetch), so Google and AI crawlers can read the list. To refresh the list,
     run Scripts/build-schools-near-me.py and paste the new file. This file is plain ASCII on purpose.
     Yoast title: Schools near me in Karachi: by area and board | SJ Academy
     Yoast description: Search __N__ Karachi schools by area, board and sector. See the address, phone number and map link for each, from DHA to North Nazimabad.
     Yoast canonical: https://www.sjacademy.pk/schools-near-me-karachi/ (so ?area= and ?board= links do not become duplicate pages). -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>

<style>
#sj.sj-p-schools-near-me .sjs-card{display:flex;flex-direction:column;gap:8px;padding:18px 16px}
#sj.sj-p-schools-near-me .sjs-card .sj-h3{font-size:17px}
#sj.sj-p-schools-near-me .sjs-card p{margin:0}
#sj.sj-p-schools-near-me .sjs-card .sj-row{gap:6px}
#sj.sj-p-schools-near-me .sjs-card .sj-chip{min-height:28px;padding:2px 10px;font-size:13px}
#sj.sj-p-schools-near-me .sjs-act{display:flex;flex-wrap:wrap;align-items:center;gap:8px 16px;margin-top:auto;padding-top:6px}
#sj.sj-p-schools-near-me .sjs-chips{gap:8px}
#sj.sj-p-schools-near-me .sjs-chips .sj-chip{min-height:44px;padding:6px 14px;cursor:pointer}
#sj.sj-p-schools-near-me .sjs-chips .sj-chip[aria-current="true"]{background:var(--sj-yellow);box-shadow:inset 0 -3px 0 var(--sj-ink)}
#sj.sj-p-schools-near-me #sjs-list:not(.is-live) .sjs-card:nth-child(n+13){display:none}
#sj.sj-p-schools-near-me .sjs-more{display:flex;justify-content:center;margin-top:var(--sj-s5)}
#sj.sj-p-schools-near-me .sjs-offer .sj-btn{width:100%}
@media (min-width:600px){#sj.sj-p-schools-near-me .sjs-offer .sj-btn{width:auto}}
</style>
<noscript><style>#sj.sj-p-schools-near-me #sjs-list .sjs-card{display:flex!important}</style></noscript>

<div id="sj" class="sj-p-schools-near-me" data-family="tool">

  <!-- 1. HERO WITH THE FINDER -->
  <section class="sj-section sj-bg-grid" data-sj-hero>
    <div class="sj-wrap sj-stack-lg">
      <nav class="sj-crumbs" aria-label="Breadcrumb"><ol><li><a href="__SITE__/">Home</a></li><li aria-current="page">Schools near me in Karachi</li></ol></nav>
      <div class="sj-stack">
        <h1 class="sj-h1"><span class="sj-pill"><span>Schools near me in Karachi</span></span>Find a Karachi school by <span class="sj-hl">area and board</span></h1>
        <p class="sj-lead sj-measure">__N__ schools across __A__ Karachi areas. Pick an area, a board or a sector, then get the address, the phone number and a map link.</p>
        <span class="sj-hand sj-tilt-l">start with your area</span>
      </div>

      <div class="sj-offset" id="sjs-finder">
        <form class="sj-stack" id="sjs-form" role="search" aria-label="Find a school in Karachi" action="#sjs-results">
          <div class="sj-filterbar">
            <div class="sj-field"><label class="sj-label" for="sjs-q">School name</label><input class="sj-input" id="sjs-q" name="q" type="search" placeholder="Type a school name" autocomplete="off"></div>
            <div class="sj-field"><label class="sj-label" for="sjs-area">Area</label><select class="sj-select" id="sjs-area" name="area"><option value="">All areas</option>__AREA_OPTS__</select></div>
            <div class="sj-field"><label class="sj-label" for="sjs-board">Board</label><select class="sj-select" id="sjs-board" name="board"><option value="">All boards</option>__BOARD_OPTS__</select></div>
            <div class="sj-field"><label class="sj-label" for="sjs-sector">Sector</label><select class="sj-select" id="sjs-sector" name="sector"><option value="">Private and government</option><option value="private">Private</option><option value="government">Government</option></select></div>
          </div>
          <div class="sj-row">
            <p class="sj-small" aria-live="polite"><b class="sj-num" id="sjs-count">__N__</b> <span id="sjs-count-l">schools found</span></p>
            <button type="button" class="sj-btn sj-btn-ghost sj-btn-sm" id="sjs-reset" hidden>Clear filters</button>
          </div>
          <div>
            <p class="sj-caption">Popular areas</p>
            <div class="sj-row sjs-chips" id="sjs-chips">__CHIPS__</div>
          </div>
        </form>
      </div>
      <p class="sj-small sj-muted">Looking for O Level or A Level tuition for your child? <a class="sj-link" href="#sjs-offer">See how our classes work</a></p>
    </div>
  </section>

  <!-- 2. RESULTS -->
  <section class="sj-section sj-bg-white" id="sjs-results">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure sj-stack">
        <h2 class="sj-h2" id="sjs-h">All Karachi schools</h2>
        <p class="sj-small sj-muted"><span id="sjs-sub">Showing 12 of __N__.</span> List refreshed __REFRESHED__. This is a directory, not a ranking.</p>
      </div>
      <ul class="sj-grid sj-grid-3" id="sjs-list">
__CARDS__
      </ul>
      <div class="sj-empty" id="sjs-empty" hidden>
        <h3 class="sj-h3">No schools match that</h3>
        <p>Try another area or board, or clear the filters. If a school is missing, tell us on WhatsApp and we will look at it.</p>
        <button type="button" class="sj-btn sj-btn-ghost sj-btn-sm" id="sjs-empty-reset">Clear filters</button>
      </div>
      <div class="sjs-more" id="sjs-more-wrap"><button type="button" class="sj-btn sj-btn-ghost" id="sjs-more">Show more schools</button></div>
    </div>
  </section>

  <!-- 3. HOW TO READ THE LIST -->
  <section class="sj-section sj-bg-dots">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure sj-stack">
        <div class="sj-eyebrow">Reading the list</div>
        <h2 class="sj-h2">Which board does the school <span class="sj-hl">follow?</span></h2>
        <p>The Board line on each card is the quickest way to narrow the list. Here is what the common ones mean.</p>
      </div>
      <div class="sj-grid sj-grid-4">
        <div class="sj-card sj-stack"><h3 class="sj-h3">Cambridge</h3><p class="sj-small">Prepares students for IGCSE, O Level and A Level exams. Some Cambridge schools also teach Matric.</p></div>
        <div class="sj-card sj-stack"><h3 class="sj-h3">Matric</h3><p class="sj-small">Follows the Sindh board syllabus and leads to the Secondary School Certificate (SSC) exam.</p></div>
        <div class="sj-card sj-stack"><h3 class="sj-h3">Intermediate</h3><p class="sj-small">The two-year college stage after Matric, under the Sindh board.</p></div>
        <div class="sj-card sj-stack"><h3 class="sj-h3">IB</h3><p class="sj-small">The International Baccalaureate: the PYP, the MYP and the Diploma Programme.</p></div>
      </div>
      <div class="sj-sticky"><span class="sj-hand">check before you go</span><p>Phone numbers, addresses and programmes change. Call the school and confirm admissions and fees first.</p></div>
    </div>
  </section>

  <!-- 4. CLASS OFFER (follows the result) -->
  <section class="sj-section sj-bg-brown sjs-offer" id="sjs-offer">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure sj-stack">
        <div class="sj-eyebrow">For parents</div>
        <h2 class="sj-h2">Your child&rsquo;s O or A Levels? <span class="sj-hl">Try a class first.</span></h2>
        <p>SJ Academy is a tuition academy, not a school. We teach Cambridge O Level and A Level students next to their school, in person at DHA Phase 7 or live online, so your school does not need to be near ours. 4,500+ students taught so far.</p>
      </div>
      <ul class="sj-ticks sj-measure">
        <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg><span>Past-paper practice marked to the mark scheme</span></li>
        <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg><span>Feedback on the marks your child lost</span></li>
        <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg><span>The teacher tells you if your child falls behind. Ask us any time.</span></li>
        <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg><span>Teachers from LUMS, IBA and ex-KGS</span></li>
        <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg><span>226+ five-star Google reviews</span></li>
        <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg><span>A free demo class (lab practicals join directly)</span></li>
      </ul>
      <div class="sj-stack">
        <div class="sj-row"><a class="sj-btn sj-btn-primary" href="__WA_DEMO__" target="_blank" rel="noopener" data-loc="offer">Book a free demo on WhatsApp</a></div>
        <p>or <a class="sj-link" href="__POPUP__" data-loc="offer">register for a class</a></p>
        <p class="sj-small"><a class="sj-link" href="__SITE__/o-level-tuition-center-karachi/">O Level tuition</a> &middot; <a class="sj-link" href="__SITE__/a-level-tuition-center-karachi/">A Level tuition</a> &middot; <a class="sj-link" href="__SITE__/fee-structure/">Fees</a> &middot; <a class="sj-link" href="__SITE__/classes-schedule/">Class timetable</a> &middot; <a class="sj-link" href="__SITE__/a-level-past-papers/business-9609/">Free past papers</a></p>
        <p class="sj-caption">SJ Academy is not affiliated with Cambridge or with the schools listed on this page.</p>
      </div>
    </div>
  </section>

  <!-- 5. FAQ -->
  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">FAQ</div>
        <h2 class="sj-h2">Questions about <span class="sj-hl">Karachi schools</span></h2>
      </div>
      <div class="sj-faq">
        __FAQ__
      </div>
    </div>
  </section>
</div>

<script>
__STD_SCRIPT__
</script>

<script>
(function(){
  var root=document.getElementById('sj');
  var list=document.getElementById('sjs-list');
  if(!root||!list){return;}
  var $=function(id){return document.getElementById(id);};
  var cards=Array.prototype.slice.call(list.children);
  cards.forEach(function(c){var h=c.querySelector('h3');c._n=(h?h.textContent:'').toLowerCase();});
  var q=$('sjs-q'),area=$('sjs-area'),board=$('sjs-board'),sector=$('sjs-sector');
  var count=$('sjs-count'),countL=$('sjs-count-l'),head=$('sjs-h'),sub=$('sjs-sub');
  var more=$('sjs-more'),moreWrap=$('sjs-more-wrap'),empty=$('sjs-empty'),reset=$('sjs-reset');
  var chips=Array.prototype.slice.call(root.querySelectorAll('#sjs-chips [data-area]'));
  var LABELS=__LABELS__;
  var START=12,STEP=24,limit=START,used=false,total=cards.length;
  var AREA_FIX={'gulshan':'Gulshan-e-Iqbal','fb area':'Federal B Area'};

  var send=function(name,loc){
    var g=window['gt'+'ag'];
    if(typeof g==='function'){g('event',name,{link_location:loc||'finder',page_family:'tool'});}
  };
  list.addEventListener('click',function(e){
    var a=e.target&&e.target.closest?e.target.closest('a'):null;
    if(!a){return;}
    var h=a.getAttribute('href')||'';
    if(h.indexOf('tel:')===0){send('school_call_click','card');}
    else if(h.indexOf('google.com/maps')>-1){send('school_map_click','card');}
  });
  var hasOption=function(sel,val){
    for(var i=0;i<sel.options.length;i++){if(sel.options[i].value===val){return true;}}
    return false;
  };
  var matchArea=function(val){
    if(!val){return '';}
    var v=AREA_FIX[val.toLowerCase()]||val;
    for(var i=0;i<area.options.length;i++){
      if(area.options[i].value.toLowerCase()===v.toLowerCase()){return area.options[i].value;}
    }
    return '';
  };
  var boardKey=function(val){
    var v=(val||'').toLowerCase();
    if(!v){return '';}
    if(hasOption(board,v)){return v;}
    if(v.indexOf('cambridge')>-1){return 'cambridge';}
    if(v.indexOf('matric')>-1){return 'matric';}
    if(v.indexOf('inter')>-1){return 'intermediate';}
    if(v.indexOf('khan')>-1){return 'agakhan';}
    if(/\bib\b/.test(v)){return 'ib';}
    return '';
  };

  /* Read old-style links such as ?area=DHA&board=Cambridge */
  try{
    var p=new URLSearchParams(window.location.search);
    area.value=matchArea(p.get('area'));
    board.value=boardKey(p.get('board'));
    var s=(p.get('sector')||'').toLowerCase();
    sector.value=(s==='private'||s==='government')?s:'';
    q.value=(p.get('q')||'').slice(0,60);
  }catch(e){}

  var headingText=function(){
    var lead=[],t;
    if(sector.value){lead.push(sector.value==='private'?'Private':'Government');}
    if(board.value){lead.push(LABELS[board.value]);}
    if(lead.length){t=lead.join(' ')+' schools in '+(area.value||'Karachi');}
    else{t=area.value?'Schools in '+area.value:'All Karachi schools';}
    if(q.value.trim()){t+=' matching "'+q.value.trim()+'"';}
    return t;
  };

  var render=function(){
    var needle=q.value.trim().toLowerCase();
    var shown=0,matched=0;
    cards.forEach(function(c){
      var ok=true;
      if(needle&&c._n.indexOf(needle)===-1){ok=false;}
      if(ok&&area.value&&c.getAttribute('data-area')!==area.value){ok=false;}
      if(ok&&board.value&&(' '+c.getAttribute('data-boards')+' ').indexOf(' '+board.value+' ')===-1){ok=false;}
      if(ok&&sector.value&&c.getAttribute('data-sector')!==sector.value){ok=false;}
      if(ok){matched++;}
      var show=ok&&matched<=limit;
      c.hidden=!show;
      if(show){shown++;}
    });
    list.classList.add('is-live');
    count.textContent=String(matched);
    countL.textContent=matched===1?'school found':'schools found';
    head.textContent=headingText();
    sub.textContent=matched===0?'Nothing to show.':(shown>=matched?'Showing all '+matched+'.':'Showing '+shown+' of '+matched+'.');
    empty.hidden=matched!==0;
    moreWrap.hidden=shown>=matched;
    if(!moreWrap.hidden){more.textContent='Show more schools ('+(matched-shown)+' left)';}
    var filtered=!!(needle||area.value||board.value||sector.value);
    reset.hidden=!filtered;
    chips.forEach(function(ch){
      if(ch.getAttribute('data-area')===area.value&&area.value){ch.setAttribute('aria-current','true');}
      else{ch.removeAttribute('aria-current');}
    });
    try{
      var u=new URLSearchParams();
      if(area.value){u.set('area',area.value);}
      if(board.value){u.set('board',board.value);}
      if(sector.value){u.set('sector',sector.value);}
      if(q.value.trim()){u.set('q',q.value.trim());}
      var qs=u.toString();
      window.history.replaceState(null,'',window.location.pathname+(qs?'?'+qs:''));
    }catch(e){}
  };

  var changed=function(){
    limit=START;
    if(!used){used=true;send('tool_complete','finder');}
    render();
  };
  var clear=function(){
    q.value='';area.value='';board.value='';sector.value='';
    limit=START;render();
  };

  q.addEventListener('input',changed);
  [area,board,sector].forEach(function(sel){sel.addEventListener('change',changed);});
  $('sjs-form').addEventListener('submit',function(e){e.preventDefault();});
  reset.addEventListener('click',clear);
  $('sjs-empty-reset').addEventListener('click',clear);
  more.addEventListener('click',function(){limit+=STEP;render();});
  chips.forEach(function(ch){
    ch.addEventListener('click',function(e){
      e.preventDefault();
      var v=ch.getAttribute('data-area');
      area.value=(area.value===v)?'':v;
      changed();
      var target=$('sjs-results');
      if(target&&target.scrollIntoView){
        var calm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        target.scrollIntoView({behavior:calm?'auto':'smooth',block:'start'});
      }
    });
  });
  render();
})();
</script>

<script type="application/ld+json">__LD_PAGE__</script>
<script type="application/ld+json">__LD_CRUMB__</script>
<script type="application/ld+json">__LD_FAQ__</script>
'''

if __name__ == "__main__":
    main()
