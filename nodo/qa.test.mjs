// Run: node --test nodo/qa.test.mjs
// Static source tests; not a browser, email-client, regulatory or vendor preflight.
import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync,existsSync} from "node:fs";
import {dirname,join} from "node:path";
import {fileURLToPath} from "node:url";
const root=dirname(fileURLToPath(import.meta.url));
const read=relative=>readFileSync(join(root,relative),"utf8");
const exists=relative=>existsSync(join(root,relative));
const social=[
 "social/feed-01-launch.svg","social/feed-02-clip.svg","social/feed-03-wrap.svg","social/feed-04-guide.svg",
 ...Array.from({length:6},(_,i)=>"social/carousel-0"+(i+1)+".svg"),
 "social/story-01-launch.svg","social/story-02-product.svg","social/story-03-reset.svg","social/linkedin-01.svg"
];
const names=["01-launch","02-the-system","03-the-reset"];
const print=[
 "print/source/label-clip-r03.svg","print/source/label-wrap-r03.svg","print/source/label-guide-r03.svg",
 "print/source/ad-a5.svg","print/source/postcard-a6.svg",
 "print/source/insert-a6.svg","print/source/sell-sheet-a4.svg",
 "print/archive/label-clip-r01.svg","print/archive/label-clip-r02.svg"
];
test("all fourteen social masters exist with accessible SVG descriptions",()=>{
 assert.equal(social.length,14);
 for(const path of social){const s=read(path);assert.match(s,/<svg /);assert.match(s,/<title /);assert.match(s,/<desc /);assert.match(s,/<\/svg>/)}
});
test("emails have preheaders, presentation tables, Outlook fallback and plain text",()=>{
 for(const name of names){
  const html=read("email/"+name+".html");
  assert.match(html,/<table role="presentation"/);
  assert.match(html,/display:none/);
  assert.match(html,/<!--\[if mso\]>/);
  assert.match(html,/<h1 /);
  assert.equal((html.match(/<table\b/g)||[]).length,(html.match(/<\/table>/g)||[]).length);
  assert.ok(exists("email/"+name+".txt"));
 }
});
test("dimensioned label and collateral source revisions exist",()=>{
 for(const p of print)assert.ok(exists(p),p);
 assert.match(read(print[0]),/width="96mm" height="136mm"/);
 assert.match(read(print[7]),/R01/);
});
test("case studies include fictional disclosure and artwork source references",()=>{
 const marketing=read("index.html"),production=read("production.html");
 assert.match(marketing,/fictional/i);
 assert.match(production,/fictional/i);
 for(const path of social)assert.ok(marketing.includes(path),"Case page missing "+path);
 for(const path of print)assert.ok(production.includes(path),"Print page missing "+path);
 for(const name of names)assert.ok(marketing.includes("email/"+name+".html"));
});
test("manifest counts match digital asset groups",()=>{
 const manifest=JSON.parse(read("manifest.json"));
 assert.equal(manifest.asset_groups.find(x=>x.category==="social").count,14);
 assert.equal(manifest.asset_groups.find(x=>x.category==="email").count,3);
});
