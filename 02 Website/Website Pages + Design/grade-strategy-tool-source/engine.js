/* SJ Academy grade strategy engine. Pure functions, no DOM. Exposed as window.SJG (or module.exports for tests). */
(function(root){
  var G=['A*','A','B','C','D','E'];
  var ASG=['a','b','c','d','e'];
  function rnd(x){return Math.floor(x+0.5);}
  /* Cambridge rule: A, B, E summed; C and D one third and two thirds from B to E (rounded down);
     A* = A plus the A-to-B gap, capped halfway between A and full marks. Returns [A*,A,B,C,D,E]. */
  function totals(as,a2,tot){
    var A=rnd(as[0]+a2[0]),B=rnd(as[1]+a2[1]),E=rnd(as[4]+a2[4]);
    var C=Math.floor(B-(B-E)/3+1e-9),D=Math.floor(B-2*(B-E)/3+1e-9);
    var S=rnd(Math.min(2*A-B,(A+tot)/2));
    return [S,A,B,C,D,E];
  }
  /* Same rule for the A2 papers alone, used only to describe the standard a mark represents. */
  function a2grades(a2,max){
    var A=a2[0],B=a2[1];
    return [Math.min(2*A-B,(A+max)/2),a2[0],a2[1],a2[2],a2[3],a2[4]];
  }
  /* PUM to weighted mark. PUM is linear between thresholds: a=80, b=70, c=60, d=50, e=40, 0=0, full marks=100. */
  function pumToMark2(p,t,max){
    p=Math.max(0,Math.min(100,p));
    if(p>=80){return t[0]+(p-80)/20*(max-t[0]);}
    if(p<40){return p/40*t[4];}
    var band=Math.floor((p-40)/10);            /* 0:e-d 1:d-c 2:c-b 3:b-a */
    var lo=t[4-band],hi=t[3-band];
    return lo+(p-(40+10*band))/10*(hi-lo);
  }
  function markToPum(m,t,max){
    if(m>=t[0]){return 80+20*(m-t[0])/(max-t[0]);}
    for(var i=0;i<4;i++){if(m>=t[i+1]){return 70-10*i+10*(m-t[i+1])/(t[i]-t[i+1]);}}
    return 40*m/t[4];
  }
  function asGradeOfPum(p){return p>=80?'a':p>=70?'b':p>=60?'c':p>=50?'d':p>=40?'e':'u';}
  function stats(list){
    var s=list.slice().sort(function(a,b){return a-b;});
    var n=s.length,mid=n%2?s[(n-1)/2]:(s[n/2-1]+s[n/2])/2;
    return {lo:s[0],hi:s[n-1],mid:mid};
  }
  function avgAS(route,keys){
    var r=[0,0,0,0,0];
    keys.forEach(function(k){for(var i=0;i<5;i++){r[i]+=route.s[k].as[i]/keys.length;}});
    return r;
  }
  /* Main calculation.
     inp: {route, keys (session keys with data, newest first), satKey (may be missing from data), pum, target (0..5)} */
  function calc(inp){
    var R=inp.route,keys=inp.keys,tot=R.asMax+R.a2Max;
    var known=!!R.s[inp.satKey];
    var asSat=known?R.s[inp.satKey].as:avgAS(R,keys);
    var M=pumToMark2(inp.pum,asSat,R.asMax);
    var out={M:M,known:known,tot:tot,asGrade:asGradeOfPum(inp.pum)};
    /* Route 1: keep AS, sit A2 only. Staged threshold = AS thresholds of your sitting + A2 thresholds of the A2 series. */
    out.carry=G.map(function(g,gi){
      var needs=keys.map(function(k){return totals(asSat,R.s[k].a2,tot)[gi]-M;});
      return stats(needs);
    });
    /* A2 standard for a needed mark, judged on the most recent series. */
    var a2Latest=a2grades(R.s[keys[0]].a2,R.a2Max);
    out.level=function(need){
      if(need<=0){return 7;}              /* nothing needed */
      if(need>R.a2Max){return -1;}        /* impossible */
      for(var i=0;i<6;i++){if(need>=a2Latest[i]-1e-9){return i;}}
      return 6;                           /* below E standard */
    };
    /* What-if: overall grade from an A2 score, per series. */
    out.gradeFor=function(a2score){
      var gs=keys.map(function(k){
        var t=totals(asSat,R.s[k].a2,tot),T=M+a2score;
        for(var i=0;i<6;i++){if(T>=t[i]-1e-9){return i;}}
        return 6;
      });
      return {best:Math.min.apply(null,gs),worst:Math.max.apply(null,gs)};
    };
    /* Route 2: re-sit AS. For a re-sit PUM q, need = A level threshold - new AS mark, per series.
       With a safety net Cambridge keeps whichever AS gives the better result. */
    out.resit=function(q,gi){
      var needs=keys.map(function(k){
        var s=R.s[k],Mn=pumToMark2(q,s.as,R.asMax);
        var nNew=totals(s.as,s.a2,tot)[gi]-Mn;
        var nOld=totals(asSat,s.a2,tot)[gi]-M;
        return Math.min(nNew,nOld);
      });
      return stats(needs);
    };
    /* Route 3: everything in one series, no AS carried. */
    out.fresh=G.map(function(g,gi){
      return stats(keys.map(function(k){return totals(R.s[k].as,R.s[k].a2,tot)[gi];}));
    });
    return out;
  }
  /* Exam series helpers. A series is {y, m} with m 6 (May/June) or 11 (Oct/Nov). */
  function seriesLabel(s){return (s.m===6?'May/June ':'Oct/Nov ')+s.y;}
  function nextSeries(s){return s.m===6?{y:s.y,m:11}:{y:s.y+1,m:6};}
  function examStart(s){return s.m===6?new Date(s.y,3,24):new Date(s.y,8,28);}
  function resultsDay(s){return s.m===6?new Date(s.y,7,10):new Date(s.y+1,0,12);}
  function monthsBetween(a,b){return (b.y-a.y)*12+(b.m-a.m);}
  /* A2 series still open to this AS result: within 13 months and not yet started. */
  function windows(asS,today){
    var out=[],s=nextSeries(asS);
    while(monthsBetween(asS,s)<=13){
      var start=examStart(s),days=(start-today)/864e5;
      if(days>0){out.push({s:s,label:seriesLabel(s),soon:days<120,days:days});}
      s=nextSeries(s);
    }
    return out;
  }
  var api={G:G,ASG:ASG,totals:totals,pumToMark:pumToMark2,markToPum:markToPum,asGradeOfPum:asGradeOfPum,calc:calc,
    seriesLabel:seriesLabel,nextSeries:nextSeries,examStart:examStart,resultsDay:resultsDay,windows:windows,monthsBetween:monthsBetween};
  if(typeof module!=='undefined'&&module.exports){module.exports=api;}else{root.SJG=api;}
})(this);
