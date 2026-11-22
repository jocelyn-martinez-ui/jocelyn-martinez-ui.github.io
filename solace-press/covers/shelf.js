(() => {
  const shelf = document.querySelector("[data-solace-shelf]");
  if (!shelf) return;
  const links = Array.from(shelf.querySelectorAll("[data-cover]"));
  const entries = Array.from(shelf.querySelectorAll("[data-solace-item]"));
  function select(title) {
    const chosen = links.find(link => link.dataset.cover === title);
    if (!chosen) return;
    for (const link of links) {
      if (link === chosen) link.setAttribute("aria-current", "true");
      else link.removeAttribute("aria-current");
    }
    for (const entry of entries) entry.hidden = entry.dataset.solaceItem !== title;
  }
  function selectionFromUrl() {
    const match = links.find(link => link.hash === window.location.hash);
    select(match ? match.dataset.cover : links[0].dataset.cover);
  }
  shelf.addEventListener("click", event => {
    const link = event.target.closest("[data-cover]");
    if (!link || event.metaKey || event.ctrlKey || event.altKey || event.shiftKey) return;
    event.preventDefault();
    select(link.dataset.cover);
    if (window.location.hash !== link.hash) window.history.pushState(null, "", link.hash);
  });
  window.addEventListener("popstate", selectionFromUrl);
  window.addEventListener("hashchange", selectionFromUrl);
  selectionFromUrl();
})();
