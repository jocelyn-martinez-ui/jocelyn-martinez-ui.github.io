(() => {
 "use strict";
 const grid=document.querySelector(".work-grid");if(!grid)return;
 const cards=new Map([...grid.querySelectorAll("[data-project]")].map(item=>[item.dataset.project,item]));
 const paths={
  featured:{ids:["plain-sight","imhere","afterform","psychictally"],text:"Four selected projects: an editorial identity, an attendance workspace, a repair service and community software."},
  all:{ids:["plain-sight","psychictally","afterform","imhere","proof","brume","holland","interval","aurea","loopline","novella","nutriva"],text:"All twelve showcased projects. Independent concepts, collaborative foundations and application work are labeled on each project."},
  ux:{ids:["psychictally","imhere","holland"],text:"Three workflow studies: community permissions, an explained attendance correction and a reading-focused visitor flow. Implementation is shown; primary-user validation remains limited."},
  graphic:{ids:["plain-sight","afterform","proof","brume"],text:"Four visual systems: editorial identity, garment repair, a graphic campaign and photography-led marketing. More cultural and identity work is available under All work."},
  visual:{ids:["proof","brume","plain-sight","interval"],text:"Four expressions of a visual system: graphic campaigns, photographic art direction, editorial storytelling and a cultural programme. Concept and AI-generated imagery are labeled."},
  web:{ids:["psychictally","imhere","aurea","holland"],text:"Four implemented interface studies. Inspect the working behavior, responsive adaptation and the limits of each prototype."}
 };
 const buttons=[...document.querySelectorAll("[data-focus]")];
 const route=document.querySelector("#work-route");
 const count=document.querySelector("#work-count");
 function show(key,update){
  const chosen=Object.prototype.hasOwnProperty.call(paths,key)?key:"featured",path=paths[chosen];
  for(const [id,card]of cards)card.hidden=!path.ids.includes(id);
  path.ids.forEach(id=>{const card=cards.get(id);if(card)grid.appendChild(card)});
  buttons.forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.focus===chosen)));
  if(route)route.textContent=path.text;
  if(count)count.textContent=path.ids.length+" projects shown.";
  if(update&&window.history&&window.history.replaceState){
   const url=new URL(window.location.href);
   chosen==="featured"?url.searchParams.delete("focus"):url.searchParams.set("focus",chosen);
   window.history.replaceState(null,"",url);
  }
 }
 buttons.forEach(b=>b.addEventListener("click",()=>show(b.dataset.focus,true)));
 const urlKey=new URLSearchParams(window.location.search).get("focus");
 show(urlKey||"featured",false);
 window.addEventListener("popstate",()=>show(new URLSearchParams(window.location.search).get("focus")||"featured",false));
})();
