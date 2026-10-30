#!/usr/bin/env python3
"""Checks which past paper files are really in storage and writes that list into the viewer widget.

Run it on your own computer (the sandbox cannot reach sjacademy.pk):
    python3 check-files.py

It reads the subjects and folder names from past-paper-viewer-elementor-widget.html, asks the file host
for every likely file (HEAD requests, nothing is downloaded), then:
  - rewrites the FILES line in the widget, so the dropdowns only offer papers that exist
  - writes files-report.md next to this script: folder used, series found, missing mark schemes

Options:
    --base URL         storage base (default: the BASE in the widget)
    --years 2019-2026  years to look for (default: 2019 to this year)
    --workers 8        requests at the same time; lower it if the host starts refusing
    --only "O Level/Accounting"   check one subject (repeat for more); other subjects keep their FILES entry
    --dry-run          print and write the report, but leave the widget unchanged

Standard library only. Re-run it whenever new papers are uploaded (for example after each series).
"""
import argparse
import concurrent.futures
import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
WIDGET = os.path.join(HERE, "past-paper-viewer-elementor-widget.html")
REPORT = os.path.join(HERE, "files-report.md")
SESSIONS = [("s", "May+June", "May/June"), ("w", "October+November", "Oct/Nov")]
TYPES = ["ms", "in", "ci"]
UA = "SJAcademy-past-paper-check/1.0"


def read_subjects(html):
    """Returns [(level name, level folder, subject name, code, [folder names])] in widget order."""
    out, level = [], None
    for line in html.splitlines():
        m = re.search(r"\{ name: '([^']+)', folder: '([^']+)', variants:", line)
        if m:
            level = (m.group(1), m.group(2))
            continue
        m = re.search(r"\{ name: '([^']+)', code: '(\d+)', folders: \[([^\]]+)\]", line)
        if m and level:
            folders = re.findall(r"'([^']+)'", m.group(3))
            out.append((level[0], level[1], m.group(1), m.group(2), folders))
    return out


def read_files(html):
    m = re.search(r"/\* FILES-START[^\n]*\n\s*var FILES = (.*);\n", html)
    return json.loads(m.group(1)) if m else {}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def direct_base(base):
    """sjacademy.pk/file/... answers with a redirect to Backblaze. Ask Backblaze directly to halve the requests."""
    probe = base.rstrip("/") + "/redirect-probe.pdf"
    req = urllib.request.Request(probe, method="HEAD", headers={"User-Agent": UA})
    try:
        urllib.request.build_opener(NoRedirect).open(req, timeout=25)
    except urllib.error.HTTPError as e:
        loc = e.headers.get("Location", "")
        if e.code in (301, 302, 303, 307, 308) and loc.endswith("/redirect-probe.pdf"):
            return loc[: -len("/redirect-probe.pdf")]
    except Exception:
        pass
    return base


def enc(folder):
    return folder.replace(" ", "+").replace("(", "%28").replace(")", "%29")


class Host:
    def __init__(self, base, workers):
        self.base = base.rstrip("/")
        self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=workers)
        self.count = 0
        self.errors = []

    def exists(self, url):
        """True, False, or None when the host gave no clear answer."""
        for attempt in range(4):
            for method, headers in (("HEAD", {}), ("GET", {"Range": "bytes=0-0"})):
                req = urllib.request.Request(url, method=method, headers=dict(headers, **{"User-Agent": UA}))
                try:
                    with urllib.request.urlopen(req, timeout=25) as r:
                        self.count += 1
                        return 200 <= r.status < 300
                except urllib.error.HTTPError as e:
                    self.count += 1
                    if e.code in (404, 410):
                        return False
                    if e.code in (403, 405) and method == "HEAD":
                        continue
                    break
                except Exception:
                    break
            time.sleep(2 ** attempt)
        self.errors.append(url)
        return None

    def many(self, urls):
        return dict(zip(urls, self.pool.map(self.exists, urls)))


def series_url(host, lvl_folder, folder, code, se, y, token):
    return "%s/%s/%s/%s+%d/%s_%s%02d_%s.pdf" % (host.base, lvl_folder, enc(folder), se[1], y, code, se[0], y % 100, token)


def qp_candidates():
    comps = ["%d%d" % (p, v) for p in range(1, 7) for v in range(1, 7)]
    comps += ["0%d" % p for p in range(1, 7)] + ["%d" % p for p in range(1, 7)]
    return comps


