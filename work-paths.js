(() => {
 "use strict";
 const grid=document.querySelector(".work-grid");if(!grid)return;
 const cards=new Map([...grid.querySelectorAll("[data-project]")].map(item=>[item.dataset.project,item]));
 const paths={
  featured:{ids:["hope-college","imhere","brume","holland","plain-sight"],text:"Explore campus communications, a lighting campaign, an attendance correction, a walking tour, or an editorial sequence."},
  all:{ids:["hope-college","proof","brume","plain-sight","holland","imhere","psychictally","afterform","interval","aurea","loopline","novella","nutriva"],text:"Thirteen selected case studies. Independent concepts, collaborative foundations and application work are labeled on each project."},
  ux:{ids:["imhere","holland","psychictally"],text:"Try an attendance correction, pause a walking tour, or inspect a community moderation decision."},
  graphic:{ids:["hope-college","proof","brume","plain-sight","afterform"],text:"Campus communications, campaign artwork, lighting studies, editorial design and a repair-service identity."},
  visual:{ids:["hope-college","proof","brume","plain-sight","interval"],text:"Compare campus communications, studio and lighting campaigns, editorial design and a cultural programme."},
  web:{ids:["psychictally","imhere","aurea","holland"],text:"Open a sample interaction to inspect its controls, feedback, and recovery states."}
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
   if (url.hash.startsWith("#work-") && !path.ids.includes(url.hash.slice(6))) url.hash = "work";
   window.history.replaceState(null,"",url);
  }
 }
 buttons.forEach(b=>b.addEventListener("click",()=>show(b.dataset.focus,true)));
 function openRoute() {
  const url = new URL(window.location.href);
  const requested = url.searchParams.get("focus");
  const focus = Object.hasOwn(paths, requested) ? requested : "featured";
  const project = url.hash.startsWith("#work-") ? url.hash.slice(6) : "";
  const card = cards.get(project);
  show(card && !paths[focus].ids.includes(project) ? "all" : focus, false);
  if (card) card.scrollIntoView({ block: "start", behavior: "instant" });
 }
 openRoute();
 window.addEventListener("popstate", openRoute);
 window.addEventListener("hashchange", openRoute);
})();
