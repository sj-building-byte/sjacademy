// SJ Academy carousel components. Each returns an HTML string for one 1080 x 1350 slide.
const TICK = `<svg class="tick" viewBox="0 0 48 48"><path d="M7 26 C13 31 17 37 20 42 C26 28 34 16 43 6"/></svg>`;
const ARROW = (c='#F7F5EF')=>`<svg class="arrow" viewBox="0 0 64 40"><path d="M4 20 H56 M40 5 L58 20 L40 35" stroke="${c}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
const CIRCLE = (w,h,style='')=>`<svg style="position:absolute;${style}" width="${w}" height="${h}" viewBox="0 0 300 120" preserveAspectRatio="none"><path d="M40 22 C120 -4 272 14 288 60 C298 106 140 118 58 100 C-4 84 6 34 74 12" stroke="#D63A2F" stroke-width="6" fill="none" stroke-linecap="round"/></svg>`;
const prog=(n,t)=>`<div class="prog">${Array.from({length:t},(_,i)=>`<i class="${i<n?'on':''}"></i>`).join('')}${n<t?`<span class="sw">Swipe ${ARROW()}</span>`:''}</div>`;
const head=(kick,n,t)=>`<div class="kick">${kick}</div><div class="count">${n}/${t}</div>`;
const wrap=(id,cls,inner)=>`<section class="s ${cls||''}" id="s${id}">${inner}</section>`;

// 1. Cover: three huge stacked words, a pill, a sub line
exports.cover=({lines,sub,pill,total,size=166})=>wrap(1,'',
 `<img src="logos/logo-on-dark.svg" style="position:absolute;left:72px;top:72px;height:80px">
  <div class="count">${pill}</div>
  <div style="position:absolute;left:72px;right:72px;top:250px" class="display">
   ${lines.map((l,i)=>`<div style="font-size:${size}px;white-space:nowrap;${i==1?'color:#FCE004':''}">${l}</div>`).join('')}
  </div>
  <p style="position:absolute;left:72px;width:880px;top:830px;font-size:50px;font-weight:500;line-height:1.3;color:#D9D4C7">${sub}</p>
  ${prog(1,total)}`);

// 2. Receipts: two bills side by side, the real price
exports.receipts=({n,total,kick,title,hl,left,right})=>{
 const rc=(r,x,rot)=>`<div class="receipt" style="left:${x}px;top:540px;transform:rotate(${rot}deg)"><div class="in">
   <div class="ttl">${r.title}</div><div class="ln"></div>
   ${r.items.map(i=>`<div class="it">${i[0]}</div><div class="v">${i[1]}</div>`).join('')}
   <div class="ln"></div><div class="tot">Total</div><div class="tv" style="position:relative;display:inline-block;padding-left:22px">${r.total}${CIRCLE(336,116,'left:-4px;top:-12px')}</div></div></div>`;
 return wrap(n,'',`${head(kick,n,total)}
  <h1 class="h1" style="position:absolute;left:72px;right:72px;top:150px;font-size:104px">${title.replace(hl,`<span class="y">${hl}</span>`)}</h1>
  ${rc(left,72,-2)}${rc(right,556,1.8)}<div class="hand y" style="position:absolute;left:96px;top:1150px;font-size:70px;transform:rotate(-4deg)">pen sold separately</div>${prog(n,total)}`);
};

// 3. Product card: brand word, price rows, tick list, stamp, catch note
exports.product=({n,total,kick,brand,models,rows,bullets,stamp,catchText})=>wrap(n,'',
 `${head(kick,n,total)}
  <div class="display y" style="position:absolute;left:72px;top:140px;font-size:168px">${brand}</div>
  <div style="position:absolute;left:76px;top:322px;font-size:50px;font-weight:600;letter-spacing:-.03em;color:#D9D4C7">${models}</div>
  <div class="card" style="position:absolute;left:72px;right:72px;top:430px;padding:40px 44px 30px;transform:rotate(-1.2deg)">
   <div class="label" style="color:#6b6252;margin-bottom:6px">Oct 2026</div>
   ${rows.map(r=>`<div style="display:flex;justify-content:space-between;align-items:baseline;padding:8px 0"><span style="font-size:36px;font-weight:600;color:#6b6252">${r[0]}</span><span class="price" style="font-size:60px">${r[1]}</span></div>`).join('')}
   <div style="border-top:3px solid rgba(21,21,21,.15);margin:20px 0 10px"></div>
   <ul style="list-style:none">${bullets.map(b=>`<li style="display:flex;align-items:center;gap:22px;font-size:44px;font-weight:600;letter-spacing:-.02em;padding:12px 0">${TICK}<span>${b}</span></li>`).join('')}</ul>
  </div>
  <div class="stamp" style="right:84px;top:985px;width:236px;height:236px;font-size:30px;transform:rotate(9deg)">${stamp}</div>
  <div class="note" style="left:72px;top:1010px;width:640px;transform:rotate(1.6deg)"><div class="label">Catch</div><p>${catchText}</p></div>
  ${prog(n,total)}`);

// 4. Marked sample: exam paper with red pen marks
exports.paper=({n,total,kick,title,hl,code,q,work,margin,subjects})=>wrap(n,'',
 `${head(kick,n,total)}
  <h1 class="h1" style="position:absolute;left:72px;right:72px;top:150px;font-size:96px">${title.replace(hl,`<span class="y">${hl}</span>`)}</h1>
  <div class="paper" style="position:absolute;left:72px;right:72px;top:430px;height:560px;transform:rotate(-.9deg);background-image:repeating-linear-gradient(transparent 0 66px,#C9D3E6 66px 68px);background-position:0 40px;overflow:hidden">
   <div style="position:absolute;left:96px;top:0;bottom:0;border-left:3px solid rgba(214,58,47,.45)"></div>
   <div style="position:absolute;left:130px;top:34px;font-size:24px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#1B2A4A">${code}</div>
   <div style="position:absolute;right:40px;top:26px;border:3px solid #D63A2F;color:#B92F25;font-size:22px;font-weight:700;letter-spacing:.12em;padding:4px 14px;border-radius:5px;transform:rotate(4deg)">SAMPLE</div>
   <div style="position:absolute;left:130px;top:108px;font-size:40px;font-weight:600;color:#1B2A4A;letter-spacing:-.01em">${q}</div>
   <div class="hand" style="position:absolute;left:150px;top:260px;font-size:84px;color:#1B2A4A;white-space:nowrap">${work}</div>
   <div class="hand" style="position:absolute;left:470px;top:222px;font-size:50px;color:#B92F25;transform:rotate(-6deg)">M1</div>
   <div class="hand" style="position:absolute;left:610px;top:222px;font-size:50px;color:#B92F25;transform:rotate(-6deg)">A1</div>
   <div class="hand" style="position:absolute;right:70px;top:380px;font-size:130px;color:#B92F25;transform:rotate(-5deg);line-height:1">2/2${CIRCLE(250,150,'left:-36px;top:-6px')}</div>
   <div class="hand" style="position:absolute;left:130px;top:400px;width:560px;line-height:1;font-size:52px;color:#B92F25;transform:rotate(-2deg)">${margin}</div>
  </div>
  <p style="position:absolute;left:72px;right:72px;top:1050px;font-size:44px;font-weight:600;letter-spacing:-.02em;line-height:1.3;color:#F7F5EF">${subjects}</p>
  ${prog(n,total)}`);

// 5. Big type: one sentence fills the frame, with an optional sticky note
exports.big=({n,total,kick,text,hl,noteLabel,noteText})=>wrap(n,'',
 `${head(kick,n,total)}
  <h1 class="h1" style="position:absolute;left:72px;right:72px;top:170px;font-size:128px;line-height:1">${text.replace(hl,`<span class="y">${hl}</span>`)}</h1>
  <div class="note" style="left:72px;top:1000px;width:700px;transform:rotate(-1.6deg)"><div class="label">${noteLabel}</div><p>${noteText}</p></div>
  ${prog(n,total)}`);

// 6. Picks: stacked paper strips
exports.picks=({n,total,kick,title,items})=>wrap(n,'',
 `${head(kick,n,total)}
  <h1 class="h1 y" style="position:absolute;left:72px;top:150px;font-size:130px">${title}</h1>
  <div style="position:absolute;left:72px;right:72px;top:340px;display:flex;flex-direction:column;gap:34px">
   ${items.map((it,i)=>`<div class="strip" style="transform:rotate(${i%2?0.8:-0.8}deg)">${TICK}<div><div class="label">${it[0]}</div><b>${it[1]}</b></div></div>`).join('')}
  </div>
  ${prog(n,total)}`);

// 7. CTA: yellow ground, offset ticket
exports.cta=({n,total,text,hl,body,button,line1,line2,foot})=>wrap(n,'yellow',
 `<img src="logos/logo-on-yellow.svg" style="position:absolute;left:72px;top:72px;height:80px">
  <div class="count" style="border-color:#151515;color:#151515">${n}/${total}</div>
  <h1 class="h1" style="position:absolute;left:72px;right:72px;top:230px;font-size:92px;color:#151515">${text.replace(hl,`<span class="hl" style="--b:#fff">${hl}</span>`)}</h1>
  <p style="position:absolute;left:72px;right:72px;top:690px;font-size:42px;font-weight:500;color:#2B2B2B">${body}</p>
  <div class="ticket" style="position:absolute;left:72px;right:88px;top:830px"><div class="big">${button}</div><div class="row">${line1}</div><div class="row" style="margin-top:6px">${line2}</div></div>
  <p style="position:absolute;left:72px;bottom:72px;font-size:34px;font-weight:600;color:#151515">${foot}</p>`);
