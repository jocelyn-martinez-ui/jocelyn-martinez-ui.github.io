(() => {
  "use strict";
  const status=document.getElementById("pt-status");
  const history=document.getElementById("pt-history");
  const feedback=document.getElementById("pt-feedback");
  const request=document.getElementById("pt-request");
  const resolve=document.getElementById("pt-resolve");
  const reset=document.getElementById("pt-reset");
  if(!status||!history||!feedback||!request||!resolve||!reset)return;
  function transition(state) {
    const updates={
      open:{label:"Open",note:"No action taken",announcement:"Example reset to open. No action is stored."},
      context:{label:"Awaiting context",note:"Context requested (sample)",announcement:"Sample report changed to awaiting context. The next step is made explicit."},
      resolved:{label:"Resolved",note:"Resolved (sample)",announcement:"Sample report marked resolved. In a real product this action would require authorization and an audit record."}
    };
    const current=updates[state];if(!current)return;
    status.dataset.state=state;status.textContent=current.label;
    history.textContent=current.note;feedback.textContent=current.announcement;
    request.disabled=state!=="open";resolve.disabled=state==="resolved";
  }
  request.addEventListener("click",()=>transition("context"));
  resolve.addEventListener("click",()=>transition("resolved"));
  reset.addEventListener("click",()=>transition("open"));
})();