def scan(host, lvl_folder, folder, code, years, series_filter=None):
    """Returns ({'s24': [tokens]}, error flag)."""
    found, bad = {}, False
    jobs = {}
    for y in years:
        for se in SESSIONS:
            key = "%s%02d" % (se[0], y % 100)
            if series_filter and key not in series_filter:
                continue
            for c in qp_candidates():
                jobs[series_url(host, lvl_folder, folder, code, se, y, "qp_" + c)] = (key, se, y, c)
    res = host.many(list(jobs))
    follow = {}
    for url, ok in res.items():
        key, se, y, c = jobs[url]
        if ok is None:
            bad = True
        if not ok:
            continue
        found.setdefault(key, ["qp_" + c])
        if ("qp_" + c) not in found[key]:
            found[key].append("qp_" + c)
        forms = [c] + ([c[1]] if c.startswith("0") else [])
        for t in TYPES:
            for f in forms:
                follow[series_url(host, lvl_folder, folder, code, se, y, "%s_%s" % (t, f))] = (key, "%s_%s" % (t, f), t, c)
    res2 = host.many(list(follow))
    taken = set()
    for url, ok in res2.items():
        key, token, t, c = follow[url]
        if ok is None:
            bad = True
        if ok and (key, t, c) not in taken:
            taken.add((key, t, c))
            found[key].append(token)
    for key in found:
        found[key].sort(key=lambda tok: (tok.split("_")[1].lstrip("0"), ["qp", "ms", "in", "ci"].index(tok.split("_")[0])))
    return found, bad


def label(key):
    return "%s 20%s" % ("May/June" if key[0] == "s" else "Oct/Nov", key[1:])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base")
    ap.add_argument("--years", default="2019-%d" % datetime.date.today().year)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--only", action="append")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    html = open(WIDGET, encoding="ascii").read()
    base = direct_base(a.base or re.search(r"var BASE = '([^']+)'", html).group(1))
    print("Checking files at %s" % base)
    y0, y1 = (int(x) for x in a.years.split("-"))
    years = list(range(y0, y1 + 1))
    recent = {"%s%02d" % (se[0], y % 100) for y in years[-2:] for se in SESSIONS}
    host = Host(base, a.workers)
    files = read_files(html)
    rows = []

    for lvl, lvl_folder, name, code, folders in read_subjects(html):
        key = lvl + "/" + name
        if a.only and key not in a.only:
            continue
        sys.stdout.write("%-40s" % key)
        sys.stdout.flush()
        chosen = None
        for folder in folders:
            probe, _ = scan(host, lvl_folder, folder, code, years, recent)
            if probe:
                chosen = folder
                break
        chosen = chosen or folders[0]
        found, bad = scan(host, lvl_folder, chosen, code, years)
        if bad:
            print(" incomplete (host errors), kept as before")
            rows.append((key, chosen, None, "Host errors: not updated. Run again."))
            continue
        if not found:
            files.pop(key, None)
            print(" nothing found in %s" % ", ".join(folders))
            rows.append((key, ", ".join(folders), {}, "No files found under any folder name. The viewer falls back to its rules."))
            continue
        files[key] = {"f": chosen, "s": {k: " ".join(v) for k, v in sorted(found.items())}}
        no_ms = ["%s %s" % (label(k), t.split("_")[1]) for k, v in found.items() for t in v
                 if t.startswith("qp_") and not any(x.startswith("ms_") and x.split("_")[1].lstrip("0") == t.split("_")[1].lstrip("0") for x in v)]
        print(" %s: %d series" % (chosen, len(found)))
        rows.append((key, chosen, found, ("No mark scheme: " + ", ".join(no_ms)) if no_ms else ""))

    print("\n%d requests, %d without a clear answer." % (host.count, len(host.errors)))
    write_report(rows, years, base)
    if a.dry_run:
        print("Dry run: widget not changed. Report: %s" % REPORT)
        return
    line = "  var FILES = %s;" % json.dumps(files, separators=(",", ":"), sort_keys=True)
    new = re.sub(r"(/\* FILES-START[^\n]*\n)\s*var FILES = .*;\n", lambda m: m.group(1) + line + "\n", html, count=1)
    new.encode("ascii")
    with open(WIDGET, "w", encoding="ascii", newline="\n") as f:
        f.write(new)
    print("Widget updated: %s\nReport: %s" % (WIDGET, REPORT))


def write_report(rows, years, base):
    all_keys = ["%s%02d" % (se[0], y % 100) for y in years for se in SESSIONS]
    out = ["# Past paper storage check", "",
           "Checked %s against `%s`, years %d to %d. Written by `check-files.py`." % (datetime.date.today().isoformat(), base, years[0], years[-1]), "",
           "| Subject | Folder in storage | Series found | Series missing | Notes |", "|---|---|---|---|---|"]
    for key, folder, found, note in rows:
        if found is None:
            out.append("| %s | %s | ? | ? | %s |" % (key, folder, note))
            continue
        missing = [label(k) for k in all_keys if k not in found]
        out.append("| %s | %s | %d | %s | %s |" % (key, folder, len(found), ", ".join(missing) or "none", note))
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
