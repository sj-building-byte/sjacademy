import re, sys, json
from playwright.sync_api import sync_playwright

B = "/tmp/claude-0/-home-claude/523af959-4481-50fc-96e3-c19fcaa09243/scratchpad/ibcc/"
widget = open(B + "ibcc-calculator-elementor-widget.html").read()
css = open(B + "sj-brand.min.css").read()
page = ("<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<title>t</title><style>body{margin:0;background:#F7F5EF}" + css + "</style></head><body>" + widget + "</body></html>")
open(B + "test-page.html", "w").write(page)
problems = []


def block(r):
    return r.abort() if r.request.url.startswith("http") else r.continue_()


def grade(pg, row, g):
    pg.select_option("#g-" + row, g)


def result(pg):
    return pg.inner_text("[data-result]")


with sync_playwright() as p:
    br = p.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])

    def new(w, h=900):
        ctx = br.new_context(viewport={"width": w, "height": h}, device_scale_factor=2 if w < 500 else 1)
        pg = ctx.new_page()
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" and "net::" not in m.text and "Failed to load" not in m.text else None)
        pg.route("**/*", block)
        pg.goto("file://" + B + "test-page.html")
        pg.evaluate("localStorage.clear()")
        pg.reload()
        return ctx, pg, errs

    # ---- Flow 1: HSSC Pakistan Pre-Engineering, O 2025, A 2026 (legacy rule) at 375
    ctx, pg, errs = new(375)
    pg.click('label:has(input[name="sji-target"][value="hssc"])')
    pg.click('label:has(input[name="sji-group"][value="pe"])')
    print("rows:", pg.eval_on_selector_all(".sji-r", "els=>els.map(e=>e.dataset.row)"))
    print("o year default:", pg.input_value("#sji-oy"))
    for r, g in [("o-eng", "A"), ("o-math", "A*"), ("o-urdu", "B"), ("o-isl", "A"), ("o-pst", "B"), ("o-e1", "A*"), ("o-e2", "A")]:
        grade(pg, r, g)
    print("partial:", result(pg).replace("\n", " | "))
    pg.select_option('select[data-subj="o-e3"]', "cs")
    grade(pg, "o-e3", "A")
    for r, g in [("a-1", "B"), ("a-2", "A"), ("a-3", "A*")]:
        grade(pg, r, g)
    txt = result(pg)
    print("FLOW1:", txt.replace("\n", " | "))
    # expected: O 2025: eng 85, math A* 94, urdu 75, isl 85, pst 75, phy A* 94, chem 85, cs 85 = 678 ; A 2026: phy B 75, chem A 85, math A* 94 = 254 ; 932
    if "932" not in txt or "/ 1100" not in txt:
        problems.append("flow1 total")
    if "678" not in pg.inner_html("[data-result]") and "753" not in txt:
        pass
    pg.screenshot(path=B + "m-flow1.png", full_page=False)
    pg.locator("[data-result]").screenshot(path=B + "m-result1.png")
    sw = pg.evaluate("document.documentElement.scrollWidth")
    if sw > 375:
        problems.append("overflow 375: %d" % sw)
    tip = pg.inner_text(".sji-tip")
    print("tip:", tip.replace("\n", " | "))
    href = pg.get_attribute(".sji-tip a", "href")
    print("wa:", href[:160])
    # persist across reload
    pg.reload()
    if "932" not in result(pg):
        problems.append("state not restored")
    # switch to new rule: O Levels 2026
    pg.select_option("#sji-oy", "2026")
    txt2 = result(pg)
    print("FLOW1 new rule:", txt2.replace("\n", " | ")[:400])
    # 2026 O: eng 85, math 94, urdu 75, isl 85, pst 75 = 414 ; + 254 = 668 / 800 * 1100 = 918.5 -> 919
    if "919" not in txt2:
        problems.append("new rule total")
    pg.screenshot(path=B + "m-flow1-new.png", full_page=True)
    if errs:
        problems.append("errors flow1 %s" % errs)
    ctx.close()

    # ---- Flow 2: SSC abroad, numeric grades at 320
    ctx, pg, errs = new(320)
    pg.click('label:has(input[name="sji-target"][value="ssc"])')
    pg.click('label:has(input[name="sji-route"][value="abroad"])')
    pg.click(".sji-more summary")
    pg.check("#sji-nums")
    for i, s in enumerate(["phy", "chem", "bio"]):
        pg.select_option('select[data-subj="o-e%d"]' % (i + 1), s)
    # duplicate check: options disabled
    dis = pg.eval_on_selector('select[data-subj="o-e3"] option[value="phy"]', "o=>o.disabled")
    print("dup disabled:", dis)
    if not dis:
        problems.append("duplicate not disabled")
    for r, g in [("o-eng", "9"), ("o-math", "8"), ("o-e1", "7"), ("o-e2", "6"), ("o-e3", "5")]:
        grade(pg, r, g)
    txt = result(pg)
    print("FLOW2:", txt.replace("\n", " | ")[:300])
    # 2026: eng 9 -> 93, 87, 82, 77, 70 = 409 /500*900 = 736.2 -> 736
    if "736" not in txt:
        problems.append("flow2 total")
    sw = pg.evaluate("document.documentElement.scrollWidth")
    if sw > 320:
        problems.append("overflow 320: %d" % sw)
    pg.screenshot(path=B + "s-flow2.png", full_page=True)
    if errs:
        problems.append("errors flow2 %s" % errs)
    ctx.close()

    # ---- Flow 3: desktop 1280, mixed years, Humanities, 2027 forecast
    ctx, pg, errs = new(1280, 1000)
    pg.click('label:has(input[name="sji-target"][value="hssc"])')
    pg.click('label:has(input[name="sji-group"][value="hum"])')
    pg.select_option("#sji-ay", "2027")
    pg.click(".sji-more summary")
    pg.check("#sji-multi")
    pg.select_option("#y-o-math", "2024")
    for i, s in enumerate(["bus", "econ", "acc"]):
        pg.select_option('select[data-subj="o-e%d"]' % (i + 1), s)
    for i, s in enumerate(["bus", "econ", "math"]):
        pg.select_option('select[data-subj="a-%d"]' % (i + 1), s)
    for r in ["o-eng", "o-math", "o-urdu", "o-isl", "o-pst", "o-e1", "o-e2", "o-e3", "a-1", "a-2", "a-3"]:
        grade(pg, r, "A*")
    txt = result(pg)
    print("FLOW3:", txt.replace("\n", " | ")[:600])
    # O 2025 (math 2024): eng 93, math(2024) 94, urdu 93, isl 94, pst 93, bus 94, econ 94, acc 94 = 749 ; A 2027->2026: 94,94,94 = 282 ; 1031
    if "1031" not in txt or "forecast" not in txt:
        problems.append("flow3")
    pg.screenshot(path=B + "d-flow3.png", full_page=False)
    pg.screenshot(path=B + "d-full.png", full_page=True)
    bar = pg.is_visible("[data-bar]")
    print("bar visible on desktop:", bar)
    if bar:
        problems.append("bar on desktop")
    # tabs
    pg.click("#sji-t2023")
    print("2023 tab panel visible:", pg.is_visible("#sji-p2023"), pg.is_visible("#sji-p2026"))
    # reset
    pg.click('[data-act="reset"]')
    print("after reset:", result(pg).replace("\n", " | "))
    if errs:
        problems.append("errors flow3 %s" % errs)
    ctx.close()

    # ---- Empty state screenshot at 390
    ctx, pg, errs = new(390, 844)
    pg.screenshot(path=B + "m-empty.png")
    pg.click('label:has(input[name="sji-target"][value="hssc"])')
    pg.click('label:has(input[name="sji-group"][value="pm"])')
    pg.screenshot(path=B + "m-step2.png", full_page=True)
    ctx.close()
    br.close()

print("PROBLEMS:", problems)
