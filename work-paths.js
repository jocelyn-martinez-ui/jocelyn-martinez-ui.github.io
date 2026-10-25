(() => {
 "use strict";
 const grid=document.querySelector(".work-grid");if(!grid)return;
 const cards=new Map([...grid.querySelectorAll("[data-project]")].map(item=>[item.dataset.project,item]));
 const paths={
  featured:{ids:["psychictally","imhere","brume","proof","afterform","holland"],text:"Six selected projects: a code-backed independent product, an academic capstone, photographic and editorial campaigns, identity work and accessibility-focused UI. View All work for the full collection."},
  all:{ids:["psychictally","imhere","brume","proof","afterform","holland","interval","aurea","loopline","novella","nutriva"],text:"All eleven showcased projects, from operational UI and accessible journeys to photography-led brand campaigns."},
  ux:{ids:["psychictally","imhere","holland","interval","aurea","loopline","nutriva","proof"],text:"Start with PsychicTally's implementation and interaction states, then ImHere's shared correction workflow and Holland's accessibility-oriented navigation."},
  graphic:{ids:["brume","proof","afterform","interval","psychictally","loopline","aurea"],text:"BRUME, PROOF and AFTERFORM lead with photographic direction, publication, emails, print and identity. PsychicTally adds a cross-channel product brand study."},
  web:{ids:["psychictally","imhere","aurea","holland","proof","brume","afterform"],text:"Start with a code-backed platform, then inspect functional UI states, responsive HTML email studies and distinct web interfaces."}
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
})();
