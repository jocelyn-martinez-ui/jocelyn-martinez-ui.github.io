document.querySelectorAll("[data-enhance]").forEach((element) => {
  element.hidden = false;
});

const authorize = document.getElementById("authorize");
const undo = document.getElementById("undo-repair");

if (authorize && undo) {
  const ticket = document.getElementById("work-order");
  const status = document.getElementById("repair-status");
  const next = document.getElementById("repair-next");

  function showAuthorization(approved) {
    status.textContent = approved ? "Authorized for repair" : "Awaiting authorization";
    next.textContent = approved
      ? "The shop can now schedule the approved work. Pickup is pending."
      : "The shop is waiting for the driver to authorize the proposed repair.";
    ticket.classList.toggle("authorized", approved);
    authorize.hidden = approved;
    undo.hidden = !approved;
    (approved ? undo : authorize).focus();
  }

  authorize.addEventListener("click", () => showAuthorization(true));
  undo.addEventListener("click", () => showAuthorization(false));
}

const playPulse = document.getElementById("play-pulse");
if (playPulse) {
  const trace = document.querySelector("#pulse-trace .wave");
  const caption = document.getElementById("pulse-caption");
  playPulse.addEventListener("click", () => {
    caption.textContent = "Two pulses. A short, strong pulse followed by a softer, longer one.";
    if (!trace.animate || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    trace.getAnimations().forEach((animation) => animation.cancel());
    const length = trace.getTotalLength();
    trace.animate(
      [
        { strokeDasharray: length, strokeDashoffset: length },
        { strokeDasharray: length, strokeDashoffset: 0 }
      ],
      { duration: 950, easing: "linear" }
    );
  });
}
