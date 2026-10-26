// Run from repository root: node --test proof/qa.test.mjs
// This simulates workflow state; it is not a browser accessibility or layout audit.
import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {fileURLToPath} from "node:url";
import {dirname,join} from "node:path";
import {runInNewContext} from "node:vm";

const here=dirname(fileURLToPath(import.meta.url));
const html=readFileSync(join(here,"workspace.html"),"utf8");
const source=readFileSync(join(here,"proof.js"),"utf8");

class ElementMock {
 constructor(id=""){this.id=id;this.textContent="";this.value="";this.checked=false;this.disabled=false;this.hidden=false;this.dataset={};this.style={};this.children=[];this.attributes={};this.firstChild={textContent:""};this.listeners={};this.focused=false;}
 addEventListener(type,fn){this.listeners[type]=fn}
 fire(type,arg={}){assert.equal(typeof this.listeners[type],"function","event listener "+this.id+" "+type);this.listeners[type](arg)}
 setAttribute(key,value){this.attributes[key]=value}
 append(...items){this.children.push(...items)}
 appendChild(item){this.children.push(item)}
 replaceChildren(...items){this.children=[...items]}
 querySelector(){return this.childMock??(this.childMock=new ElementMock())}
 focus(){this.focused=true}
}
function mount(){
 const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
 const nodes=Object.fromEntries(ids.map(id=>[id,new ElementMock(id)]));
 const buttons=["poster","social","guide"].map(job=>{const node=new ElementMock(job);node.dataset.job=job;return node});
 const document={
  getElementById:id=>nodes[id],
  querySelectorAll:selector=>selector==="[data-job]"?buttons:[],
  querySelector:selector=>buttons.find(node=>node.dataset.job===selector.match(/data-job="([^"]+)"/)?.[1]),
  createElement:name=>new ElementMock(name)
 };
 const calls={prints:0};
 const window={print:()=>{calls.prints++}};
 runInNewContext(source,{document,window});
 return {nodes,buttons,calls};
}
test("approval plus preflight unlocks sample release, a new revision locks it again",()=>{
 const {nodes:n,calls}=mount();
 assert.equal(n["current-revision"].textContent,"03");
 assert.equal(n["print-brief"].disabled,true);
 n["approve-proof"].fire("click");
 assert.equal(n["current-state"].textContent,"Revision approved");
 assert.equal(n["print-brief"].disabled,true);
 for(const id of ["check-copy","check-rights","check-output"]){n[id].checked=true;n[id].fire("change")}
 assert.equal(n["print-brief"].disabled,false);
 n["print-brief"].fire("click");
 assert.equal(calls.prints,1);
 assert.ok(n["print-area"].children.length>5);
 n["submit-revision"].fire("click");
 assert.equal(n["current-revision"].textContent,"04");
 assert.equal(n["current-state"].textContent,"Awaiting review");
 assert.equal(n["print-brief"].disabled,true);
 assert.equal(n["check-copy"].checked,false);
});
test("change request requires actionable feedback and never carries approval forward",()=>{
 const {nodes:n}=mount();
 n["request-change"].fire("click");
 assert.equal(n["review-error"].hidden,false);
 assert.equal(n["review-note"].focused,true);
 assert.equal(n["current-state"].textContent,"Awaiting review");
 n["review-note"].value="Increase the date contrast";
 n["review-note"].fire("input",{target:n["review-note"]});
 n["request-change"].fire("click");
 assert.equal(n["current-state"].textContent,"Changes requested");
 assert.equal(n["approve-proof"].disabled,true);
 n["submit-revision"].fire("click");
 assert.equal(n["current-state"].textContent,"Awaiting review");
 assert.equal(n["current-revision"].textContent,"04");
 assert.equal(n["print-brief"].disabled,true);
});
test("per-brief state is independent and reset returns all jobs to the baseline",()=>{
 const {nodes:n,buttons}=mount();
 n["approve-proof"].fire("click");
 buttons[1].fire("click");
 assert.equal(n["current-title"].textContent,"Social announcement set");
 assert.equal(n["current-state"].textContent,"Awaiting review");
 n["request-change"].fire("click");
 n["review-note"].value="Correct the social crop";
 n["review-note"].fire("input",{target:n["review-note"]});
 n["request-change"].fire("click");
 buttons[0].fire("click");
 assert.equal(n["current-state"].textContent,"Revision approved");
 buttons[1].fire("click");
 assert.equal(n["current-state"].textContent,"Changes requested");
 n["reset-all"].fire("click");
 assert.equal(n["current-title"].textContent,"Public programme poster");
 assert.equal(n["current-revision"].textContent,"03");
 assert.equal(n["current-state"].textContent,"Awaiting review");
});
