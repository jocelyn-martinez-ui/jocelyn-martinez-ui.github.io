(() => {
 "use strict";
 const grid=document.querySelector(".work-grid");if(!grid)return;
 const cards=new Map([...grid.querySelectorAll("[data-project]")].map(item=>[item.dataset.project,item]));
 const paths={
  featured:{ids:["afterform","brume","proof","imhere","holland","interval"],text:"Six selected studies spanning marketing graphics, brand identity, operational UI, accessible experiences and editorial design. View all work for the complete collection."},
  all:{ids:["afterform","brume","proof","imhere","holland","interval","aurea","loopline","novella","nutriva"],text:"All ten projects, including more consumer and editorial UI work."},
  ux:{ids:["imhere","proof","holland","interval","nutriva","afterform","loopline"],text:"Start with ImHere and PROOF to examine real interaction states, then look at accessible choices, scheduling conflicts and connected data."},
  graphic:{ids:["brume","afterform","interval","proof","loopline","aurea"],text:"Start with BRUME’s photographic social and email art direction; compare AFTERFORM’s print and identity work with INTERVAL’s cultural campaign."},
  web:{ids:["proof","brume","aurea","holland","novella","imhere","afterform"],text:"Explore PROOF’s stateful prototype, BRUME’s responsive photographic HTML email series, and responsive, accessible UI and editorial experiences."}
 };
 const buttons=[...document.querySelectorAll("[data-focus]")];
 const route=document.querySelector("#work-route");
 const count=document.querySelector("#work-count");
 function show(key,update){
  const chosen=Object.hasOwn(paths,key)?key:"featured",path=paths[chosen];
  for(const [id,card]of cards)card.hidden=!path.ids.includes(id);
  path.ids.forEach(id=>{const card=cards.get(id);if(card)grid.appendChild(card)});
  buttons.forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.focus===chosen)));
  if(route)route.textContent=path.text;
  if(count)count.textContent=path.ids.length+" projects shown.";
  if(update&&window.history?.replaceState){
   const url=new URL(window.location.href);
   chosen==="featured"?url.searchParams.delete("focus"):url.searchParams.set("focus",chosen);
   window.history.replaceState(null,"",url);
  }
 }
 buttons.forEach(b=>b.addEventListener("click",()=>show(b.dataset.focus,true)));
 const urlKey=new URLSearchParams(window.location.search).get("focus");
 show(urlKey||"featured",false);
})();