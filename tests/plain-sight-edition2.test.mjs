import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

const root=path.resolve(import.meta.dirname,'../plain-sight');
const pages=['index','case-study','publication','gestures','arrangements','in-between','studio','contact','email','motion'];
const read=p=>fs.readFileSync(path.join(root,p),'utf8');

test('Edition 02 keeps all studio pages and a consistent visual system',()=>{
  for(const name of pages){
    const file=read(name+'.html');
    assert.match(file,/editorial-v2\.css/,'Missing Edition 02 style in '+name);
    assert.match(file,/class="topbar wrap"/,'Missing navigation '+name);
    if(file.includes('<img')) assert.match(file,/alt="/,'Missing image descriptions '+name);
  }
  assert.match(read('index.html'),/v2-hero-stage/);
  assert.match(read('index.html'),/v2-sequence-grid/);
  assert.match(read('case-study.html'),/v2-type-plates/);
  assert.match(read('assets/editorial-v2.css'),/Bodoni\+Moda/);
  assert.match(read('assets/editorial-v2.css'),/IBM\+Plex\+Mono/);
});
test('All project pages resolve local links, images and scripts',()=>{
 for(const name of pages){
  const file=read(name+'.html');
  for(const match of file.matchAll(/(?:href|src)="([^"]+)"/g)){
    const value=match[1];
    if(/^(https?:|mailto:|tel:|#|data:)/.test(value))continue;
    const target=value.split(/[?#]/)[0];
    assert.ok(fs.existsSync(path.join(root,target))||fs.existsSync(path.resolve(root,path.dirname(name+'.html'),target)),name+' missing '+value);
  }
 }
});
test('Print editions and editable SVG work remain source artifacts',()=>{
 for(const [file,min] of [['downloads/PLAIN_SIGHT_Studies_01-03.pdf',100_000],['downloads/PLAIN_SIGHT_Identity_and_Production_Guide.pdf',100_000]]){
   const full=path.join(root,file);
   assert.ok(fs.statSync(full).size>min);
   assert.equal(fs.readFileSync(full).subarray(0,4).toString(),'%PDF');
 }
 const poster=read('assets/posters/poster-06.svg');
 assert.match(poster,/<svg/);assert.match(poster,/<text/);
 assert.match(read('docs/EDITORIAL_REFINEMENT_MASTER_PROMPT.md'),/Pinterest/);
});
