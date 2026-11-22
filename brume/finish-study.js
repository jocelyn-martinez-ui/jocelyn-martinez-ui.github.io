(() => {
  const nav = document.querySelector(".finish-controls");
  if (!nav) return;
  const links = Array.from(nav.querySelectorAll("a[href^='#']"));
  const frames = links.map(link => document.getElementById(link.hash.slice(1)));
  if (frames.some(frame => !frame)) return;

  function show(hash) {
    const index = links.findIndex(link => link.hash === hash);
    links.forEach((link, i) => {
      const active = i === index;
      if (active) link.setAttribute("aria-current", "true");
      else link.removeAttribute("aria-current");
      frames[i].hidden = !active;
    });
  }

  function fromLocation() {
    const active = links.find(link => link.hash === location.hash);
    show((active || links[0]).hash);
  }

  links.forEach(link => link.addEventListener("click", event => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    if (link.hash !== location.hash) history.pushState(null, "", link.hash);
    show(link.hash);
  }));
  window.addEventListener("popstate", fromLocation);
  window.addEventListener("hashchange", fromLocation);
  fromLocation();
})();
