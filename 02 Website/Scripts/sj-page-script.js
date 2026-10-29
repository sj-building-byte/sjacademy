(function(){
  var root=document.getElementById('sj');
  if(!root){return;}
  var each=function(list,fn){Array.prototype.forEach.call(list,fn);};

  /* Tabs: role="tablist" > role="tab" aria-controls="panel-id" */
  each(root.querySelectorAll('[role="tablist"]'),function(list){
    var tabs=Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    var pick=function(tab,focus){
      tabs.forEach(function(t){
        var on=t===tab;
        t.setAttribute('aria-selected',on?'true':'false');
        t.tabIndex=on?0:-1;
        var panel=document.getElementById(t.getAttribute('aria-controls'));
        if(panel){panel.hidden=!on;}
      });
      if(focus){tab.focus();}
    };
    tabs.forEach(function(tab,i){
      tab.addEventListener('click',function(){pick(tab,false);});
      tab.addEventListener('keydown',function(e){
        var step=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;
        if(!step){return;}
        e.preventDefault();
        pick(tabs[(i+step+tabs.length)%tabs.length],true);
      });
    });
  });

  /* Phone bottom bar: shows once the element marked data-sj-hero has scrolled away */
  var bar=root.querySelector('.sj-bar');
  var hero=root.querySelector('[data-sj-hero]');
  if(bar&&hero&&'IntersectionObserver' in window){
    root.classList.add('sj-has-bar');
    new IntersectionObserver(function(entries){
      bar.classList.toggle('is-on',!entries[0].isIntersecting);
    }).observe(hero);
  }

  /* Video: loads the player only after a tap */
  each(root.querySelectorAll('.sj-video[data-src]'),function(v){
    v.addEventListener('click',function(e){
      e.preventDefault();
      var f=document.createElement('iframe');
      f.src=v.getAttribute('data-src');
      f.title=v.getAttribute('data-title')||'Video';
      f.allow='autoplay; encrypted-media; picture-in-picture';
      f.allowFullscreen=true;
      f.style.cssText='position:absolute;inset:0;width:100%;height:100%;border:0';
      v.innerHTML='';
      v.appendChild(f);
    });
  });

  /* Measurement: one event name per action, location read from data-loc */
  var send=function(name,loc){
    var g=window['gt'+'ag'];
    if(typeof g==='function'){g('event',name,{link_location:loc||'unknown',page_family:root.getAttribute('data-family')||''});}
  };
  root.addEventListener('click',function(e){
    var a=e.target.closest?e.target.closest('a,button'):null;
    if(!a){return;}
    var href=a.getAttribute('href')||'';
    var loc=a.getAttribute('data-loc');
    if(href.indexOf('wa.me')>-1){send('whatsapp_click',loc);}
    else if(href.indexOf('popup%3Aopen')>-1){send('register_open',loc);}
    else if(a.hasAttribute('download')){send('resource_download',loc);}
    else if(a.hasAttribute('data-event')){send(a.getAttribute('data-event'),loc);}
  });
})();
