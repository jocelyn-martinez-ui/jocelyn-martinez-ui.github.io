import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const root=path.resolve(import.meta.dirname,'../plain-sight');
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const sources=JSON.parse(read('src/collection.json'));
const pages=JSON.parse(read('src/publication-pages.json'));
const model=require('../plain-sight/assets/model.js');
const names=['index','case-study','publication','gestures','arrangements','in-between','studio','contact','email','motion','light-table'];

test('five distinct source scenes own exactly eleven unique derivative crops',()=>{
 assert.equal(sources.length,5);
 const sourceIds=sources.map(x=>x.id),cropIds=sources.flatMap(x=>x.crops.map(c=>c.id));
 assert.equal(new Set(sourceIds).size,5);assert.equal(cropIds.length,11);assert.equal(new Set(cropIds).size,11);
 for(const id of cropIds)assert.ok(!sourceIds.includes(id));
 assert.deepEqual(sources.reduce((a,x)=>(a[x.series]=(a[x.series]||0)+1,a),{}),{gestures:2,arrangements:2,'in-between':1});
});
test('every source and derivative has an asset, meaningful description and valid publication destination',()=>{
 for(const source of sources)for(const item of [source,...source.crops]){
  assert.ok(fs.existsSync(path.join(root,'assets/images',item.id+'.webp')));
  assert.ok(fs.existsSync(path.join(root,'assets/thumbs',item.id+'.webp')));
  assert.ok(item.alt.length>50);assert.ok(item.note.length>70);assert.ok(item.width>0&&item.height>0);
  assert.equal(pages[item.page-1].sourceId,source.id,'Publication lineage mismatch: '+item.id);
 }
});
test('filtering counts original sources and does not mutate the collection',()=>{
 const before=JSON.stringify(sources);
 assert.equal(model.filterSources(sources,'all').length,5);
 assert.deepEqual(model.filterSources(sources,'gestures').map(x=>x.id),['gesture-seated','gesture-fabric']);
 assert.equal(model.filterSources(sources,'arrangements').length,2);assert.equal(model.filterSources(sources,'in-between').length,1);
 assert.equal(JSON.stringify(sources),before);
});
test('all eleven derivative selections round-trip to the correct parent',()=>{
 for(const source of sources)for(const crop of source.crops){
  const parsed=model.readState('?source='+source.id+'&crop='+crop.id,sources);
  assert.equal(parsed.source.id,source.id);assert.equal(parsed.crop.id,crop.id);
 }
});
test('a crop from a different source cannot be paired silently with the selected parent',()=>{
 const value=model.readState('?source=between-room&crop=gesture-fabric-detail',sources);
 assert.equal(value.source.id,'between-room');assert.equal(value.crop.id,'between-room-window');
});
test('invalid and missing URL state recovers to defined content without interpreting markup',()=>{
 for(const query of ['', '?source=missing&crop=missing&series=missing&look=missing', '?source=%3Cscript%3E']){
  const value=model.readState(query,sources);assert.equal(value.source.id,'gesture-seated');assert.equal(value.crop.id,'gesture-seated-detail');assert.equal(value.series,'all');assert.equal(value.look,null);
 }
});
test('publication page boundaries and malformed values recover predictably',()=>{
 for(const [input,expected] of [['-2',1],['0',1],['25',24],['99999',24],['1.5',1],['Infinity',1],['nope',1],['13',13]])assert.equal(model.readState('?page='+input,sources).page,expected);
});
test('manual sequence movement never wraps unexpectedly beyond either boundary',()=>{
 assert.equal(model.stepIndex(0,-1,5),0);assert.equal(model.stepIndex(4,1,5),4);assert.equal(model.stepIndex(2,1,5),3);assert.equal(model.stepIndex(2,-1,5),1);assert.equal(model.stepIndex(0,1,1),0);
});
test('URL changes preserve unrelated state and remove closed or default selections',()=>{
 assert.equal(model.query('?source=between-room&crop=between-room-chair',{look:'between-room'}),'?source=between-room&crop=between-room-chair&look=between-room');
 assert.equal(model.query('?source=between-room&look=between-room',{look:null}),'?source=between-room');
 assert.equal(model.query('?series=gestures',{series:'all'}),'');
});
test('all 24 publication records have exact previews and a readable text companion',()=>{
 assert.equal(pages.length,24);
 pages.forEach((p,i)=>{assert.equal(p.page,i+1);assert.ok(p.text.length>100);assert.ok(p.description.length>35);for(const prefix of ['page','thumb'])assert.ok(fs.statSync(path.join(root,'assets/publication',prefix+'-'+String(i+1).padStart(2,'0')+'.webp')).size>500);});
});
test('the three chapter routes form a complete cycle, with visible return links',()=>{
 for(const [current,next] of [['gestures','arrangements'],['arrangements','in-between'],['in-between','gestures']]){
  const file=read(current+'.html');assert.match(file,new RegExp('class="next-study" href="'+next+'\\.html"'));assert.match(file,/href="index\.html#work">← All studies/);
  for(const chapter of ['gestures','arrangements','in-between'])assert.ok(file.includes('href="'+chapter+'.html"'));
 }
});
test('public pages retain one heading, one styling system and non-script navigation',()=>{
 for(const name of names){const file=read(name+'.html');assert.equal([...file.matchAll(/<h1(?:\s|>)/g)].length,1,name);assert.equal([...file.matchAll(/rel="stylesheet"/g)].length,1,name);assert.ok(!file.includes('editorial-v2.css'));assert.match(file,/href="#main"/);assert.match(file,/href="contact\.html"/);}
 assert.ok(!read('assets/styles.css').includes('@import'));
 assert.match(read('assets/styles.css'),/prefers-reduced-motion/);
});
test('all local page links and image/script references resolve, including fragment targets',()=>{
 for(const name of names){const file=read(name+'.html');for(const match of file.matchAll(/(?:href|src)="([^"]+)"/g)){
  const value=match[1].replaceAll('&amp;','&');if(/^(https?:|mailto:|tel:|data:)/.test(value))continue;
  const [base,fragment]=value.split('#'),rel=base.split('?')[0]||name+'.html';const target=path.resolve(root,rel);
  assert.ok(fs.existsSync(target),name+' missing '+value);
  if(fragment&&/\.html$/.test(target)){const targetText=fs.readFileSync(target,'utf8');assert.ok(targetText.includes('id="'+fragment+'"'),name+' missing fragment '+value);}
 }}
});
test('contact is a real email route, with no nonfunctional data-collection form',()=>{
 const file=read('contact.html');assert.match(file,/mailto:jocelyn\.wisteria@gmail\.com/);assert.ok(!/<form\b/.test(file));assert.match(file,/does not collect inquiries/);
});
test('original publication and editable campaign masters are preserved',()=>{
 for(const file of ['downloads/PLAIN_SIGHT_Studies_01-03.pdf','downloads/archive/PLAIN_SIGHT_Studies_Edition02.pdf','downloads/PLAIN_SIGHT_Identity_and_Production_Guide.pdf'])assert.equal(fs.readFileSync(path.join(root,file)).subarray(0,4).toString(),'%PDF');
 for(let i=1;i<=6;i++){const svg=read('assets/posters/poster-'+String(i).padStart(2,'0')+'.svg');assert.match(svg,/<svg/);assert.match(svg,/<text/);}
});
