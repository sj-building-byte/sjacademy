import asyncio, json
from playwright.async_api import async_playwright
css=open(''+__import__('os').environ.get('SJ_CSS','/mnt/user-data/uploads/01 Brand/sj-brand.css')+'',encoding='utf-8').read()
w=open('a-level-subject-combinations-tool-elementor-widget.html',encoding='utf-8').read()
html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+css+'</style></head><body style="margin:0">'+w+'</body></html>'
open('test.html','w',encoding='utf-8').write(html)
SC=[
 ("Medicine PCB",['biology','chemistry','physics','math'],'science',['medicine'],[]),
 ("Medicine no physics",['biology','chemistry'],'science',['medicine'],['physics']),
 ("Business",['econ','business','accounting'],'systems',['business'],[]),
 ("Business no math",['econ','business','accounting'],'systems',['business'],['math']),
 ("CS",['math','physics','cs'],'logic',['cs'],[]),
 ("Law",['english','history'],'essays',['law'],[]),
 ("Law no essay",['english'],'essays',['law'],['essay']),
 ("Creative",['art','math'],'projects',['creative'],[]),
 ("Undecided",['math','econ'],'logic',['undecided'],[]),
 ("Eng+Med",['math','physics','chemistry','biology'],'logic',['engineering','medicine'],[]),
 ("Eng no math",['physics'],'logic',['engineering'],['math']),
 ("Ban everything",['math'],'logic',['engineering'],['math','physics','biology','chemistry','cs','econ','accounting','essay']),
]
async def run(page,sc):
    name,strong,style,dirs,bans=sc
    await page.evaluate("document.getElementById('sjc-reset')&&!document.getElementById('sjc-done').hidden&&document.getElementById('sjc-reset').click()")
    for s in strong: await page.check(f'input[data-g=strong][value={s}]',force=True)
    await page.click('#sjc-next')
    await page.check(f'input[value={style}]',force=True)
    await page.click('#sjc-next')
    for d in dirs: await page.check(f'input[data-g=dirs][value={d}]',force=True)
    await page.click('#sjc-next')
    for b in bans: await page.check(f'input[data-g=bans][value={b}]',force=True)
    await page.click('#sjc-next')
    titles=await page.eval_on_selector_all('#sjc-routes article h3','els=>els.map(e=>e.textContent)')
    note=await page.evaluate("document.getElementById('sjc-note').innerText")
    empty=await page.evaluate("!!document.querySelector('#sjc-routes .sj-empty')")
    print(f"{name:22} -> {titles}{' EMPTY' if empty else ''} | note: {note.replace(chr(10),' / ')}")
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1280,'height':900})
        errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
        await pg.goto('file://'+__import__('os').path.abspath('test.html'))
        for sc in SC: await run(pg,sc)
        print('JS errors:',errs)
        # screenshots: quiz step1, results (eng+med) desktop; mobile
        await pg.evaluate("document.getElementById('sjc-reset').click()")
        await pg.screenshot(path='s_quiz_desktop.png',full_page=False)
        await run(pg,SC[9])
        await pg.screenshot(path='s_result_desktop.png',full_page=True)
        m=await b.new_page(viewport={'width':360,'height':800})
        await m.goto('file://'+__import__('os').path.abspath('test.html'))
        await m.screenshot(path='s_quiz_mobile.png')
        for sc in [SC[0]]:
            await run(m,sc)
        await m.screenshot(path='s_result_mobile.png',full_page=True)
        for vw in (320,360,390):
            await m.set_viewport_size({'width':vw,'height':800})
            sw=await m.evaluate("[document.documentElement.scrollWidth,document.documentElement.clientWidth]")
            print('viewport',vw,'scroll/client',sw)
        # static content with JavaScript off
        ctx=await b.new_context(java_script_enabled=False,viewport={'width':1280,'height':900})
        n=await ctx.new_page()
        await n.goto('file://'+__import__('os').path.abspath('test.html'))
        print('no-JS goals h3:',await n.eval_on_selector_all('#sjc-goals h3','e=>e.length'),'list rows:',await n.eval_on_selector_all('#sjc-list tbody tr','e=>e.length'),'faq:',await n.eval_on_selector_all('.sj-faq details','e=>e.length'),'h1:',await n.eval_on_selector_all('h1','e=>e.map(x=>x.innerText)'))
        # JSON-LD parity
        import json,re
        w=open('a-level-subject-combinations-tool-elementor-widget.html').read()
        lds=[json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>',w,re.S)]
        faq=[l for l in lds if l['@type']=='FAQPage'][0]['mainEntity']
        import html as _h
        det=re.findall(r'<details[^>]*><summary>(.*?)</summary><div class="sj-faq-a"><p>(.*?)</p>',w)
        print('faq parity:',[(q['name'],q['acceptedAnswer']['text']) for q in faq]==[(_h.unescape(x),_h.unescape(y)) for x,y in det])
        await n.screenshot(path='s_static_goals.png',clip=None,full_page=True)
        m2=await b.new_page(viewport={'width':320,'height':800})
        await m2.goto('file://'+__import__('os').path.abspath('test.html'))
        print('320 static scroll/client',await m2.evaluate("[document.documentElement.scrollWidth,document.documentElement.clientWidth]"))
        await m2.locator('#sjc-list').screenshot(path='s_list_mobile.png')
        await b.close()
asyncio.run(main())
