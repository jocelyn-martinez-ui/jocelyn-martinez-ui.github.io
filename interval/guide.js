(() => {
const spreads=[[1],[2,3],[4,5],[6,7],[8,9],[10,11],[12]],$=s=>document.querySelector(s);let current=0;
function show(){const n=Number((location.hash.match(/page-(\d+)/)||[])[1]||1);current=Math.max(0,spreads.findIndex(p=>p.includes(n)));document.querySelectorAll('[data-spread]').forEach((el,i)=>el.hidden=i!==current);$('#previous-spread').disabled=current===0;$('#next-spread').disabled=current===spreads.length-1;$('#page-select').value=String(n>=1&&n<=12?n:1);$('#reader-status').textContent=(spreads[current].length===1?'Page '+spreads[current][0]:'Pages '+spreads[current].join('–'))+' / 12';}
$('#previous-spread').addEventListener('click',()=>{if(current>0)location.hash='page-'+spreads[current-1][0];});$('#next-spread').addEventListener('click',()=>{if(current<spreads.length-1)location.hash='page-'+spreads[current+1][0];});$('#page-select').addEventListener('change',e=>location.hash='page-'+e.target.value);window.addEventListener('hashchange',show);show();
})();
