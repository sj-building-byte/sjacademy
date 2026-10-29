from playwright.sync_api import sync_playwright
from PIL import Image
B="/tmp/claude-0/-home-claude/523af959-4481-50fc-96e3-c19fcaa09243/scratchpad/ibcc/"
P=[]
def audit(pg,tag):
    r=pg.evaluate("""()=>{const out=[];const app=document.querySelector('[data-sji]');
    app.querySelectorAll('select,input').forEach(e=>{ if(e.offsetParent===null&&e.type!=='radio'&&e.type!=='checkbox')return;
      const lab=(e.labels&&e.labels.length)||e.getAttribute('aria-label')||e.closest('label');
      if(!lab) out.push('no label: '+(e.id||e.name));
      if(e.tagName==='SELECT'){const fs=parseFloat(getComputedStyle(e).fontSize); if(fs<16) out.push('font<16 '+e.id+' '+fs); const h=e.getBoundingClientRect().height; if(h&&h<44) out.push('short '+e.id+' '+h);}});
    app.querySelectorAll('.sji-seg span,.sj-check,.sji-more summary,button,a.sj-btn').forEach(e=>{if(e.offsetParent===null)return;const h=e.getBoundingClientRect().height; if(h<44) out.push('target<44 '+e.className+' '+Math.round(h))});
    return out;}""")
    if r: P.append((tag,r))
with sync_playwright() as p:
    br=p.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox"])
    ctx=br.new_context(viewport={"width":390,"height":700},device_scale_factor=2,has_touch=True,is_mobile=True); pg=ctx.new_page()
    pg.route("**/*",lambda r:r.abort() if r.request.url.startswith("http") else r.continue_())
    pg.goto("file://"+B+"test-page.html"); pg.evaluate("localStorage.clear()"); pg.reload()
    pg.screenshot(path=B+"u1.png")
    audit(pg,'empty')
    pg.tap('label:has(input[name="sji-target"][value="hssc"])'); pg.wait_for_timeout(700)
    print('scrollY after target:',pg.evaluate("window.scrollY"))
    pg.screenshot(path=B+"u2.png")
    pg.tap('label:has(input[name="sji-route"][value="pk"])'); pg.wait_for_timeout(700)
    print('scrollY after route:',pg.evaluate("window.scrollY"))
    pg.screenshot(path=B+"u3.png")
    pg.tap('label:has(input[name="sji-group"][value="pm"])'); pg.wait_for_timeout(700)
    print('scrollY after group:',pg.evaluate("window.scrollY"))
    pg.screenshot(path=B+"u4.png")
    audit(pg,'hssc-pm')
    print('numbering:',pg.eval_on_selector_all('.sji-qt',"els=>els.filter(e=>e.offsetParent).map(e=>e.textContent.trim().slice(0,30))"))
    print('overflow:',pg.evaluate("document.documentElement.scrollWidth"))
    # keyboard: radios reachable
    pg.evaluate("window.scrollTo(0,0)"); pg.focus('input[name="sji-target"]'); pg.keyboard.press('ArrowRight')
    print('kb target:',pg.evaluate("document.querySelector('input[name=sji-target]:checked').value"))
    br.close()
print('A11Y/UX PROBLEMS:',P)
