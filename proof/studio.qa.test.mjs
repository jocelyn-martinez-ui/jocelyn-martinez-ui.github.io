// Reproducible source integrity tests, not actual browser or commercial printer sign-off.
// Run: node --test proof/studio.qa.test.mjs
import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync,existsSync} from "node:fs";
import {join,dirname,resolve} from "node:path";
import {fileURLToPath} from "node:url";
import {Script} from "node:vm";
const root=dirname(fileURLToPath(import.meta.url));
const read=p=>readFileSync(join(root,p),"utf8");
const exists=p=>existsSync(join(root,p));
const pulp=["01-hero","02-overprint","03-pigment","social-01","social-02","social-03","social-04"];
const field=Array.from({length:12},(_,i)=>"page-"+String(i+1).padStart(2,"0"));
const guide=Array.from({length:12},(_,i)=>"guide-"+String(i+1).padStart(2,"0"));
const terra=["label-mist-r03","label-ember-r03","label-chalk-r03","ad-a5","sell-sheet-a4"];
test("all creative masters exist with self-contained vector content",()=>{
 for(const s of pulp)assert.match(read("commissions/pulp/"+s+".svg"),/<svg[^>]+>/);
 for(const s of field)assert.match(read("commissions/field/"+s+".svg"),/width="148mm" height="210mm"/);
 for(const s of guide)assert.match(read("commissions/pulp/"+s+".svg"),/width="210mm" height="297mm"/);
 for(const s of terra)assert.match(read("commissions/terra/"+s+".svg"),/width="\d+mm" height="\d+mm"/);
 for(const s of ["label-mist-r01","label-mist-r02"])assert.ok(exists("commissions/terra/archive/"+s+".svg"));
});
test("flagship and preserved workflow both retain required local dependencies",()=>{
 const index=read("index.html");
 for(const name of ["studio.css","studio.js","workspace.html","PRODUCTION_HANDOFF.md","ART_DIRECTION_AND_RESEARCH.md"])assert.ok(index.includes(name));
 assert.ok(exists("workspace.html"));assert.ok(exists("proof.js"));assert.ok(exists("proof.css"));
 new Script(read("studio.js"));new Script(read("proof.js"));
});
test("three marketing emails include corresponding text alternatives",()=>{
 for(const name of ["01-announcement","02-method","03-studio"]){
  const mail=read("commissions/pulp/email/"+name+".html");
  assert.match(mail,/role="presentation"/);
  assert.match(mail,/display:none/);
  assert.match(mail,/<!--\[if mso\]>/);
  assert.equal((mail.match(/<table\b/g)||[]).length,(mail.match(/<\/table>/g)||[]).length);
  assert.ok(exists("commissions/pulp/email/"+name+".txt"));
 }
});
test("studio HTML references all expected pages, social masters and relevant lab controls",()=>{
 const html=read("index.html");
 for(const s of pulp)assert.ok(html.includes("commissions/pulp/"+s+".svg"));
 for(const s of field)assert.ok(html.includes("commissions/field/"+s+".svg"));
 for(const s of guide)assert.ok(html.includes("commissions/pulp/"+s+".svg"));
 for(const id of ["compareSlider","afterClip","issueImage","showTrim","showSafe","releaseState"])assert.ok(html.includes('id="'+id+'"'));
});
test("all direct page-relative links and images resolve to files",()=>{
 const src=read("index.html");
 const links=[...src.matchAll(/(?:src|href)="([^"]+)"/g)].map(x=>x[1]).filter(x=>x&&!/^(?:https?:|mailto:|#|tel:|data:)/.test(x));
 for(const link of links){
  const path=link.split(/[?#]/)[0];if(!path)continue;
  assert.ok(existsSync(resolve(root,path)),"Broken local link: "+link);
 }
});
