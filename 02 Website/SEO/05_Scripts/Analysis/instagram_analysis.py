"""Analyse the Instagram post export (Meta Business Suite, lifetime metrics per post).

Run from the workspace root:
  python3 05_Scripts/Analysis/instagram_analysis.py [path/to/export.csv]
"""
import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from statistics import median

PATH = sys.argv[1] if len(sys.argv) > 1 else "04_Data/Instagram/Instagram_Posts_Export_2026-09-30.csv"
NUM = ["Views", "Reach", "Likes", "Shares", "Follows", "Comments", "Saves", "Duration (sec)"]

THEMES = [  # first match wins, order matters
    ("Meme / relatable", r"caiememes|meme|💀|😭|pov|relatable|be like|when you|when the"),
    ("Giveaway / comment-to-get", r"comment\s*[\"“']?\w+[\"”']?\s*(to|and|for)|giveaway|free ebook|get your ebook"),
    ("Promo / enrolment", r"enrol|enroll|admission|register|registration|demo|batch|seats|fee|discount|offer|join us|classes (start|begin)|book (a|your)"),
    ("Results / celebration", r"result|congrat|a\*s?\b.*(student|scored|achiev)|topper|straight a|proud"),
    ("Teacher advice / exam tips", r"advice|tips?|guide|mistake|how to|examiner|paper \d|revision|revise|mark scheme|command word|sir |miss |ma'am"),
    ("Event / campus life", r"event|workshop|seminar|trip|celebrat|campus|practical|lab|orientation|farewell"),
]


def theme(desc: str) -> str:
    d = desc.lower()
    for name, pat in THEMES:
        if re.search(pat, d):
            return name
    return "Other"


def load():
    rows = list(csv.DictReader(open(PATH, encoding="utf-8-sig")))
    for r in rows:
        for k in NUM:
            try:
                r[k] = float(r[k] or 0)
            except ValueError:
                r[k] = 0.0
        r["dt"] = datetime.strptime(r["Publish time"], "%m/%d/%Y %H:%M")
        r["eng"] = r["Likes"] + r["Comments"] + r["Shares"] + r["Saves"]
        r["theme"] = theme(r["Description"] or "")
    return rows


def rate(num, den):
    return (num / den * 100) if den else 0.0


def summarise(group, label):
    reach = sum(r["Reach"] for r in group)
    print(f"{label:<28} n={len(group):>3}  med views={median([r['Views'] for r in group]):>8.0f}  "
          f"med reach={median([r['Reach'] for r in group]):>7.0f}  eng/reach={rate(sum(r['eng'] for r in group), reach):>5.1f}%  "
          f"shares/1k reach={sum(r['Shares'] for r in group)/reach*1000 if reach else 0:>5.1f}  "
          f"saves/1k={sum(r['Saves'] for r in group)/reach*1000 if reach else 0:>5.1f}  "
          f"follows/1k={sum(r['Follows'] for r in group)/reach*1000 if reach else 0:>4.2f}  total follows={sum(r['Follows'] for r in group):.0f}")


def main():
    rows = load()
    rows.sort(key=lambda r: r["dt"])
    print(f"Posts: {len(rows)}  from {rows[0]['dt']:%d %b %Y} to {rows[-1]['dt']:%d %b %Y}")
    print(f"Totals: views {sum(r['Views'] for r in rows):,.0f}, reach {sum(r['Reach'] for r in rows):,.0f}, "
          f"follows {sum(r['Follows'] for r in rows):,.0f}, shares {sum(r['Shares'] for r in rows):,.0f}, saves {sum(r['Saves'] for r in rows):,.0f}")
    print("Date column values:", Counter(r["Date"] for r in rows))

    print("\n== By post type")
    for t, g in sorted(group_by(rows, "Post type").items(), key=lambda x: -len(x[1])):
        summarise(g, t)

    print("\n== By theme (caption-based classification)")
    for t, g in sorted(group_by(rows, "theme").items(), key=lambda x: -len(x[1])):
        summarise(g, t)

    print("\n== By month")
    months = defaultdict(list)
    for r in rows:
        months[r["dt"].strftime("%Y-%m")].append(r)
    for m in sorted(months):
        g = months[m]
        types = Counter(r["Post type"].replace("IG ", "") for r in g)
        print(f"{m}  posts={len(g):>3}  med reach={median([r['Reach'] for r in g]):>7.0f}  max views={max(r['Views'] for r in g):>8.0f}  "
              f"follows={sum(r['Follows'] for r in g):>4.0f}  {dict(types)}")

    print("\n== Reel length buckets")
    reels = [r for r in rows if r["Post type"] == "IG reel"]
    for lo, hi in [(0, 8), (8, 15), (15, 30), (30, 60), (60, 120), (120, 10**6)]:
        g = [r for r in reels if lo <= r["Duration (sec)"] < hi]
        if g:
            summarise(g, f"{lo}-{hi if hi < 10**6 else '+'}s")

    print("\n== Day of week (publish time as exported)")
    for d in range(7):
        g = [r for r in rows if r["dt"].weekday() == d]
        if g:
            summarise(g, datetime(2026, 1, 5 + d).strftime("%a"))
    print("\n== Hour of day (as exported)")
    for h, g in sorted(group_by(rows, None, key=lambda r: r["dt"].hour).items()):
        summarise(g, f"{h:02d}:00")

    def show(title, key, n=12):
        print(f"\n== {title}")
        for r in sorted(rows, key=key, reverse=True)[:n]:
            desc = re.sub(r"\s+", " ", r["Description"] or "")[:70]
            print(f"{r['dt']:%Y-%m-%d} {r['Post type'].replace('IG ',''):<8} views={r['Views']:>8.0f} reach={r['Reach']:>7.0f} "
                  f"sh={r['Shares']:>5.0f} sv={r['Saves']:>4.0f} fol={r['Follows']:>3.0f} cm={r['Comments']:>4.0f} [{r['theme'][:12]}] {desc}")

    show("Top by views", lambda r: r["Views"])
    show("Top by follows", lambda r: r["Follows"])
    show("Top by saves", lambda r: r["Saves"])
    show("Top by comments", lambda r: r["Comments"])

    print("\n== Captions")
    has_link = sum(1 for r in rows if re.search(r"sjacademy\.pk|link in bio|website", (r["Description"] or "").lower()))
    has_cta_wa = sum(1 for r in rows if re.search(r"whatsapp|dm us|message us|call", (r["Description"] or "").lower()))
    print(f"Mention website/link in bio: {has_link}/{len(rows)}; WhatsApp/DM CTA: {has_cta_wa}/{len(rows)}")
    tags = Counter(t.lower() for r in rows for t in re.findall(r"#\w+", r["Description"] or ""))
    print("Top hashtags:", tags.most_common(15))
    print("Empty captions:", sum(1 for r in rows if not (r["Description"] or "").strip()))
    teachers = Counter(m.lower() for r in rows for m in re.findall(r"\b(?:sir|miss|ma'am|mam)\s+[A-Z][a-z]+", r["Description"] or ""))
    print("Teachers named:", teachers.most_common(12))


def group_by(rows, field, key=None):
    out = defaultdict(list)
    for r in rows:
        out[key(r) if key else r[field]].append(r)
    return out


if __name__ == "__main__":
    main()
