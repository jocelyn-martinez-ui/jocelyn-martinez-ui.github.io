(() => {
 'use strict';
 const grid=document.querySelector('.work-grid');if(!grid)return;
 const cards=new Map([...grid.querySelectorAll('[data-project]')].map(x=>[x.dataset.project,x]));
 const paths={
  all:{ids:['imhere','afterform','holland','interval','aurea','loopline','novella','nutriva'],text:'Start with a consequential workflow, then explore identity, civic interaction and cultural design.'},
  ux:{ids:['imhere','interval','holland','nutriva','afterform','loopline'],text:'Start with ImHere’s explained corrections. Continue through programme conflicts, visitor choices and connected household data.'},
  graphic:{ids:['afterform','interval','loopline','aurea'],text:'Start with AFTERFORM’s identity and publication. Compare cultural communication, practical service graphics and an editorial archive.'},
  web:{ids:['aurea','holland','novella','imhere','afterform'],text:'Start with Áurea’s database. Explore a civic guide, a reading experience and interfaces that reveal their underlying decisions.'}
 };
 function show(key,update){const chosen=paths[key]?key:'all';const path=paths[chosen];for(const [id,card]of cards)card.hidden=!path.ids.includes(id);path.ids.forEach(id=>grid.appendChild(cards.get(id)));document.querySelectorAll('[data-focus]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.focus===chosen)));document.querySelector('#work-route').textContent=path.text;document.querySelector('#work-count').textContent=path.ids.length+' projects shown.';if(update&&window.history?.replaceState){const url=new URL(window.location.href);chosen==='all'?url.searchParams.delete('focus'):url.searchParams.set('focus',chosen);window.history.replaceState(null,'',url);} }
 document.querySelectorAll('[data-focus]').forEach(b=>b.addEventListener('click',()=>show(b.dataset.focus,true)));
 const key=new URLSearchParams(window.location.search).get('focus');show(key||'all',false);
})();
