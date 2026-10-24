(()=>{
"use strict";
const $=id=>document.getElementById(id);
const range=$("compareSlider"),clip=$("afterClip"),value=$("compareValue"),image=$("compareAfter"),area=$("compareArea");
function updateCompare(){
 if(!range||!clip||!area)return;
 const n=Number(range.value);
 clip.style.width=n+"%";
 if(image){image.style.width=area.clientWidth+"px";image.style.height=area.clientHeight+"px";image.style.maxWidth="none";image.style.objectFit="fill";}
 if(value)value.textContent=n+"% alternative";
}
if(range){range.addEventListener("input",updateCompare);updateCompare();if(typeof ResizeObserver!=="undefined"){new ResizeObserver(updateCompare).observe(area)}else window.addEventListener("resize",updateCompare)}
const findings={
 logo:{code:"CHECK / 01 · WORDMARK",title:"Give the wordmark a working margin.",text:"The concept master provides a dedicated top band for the wordmark. Review the final clear-space rule and proof it at the intended reproduction size. A margin seen on-screen is not a tested print allowance.",action:"Action: inspect top-edge clearance and measure at 1:1 size.",image:"commissions/terra/label-mist-r03.svg",alt:"TERRA Mist specimen, current R03 label"},
 hierarchy:{code:"CHECK / 02 · HIERARCHY",title:"Does the reader know what matters?",text:"The PULP exploration uses overlapping ink textures and a very loud headline. For small viewing sizes, protect a clean reading order. A full-size poster and a mobile feed graphic need separate hierarchy checks.",action:"Action: compare mobile crop and printed proof before approving.",image:"commissions/pulp/02-overprint.svg",alt:"PULP expressive overprint campaign composition"},
 production:{code:"CHECK / 03 · VERSION",title:"Copy must match the master record.",text:"TERRA's archived R02 was purposely left with an outdated 10 mm claim; concept-current R03 is labeled 12 mm. This is an intentionally scripted QA scenario, not a real production correction.",action:"Action: quarantine R02, validate sample specification, then release an approved R03.",image:"commissions/terra/archive/label-mist-r02.svg",alt:"TERRA Mist archived revision R02 showing outdated size copy"}
};
for(const b of document.querySelectorAll("[data-issue]")){
 b.addEventListener("click",()=>{
  const f=findings[b.dataset.issue];if(!f)return;
  document.querySelectorAll("[data-issue]").forEach(el=>el.setAttribute("aria-pressed",String(el===b)));
  const code=$("issueCode"),title=$("issueTitle"),text=$("issueText"),action=$("issueAction"),img=$("issueImage");
  if(code)code.textContent=f.code;
  if(title)title.textContent=f.title;
  if(text)text.textContent=f.text;
  if(action)action.textContent=f.action;
  if(img){img.src=f.image+"?v=20261024-coherent-v2";img.alt=f.alt}
 });
}
const colorPairs={ink:["#253E3E","#F4E4D4"],high:["#F4E4D4","#184649"],low:["#E7BC4F","#D9A6B7"],red:["#BC4B42","#F4E4D4"]};
function luminance(hex){const a=[1,3,5].map(i=>parseInt(hex.slice(i,i+2),16)/255).map(x=>x<=.04045?x/12.92:Math.pow((x+.055)/1.055,2.4));return .2126*a[0]+.7152*a[1]+.0722*a[2]}
function contrast(fg,bg){const a=luminance(fg),b=luminance(bg);return (Math.max(a,b)+.05)/(Math.min(a,b)+.05)}
const pair=$("contrastPair");function updateContrast(){if(!pair)return;const [fg,bg]=colorPairs[pair.value]||colorPairs.ink,ratio=contrast(fg,bg);const sample=$("contrastExample"),out=$("contrastRatio"),verdict=$("contrastVerdict");if(sample){sample.style.color=fg;sample.style.backgroundColor=bg;}if(out)out.textContent=ratio.toFixed(2)+":1";if(verdict)verdict.textContent="WCAG AA: "+(ratio>=4.5?"normal text passes":ratio>=3?"large text only":"fails normal and large text")+". Browser colors only; print proof required.";}
pair?.addEventListener("change",updateContrast);updateContrast();
const art=$("preflightArt"),trim=$("showTrim"),safe=$("showSafe"),status=$("releaseState"),checks=[...document.querySelectorAll("[data-preflight]")];
function updatePreflight(){
 if(art)art.classList.toggle("show-trim",!!trim?.checked);
 if(art)art.classList.toggle("show-safe",!!safe?.checked);
 const n=checks.filter(x=>x.checked).length;
 if(status){status.dataset.ready=String(n===checks.length);status.textContent=n===checks.length?"Three simulated checklist steps complete. This illustrates a potential HANDOFF REQUEST, not printer authorization; vendor and physical validation remain outstanding.":n+" / "+checks.length+" demonstration steps completed. No commercial production release can be inferred.";}
}
trim?.addEventListener("change",updatePreflight);safe?.addEventListener("change",updatePreflight);checks.forEach(c=>c.addEventListener("change",updatePreflight));updatePreflight();
})();