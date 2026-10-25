// Node built-in tests. Run: node --test proof/marketing/qa.test.mjs
import test from "node:test";import assert from "node:assert/strict";
import {existsSync,readFileSync} from "node:fs";import {dirname,resolve,join} from "node:path";import {fileURLToPath} from "node:url";import {Script} from "node:vm";
const root=dirname(fileURLToPath(import.meta.url)),read=x=>readFileSync(join(root,x),"utf8"),exists=x=>existsSync(join(root,x));
const six=Array.from({length:6},(_,i)=>String(i+1).padStart(2,"0"));
test("Twelve self-contained carousel SVG masters, plus stories and digital ads",()=>{
 const paths=[...six.map(n=>"social/carousel-a-"+n+".svg"),...six.map(n=>"social/carousel-b-"+n+".svg"),"social/story-01.svg","social/story-02.svg",...["square-awareness","portrait-process","landscape-read","display-banner"].map(n=>"ads/"+n+".svg")];
 assert.equal(paths.length,18);
 for(const p of paths){const svg=read(p);assert.match(svg,/<svg /);assert.match(svg,/<title>/);assert.match(svg,/data:image\/webp;base64,/);assert.doesNotMatch(svg,/<image\b[^>]+href="(?:\.\.\/|https?:)/)}
});
test("Four responsive marketing emails contain live text, Outlook fallback, accessible images and TXT alternatives",()=>{
 for(const p of ["01-edition-launch","02-editorial-discovery","03-process-and-revisions","04-across-formats"]){
 const x=read("email/"+p+".html");
 assert.equal((x.match(/<table\b/g)||[]).length,(x.match(/<\/table>/g)||[]).length);
 assert.match(x,/<!--\[if mso\]>/);assert.match(x,/display:none/);assert.match(x,/<h1 class="title"/);assert.match(x,/alt="/);
 assert.match(x,/https:\/\/jocelyn-martinez-ui.github.io/);assert.ok(exists("email/"+p+".txt"));
 }
});
test("Physical trim-and-bleed sources are present",()=>{
 for(const [path,w,h] of [["print/advert-a5.svg",154,216],["print/postcard-a6.svg",154,111],["print/sell-sheet-a4.svg",216,303]])assert.match(read(path),new RegExp("width=\\""+w+"mm\\" height=\\""+h+"mm\\""));
});
test("Interactive campaign script and two browser motion previews are available",()=>{
 new Script(read("campaign.js"));for(const n of ["01-contact-to-title","02-revision-pulse"]){const x=read("motion/"+n+".html");assert.match(x,/prefers-reduced-motion/);assert.match(x,/PAUSE MOTION/);}
});
test("Internal campaign case page asset paths resolve",()=>{
 const src=read("index.html");const attrs=[...src.matchAll(/(?:src|href)="([^"]+)"/g)].map(x=>x[1]);
 for(const raw of attrs){if(/^(https?:|#|mailto:|data:)/.test(raw))continue;let p=raw.split(/[?#]/)[0];if(p)assert.ok(existsSync(resolve(root,p)),"Missing source: "+raw);}
});
