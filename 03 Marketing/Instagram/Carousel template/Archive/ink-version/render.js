// SJ Academy carousel renderer.
// Setup once: npm i playwright-core   (needs a Chromium; set CHROME_PATH if not in /opt/pw-browsers)
// Usage: node render.js deck-tablets.js [outDir]
const fs=require('fs'),path=require('path');
const {chromium}=require('playwright-core');
const deck=require(path.resolve(process.argv[2]||'deck-tablets.js'));
const out=path.resolve(process.argv[3]||'out');fs.mkdirSync(out,{recursive:true});
const css=fs.readFileSync(path.join(__dirname,'template.css'),'utf8');
fs.writeFileSync(path.join(__dirname,'_deck.html'),`<!doctype html><meta charset=utf-8><style>${css}</style>${deck.slides.join('\n')}`);
(async()=>{
 const exe=require('child_process').execSync('ls /opt/pw-browsers/chromium-*/chrome-linux*/chrome | head -1').toString().trim();
 const b=await chromium.launch({executablePath:exe});
 const p=await b.newPage({viewport:{width:1100,height:1400}});
 await p.goto('file://'+path.join(__dirname,'_deck.html'));
 await p.evaluate(()=>document.fonts.ready);
 for(let i=1;i<=deck.slides.length;i++){
  await p.locator('#s'+i).screenshot({path:path.join(out,`${deck.name}-${i}.png`)});
  const info=await p.evaluate(i=>{const s=document.getElementById('s'+i);
   const words=[...s.querySelectorAll('*')].filter(e=>!e.closest('.kick,.count,.prog')).map(e=>[...e.childNodes].filter(n=>n.nodeType==3).map(n=>n.textContent).join(' ')).join(' ').split(/\s+/).filter(x=>/[A-Za-z0-9]/.test(x)).length;
   const bad=[...s.querySelectorAll('*')].filter(e=>e.children.length==0&&e.textContent.trim()&&!e.closest('.prog,.stamp')).filter(e=>{const r=e.getBoundingClientRect(),sr=s.getBoundingClientRect();return r.right>sr.right-60||r.left<sr.left+60||r.bottom>sr.bottom-60}).map(e=>e.textContent.trim().slice(0,28));
   return {words,bad}},i);
  console.log(i,JSON.stringify(info));
 }
 await b.close();
})();
