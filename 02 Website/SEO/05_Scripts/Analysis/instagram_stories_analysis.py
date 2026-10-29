"""Analyse the Instagram stories export (lifetime metrics per story).

Run from the workspace root:
  python3 05_Scripts/Analysis/instagram_stories_analysis.py [path/to/stories.csv]
"""
import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from statistics import median

PATH = sys.argv[1] if len(sys.argv) > 1 else "04_Data/Instagram/Instagram_Stories_Export_2026-09-30.csv"
NUM = ["Views", "Reach", "Likes", "Shares", "Replies", "Navigation", "Profile visits", "Link clicks", "Follows", "Sticker taps"]


def main():
    rows = list(csv.DictReader(open(PATH, encoding="utf-8-sig")))
    for r in rows:
        r["has_link"] = r["Link clicks"] != ""
        for k in NUM:
            r[k] = float(r[k] or 0)
        r["dt"] = datetime.strptime(r["Publish time"], "%m/%d/%Y %H:%M")
        r["d"] = re.sub(r"\s+", " ", r["Description"] or "")
    rows.sort(key=lambda r: r["dt"])
    days = (rows[-1]["dt"] - rows[0]["dt"]).days + 1
    print(f"Stories: {len(rows)} ({len(rows)/days:.1f}/day), {rows[0]['dt']:%d %b %Y} to {rows[-1]['dt']:%d %b %Y}")
    for k in ("Reach", "Profile visits", "Link clicks", "Follows", "Replies", "Sticker taps"):
        print(f"  total {k}: {sum(r[k] for r in rows):,.0f}")
    print(f"  median reach per story: {median(r['Reach'] for r in rows):.0f}")

    print("\nBy month")
    months = defaultdict(list)
    for r in rows:
        months[r["dt"].strftime("%Y-%m")].append(r)
    for m in sorted(months):
        g = months[m]
        lk = [r for r in g if r["has_link"]]
        print(f"  {m} stories={len(g):>4} med reach={median(r['Reach'] for r in g):>5.0f} "
              f"profile visits={sum(r['Profile visits'] for r in g):>5.0f} link stories={len(lk):>3} "
              f"link clicks={sum(r['Link clicks'] for r in lk):>5.0f}")

    lk = [r for r in rows if r["has_link"]]
    print(f"\nLink-sticker stories: {len(lk)}, clicks {sum(r['Link clicks'] for r in lk):.0f}, "
          f"click rate {sum(r['Link clicks'] for r in lk)/sum(r['Reach'] for r in lk)*100:.2f}%")
    for r in sorted(lk, key=lambda r: -r["Link clicks"])[:10]:
        print(f"  {r['dt']:%Y-%m-%d} reach={r['Reach']:>6.0f} clicks={r['Link clicks']:>4.0f} {r['d'][:70]}")

    print("\nReach by position in the day's sequence")
    byday = defaultdict(list)
    for r in rows:
        byday[r["dt"].date()].append(r)
    pos = defaultdict(list)
    for g in byday.values():
        for i, r in enumerate(sorted(g, key=lambda r: r["dt"])):
            pos[min(i + 1, 10)].append(r["Reach"])
    for i in sorted(pos):
        print(f"  #{i if i < 10 else '10+'}: n={len(pos[i]):>4} median reach={median(pos[i]):>5.0f}")
    print("Interactive keywords in captions:",
          Counter(k for r in rows for k in ("poll", "quiz", "question", "comment", "link", "whatsapp", "demo") if k in r["d"].lower()))


if __name__ == "__main__":
    main()
