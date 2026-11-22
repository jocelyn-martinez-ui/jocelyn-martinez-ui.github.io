(() => {
  "use strict";
  const status=document.getElementById("pt-status");
  const history=document.getElementById("pt-history");
  const feedback=document.getElementById("pt-feedback");
  const request=document.getElementById("pt-request");
  const resolve=document.getElementById("pt-resolve");
  const reset=document.getElementById("pt-reset");
  if(!status||!history||!feedback||!request||!resolve||!reset)return;
  const queue=document.getElementById("pt-queue-state");
  const mirror=document.querySelector("[data-queue-mirror]");
  const trail=[];
  function transition(state) {
    const updates={
      open:{label:"Open",note:"No action taken",announcement:"Example reset to open. No action is stored."},
      context:{label:"Awaiting context",note:"Context requested (sample)",announcement:"Sample report changed to awaiting context. The next step is made explicit."},
      resolved:{label:"Resolved",note:"Resolved (sample)",announcement:"Sample report marked resolved. In a real product this action would require authorization and an audit record."}
    };
    const current=updates[state];if(!current)return;
    status.dataset.state=state;status.textContent=current.label;
    if(state==="open")trail.length=0;
    else trail.push(current.note);
    history.textContent=trail.length?trail.join(" · "):current.note;
    if(queue)queue.textContent=current.label;
    if(mirror)mirror.textContent=current.label;
    feedback.textContent=current.announcement+" The example discussion remains public.";
    request.disabled=state!=="open";resolve.disabled=state==="resolved";
  }
  request.addEventListener("click",()=>{transition("context");resolve.focus()});
  resolve.addEventListener("click",()=>{transition("resolved");reset.focus()});
  reset.addEventListener("click",()=>transition("open"));
})();