(()=>{
 const range=document.getElementById('reviewRange'),reveal=document.getElementById('afterReveal'),compare=document.getElementById('compare'),after=document.getElementById('afterImage'),value=document.getElementById('rangeValue');
 function size(){if(!range||!compare)return;reveal.style.width=range.value+'%';after.style.width=compare.clientWidth+'px';if(value)value.textContent=range.value+'% final composition';}
 range?.addEventListener('input',size);window.addEventListener('resize',size);size();
 const proof=document.getElementById('proofSheet'),trim=document.getElementById('trimSwitch'),safe=document.getElementById('safeSwitch');
 function guides(){proof?.classList.toggle('show-trim',Boolean(trim?.checked));proof?.classList.toggle('show-safe',Boolean(safe?.checked));}
 trim?.addEventListener('change',guides);safe?.addEventListener('change',guides);guides();
})();
