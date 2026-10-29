// Components for the SJ Academy dotted-notebook carousel style (v2).
const LOGO='<img class="logo" src="logos/logo-on-light.svg">';
const pill=t=>`<div class="pill">${t}</div>`;
const wrap=(id,inner)=>`<section class="s" id="s${id}">${inner}</section>`;
const ARROW=(c='#fff')=>`<svg width="56" height="34" viewBox="0 0 64 40"><path d="M4 20 H56 M40 5 L58 20 L40 35" stroke="${c}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
const ARROWB=ARROW('#B54200');
const CIRC=(w,h,st='')=>`<svg style="position:absolute;pointer-events:none;${st}" width="${w}" height="${h}" viewBox="0 0 300 120" preserveAspectRatio="none"><path d="M40 20 C120 -6 272 12 290 58 C300 104 140 120 58 100 C-6 84 4 32 78 10 C130 -4 200 -2 240 8" stroke="#B54200" stroke-width="6" fill="none" stroke-linecap="round"/></svg>`;
// Flat vector tablet (drawn in code, not a photo). kind: ipad | samsung | xiaomi
function tablet(kind,w=230){
 const c={ipad:['#8DB3D6','#fff'],samsung:['#9DB4A9','#2b2f33'],xiaomi:['#585C62','#f3f1ea']}[kind];
 const cam=kind=='xiaomi'?'<circle cx="34" cy="48" r="13" fill="#222" stroke="#151515" stroke-width="3"/><circle cx="34" cy="80" r="13" fill="#222" stroke="#151515" stroke-width="3"/>':'<circle cx="34" cy="46" r="11" fill="#222" stroke="#151515" stroke-width="3"/>';
 const pen=kind=='samsung'?`<g transform="rotate(14 212 140)"><rect x="206" y="40" width="9" height="200" rx="4.5" fill="${c[1]}" stroke="#151515" stroke-width="3"/></g>`:`<rect x="208" y="30" width="10" height="200" rx="5" fill="${c[1]}" stroke="#151515" stroke-width="3"/>`;
 return `<svg width="${w}" height="${w*1.2}" viewBox="0 0 226 270"><rect x="8" y="22" width="150" height="226" rx="16" fill="${c[0]}" stroke="#151515" stroke-width="4"/>${cam}
 <rect x="46" y="8" width="150" height="240" rx="16" fill="#1d1d20" stroke="#151515" stroke-width="4"/>
 <rect x="56" y="20" width="130" height="216" rx="7" fill="#fff"/>
 <rect x="66" y="32" width="64" height="9" rx="4" fill="#C9C4B4"/><rect x="66" y="50" width="110" height="6" rx="3" fill="#DDD8C8"/><rect x="66" y="64" width="96" height="6" rx="3" fill="#DDD8C8"/>
 <path d="M68 108 C78 94 86 124 96 108 S112 96 122 110 S142 120 168 100" stroke="#1B2A4A" stroke-width="3.5" fill="none" stroke-linecap="round"/>
 <path d="M68 140 C80 128 90 152 102 138 S120 128 136 140" stroke="#1B2A4A" stroke-width="3.5" fill="none" stroke-linecap="round"/>
 <path d="M146 134 L154 144 L170 122" stroke="#D63A2F" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
 <circle cx="150" cy="186" r="24" stroke="#D63A2F" stroke-width="4.5" fill="none"/><path d="M66 176 H120 M66 192 H112 M66 208 H126" stroke="#DDD8C8" stroke-width="6" stroke-linecap="round"/>
 ${pen}</svg>`;
}
exports.cover=({pill:p,l1,l2hl,l2pre,sub,cards,hand,cta,total})=>wrap(1,
 `${LOGO}${pill(p)}
  <div class="col" style="top:300px;gap:22px"><h1 style="font-size:104px;white-space:nowrap">${l1}<br>${l2pre} <span class="mark">${l2hl}</span></h1>
   <p style="font-size:52px;font-weight:500;letter-spacing:-.02em;color:#2B2B2B;margin-top:8px">${sub}</p></div>
  ${cards.map((k,i)=>{const x=72+i*(293+28.5);return `<div class="minicard" style="left:${x}px;top:800px;width:293px;height:300px;padding-top:150px"><div style="position:absolute;left:50%;top:-120px;transform:translateX(-50%)">${tablet(k.kind,190)}</div><div class="n">${k.name}</div><div class="p">${k.price}</div></div>`}).join('')}
  <div class="hand" style="position:absolute;left:72px;bottom:80px;font-size:68px;display:flex;align-items:center;gap:14px">${hand} ${ARROWB}</div>
  <div class="cta" style="position:absolute;right:72px;bottom:72px">${cta} ${ARROW()}</div>`);
exports.product=({n,pillText,kind,title,price,bullets,circleIdx,hand,catchText,cardH=430,bs=44,tw=250,cs=38,gap=26,hs=62})=>wrap(n,
 `${LOGO}${pill(pillText)}
  <div class="col" style="top:236px;gap:${gap}px">
   <h1 class="center" style="font-size:84px">${title}</h1>
   <div class="strip">${price}</div>
   <div class="card" style="margin-top:14px;height:${cardH}px;padding:6px 36px"><ul style="width:590px;margin-top:16px">${bullets.map((b,i)=>`<li style="position:relative;font-size:${bs}px">${b}${i===circleIdx?CIRC(300,84,'left:40px;top:36px'):''}</li>`).join('')}</ul>
    <div style="position:absolute;right:30px;bottom:26px">${tablet(kind,tw)}</div></div>
   ${hand?`<div class="hand" style="font-size:${hs}px;margin-top:0;padding-left:12px">${hand}</div>`:''}
   <div class="catch" style="font-size:${cs}px">${catchText}</div>
  </div>`);
exports.pen=({n,pillText,title,hl,q,work,subjects,warn,hand})=>wrap(n,
 `${LOGO}${pill(pillText)}
  <div class="col" style="top:236px;gap:34px">
   <h1 class="center" style="font-size:86px">${title.replace(hl,`<span class="mark">${hl}</span>`)}</h1>
   <div class="paper" style="height:330px;transform:rotate(-.9deg);background-image:repeating-linear-gradient(transparent 0 58px,#C9D3E6 58px 60px);background-position:0 38px">
    <div style="position:absolute;left:84px;top:0;bottom:0;border-left:3px solid rgba(214,58,47,.45)"></div>
    <div style="position:absolute;right:28px;top:22px;border:3px solid #D63A2F;color:#B92F25;font-size:22px;font-weight:700;letter-spacing:.12em;padding:3px 12px;border-radius:5px;transform:rotate(4deg)">SAMPLE</div>
    <div style="position:absolute;left:112px;top:34px;font-size:36px;font-weight:600;color:#1B2A4A">${q}</div>
    <div class="hand" style="position:absolute;left:130px;top:140px;font-size:84px;color:#1B2A4A;white-space:nowrap">${work}</div>
    <div class="hand" style="position:absolute;left:372px;top:106px;font-size:48px;color:#B92F25;transform:rotate(-6deg)">M1</div>
    <div class="hand" style="position:absolute;left:520px;top:106px;font-size:48px;color:#B92F25;transform:rotate(-6deg)">A1</div>
    <div class="hand" style="position:absolute;right:56px;top:196px;font-size:110px;color:#B92F25;transform:rotate(-5deg);line-height:1">2/2${CIRC(220,120,'left:-28px;top:-6px').replace('#B54200','#D63A2F')}</div>
   </div>
   <p class="center" style="font-size:44px;font-weight:600;letter-spacing:-.02em;line-height:1.3">${subjects}</p>
   <div class="catch" style="text-align:center">${warn}</div>
   <div class="hand" style="font-size:64px;text-align:center">${hand}</div>
  </div>`);
exports.table=({n,pillText,title,sub,headers,rows,hand})=>wrap(n,
 `${LOGO}${pill(pillText)}
  <div class="col" style="top:220px;gap:20px">
   <h1 class="center" style="font-size:82px"><span class="mark">${title}</span></h1>
   <p class="center" style="font-size:34px;font-weight:500;color:#2B2B2B">${sub}</p>
   <div class="card" style="overflow:hidden;padding:0">
    <table style="width:100%;border-collapse:collapse;font-size:28px">
     <thead><tr style="background:#F7F5EF;border-bottom:4px solid #151515">${headers.map(h=>`<th style="padding:22px 20px;text-align:left;font-size:22px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#6b6252">${h}</th>`).join('')}</tr></thead>
     <tbody>${rows.map(r=>`<tr style="border-top:2px solid #E2DDD0;background:${r[4]?'#FFF9CC':'#fff'}"><td style="padding:24px 20px;font-weight:700">${r[0]}</td><td style="padding:24px 20px;font-weight:700">${r[1]}</td><td style="padding:24px 20px;color:${r[2].startsWith('No ')?'#B92F25':'#2B2B2B'}">${r[2]}</td><td style="padding:24px 20px">${r[3]}</td></tr>`).join('')}</tbody>
    </table>
   </div>
   ${hand?`<div class="hand center" style="font-size:52px">${hand}</div>`:''}
  </div>`);
exports.picks=({n,pillText,title,items})=>wrap(n,
 `${LOGO}${pill(pillText)}
  <div class="col" style="top:236px;gap:38px">
   <h1 class="center" style="font-size:120px"><span class="mark">${title}</span></h1>
   ${items.map(it=>`<div class="pick"><div class="l">${it[0]}</div><b>${it[1]}</b></div>`).join('')}
  </div>`);
exports.cta=({n,text,hl,body,button,line1,line2,foot,pillText})=>wrap(n,
 `${LOGO}
  <div class="col" style="top:260px;gap:40px">
   <h1 style="font-size:92px">${text.replace(hl,`<span class="mark">${hl}</span>`)}</h1>
   <p style="font-size:44px;font-weight:500;color:#2B2B2B">${body}</p>
   <div class="card y" style="padding:40px 46px;margin-right:14px"><div style="font-size:68px;font-weight:800;letter-spacing:-.04em;line-height:1">${button}</div><div style="font-size:38px;font-weight:600;margin-top:18px">${line1}</div><div style="font-size:38px;font-weight:600;margin-top:6px;color:#2B2B2B">${line2}</div></div>
   <div><span class="cta">${foot} ${ARROW()}</span></div>
  </div>`);
