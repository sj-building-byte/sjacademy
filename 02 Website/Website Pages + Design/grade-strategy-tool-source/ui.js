/* Grade strategy tool UI. Needs window.SJG (engine) and window.SJG_DATA. Every id starts with sjg-. */
(function(){
  var root=document.getElementById('sj');
  if(!root||!root.classList.contains('sj-p-grade-strategy')||!window.SJG||!window.SJG_DATA){return;}
  var E=window.SJG,D=window.SJG_DATA,$=function(id){return document.getElementById(id);};
  var G=E.G,KEYS=D.sessions.map(function(s){return s.k;});
  var PAGE='https://www.sjacademy.pk/a-level-grade-strategy-tool/';
  var WA='https://wa.me/923362144454?text=';
  var LS='sjg-v1';
  var POS={a:[83,89,96],b:[72,75,78],c:[62,65,68],d:[52,55,58],e:[42,45,48],u:[18,28,36]};
  var today=new Date();

  /* ---------- Sessions the visitor can pick: loaded ones, plus any newer series whose results are out ---------- */
  var SESS=D.sessions.map(function(s){return {k:s.k,label:s.label,y:s.y,m:s.m,known:true};});
  (function(){
    var n=E.nextSeries({y:SESS[0].y,m:SESS[0].m});
    while(E.resultsDay(n)<=today){
      SESS.unshift({k:(n.m===6?'s':'w')+String(n.y).slice(2),label:E.seriesLabel(n),y:n.y,m:n.m,known:false});
      n=E.nextSeries(n);
    }
  })();

  var st={code:'9709',route:0,sat:SESS[0].k,mode:'pum',pum:75,grade:'b',pos:1,target:1,wi:null};

  /* ---------- Restore: link parameters first, then this browser's last answers ---------- */
  try{var saved=JSON.parse(localStorage.getItem(LS)||'null');if(saved&&saved.code){for(var k in saved){if(k in st&&k!=='wi'){st[k]=saved[k];}}}}catch(e){}
  try{
    var q=new URLSearchParams(location.search);
    if(q.get('s')){st.code=q.get('s');st.route=0;}
    if(q.get('r')){st.route=parseInt(q.get('r'),10)||0;}
    if(q.get('x')){st.sat=q.get('x');}
    if(q.get('p')){st.mode='pum';st.pum=parseInt(q.get('p'),10);}
    if(q.get('t')){var ti=G.indexOf(q.get('t').replace(' ','*').toUpperCase());if(ti>-1){st.target=ti;}}
  }catch(e){}
  var subj=function(){for(var i=0;i<D.subjects.length;i++){if(D.subjects[i].code===st.code){return D.subjects[i];}}return null;};
  if(!subj()){st.code=D.subjects[0].code;}
  if(!(st.route>=0&&st.route<subj().routes.length)){st.route=0;}
  if(!SESS.some(function(s){return s.k===st.sat;})){st.sat=SESS[0].k;}
  if(!(st.pum>=0&&st.pum<=100)){st.pum=75;}
  if(!(st.target>=0&&st.target<6)){st.target=1;}

  /* ---------- Build the inputs ---------- */
  var sel=$('sjg-subj');
  D.subjects.forEach(function(s){var o=document.createElement('option');o.value=s.code;o.textContent=s.name+' ('+s.code+')';sel.appendChild(o);});
  var satSel=$('sjg-sat');
  SESS.forEach(function(s){var o=document.createElement('option');o.value=s.k;o.textContent=s.label+(s.known?'':' (estimate)');satSel.appendChild(o);});
  function fillRoutes(){
    var rs=subj().routes,r=$('sjg-route');r.innerHTML='';
    rs.forEach(function(x,i){var o=document.createElement('option');o.value=i;o.textContent=x.label;r.appendChild(o);});
    $('sjg-route-f').hidden=rs.length<2;
    r.value=st.route;
  }

  /* ---------- Helpers ---------- */
  var up=function(x){return Math.max(0,Math.ceil(x-1e-9));};
  var rng=function(s,max){var lo=up(s.lo),hi=up(s.hi);if(max&&hi>max){hi=max;}return lo===hi?String(lo):lo+'&ndash;'+hi;};
  var paren=function(s,max){var t=rng(s,max);return t.indexOf('&ndash;')<0?'':' <span class="sj-muted">('+t+')</span>';};
  var pumNow=function(){return st.mode==='pum'?st.pum:POS[st.grade][st.pos];};
  var STD=['A*','A','B','C','D','E'];
  function standard(L){
    if(L===7){return 'no A2 marks at all';}
    if(L===-1){return 'more than the papers are worth';}
    if(L===6){return 'less than E-grade standard on the A2 papers';}
    return (L===0?'A*':STD[L])+'-grade standard on the A2 papers';
  }
  function asIdx(g){return {a:1,b:2,c:3,d:4,e:5,u:6}[g];}
  function satInfo(){for(var i=0;i<SESS.length;i++){if(SESS[i].k===st.sat){return SESS[i];}}return SESS[0];}

  /* ---------- Main render ---------- */
  function render(){
    var S=subj(),R=S.routes[st.route],p=pumNow(),gi=st.target,tg=G[gi];
    var o=E.calc({route:R,keys:KEYS,satKey:st.sat,pum:p,target:gi});
    var c=o.carry[gi],need=up(c.mid),L=o.level(c.mid),ag=o.asGrade,si=satInfo();
    var wins=E.windows({y:si.y,m:si.m},today);
    var impossible=c.lo>R.a2Max,shaky=!impossible&&c.hi>R.a2Max,over=!impossible&&up(c.mid)>R.a2Max;
    var jump=(L===7)?-9:(L===-1?9:asIdx(ag)-L);
    var pct=Math.round(need/R.a2Max*100);

    /* readouts */
    $('sjg-pum-g').textContent='= AS grade '+ag;

    /* verdict */
    var v;
    if(!wins.length){v={k:'fresh',t:'Start again: all papers in one series',c:'sj-alert-deadline'};}
    else if(L===7){v={k:'keep',t:'Keep your AS. It has already done the work',c:'sj-alert-ok'};}
    else if(impossible){v={k:'resit',t:'Re-sit AS. Keeping it cannot reach '+tg,c:'sj-alert-err'};}
    else if(over){v={k:'resit',t:'Re-sit AS. Keeping it makes '+tg+' a long shot',c:'sj-alert-err'};}
    else if(shaky||jump>=2){v={k:'resit',t:'Re-sit AS too, or aim one grade lower',c:'sj-alert-deadline'};}
    else if(jump===1){v={k:'keep',t:'Keep your AS, and plan for a stretch',c:'sj-alert-deadline'};}
    else{v={k:'keep',t:'Keep your AS. This is realistic',c:'sj-alert-ok'};}

    /* quick answer in the tool card */
    var head;
    if(!wins.length){head='Your '+si.label+' AS can&rsquo;t be carried forward any more, so you&rsquo;d sit all papers again and need about <b>'+up(o.fresh[gi].mid)+' out of '+o.tot+'</b> overall for '+tg+'.';}
    else if(L===7){head='Your AS already covers an overall '+tg+'. You still have to sit the A2 papers, but any mark gets you there.';}
    else if(impossible){head='Keeping this AS, even full marks in A2 wouldn&rsquo;t reach an overall '+tg+'. Re-sitting AS is the way.';}
    else if(over){head='Keeping this AS, an overall '+tg+' only works in an easy series: at least <b>'+up(c.lo)+' out of '+R.a2Max+'</b> in A2. Re-sitting AS is safer.';}
    else{head='Keep your AS and you need about <b>'+need+' out of '+R.a2Max+'</b> in A2 ('+pct+'%) for an overall '+tg+'.';}
    $('sjg-stamp').textContent=tg;
    $('sjg-head').innerHTML=head;
    $('sjg-verdict').textContent=v.t+'.';

    /* summary line */
    $('sjg-sum').innerHTML='<b>'+S.name+' ('+S.code+')</b>. AS grade '+ag+', PUM '+Math.round(p)+(st.mode==='grade'?' (estimated from your grade)':'')+', '+si.label+'. That is about <b>'+o.M.toFixed(0)+' of '+R.asMax+'</b> weighted AS marks. Target: <b>'+tg+'</b>.'+
      (si.known?'':' <span class="sj-muted">Cambridge&rsquo;s '+si.label+' thresholds are not in the tool yet, so your AS mark is estimated from earlier series.</span>');

    /* recommendation */
    var why='';
    var lvlTxt=standard(L);
    if(v.k==='fresh'){
      why='Your AS can only count for 13 months. By the next series you can still enter, your '+si.label+' AS has expired, so plan for all '+(R.asPapers.length+R.a2Papers.length)+' papers in one series.';
    }else if(L===7){
      why='Your AS mark is high enough that the A Level threshold for '+tg+' is already covered. Use A2 to push for the grade above.';
    }else if(impossible||over){
      why=impossible?'You would need '+up(c.lo)+' out of '+R.a2Max+' in A2, and the papers are only worth '+R.a2Max+'. Re-sitting AS raises the marks you carry in.':'In two of the last three series you would have needed more than full marks in A2. Re-sitting AS raises the marks you carry in.';
    }else{
      why='You need '+lvlTxt+'. Your AS was a grade '+ag+'. '+
        (jump<=0?'That is the standard you have already shown, so carrying forward makes sense.':
         jump===1?'That is one grade above your AS standard: doable with serious past-paper practice, so have a plan B.':
         'That is '+(jump>=9?'beyond':jump+' grades above')+' your AS standard. Re-sitting AS lowers the A2 marks you need (see the table), at the cost of more papers in one series.');
    }
    $('sjg-rec').className='sj-alert '+v.c;
    $('sjg-rec').innerHTML='<b>'+v.t+'</b><p>'+why+'</p>';

    /* card 1: keep AS */
    var c1=$('sjg-c1');
    c1.classList.toggle('sj-tagged',v.k==='keep');
    var winTxt=wins.length?'Series you can still use: <b>'+wins.map(function(w){return w.label;}).join(' or ')+'</b>.'+(wins[0].soon?' Entries for '+wins[0].label+' may be closing: check with your school or the British Council now.':' Book your entry early.'):'Your '+si.label+' AS has passed the 13-month limit for every series still open, so this route is closed.';
    var split='';
    if(!impossible&&!over&&L!==7){
      var f=Math.min(1,need/R.a2Max);
      split='<p class="sj-small">For example: '+R.a2Papers.map(function(pp){return Math.min(pp[2],Math.ceil(f*pp[2]-1e-9))+'/'+pp[2]+' on '+(pp[0].indexOf('Paper')===0?pp[0]:pp[0]+' '+pp[1]);}).join(' and ')+'.</p>';
    }
    c1.querySelector('.sjg-body').innerHTML=!wins.length?'<p class="sjg-big">Closed</p><p class="sj-small">'+winTxt+'</p>':
      (v.k==='keep'?'<span class="sj-tag">best fit</span>':'')+
      (impossible?'<p class="sjg-big">Not possible</p><p>You would need '+up(c.lo)+' out of '+R.a2Max+'.</p>':over?'<p class="sjg-big">'+up(c.lo)+'+</p><p class="sj-small">Only in the easiest recent series. In the others you would need more than '+R.a2Max+'.</p>':
       L===7?'<p class="sjg-big">0</p><p>Your AS already covers '+tg+'.</p>':
       '<p><span class="sjg-big">'+need+'</span> <span class="sjg-of">out of '+R.a2Max+' ('+pct+'%)</span></p>'+
       '<p class="sj-small sj-muted">'+(up(c.lo)===up(c.hi)?'The same in all three recent series.':rng(c,R.a2Max+1)+' across the last three series. Boundaries move.')+'</p>'+
       '<p>That is '+lvlTxt+'.</p>'+split)+
      '<p class="sj-small">'+winTxt+'</p>';

    /* what-if slider */
    var wi=$('sjg-wi');
    wi.max=Math.round(R.a2Max);
    if(st.wi===null||st.wi>R.a2Max){st.wi=Math.min(Math.round(R.a2Max),Math.max(0,need||Math.round(R.a2Max*.6)));}
    wi.value=st.wi;
    c1.querySelector('.sjg-wi').hidden=!wins.length||impossible;
    whatIf(o,R);

    /* card 2: re-sit AS */
    var rows='',levels=[[90,'a (PUM 90)'],[80,'a (PUM 80)'],[70,'b (PUM 70)'],[60,'c (PUM 60)'],[50,'d (PUM 50)']];
    levels.forEach(function(x){
      if(x[0]<=p+0.5){return;}
      var r=o.resit(x[0],gi),nn=up(r.mid),ll=o.level(r.mid);
      var cell='<span>'+(r.lo>R.a2Max?'Not possible':up(r.mid)>R.a2Max?up(r.lo)+'+ (easy series only)':(ll===7?'0':nn+paren(r,R.a2Max)))+'</span>';
      rows+='<tr><td data-label="AS re-sit result">'+x[1]+'</td><td data-label="A2 marks needed" class="sj-num">'+cell+'</td></tr>';
    });
    var keepCell='<span>'+(impossible?'Not possible':over?up(c.lo)+'+ (easy series only)':(L===7?'0':need+paren(c,R.a2Max)))+'</span>';
    rows+='<tr class="is-key"><td data-label="AS re-sit result">Keep your '+ag+' (PUM '+Math.round(p)+')</td><td data-label="A2 marks needed" class="sj-num">'+keepCell+'</td></tr>';
    $('sjg-c2').classList.toggle('sj-tagged',v.k==='resit');
    $('sjg-c2-tag').hidden=v.k!=='resit';
    if(!wins.length){rows='<tr><td data-label="AS re-sit result" colspan="2"><span>No AS to fall back on, so a re-sit is Route 3.</span></td></tr>';}
    $('sjg-resit').innerHTML=rows;
    $('sjg-resit-max').textContent=String(R.a2Max);

    /* card 3: fresh */
    var fr=o.fresh[gi];
    $('sjg-c3').classList.toggle('sj-tagged',v.k==='fresh');
    $('sjg-c3-tag').hidden=v.k!=='fresh';
    $('sjg-fresh').innerHTML='<p><span class="sjg-big">'+up(fr.mid)+'</span> <span class="sjg-of">out of '+o.tot+' ('+Math.round(up(fr.mid)/o.tot*100)+'%)</span></p><p class="sj-small sj-muted">'+rng(fr)+' across the last three series. Roughly '+Math.round(up(fr.mid)/o.tot*100)+'% on every paper.</p>';

    /* ladder */
    var lad='';
    for(var i=0;i<6;i++){
      var ci=o.carry[i],li=o.level(ci.mid),n=up(ci.mid);
      var ov=ci.lo<=R.a2Max&&n>R.a2Max;
      var txt=ci.lo>R.a2Max?'Not possible':ov?'Easy series only':(li===7?'0':n+' of '+R.a2Max+' ('+Math.round(n/R.a2Max*100)+'%)');
      var rngTxt=(ci.lo>R.a2Max||li===7)?'&ndash;':ov?up(ci.lo)+'+':rng(ci,R.a2Max);
      lad+='<tr'+(i===gi?' class="is-key"':'')+'><td data-label="Overall grade"><b>'+G[i]+'</b></td><td data-label="A2 marks needed" class="sj-num">'+txt+'</td><td data-label="Recent range" class="sj-num">'+rngTxt+'</td><td data-label="Standard on A2">'+(li===-1?(ov?'Above A*':'Not possible'):li===7?'Already covered':(li===0?'A*':li===6?'Below E':STD[li]))+'</td></tr>';
    }
    $('sjg-ladder').innerHTML=lad;
    $('sjg-ladder-cap').textContent=S.name+', AS '+ag+' (PUM '+Math.round(p)+'), keeping your AS';

    /* links */
    var msg='Hi SJ Academy, I used the A Level grade calculator.\nSubject: '+S.name+' ('+S.code+')\nAS: '+ag+', PUM '+Math.round(p)+' ('+si.label+')\nTarget: '+tg+'\nI would like advice on my options.\n(Ref: TL-GRADE)\nMy name is ';
    $('sjg-wa').href=WA+encodeURIComponent(msg);
    var link=PAGE+'?s='+S.code+(st.route?'&r='+st.route:'')+'&x='+st.sat+'&p='+Math.round(p)+'&t='+encodeURIComponent(tg);
    $('sjg-share').href='https://wa.me/?text='+encodeURIComponent('My A Level plan for '+S.name+' (from SJ Academy’s grade calculator): '+link);

    try{localStorage.setItem(LS,JSON.stringify({code:st.code,route:st.route,sat:st.sat,mode:st.mode,pum:st.pum,grade:st.grade,pos:st.pos,target:st.target}));}catch(e){}
  }

  function whatIf(o,R){
    var s=parseInt($('sjg-wi').value,10)||0,r=o.gradeFor(s),gl=function(i){return i===6?'U':G[i];};
    $('sjg-wi-v').textContent=s+' of '+R.a2Max;
    $('sjg-wi-out').innerHTML=r.best===r.worst?'Overall grade: <b>'+gl(r.best)+'</b> in all three recent series.':'Overall grade: <b>'+gl(r.worst)+'</b> to <b>'+gl(r.best)+'</b>, depending on the series.';
  }

  /* ---------- Sync inputs with state ---------- */
  function syncInputs(){
    sel.value=st.code;fillRoutes();satSel.value=st.sat;
    $('sjg-pum').value=st.pum;$('sjg-pum-r').value=st.pum;
    var m=st.mode==='pum';
    $('sjg-m-pum').setAttribute('aria-pressed',m?'true':'false');$('sjg-m-grade').setAttribute('aria-pressed',m?'false':'true');
    $('sjg-pum-box').hidden=!m;$('sjg-grade-box').hidden=m;
    var gr=root.querySelector('input[name="sjg-grade"][value="'+st.grade+'"]');if(gr){gr.checked=true;}
    var po=root.querySelector('input[name="sjg-pos"][value="'+st.pos+'"]');if(po){po.checked=true;}
    var t=root.querySelector('input[name="sjg-tg"][value="'+st.target+'"]');if(t){t.checked=true;}
  }

  sel.addEventListener('change',function(){st.code=sel.value;st.route=0;st.wi=null;fillRoutes();render();});
  $('sjg-route').addEventListener('change',function(){st.route=parseInt(this.value,10)||0;st.wi=null;render();});
  satSel.addEventListener('change',function(){st.sat=satSel.value;render();});
  $('sjg-m-pum').addEventListener('click',function(){if(st.mode==='grade'){st.pum=POS[st.grade][st.pos];}st.mode='pum';syncInputs();render();});
  $('sjg-m-grade').addEventListener('click',function(){if(st.mode==='pum'){st.grade=E.asGradeOfPum(st.pum);st.pos=1;}st.mode='grade';syncInputs();render();});
  var setPum=function(v,from){
    v=parseInt(v,10);
    var bad=isNaN(v)||v<0||v>100;
    $('sjg-pum-f').classList.toggle('is-error',bad);
    if(bad){return;}
    st.pum=v;if(from!=='n'){$('sjg-pum').value=v;}if(from!=='r'){$('sjg-pum-r').value=v;}
    render();
  };
  $('sjg-pum').addEventListener('input',function(){setPum(this.value,'n');});
  $('sjg-pum-r').addEventListener('input',function(){setPum(this.value,'r');});
  root.addEventListener('change',function(e){
    var t=e.target;if(!t||!t.name){return;}
    if(t.name==='sjg-grade'){st.grade=t.value;render();}
    else if(t.name==='sjg-pos'){st.pos=parseInt(t.value,10);render();}
    else if(t.name==='sjg-tg'){st.target=parseInt(t.value,10);st.wi=null;render();}
  });
  $('sjg-wi').addEventListener('input',function(){
    st.wi=parseInt(this.value,10)||0;
    var S=subj(),R=S.routes[st.route];
    whatIf(E.calc({route:R,keys:KEYS,satKey:st.sat,pum:pumNow(),target:st.target}),R);
  });
  $('sjg-reset').addEventListener('click',function(){
    try{localStorage.removeItem(LS);}catch(e){}
    st={code:'9709',route:0,sat:SESS[0].k,mode:'pum',pum:75,grade:'b',pos:1,target:1,wi:null};
    syncInputs();render();
  });

  try{syncInputs();render();}
  catch(err){$('sjg-err').hidden=false;}
})();
