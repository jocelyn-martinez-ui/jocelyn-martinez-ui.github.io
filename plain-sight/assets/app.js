(()=>{'use strict';
 const toggle=document.querySelector('[data-nav-toggle]'),nav=document.querySelector('#site-nav');
 if(toggle&&nav){toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));toggle.textContent=open?'Close −':'Menu +';nav.classList.toggle('is-open',open)});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{toggle.setAttribute('aria-expanded','false');toggle.textContent='Menu +';nav.classList.remove('is-open')}));}
 const filters=document.querySelectorAll('[data-filter]'),cards=document.querySelectorAll('[data-series]'),count=document.querySelector('#project-count');
 if(filters.length){filters.forEach(b=>b.addEventListener('click',()=>{const selected=b.dataset.filter;let visible=0;filters.forEach(x=>x.setAttribute('aria-pressed',String(x===b)));cards.forEach(c=>{const on=selected==='all'||c.dataset.series===selected;c.hidden=!on;if(on)visible++});if(count)count.textContent=visible+' series shown';}));}
 const form=document.querySelector('#contact-form'),msg=document.querySelector('#form-message');
 if(form&&msg){form.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;msg.textContent='This is a portfolio-only form demonstration. Your message was not sent. Please use the email link instead.';msg.focus();});}
})();
