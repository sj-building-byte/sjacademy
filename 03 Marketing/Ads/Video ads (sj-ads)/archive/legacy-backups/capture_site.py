# Captures real frames of sjacademy.pk at a phone viewport (390x844 @3x) for the launch film.
import asyncio, json
from playwright.async_api import async_playwright

OUT = "assets/site"
HIDE_JS = """() => {
  const kill = (el) => el.style.setProperty('display','none','important');
  document.querySelectorAll('header, [data-elementor-type="header"], .joinchat, #back-to-top, .elementor-popup-modal, [class*="cookie"], [id*="cookie"]').forEach(kill);
  for (const el of document.querySelectorAll('body *')) {
    const p = getComputedStyle(el).position;
    if (p === 'fixed' || p === 'sticky') kill(el);
  }
  window.scrollTo(window.scrollX, window.scrollY);
}"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=3, is_mobile=True, has_touch=True,
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")
        pg = await ctx.new_page()
        await pg.goto("https://www.sjacademy.pk", wait_until="networkidle", timeout=90000)
        h = await pg.evaluate("document.body.scrollHeight")
        for y in range(0, h, 600):
            await pg.evaluate(f"window.scrollTo(0,{y})"); await pg.wait_for_timeout(100)
        await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(1000)
        await pg.evaluate(HIDE_JS); await pg.wait_for_timeout(400)
        info = {}
        async def ytop(sel_text):
            return await pg.evaluate("""(t) => { const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
                while (w.nextNode()) { if (w.currentNode.textContent.trim().startsWith(t)) { const r = w.currentNode.parentElement.getBoundingClientRect(); return r.top + window.scrollY; } } return null; }""", sel_text)
        info["find_title"] = await ytop("Find your class")
        info["tools_eyebrow"] = await ytop("Free tools") or await ytop("FREE TOOLS")
        info["tools_last"] = await ytop("CAIE date sheet")
        info["doc"] = await pg.evaluate("document.documentElement.scrollHeight")
        await pg.screenshot(path=f"{OUT}/full.png", full_page=True)
        # O Level tab, then tap a subject
        fy = info["find_title"]
        await pg.evaluate(f"window.scrollTo(0,{fy - 60})"); await pg.wait_for_timeout(500)
        await pg.get_by_role("button", name="O Level", exact=True).first.click(); await pg.wait_for_timeout(600)
        await pg.evaluate(HIDE_JS)
        info["find_scroll"] = await pg.evaluate("window.scrollY")
        await pg.screenshot(path=f"{OUT}/find-olevel.png")
        btns = await pg.evaluate("""() => [...document.querySelectorAll('button')].filter(b=>b.offsetParent).map(b=>{const r=b.getBoundingClientRect();return {t:b.innerText.trim().replace(/\\s+/g,' '),x:r.x,y:r.y,w:r.width,h:r.height}})""")
        info["buttons_olevel"] = [x for x in btns if 0 < x["y"] < 844]
        target = next(x for x in info["buttons_olevel"] if x["t"].startswith("Physics"))
        info["tap"] = target
        await pg.mouse.click(target["x"] + target["w"] / 2, target["y"] + target["h"] / 2); await pg.wait_for_timeout(4000)
        await pg.evaluate(HIDE_JS)
        await pg.screenshot(path=f"{OUT}/find-tapped.png")
        info["after_text"] = await pg.evaluate("""() => { const r=[]; const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
            while(w.nextNode()){const e=w.currentNode.parentElement; const b=e.getBoundingClientRect(); const t=w.currentNode.textContent.trim(); if(t && b.top>0 && b.top<844) r.push([Math.round(b.top), t.slice(0,60)]);} return r; }""")
        await b.close()
    json.dump(info, open(f"{OUT}/info.json", "w"), indent=1)
    print(json.dumps({k: v for k, v in info.items() if k not in ("buttons_olevel", "after_text")}))
    for t in info["after_text"]: print(t)

asyncio.run(main())
