(() => {
"use strict";
const briefs = {
 poster:{id:"PR—017 / PRINT",title:"Public programme poster",output:"A2 / PRINT",owner:"CREATIVE TEAM",format:"A2, portrait",color:"CMYK conversion pending",destination:"Print vendor / unassigned",kind:"COMMUNITY PROGRAMME",headline:"SPACE\nTO\nMAKE.",foot:"SAT / 14:00 · STUDIO 01",revision:3},
 social:{id:"PR—018 / DIGITAL",title:"Social announcement set",output:"1080 × 1350",owner:"CAMPAIGN DESIGN",format:"4:5 social master",color:"RGB / screen output",destination:"Campaign channels / draft",kind:"SOCIAL EDITION / 02",headline:"MAKE\nROOM.",foot:"A NEW SERIES · SAMPLE CAMPAIGN",revision:2},
 guide:{id:"PR—019 / EDITORIAL",title:"Programme guide",output:"A5 / 16 PAGES",owner:"EDITORIAL TEAM",format:"A5 booklet, 16 pp",color:"Spot + CMYK intent",destination:"Short-run printer / pending",kind:"EDITORIAL ISSUE / 01",headline:"TAKE\nA\nLOOK.",foot:"INSIDE / AN OPEN PROGRAMME",revision:1}
};
const $ = id => document.getElementById(id);
const checkIds=["check-copy","check-rights","check-output"];
const statusLabels={awaiting:"Awaiting review",changes:"Changes requested",approved:"Revision approved"};
const makeState=()=>Object.fromEntries(Object.entries(briefs).map(([key,b])=>[key,{
 revision:b.revision,status:"awaiting",note:"",checks:[false,false,false],
 log:[{revision:b.revision,summary:"Proof submitted for review",detail:"Illustrative starting state"}]
}]));
let states=makeState();
let selected="poster";
const safe=(value)=>String(value||"");
function current(){return states[selected]}
function revLabel(v){return String(v).padStart(2,"0")}
function record(summary,detail){const state=current();state.log.unshift({revision:state.revision,summary,detail:detail||""})}
function syncChecks(){const state=current();checkIds.forEach((id,i)=>{state.checks[i]=$(id).checked})}
function meetsRelease(){const state=current();return state.status==="approved"&&state.checks.every(Boolean)}
function announce(message,type){const node=$("decision-notice");node.textContent=message;node.dataset.type=type||"info"}
function render(){
 const brief=briefs[selected],state=current();
 $("current-id").textContent=brief.id;$("current-title").textContent=brief.title;
 $("current-revision").textContent=revLabel(state.revision);$("current-output").textContent=brief.output;
 $("current-owner").textContent=brief.owner;$("current-state").textContent=statusLabels[state.status];
 $("current-state").dataset.state=state.status;
 $("spec-format").textContent=brief.format;$("spec-color").textContent=brief.color;
 $("spec-destination").textContent=brief.destination;
 $("art-kind").textContent=brief.kind;$("art-headline").textContent=brief.headline;
 $("art-headline").style.whiteSpace="pre-line";$("art-foot").textContent=brief.foot;
 $("review-note").value=state.note;
 $("review-error").hidden=true;$("review-note").setAttribute("aria-invalid","false");
 checkIds.forEach((id,i)=>{$(id).checked=state.checks[i]});
 $("request-change").disabled=state.status!=="awaiting";
 $("approve-proof").disabled=state.status!=="awaiting";
 $("submit-revision").disabled=state.status==="awaiting";
 $("print-brief").disabled=!meetsRelease();
 $("handoff-explain").textContent=meetsRelease()
  ?"All checks are complete for revision "+revLabel(state.revision)+". Print a sample release brief."
  :state.status!=="approved"
  ?"Blocked: the current revision needs explicit approval and all three preflight checks."
  :"Blocked: complete the remaining preflight checks to produce a sample release brief.";
 document.querySelectorAll("[data-job]").forEach(btn=>{
  const key=btn.dataset.job;
  btn.setAttribute("aria-pressed",String(key===selected));
  btn.querySelector(".job-state").firstChild.textContent=statusLabels[states[key].status]+" ";
 });
 const history=$("history-list");history.replaceChildren();
 state.log.forEach(entry=>{
  const li=document.createElement("li");
  const title=document.createElement("strong");title.textContent=entry.summary;
  const metadata=document.createElement("span");
  metadata.textContent="REV "+revLabel(entry.revision)+(entry.detail?" / "+entry.detail:"");
  li.append(title,metadata);history.append(li);
 });
}
function selectJob(key){if(!Object.hasOwn(briefs,key))return;states[selected].note=$("review-note").value;selected=key;render();announce("Now reviewing "+briefs[key].title+" / revision "+revLabel(current().revision)+".")}
document.querySelectorAll("[data-job]").forEach(b=>b.addEventListener("click",()=>selectJob(b.dataset.job)));
$("review-note").addEventListener("input",event=>{current().note=event.target.value;if(event.target.value.trim()){$("review-error").hidden=true;event.target.setAttribute("aria-invalid","false")}});
$("request-change").addEventListener("click",()=>{
 const note=$("review-note").value.trim();
 if(!note){
  $("review-error").hidden=false;$("review-note").setAttribute("aria-invalid","true");
  $("review-note").focus();announce("A clear explanation is required to request changes.","error");return;
 }
 const state=current();if(state.status!=="awaiting")return;
 state.note=note;state.status="changes";state.checks=[false,false,false];
 record("Changes requested",note.slice(0,100));
 render();announce("Changes requested for revision "+revLabel(state.revision)+". Submit a new revision to continue.","error");
});
$("approve-proof").addEventListener("click",()=>{
 const state=current();if(state.status!=="awaiting")return;
 state.note=$("review-note").value.trim();state.status="approved";
 record("Explicit approval recorded",state.note?state.note.slice(0,100):"No rationale entered");
 render();announce("Revision "+revLabel(state.revision)+" approved. This does not make the file production ready.","success");
});
$("submit-revision").addEventListener("click",()=>{
 const state=current();if(state.status==="awaiting")return;
 state.revision++;state.status="awaiting";state.checks=[false,false,false];state.note="";
 record("Simulated new revision","Previous approval and preflight flags cleared");
 render();announce("Sample revision "+revLabel(state.revision)+" is awaiting a fresh decision. Prior approval is no longer valid.");
});
checkIds.forEach((id)=>$(id).addEventListener("change",()=>{
 syncChecks();const ready=meetsRelease();$("print-brief").disabled=!ready;
 $("handoff-explain").textContent=ready
  ?"All checks are complete for revision "+revLabel(current().revision)+". Print a sample release brief."
  :current().status!=="approved"
  ?"Blocked: the current revision needs explicit approval and all three preflight checks."
  :"Blocked: complete the remaining preflight checks to produce a sample release brief.";
 if(ready)announce("Preflight checklist complete. The sample release brief is available.","success");
}));
$("reset-all").addEventListener("click",()=>{
 states=makeState();selected="poster";render();
 announce("All sample decisions were reset.");
 document.querySelector('[data-job="poster"]').focus();
});
function printElement(tag,text,parent){
 const node=document.createElement(tag);node.textContent=safe(text);parent.appendChild(node);return node;
}
$("print-brief").addEventListener("click",()=>{
 if(!meetsRelease())return;
 const brief=briefs[selected],state=current(),area=$("print-area");
 area.replaceChildren();
 printElement("p","PROOF® / LOCAL DEMO DOCUMENT — NOT A VERIFIED PRINT RELEASE",area);
 printElement("h1","Release brief / "+brief.title,area);
 printElement("p",brief.id+" / Revision "+revLabel(state.revision)+" / Current approval recorded",area);
 printElement("h2","Artwork specification",area);
 const table=document.createElement("table"),body=document.createElement("tbody");
 [["Deliverable",brief.title],["Format",brief.format],["Output",brief.output],["Color intent",brief.color],
 ["Destination",brief.destination],["Approval status",statusLabels[state.status]],
 ["Revision",revLabel(state.revision)],["Review rationale",state.note||"Explicit approval without comment"],
 ["Copy / dates","Checked in demo"],["Rights / credits","Checked in demo"],["Output size / color","Checked in demo"]
 ].forEach(([name,value])=>{
  const row=document.createElement("tr");
  printElement("th",name,row);printElement("td",value,row);body.append(row);
 });
 table.append(body);area.append(table);
 printElement("h2","Revision activity",area);
 const list=document.createElement("ol");
 state.log.forEach(entry=>printElement("li","Rev "+revLabel(entry.revision)+": "+entry.summary+" — "+entry.detail,list));
 area.append(list);
 const legal=printElement("p","This is a fictional browser prototype. Approval, checklist and file specifications are sample records, not a real signature, output inspection or print-vendor authorization.",area);
 legal.className="print-legal";
 window.print();
});
render();
})();