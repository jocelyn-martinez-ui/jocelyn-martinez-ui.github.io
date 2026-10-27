import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

// Production state transitions with a small DOM double. Browser layout and
// keyboard checks are separate; this does not pretend to emulate a browser.
const source = fs.readFileSync(new URL('../experiences/experience.js', import.meta.url), 'utf8');
function load(app='imhere', search='') {
  const root={innerHTML:'',querySelector:s=>s==='main'?{appendChild(){}}:null,querySelectorAll:()=>[],addEventListener(){}};
  const toast={textContent:'',classList:{add(){},remove(){}}};
  const document={body:{dataset:{app},classList:{add(){},remove(){},toggle(){}}},querySelector:s=>s==='#app'?root:s==='#status'?toast:null,querySelectorAll:()=>[],createElement:()=>({})};
  const context={document,location:{search},URLSearchParams,window:{scrollTo(){}},matchMedia:()=>({matches:false}),setTimeout:()=>1,clearTimeout(){}};
  const expose=`globalThis.api={beginCorrection,saveAttendanceCorrection,reconstructionAction,depthAction,attendanceRows,attendanceWorkspace,correctionScreen,comparisonBench,replaceComparedSlot,studentCorrectionNotes,render,
    state:()=>JSON.parse(JSON.stringify({roster,attendanceAudit,correction,lastCorrection,view,compared:[...compared]})),
    setStatus:(i,s)=>roster[i]=s,setQuery:q=>rosterQuery=q,setFilter:f=>rosterFilter=f,setView:v=>view=v,setCompared:ids=>compared=new Set(ids),setHighlight:v=>highlightShared=v,markup:()=>root.innerHTML};`;
  assert.ok(source.endsWith('render();\n})();\n'));
  vm.runInNewContext(source.replace(/render\(\);\n\}\)\(\);\n$/,expose+'\n})();'),context);
  return context.api;
}
test('proposals require a bounded explanation before any attendance mutation',()=>{
  const a=load();assert.equal(a.beginCorrection(3,'Present'),true);
  assert.match(a.saveAttendanceCorrection('  ').error,/Explain/);
  assert.match(a.saveAttendanceCorrection('x'.repeat(501)).error,/500/);
  assert.equal(a.state().roster[3],'Needs review');assert.equal(a.state().attendanceAudit.length,0);
  assert.match(a.correctionScreen(),/Current record/);assert.match(a.correctionScreen(),/Proposed record/);
});
test('cancel preserves the record and returns to the originating review queue',()=>{
  const a=load();a.setView('reviews');a.beginCorrection(3,'Absent');a.depthAction('cancel-correction');
  assert.equal(a.state().view,'reviews');assert.equal(a.state().correction,null);
  assert.equal(a.state().roster[3],'Needs review');assert.equal(a.state().attendanceAudit.length,0);
});
test('one saved correction appears in the shared record, student context and audit',()=>{
  const a=load();a.beginCorrection(0,'Present');assert.equal(a.saveAttendanceCorrection('  Confirmed sample participation.  ').returnView,'faculty');
  const s=a.state();assert.equal(s.roster.join('|'),'Present|Present|Present|Needs review');assert.equal(s.attendanceAudit.length,1);
  assert.equal(s.attendanceAudit[0].from,'Not checked in');assert.equal(s.attendanceAudit[0].reason,'Confirmed sample participation.');
  assert.match(a.studentCorrectionNotes(),/Confirmed sample participation/);assert.match(a.attendanceWorkspace(false),/Undo correction/);
});
test('undo appends a reversal without erasing the explanation',()=>{
  const a=load();a.beginCorrection(3,'Present');a.saveAttendanceCorrection('Reviewed sample record.');a.reconstructionAction('undo-correction');
  const s=a.state();assert.equal(s.roster[3],'Needs review');assert.equal(s.attendanceAudit.length,2);
  assert.equal(s.attendanceAudit[0].reason,'Reviewed sample record.');assert.equal(s.attendanceAudit[1].by,'Faculty undo');assert.equal(s.lastCorrection,null);
});
test('stale save and stale undo do not overwrite a later status',()=>{
  const a=load();a.beginCorrection(3,'Present');a.setStatus(3,'Absent');
  assert.match(a.saveAttendanceCorrection('Reviewed.').error,/record changed/);assert.equal(a.state().roster[3],'Absent');assert.equal(a.state().attendanceAudit.length,0);
  a.beginCorrection(3,'Present');a.saveAttendanceCorrection('Reviewed later record.');a.setStatus(3,'Needs review');a.reconstructionAction('undo-correction');
  assert.equal(a.state().roster[3],'Needs review');assert.equal(a.state().attendanceAudit.length,1);
});
test('invalid and no-op proposals are rejected',()=>{
  const a=load();for(const pair of [[-1,'Present'],[99,'Present'],[1.5,'Present'],[0,'Unknown'],[1,'Present']])assert.equal(a.beginCorrection(...pair),false);
  assert.equal(a.state().correction,null);
});
test('query and status intersect; empty results clear the stale inspector',()=>{
  const a=load();a.setFilter('Present');a.setQuery('03');assert.equal(a.attendanceRows().length,1);assert.equal(a.attendanceRows()[0].id,2);
  a.setQuery('04');assert.equal(a.attendanceRows().length,0);const html=a.attendanceWorkspace(false);
  assert.match(html,/No matching records/);assert.match(html,/No record selected/);assert.doesNotMatch(html,/id="inspector-status"/);
});
test('user explanations are escaped in history and contextual review',()=>{
  const a=load();a.beginCorrection(0,'Present');a.saveAttendanceCorrection('<img src=x onerror=alert(1)>');
  const html=a.studentCorrectionNotes()+a.attendanceWorkspace(false);assert.match(html,/&lt;img/);assert.doesNotMatch(html,/<img src=x/);
});
test('replacing one perfume retains the other and rejects invalid or duplicate slots',()=>{
  const a=load('aurea','?scene=1&view=compare');assert.equal(a.state().compared.join(','),'0,2');
  assert.equal(a.replaceComparedSlot(1,1),true);assert.equal(a.state().compared.join(','),'0,1');
  for(const pair of [[1,0],[-1,2],[2,2],[0,99],[0,1.5]])assert.equal(a.replaceComparedSlot(...pair),false);
  assert.equal(a.state().compared.join(','),'0,1');
});
test('shared notes are named in text and incomplete comparisons preserve the remaining profile',()=>{
  const a=load('aurea');a.setCompared([0,1]);assert.match(a.comparisonBench(),/1 shared note: Bergamot/);assert.match(a.comparisonBench(),/is-shared/);
  a.setHighlight(false);assert.doesNotMatch(a.comparisonBench(),/is-shared/);assert.match(a.comparisonBench(),/1 shared note: Bergamot/);
  a.setCompared([1]);const html=a.comparisonBench();assert.match(html,/KEPT IN YOUR SHORTLIST/);assert.match(html,/Sol Mist/);assert.doesNotMatch(html,/data-action="compare:1"[^>]*>Compare Sol Mist/);
  a.setCompared([]);assert.match(a.comparisonBench(),/BEGIN YOUR SHORTLIST/);
});
test('shared renderer supports all six projects and key deep links',()=>{
  const routes={imhere:['faculty','reviews','student','history','directory','audit','correction'],aurea:['discover','compare','detail','finder','archive','paper'],holland:['discover','detail','walk','builder','paper'],loopline:['dashboard','create','confirmed','tracking'],novella:['discover','reader','blind','passages','paper'],nutriva:['tonight','recipe','pantry','grocery','paper']};
  for(const [app,views]of Object.entries(routes))for(const view of views){const a=load(app,'?scene=1&view='+view);assert.doesNotThrow(()=>a.render(),app+':'+view);assert.match(a.markup(),/<main/);assert.doesNotMatch(a.markup(),/\bundefined\b/);}
});
