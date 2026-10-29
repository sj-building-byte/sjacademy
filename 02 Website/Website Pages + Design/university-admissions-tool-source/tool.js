/* University admission criteria checker. Wrapped in a function, no jQuery, every id starts with sju-. */
(function(){
  var root=document.getElementById('sj');
  if(!root||!root.classList.contains('sj-p-uni-criteria')){return;}
  var $=function(id){return document.getElementById(id);};
  var D;
  try{D=JSON.parse($('sju-data').textContent);}catch(err){$('sju-err').hidden=false;return;}

  /* ---------- Constants ---------- */
  var SUB={};D.subjects.forEach(function(s){SUB[s[0]]=s[1];});
  var AREA={};D.areas.forEach(function(a){AREA[a[0]]=a[1];});
  var PTS={'A*':6,'A':5,'B':4,'C':3,'D':2,'E':1};
  var GR=['','E','D','C','B','A','A*'];
  var GRADES=['A*','A','B','C','D','E'];
  /* IBCC conversion. A* uses IBCC's 2026 table; letters are fixed. */
  var AM={'A':85,'B':75,'C':65,'D':55,'E':45};
  var AST={phy:95,chem:94,bio:94,cs:93,math:94};
  var amark=function(s,g){return g==='A*'?(AST[s]||94):AM[g];};
  var omark=function(g){return g==='A*'?94:AM[g];};
  /* Subjects SJ Academy teaches at A Level, with their pages */
  var TEACH={math:'/a-level-maths-tuition/',phy:'/a-level-physics-tuition/',chem:'/a-level-chemistry-tuition/',bio:'/a-level-biology-tuition/',cs:'/a-level-computer-science-tuition/',econ:'/a-level-economics-tuition/',bus:'/a-level-business-tuition/',acc:''};
  var WA='https://wa.me/923362144454?text=';
  var KEY='sju-v1';
  var TODAY=new Date();TODAY.setHours(0,0,0,0);
  var MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var TICK='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg>';
  var CROSS='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';

  var esc=function(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');};
  var send=function(name,loc){var g=window['gt'+'ag'];if(typeof g==='function'){g('event',name,{link_location:loc||'tool',page_family:'tool'});}};
  var fresh=function(){return {mode:'look',uni:'',prog:'',a:[{s:'',g:''},{s:'',g:''},{s:'',g:''}],o:{'A*':0,'A':0,'B':0,'C':0,'D':0,'E':0},areas:[],time:'',city:'any',sat:'',short:[],step:1,done:false};};
  var st=fresh();
  var save=function(){try{localStorage.setItem(KEY,JSON.stringify(st));}catch(err){}};
  try{var raw=localStorage.getItem(KEY);if(raw){var got=JSON.parse(raw);if(got&&got.a&&got.o){st=got;}}}catch(err){}

  var parseDate=function(iso){var p=iso.split('-');return new Date(+p[0],+p[1]-1,+p[2]);};
  var daysTo=function(iso){return Math.round((parseDate(iso)-TODAY)/864e5);};
  var fmt=function(iso){var d=parseDate(iso);return d.getDate()+' '+MON[d.getMonth()]+' '+d.getFullYear();};
  var left=function(n){return n===0?'Today':n===1?'Tomorrow':n+' days left';};
  var nameList=function(ids,j){var n=ids.map(function(i){return SUB[i];});return n.length<2?n.join(''):n.slice(0,-1).join(', ')+' '+(j||'and')+' '+n[n.length-1];};

  /* ---------- Profile from answers ---------- */
  function profile(s){
    var a=[],seen={},subs={};
    s.a.forEach(function(r){if(r.s&&r.g&&!seen[r.s]){seen[r.s]=1;a.push({s:r.s,g:r.g});subs[r.s]=r.g;}});
    var on=0,osum=0,opts=0;
    GRADES.forEach(function(g){var n=+s.o[g]||0;on+=n;osum+=n*omark(g);opts+=n*PTS[g];});
    var top=a.map(function(r){return amark(r.s,r.g);}).sort(function(x,y){return y-x;}).slice(0,3);
    var asum=top.reduce(function(t,x){return t+x;},0);
    return {a:a,subs:subs,on:on,olPct:on?osum/on:0,olAvg:on?opts/on:0,
      hssc:(on+top.length)?(osum+asum)/((on+top.length)):0};
  }

  /* The three A Levels a university would count: required ones first, then the best of the rest */
  function counted(P,r){
    var ex=r.exclude||[];
    var pool=P.a.filter(function(x){return ex.indexOf(x.s)<0;});
    var req=(r.need||[]).slice();
    if(r.sets){var m=r.sets.filter(function(set){return set.every(function(x){return P.subs[x];});})[0];if(m){req=req.concat(m);}}
    if(r.minEach){Object.keys(r.minEach).forEach(function(k){req.push(k);});}
    var pick=[],used={};
    pool.forEach(function(x){if(req.indexOf(x.s)>-1&&pick.length<3){pick.push(x);used[x.s]=1;}});
    pool.filter(function(x){return !used[x.s];}).sort(function(x,y){return PTS[y.g]-PTS[x.g];}).forEach(function(x){if(pick.length<3){pick.push(x);}});
    return {pool:pool,pick:pick,pts:pick.map(function(x){return PTS[x.g];}).sort(function(x,y){return y-x;})};
  }

  function rulesFor(u,p){var r={},k;for(k in u.common){r[k]=u.common[k];}for(k in p.rules){r[k]=p.rules[k];}return r;}

  function check(u,p,P){
    var r=rulesFor(u,p),out=[],c=counted(P,r);
    var mine=function(list){return list.map(function(x){return x.g;}).join(' ');};
    if(r.count3){var ok3=c.pool.length>=3;out.push({ok:ok3,type:'subject',t:ok3?'Three full A Levels that count':'Needs three full A Levels'+(r.exclude&&r.exclude.length?' ('+nameList(r.exclude)+' does not count)':'')});}
    if(r.sets){var hit=r.sets.some(function(set){return set.every(function(x){return P.subs[x];});});out.push({ok:hit,type:'subject',t:p.setLabel||'Required subject combination'});}
    if(r.need){var miss=r.need.filter(function(x){return !P.subs[x];});out.push({ok:!miss.length,type:'subject',t:'A Level '+nameList(r.need)+(r.need.length>1?' required':' required')});}
    if(r.minEach){Object.keys(r.minEach).forEach(function(k){
      var want=r.minEach[k],g=P.subs[k];
      if(!g){out.push({ok:false,type:'subject',t:SUB[k]+' at '+want+' or better (not taken)'});}
      else{out.push({ok:PTS[g]>=PTS[want],type:'grade',t:SUB[k]+' at '+want+' or better (you: '+g+')',sub:k});}
    });}
    if(r.oneOfMin){var o=r.oneOfMin,have=o.subs.filter(function(x){return P.subs[x];});
      if(!have.length){out.push({ok:false,type:'subject',t:nameList(o.subs,'or')+' at '+o.g+' or better (neither taken)'});}
      else{var b=Math.max.apply(null,have.map(function(x){return PTS[P.subs[x]];}));out.push({ok:b>=PTS[o.g],type:'grade',t:nameList(o.subs,'or')+' at '+o.g+' or better (you: '+GR[b]+')'});}
    }
    if(r.best3Avg){var n=c.pts.length,avg=n?c.pts.reduce(function(t,x){return t+x;},0)/3:0;
      out.push({ok:n>=3&&avg>=PTS[r.best3Avg]-1e-9,type:'grade',t:'Average '+r.best3Avg+' across your best three (you: '+(mine(c.pick)||'none')+')'});}
    if(r.minSorted){var okS=r.minSorted.every(function(g,i){return (c.pts[i]||0)>=PTS[g];});
      out.push({ok:okS,type:'grade',t:'At least '+r.minSorted.join(', ')+' (you: '+(mine(c.pick)||'none')+')'});}
    if(r.monashScore){var ms=P.a.map(function(x){return Math.min(5,PTS[x.g]);}).sort(function(x,y){return y-x;}).slice(0,3);
      var tot=ms.reduce(function(t,x){return t+x;},0)+(P.a.some(function(x){return x.g==='A*';})?1:0);
      out.push({ok:ms.length>=3&&tot>=r.monashScore,type:'grade',t:'Monash score '+r.monashScore+' or more (you: '+(ms.length>=3?tot:'needs three A Levels')+')'});}
    if(r.olMin){out.push({ok:P.on>=r.olMin,type:'hard',t:'At least '+r.olMin+' O Levels (you entered '+P.on+')'});}
    if(r.olAvg){out.push({ok:P.olAvg>=PTS[r.olAvg]-0.001,type:'hard',t:'O Level average '+r.olAvg+' or better (you: about '+(GR[Math.round(P.olAvg)]||'none')+')'});}
    if(r.ssc){out.push({ok:P.olPct>=r.ssc,type:'hard',t:'O Level (SSC) equivalence '+r.ssc+'% or more (you: about '+Math.round(P.olPct)+'%)'});}
    if(r.hssc){out.push({ok:P.hssc>=r.hssc,type:'grade',t:'HSSC equivalence '+r.hssc+'% or more (you: about '+Math.round(P.hssc)+'%)'});}
    var fails=out.filter(function(x){return !x.ok;});
    var status=!fails.length?'yes':fails.some(function(x){return x.type!=='grade';})?'no':'close';
    return {status:status,checks:out};
  }

  function inScope(u,p,s){
    var areas=s.areas.length&&s.areas.indexOf('all')<0?s.areas:null;
    if(areas&&!p.areas.some(function(a){return areas.indexOf(a)>-1;})){return false;}
    if(s.city&&s.city!=='any'&&u.cities.indexOf(s.city)<0){return false;}
    return true;
  }
  function run(s){
    var P=profile(s),rows=[];
    D.unis.forEach(function(u){u.progs.forEach(function(p){if(inScope(u,p,s)){var r=check(u,p,P);rows.push({u:u,p:p,status:r.status,checks:r.checks});}});});
    return {P:P,rows:rows};
  }

  /* The grade change that opens the most programmes: one step first, then two */
  function unlock(s,base){
    var was={};base.rows.forEach(function(r){was[r.p.id]=r.status;});
    var idx=[];s.a.forEach(function(row,i){if(row.s&&row.g){idx.push(i);}});
    var tries=[];
    idx.forEach(function(i){tries.push([i]);});
    var best=null,pass=function(list){
      list.forEach(function(t){
        var copy=JSON.parse(JSON.stringify(s)),ok=true;
        t.forEach(function(i){var g=copy.a[i].g;if(g==='A*'){ok=false;return;}copy.a[i].g=GR[PTS[g]+1];});
        if(!ok){return;}
        var opened=run(copy).rows.filter(function(r){return r.status==='yes'&&was[r.p.id]!=='yes';});
        if(!opened.length){return;}
        var steps=t.map(function(i){return {sub:s.a[i].s,from:s.a[i].g,to:copy.a[i].g};});
        var low=t.reduce(function(m,i){return Math.min(m,PTS[s.a[i].g]);},9);
        if(!best||opened.length>best.list.length||(opened.length===best.list.length&&low<best.low)){best={steps:steps,list:opened,low:low};}
      });
    };
    pass(tries);
    if(!best){
      var two=[];idx.forEach(function(i,a){idx.forEach(function(j,b){if(b>=a){two.push([i,j]);}});});
      pass(two);
    }
    if(best){ /* merge a subject raised twice into one step */
      var m={};best.steps.forEach(function(x){if(m[x.sub]){m[x.sub].to=x.to;}else{m[x.sub]=x;}});
      best.steps=Object.keys(m).map(function(k){return m[k];});
    }
    return best;
  }

  /* ---------- Quiz ---------- */
  var arows=$('sju-arows'),tpl=$('sju-arow-t');
  function drawRows(){
    arows.innerHTML='';
    st.a.forEach(function(r,i){
      var node=tpl.content.firstElementChild.cloneNode(true);
      var sels=node.querySelectorAll('select');
      sels[0].value=r.s||'';sels[1].value=r.g||'';
      sels[0].setAttribute('aria-label','A Level subject '+(i+1));sels[1].setAttribute('aria-label','Grade for subject '+(i+1));
      sels[0].addEventListener('change',function(){st.a[i].s=this.value;save();hint('');});
      sels[1].addEventListener('change',function(){st.a[i].g=this.value;save();hint('');});
      var x=node.querySelector('.sju-x');
      if(st.a.length<=3){x.hidden=true;}
      x.addEventListener('click',function(){st.a.splice(i,1);save();drawRows();});
      arows.appendChild(node);
    });
    $('sju-add').hidden=st.a.length>=4;
  }
  $('sju-add').addEventListener('click',function(){if(st.a.length<4){st.a.push({s:'',g:''});save();drawRows();arows.lastElementChild.querySelector('select').focus();}});

  function drawCounts(){
    var tot=0;GRADES.forEach(function(g){$('sju-o-'+g.replace('*','s')).value=st.o[g];$('sju-o-'+g.replace('*','s')).textContent=st.o[g];tot+=+st.o[g];});
    $('sju-otot').textContent=tot+' of 8 entered'+(tot>8?' (IBCC counts 8; use your 8 required subjects)':'');
  }
  root.querySelectorAll('[data-o]').forEach(function(b){
    b.addEventListener('click',function(){
      var g=b.getAttribute('data-o'),d=+b.getAttribute('data-d');
      st.o[g]=Math.max(0,Math.min(12,(+st.o[g]||0)+d));save();drawCounts();hint('');
    });
  });
  var areaBoxes=root.querySelectorAll('input[name="sju-area"]');
  areaBoxes.forEach(function(b){
    b.addEventListener('change',function(){
      if(b.value==='all'&&b.checked){areaBoxes.forEach(function(x){if(x!==b){x.checked=false;}});}
      if(b.value!=='all'&&b.checked){areaBoxes.forEach(function(x){if(x.value==='all'){x.checked=false;}});}
      var picked=[].filter.call(areaBoxes,function(x){return x.checked&&x.value!=='all';});
      if(picked.length>3){b.checked=false;hint('Pick up to three, or choose "Show me everything".');return;}
      st.areas=[].filter.call(areaBoxes,function(x){return x.checked;}).map(function(x){return x.value;});save();hint('');
    });
  });
  root.querySelectorAll('input[name="sju-time"]').forEach(function(r){r.addEventListener('change',function(){st.time=r.value;save();});});
  root.querySelectorAll('input[name="sju-city"]').forEach(function(r){r.addEventListener('change',function(){st.city=r.value;save();});});
  $('sju-sat').addEventListener('input',function(){st.sat=this.value;save();});

  function syncInputs(){
    drawRows();drawCounts();
    areaBoxes.forEach(function(x){x.checked=st.areas.indexOf(x.value)>-1;});
    root.querySelectorAll('input[name="sju-time"]').forEach(function(r){r.checked=r.value===st.time;});
    root.querySelectorAll('input[name="sju-city"]').forEach(function(r){r.checked=r.value===(st.city||'any');});
    $('sju-sat').value=st.sat||'';
  }
  function hint(t){$('sju-hint').textContent=t;}
  function valid(step){
    if(step===1){
      var full=st.a.filter(function(r){return r.s&&r.g;});
      var part=st.a.filter(function(r){return (r.s&&!r.g)||(!r.s&&r.g);});
      var subs=full.map(function(r){return r.s;});
      if(part.length){return 'Pick a subject and a grade for every row, or remove the row.';}
      if(full.length<3){return 'Add at least three A Levels with a grade.';}
      if(subs.some(function(x,i){return subs.indexOf(x)!==i;})){return 'Each subject can only appear once.';}
      return '';
    }
    if(step===2){var t=0;GRADES.forEach(function(g){t+=+st.o[g]||0;});return t<5?'Add your O Level grades. Most students have 8.':'';}
    if(step===3){return st.areas.length?'':'Pick at least one area, or "Show me everything".';}
    return '';
  }
  function showStep(n){
    st.step=n;save();
    root.querySelectorAll('[data-step]').forEach(function(f){f.hidden=+f.getAttribute('data-step')!==n;});
    $('sju-count').textContent='Step '+n+' of 4';
    root.querySelectorAll('.sju-prog li').forEach(function(li,i){li.classList.toggle('is-on',i<n);});
    $('sju-back').hidden=n===1;
    $('sju-next').textContent=n===4?'See my results':'Continue';
    hint('');
  }
  $('sju-next').addEventListener('click',function(){
    var msg=valid(st.step);
    if(msg){hint(msg);return;}
    if(st.step<4){showStep(st.step+1);var f=root.querySelector('[data-step="'+st.step+'"] select, [data-step="'+st.step+'"] input, [data-step="'+st.step+'"] button');if(f){f.focus();}return;}
    finish(true);
  });
  $('sju-back').addEventListener('click',function(){if(st.step>1){showStep(st.step-1);}});
  $('sju-edit').addEventListener('click',function(){
    $('sju-done').hidden=true;$('sju-quiz').hidden=false;showStep(1);
    $('sju-tool').scrollIntoView({behavior:'smooth',block:'start'});
  });
  $('sju-reset').addEventListener('click',function(){
    st=fresh();save();syncInputs();
    $('sju-done').hidden=true;$('sju-quiz').hidden=false;$('sju-result').hidden=true;showStep(1);
    $('sju-tool').scrollIntoView({behavior:'smooth',block:'start'});
  });

  /* ---------- Results ---------- */
  function nextDate(u){
    var up=u.dates.filter(function(d){return daysTo(d.d)>=0;});
    return up[0]||null;
  }
  function calLink(u,d){
    var dt=d.d.replace(/-/g,''),nx=parseDate(d.d);nx.setDate(nx.getDate()+1);
    var end=nx.getFullYear()+('0'+(nx.getMonth()+1)).slice(-2)+('0'+nx.getDate()).slice(-2);
    return 'https://calendar.google.com/calendar/render?action=TEMPLATE&text='+encodeURIComponent(u.short+': '+d.t)+'&dates='+dt+'/'+end+'&details='+encodeURIComponent('Check the official page: '+u.url);
  }
  function satLine(u,p){
    var s=+st.sat;if(!s){return '';}
    var biz=p.areas.some(function(a){return ['business','econ','soc'].indexOf(a)>-1;});
    if(u.id==='lums'){return 'Your SAT '+s+' can be your LUMS test. LUMS publishes no minimum.';}
    if(u.id==='iba'){return 'SAT '+s+': IBA ranks SAT scorers, and only the top get direct admission or an interview. Sit the aptitude test too.';}
    if(u.id==='nust'){return biz?'NUST SAT route: 550 or more in each section, applications 20 April to 25 July 2027.':'This NUST programme takes ACT (25+, Science 25+), not SAT.';}
    if(u.id==='fast'){return 'FAST accepts your SAT in place of its own test.';}
    if(u.id==='szabist'){return s>=1100?'Your SAT '+s+' can replace the SZABIST test.':'SZABIST needs SAT 1100 or more to replace its test.';}
    if(u.id==='pieas'){return 'PIEAS takes SAT II or ACT, not the SAT.';}
    return '';
  }
  function timeLine(u,status){
    if(u.id==='lums'&&st.time==='done'&&status!=='yes'){return 'You have finished A Levels: only October/November 2026 resits can fix this for Fall 2027.';}
    if(u.id==='lums'&&st.time==='jun27'&&status!=='yes'){return 'If these are predicted grades, you can still apply; LUMS confirms the offer when your results arrive.';}
    if(u.id==='aku'){return 'AS grades do not count, and A Level results must reach AKU by mid-August.';}
    if(u.id==='toronto'){return 'U of T publishes no minimum grades. Popular programmes admit students well above any floor.';}
    if(u.id==='uet'){return 'Outside Punjab and Islamabad? You apply under the AP1 or AP2 categories, not open merit A1 or A2.';}
    if(u.id==='manchester'&&status==='yes'){return 'Grades shown are the typical offer. Manchester also reads your personal statement and reference.';}
    if(u.id==='mdcat'&&st.time!=='done'){return 'You apply after results, once you hold IBCC Pre-Medical equivalence.';}
    return '';
  }
  function meritBlock(u,p,P){
    var w=p.merit_w||u.merit_w;if(!w){return '';}
    var acad=(w.ol||0)*P.olPct/100+(w.hssc||0)*P.hssc/100,room=100-w.test;
    var tn=u.test_name||'test';
    return '<div class="sju-merit" data-test="'+w.test+'" data-acad="'+acad.toFixed(2)+'" data-min="'+(u.min_test||0)+'">'+
      '<p class="sj-small">'+esc(p.merit_formula||u.merit_formula)+'</p>'+
      '<p>Your grades give you about <b>'+acad.toFixed(1)+' of '+room+'</b> points. The other '+w.test+' come from the '+esc(tn)+'.</p>'+
      '<label>Expected '+esc(tn)+' score <input class="sj-input" type="number" inputmode="numeric" min="0" max="100" placeholder="%" aria-label="Expected '+esc(tn)+' score in percent"> %</label>'+
      '<p class="sju-out" aria-live="polite"></p></div>';
  }
  function card(row,P){
    var u=row.u,p=row.p,on=st.short.indexOf(p.id)>-1;
    var shown=row.status==='no'?row.checks.filter(function(c){return !c.ok;}):row.checks;
    var checks=shown.map(function(c){return '<li class="'+(c.ok?'is-ok':'is-no')+'">'+(c.ok?TICK:CROSS)+'<span>'+esc(c.t)+'</span></li>';}).join('');
    var nd=nextDate(u);
    var next=nd?'<b>'+esc(nd.t)+'</b>: '+fmt(nd.d)+' <span class="sju-tag">'+left(daysTo(nd.d))+'</span>':esc(u.expected);
    var extra=[satLine(u,p),timeLine(u,row.status)].filter(Boolean).map(function(t){return '<p class="sj-small">'+esc(t)+'</p>';}).join('');
    var notes=u.notes.map(function(n){return '<p>'+esc(n)+'</p>';}).join('');
    return '<article class="sj-card sju-card" data-id="'+p.id+'">'+
      '<div class="sju-top"><div><p class="sj-caption">'+esc(u.short)+' &middot; '+esc(u.city)+'</p><h3 class="sj-h4">'+esc(p.name)+'</h3></div>'+
      '<button type="button" class="sju-star" data-star="'+p.id+'" aria-pressed="'+(on?'true':'false')+'">'+(on?'\u2605 Shortlisted':'\u2606 Shortlist')+'</button></div>'+
      (row.status==='yes'?'<p><span class="sj-stamp-box">Meets minimum</span></p>':'')+
      '<ul class="sj-ticks sju-checks">'+checks+'</ul>'+
      (row.status!=='no'?'<dl class="sju-dl"><div><dt>Test</dt><dd>'+esc(p.test||u.test)+'</dd></div><div><dt>Next date</dt><dd>'+next+'</dd></div></dl>'+meritBlock(u,p,P):'')+
      extra+
      '<details class="sju-more"><summary>Fees, notes and official page</summary><div><p><b>How seats are decided:</b> '+esc(u.merit)+'</p><p><b>Fees:</b> '+esc(u.fee)+'</p>'+notes+
      '<p><a class="sj-link sj-link-go" href="'+esc(u.url)+'" target="_blank" rel="noopener">Official '+esc(u.short)+' page</a></p></div></details>'+
      '</article>';
  }
  function empty(text){return '<div class="sj-empty"><b>Nothing here</b><p>'+esc(text)+'</p></div>';}

  var last=null;
  function render(){
    var res=run(st),P=res.P;last=res;
    var buckets={yes:[],close:[],no:[]};
    res.rows.forEach(function(r){buckets[r.status].push(r);});
    $('sju-p1').innerHTML=buckets.yes.length?'<div class="sju-list">'+buckets.yes.map(function(r){return card(r,P);}).join('')+'</div>':empty('No programme in your areas matches these grades yet. Check the other two tabs for what to change.');
    $('sju-p2').innerHTML=buckets.close.length?'<div class="sju-list">'+buckets.close.map(function(r){return card(r,P);}).join('')+'</div>':empty('Nothing waiting on better grades.');
    $('sju-p3').innerHTML=buckets.no.length?'<p class="sj-small sj-muted" style="margin-bottom:16px">These need a subject you are not taking, or an O Level record that is already fixed.</p><div class="sju-list">'+buckets.no.map(function(r){return card(r,P);}).join('')+'</div>':empty('Your subjects fit every programme in your areas.');
    $('sju-n1').textContent='\u00a0('+buckets.yes.length+')';$('sju-n2').textContent='\u00a0('+buckets.close.length+')';$('sju-n3').textContent='\u00a0('+buckets.no.length+')';
    $('sju-stamp').textContent=buckets.yes.length;
    var areas=st.areas.indexOf('all')>-1||!st.areas.length?'every area':st.areas.map(function(a){return AREA[a].charAt(0).toLowerCase()+AREA[a].slice(1);}).join('; ');
    $('sju-lede').textContent='You meet the published minimum for '+buckets.yes.length+' of '+res.rows.length+' programmes in '+areas+(st.city&&st.city!=='any'?({karachi:', in Karachi',lahore:', in Lahore',islamabad:', around Islamabad',abroad:', abroad'})[st.city]:'')+'.';
    var top=P.a.slice().sort(function(x,y){return PTS[y.g]-PTS[x.g];}).slice(0,3).map(function(x){return x.g;}).join(' ');
    $('sju-nums').innerHTML='<div><b>'+esc(top)+'</b>Your best three A Levels</div>'+
      '<div><b>~'+Math.round(P.olPct)+'%</b>O Level (SSC) equivalence</div>'+
      '<div><b>~'+Math.round(P.hssc)+'%</b>HSSC equivalence estimate</div>';
    /* Unlock tip */
    var un=unlock(st,res),box=$('sju-unlock');
    if(un){
      var names=un.list.slice(0,4).map(function(r){return r.u.short+' '+r.p.name.split(' (')[0];});
      var more=un.list.length>4?' and '+(un.list.length-4)+' more':'';
      var lead=un.steps[0],change=un.steps.map(function(x){return SUB[x.sub]+' from '+x.from+' to '+x.to;}).join(' and ');
      var teach=TEACH.hasOwnProperty(lead.sub);
      var waText='Hi SJ Academy, I used the university admissions tool. I want to raise my A Level '+change+'.\nI\'d like to book a free demo class.\nMode (in class or online): \n(Ref: TL-UNI)\nMy name is ';
      box.innerHTML='<div class="sj-alert sj-alert-deadline"><b>Your highest-value '+(un.steps.length>1||lead.to!==GR[PTS[lead.from]+1]?'grades':'grade')+': '+esc(change)+'</b>'+
        '<p>That opens '+un.list.length+' more programme'+(un.list.length>1?'s':'')+': '+esc(names.join(', ')+more)+'.</p>'+
        (teach?'<p class="sj-row" style="margin-top:8px"><a class="sj-btn sj-btn-wa sj-btn-sm" href="'+WA+encodeURIComponent(waText)+'" target="_blank" rel="noopener" data-loc="unlock">Free '+esc(SUB[lead.sub])+' demo</a>'+(TEACH[lead.sub]?'<a class="sj-link sj-link-go" href="https://www.sjacademy.pk'+TEACH[lead.sub]+'">A Level '+esc(SUB[lead.sub])+' classes</a>':'')+'</p>':'')+
        '</div>';
    }else{box.innerHTML='';}
    drawShort();
    drawSummary(P);
    setWA();
  }
  function setWA(){
    var gradeLine=last.P.a.map(function(r){return SUB[r.s]+' '+r.g;}).join(', ');
    var shortNames=shortRows().map(function(r){return r.u.short+' '+r.p.name.split(' (')[0];});
    $('sju-wa').href=WA+encodeURIComponent('Hi SJ Academy, I used the university admissions tool.\nMy A Levels: '+gradeLine+'\n'+(shortNames.length?'My shortlist: '+shortNames.join('; ')+'\n':'')+'I\'d like advice on my plan and a free demo class.\nSubject: \n(Ref: TL-UNI)\nMy name is ');
  }
  function shortRows(){
    if(!last){return [];}
    var out=[];
    D.unis.forEach(function(u){u.progs.forEach(function(p){if(st.short.indexOf(p.id)>-1){out.push({u:u,p:p});}});});
    return out;
  }
  function drawShort(){
    var rows=shortRows(),body=$('sju-short-body');
    if(!rows.length){
      body.innerHTML='<div class="sj-empty"><b>No shortlist yet</b><p>Tap Shortlist on any programme above. Its deadlines land here, with a reminder link for your calendar.</p></div>';
      $('sju-share').hidden=true;return;
    }
    var unis=[],seen={};rows.forEach(function(r){if(!seen[r.u.id]){seen[r.u.id]=1;unis.push(r.u);}});
    var items=[];unis.forEach(function(u){u.dates.forEach(function(d){if(daysTo(d.d)>=0){items.push({u:u,d:d});}});});
    items.sort(function(x,y){return x.d.d<y.d.d?-1:1;});
    var tickets=items.map(function(it){var dd=parseDate(it.d.d);
      return '<li class="sj-ticket"><div class="sj-ticket-stub"><b>'+dd.getDate()+'</b>'+MON[dd.getMonth()]+' '+dd.getFullYear()+'</div><div class="sj-ticket-body"><b>'+esc(it.u.short)+'</b><span>'+esc(it.d.t)+'</span><span class="sju-left">'+left(daysTo(it.d.d))+'</span><span><a class="sj-link" href="'+calLink(it.u,it.d)+'" target="_blank" rel="noopener" data-event="calendar_add" data-loc="shortlist">Add to calendar</a></span></div></li>';}).join('');
    var later=unis.filter(function(u){return !u.dates.some(function(d){return daysTo(d.d)>=0;});}).map(function(u){return '<li>'+TICK+'<span><b>'+esc(u.short)+':</b> '+esc(u.expected)+'</span></li>';}).join('');
    var progs='<p class="sj-small">'+rows.length+' programme'+(rows.length>1?'s':'')+': '+esc(rows.map(function(r){return r.u.short+' '+r.p.name.split(' (')[0];}).join('; '))+'</p>';
    body.innerHTML=progs+(tickets?'<ol class="sju-tickets">'+tickets+'</ol>':'')+(later?'<ul class="sj-ticks" style="margin-top:16px">'+later+'</ul>':'');
    var txt='My university shortlist:\n'+rows.map(function(r){return '- '+r.u.short+' '+r.p.name.split(' (')[0];}).join('\n')+
      (items.length?'\n\nDeadlines:\n'+items.slice(0,8).map(function(it){return '- '+fmt(it.d.d)+': '+it.u.short+', '+it.d.t;}).join('\n'):'')+
      '\n\nMade with the free SJ Academy admissions checker: https://www.sjacademy.pk/university-admission-criteria-tool/';
    $('sju-share').href='https://wa.me/?text='+encodeURIComponent(txt);$('sju-share').hidden=false;
  }
  function drawSummary(P){
    var areas=st.areas.indexOf('all')>-1?'Everything':st.areas.map(function(a){return AREA[a];}).join(', ');
    var o=GRADES.filter(function(g){return +st.o[g];}).map(function(g){return st.o[g]+' '+g;}).join(', ');
    $('sju-sum').innerHTML='<div><dt>A Levels</dt><dd>'+esc(P.a.map(function(r){return SUB[r.s]+' '+r.g;}).join(', '))+'</dd></div>'+
      '<div><dt>O Levels</dt><dd>'+esc(o)+'</dd></div><div><dt>Studying</dt><dd>'+esc(areas)+'</dd></div>';
  }
  function finish(scroll){
    try{
      st.done=true;if(scroll){st.mode='grades';}save();render();
      $('sju-quiz').hidden=true;$('sju-done').hidden=false;$('sju-result').hidden=st.mode!=='grades';$('sju-err').hidden=true;
      if(scroll){$('sju-rh').scrollIntoView({behavior:'smooth',block:'start'});$('sju-rh').focus({preventScroll:true});send('tool_complete','tool');}
    }catch(err){$('sju-err').hidden=false;if(window.console){console.error(err);}}
  }

  /* Delegated events inside results: shortlist and merit inputs */
  $('sju-result').addEventListener('click',function(e){
    var b=e.target.closest?e.target.closest('[data-star]'):null;if(!b){return;}
    var id=b.getAttribute('data-star'),i=st.short.indexOf(id);
    if(i>-1){st.short.splice(i,1);}else{st.short.push(id);send('shortlist_add','result');}
    save();
    root.querySelectorAll('[data-star="'+id+'"]').forEach(function(x){var on=st.short.indexOf(id)>-1;x.setAttribute('aria-pressed',on?'true':'false');x.textContent=on?'\u2605 Shortlisted':'\u2606 Shortlist';});
    drawShort();setWA();
  });
  $('sju-result').addEventListener('input',function(e){
    var inp=e.target;if(!inp.closest){return;}var m=inp.closest('.sju-merit');if(!m){return;}
    var out=m.querySelector('.sju-out'),t=parseFloat(inp.value);
    if(isNaN(t)){out.textContent='';return;}
    t=Math.max(0,Math.min(100,t));
    var agg=+m.getAttribute('data-acad')+(+m.getAttribute('data-test'))*t/100,min=+m.getAttribute('data-min');
    out.innerHTML='Estimated aggregate: <b>'+agg.toFixed(1)+'%</b>'+(min&&t<min?'. Below the '+min+'% test pass mark, so this would not qualify.':'. Compare it with last year&rsquo;s closing merit on the official site.');
  });


  /* ---------- Look up a university ---------- */
  var uniSel=$('sju-uni'),progSel=$('sju-prog'),lookOut=$('sju-look-out');
  var findUni=function(id){return D.unis.filter(function(u){return u.id===id;})[0]||null;};
  function setMode(m,focus){
    st.mode=m;save();
    $('sju-m-look').setAttribute('aria-pressed',m==='look'?'true':'false');
    $('sju-m-grades').setAttribute('aria-pressed',m==='grades'?'true':'false');
    $('sju-look').hidden=m!=='look';$('sju-grades').hidden=m!=='grades';
    $('sju-result').hidden=!(m==='grades'&&st.done);
    if(focus){var f=m==='look'?uniSel:root.querySelector('#sju-grades select, #sju-grades button');if(f){f.focus();}}
  }
  $('sju-m-look').addEventListener('click',function(){setMode('look',true);});
  $('sju-m-grades').addEventListener('click',function(){setMode('grades',true);});
  function fillProgs(u){
    progSel.innerHTML='<option value="">All programmes</option>'+(u?u.progs.map(function(p){return '<option value="'+p.id+'">'+esc(p.name)+'</option>';}).join(''):'');
    progSel.disabled=!u;
    progSel.value=u&&u.progs.some(function(p){return p.id===st.prog;})?st.prog:'';
  }
  function drawLook(){
    var u=findUni(st.uni);
    uniSel.value=u?u.id:'';fillProgs(u);
    if(!u){lookOut.innerHTML='<p class="sj-help">Choose a university to see its criteria here.</p>';return;}
    var p=u.progs.filter(function(x){return x.id===progSel.value;})[0]||null;
    var nd=nextDate(u);
    var next=nd?'<b>'+esc(nd.t)+'</b>: '+fmt(nd.d)+' <span class="sju-tag">'+left(daysTo(nd.d))+'</span>':esc(u.expected);
    var w=(p&&p.merit_w)||u.merit_w||(u.progs.length===1&&u.progs[0].merit_w)||null;
    var calc='';
    if(w){
      var tn=u.test_name||'test';
      calc='<div class="sju-merit sju-lcalc" data-w=\''+JSON.stringify(w)+'\' data-min="'+(u.min_test||0)+'">'+
        '<p class="sj-small"><b>Aggregate calculator:</b> '+esc((p&&p.merit_formula)||u.merit_formula||'')+'</p>'+
        '<label>'+esc(tn)+' score <input class="sj-input" type="number" inputmode="numeric" min="0" max="100" data-k="test" placeholder="%" aria-label="'+esc(tn)+' score in percent"> %</label>'+
        '<label>O Level equivalence <input class="sj-input" type="number" inputmode="numeric" min="0" max="100" data-k="ol" placeholder="%" aria-label="O Level equivalence in percent"> %</label>'+
        (w.hssc?'<label>HSSC equivalence <input class="sj-input" type="number" inputmode="numeric" min="0" max="100" data-k="hssc" placeholder="%" aria-label="HSSC equivalence in percent"> %</label>':'')+
        '<p class="sju-out" aria-live="polite"></p>'+
        '<p class="sj-small">Not sure of your equivalence? <a class="sj-link" href="https://www.sjacademy.pk/ibcc-equivalence-calculator/">Work it out with our IBCC calculator</a>.</p></div>';
    }
    lookOut.innerHTML='<div class="sj-stack">'+
      '<h2 class="sj-h3">'+esc(u.short)+(p?' '+esc(p.name.split(' (')[0]):'')+' admission criteria</h2>'+
      '<dl class="sju-dl">'+
        '<div><dt>A Level minimum</dt><dd>'+esc(u.glance_grades)+'</dd></div>'+
        '<div><dt>'+(p?'This programme':'Subjects')+'</dt><dd>'+esc(p?p.desc:u.glance_subjects)+'</dd></div>'+
        '<div><dt>Admission test</dt><dd>'+esc((p&&p.test)||u.test)+'</dd></div>'+
        '<div><dt>How seats are decided</dt><dd>'+esc(u.merit)+'</dd></div>'+
        '<div><dt>Next date</dt><dd>'+next+'</dd></div>'+
        '<div><dt>Fees</dt><dd>'+esc(u.fee)+'</dd></div>'+
      '</dl>'+calc+
      '<div class="sj-row"><button type="button" class="sj-btn sj-btn-primary" id="sju-look-go" data-event="lookup_to_grades" data-loc="lookup">Check my grades</button>'+
      '<a class="sj-link sj-link-go" href="#sju-unis" id="sju-look-full">All '+esc(u.short)+' programmes and dates</a></div>'+
      '</div>';
  }
  function setUrl(id){try{var q=new URL(location.href);if(id){q.searchParams.set('uni',id);}else{q.searchParams.delete('uni');}history.replaceState(null,'',q.toString());}catch(err){}}
  uniSel.addEventListener('change',function(){st.uni=this.value;st.prog='';save();drawLook();setUrl(st.uni);send('university_lookup','hero');});
  progSel.addEventListener('change',function(){st.prog=this.value;save();drawLook();});
  function openTab(id){
    var t=$('sju-tab-'+id);if(!t){return;}
    t.parentNode.querySelectorAll('[role="tab"]').forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on?'true':'false');x.tabIndex=on?0:-1;var pn=$(x.getAttribute('aria-controls'));if(pn){pn.hidden=!on;}});
  }
  lookOut.addEventListener('click',function(e){
    var t=e.target;
    if(t.id==='sju-look-go'){setMode('grades',true);$('sju-tool').scrollIntoView({behavior:'smooth',block:'start'});}
    if(t.id==='sju-look-full'){e.preventDefault();openTab(st.uni);$('sju-unis').scrollIntoView({behavior:'smooth',block:'start'});}
  });
  lookOut.addEventListener('input',function(e){
    var m=e.target.closest?e.target.closest('.sju-lcalc'):null;if(!m){return;}
    var w=JSON.parse(m.getAttribute('data-w')),v={},miss=false;
    m.querySelectorAll('input[data-k]').forEach(function(i){var x=parseFloat(i.value);if(isNaN(x)){miss=true;}v[i.getAttribute('data-k')]=Math.max(0,Math.min(100,x));});
    var out=m.querySelector('.sju-out');
    if(miss){out.textContent='';return;}
    var agg=w.test*v.test/100+(w.ol||0)*v.ol/100+(w.hssc||0)*(v.hssc||0)/100,min=+m.getAttribute('data-min');
    out.innerHTML='Your aggregate: <b>'+agg.toFixed(2)+'%</b>'+(min&&v.test<min?'. Below the '+min+'% test pass mark, so this would not qualify.':'');
  });

  /* ---------- Static calendar: days left, past dates hidden ---------- */
  var cal=$('sju-cal');
  if(cal){
    var shown=0;
    cal.querySelectorAll('[data-date]').forEach(function(li){
      var n=daysTo(li.getAttribute('data-date'));
      if(n<0){li.hidden=true;return;}
      shown++;li.querySelector('.sju-left').textContent=left(n);
      if(shown>6){li.hidden=true;li.setAttribute('data-more','1');}
    });
    if(!shown){cal.hidden=true;$('sju-cal-empty').hidden=false;}
    if(shown>6){var mb=$('sju-cal-more');mb.hidden=false;mb.textContent='Show all '+shown+' dates';
      mb.addEventListener('click',function(){cal.querySelectorAll('[data-more]').forEach(function(li){li.hidden=false;});mb.hidden=true;});}
  }

  /* ---------- Start ---------- */
  syncInputs();
  var qs=null;try{qs=new URLSearchParams(location.search).get('uni');}catch(err){}
  if(qs&&findUni(qs)){st.uni=qs;st.prog='';st.mode='look';}
  drawLook();
  if(st.done&&valid(1)===''&&valid(2)===''&&valid(3)===''){finish(false);}
  else{st.done=false;showStep(st.step&&st.step<=4?st.step:1);}
  setMode(st.mode==='grades'?'grades':'look',false);
  if(qs&&findUni(qs)){openTab(qs);}
})();
