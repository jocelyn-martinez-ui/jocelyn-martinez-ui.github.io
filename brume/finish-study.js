// A fragment remains a usable edition link when scripts are unavailable.
(() => {
  const cover = document.getElementById("campaign");
  if (!cover) return;
  const links = Array.from(cover.querySelectorAll("[data-finish]"));
  const editions = new Set(links.map(link => link.dataset.finish));
  const fromUrl = () => location.hash.slice(1).toLowerCase();

  function select(finish) {
    cover.dataset.selected = finish;
    for (const link of links) {
      if (link.dataset.finish === finish) link.setAttribute("aria-current", "true");
      else link.removeAttribute("aria-current");
    }
  }

  select(editions.has(fromUrl()) ? fromUrl() : "plum");
  for (const link of links) {
    link.addEventListener("click", event => {
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.altKey || event.shiftKey) return;
      event.preventDefault();
      if (location.hash !== link.hash) history.pushState(null, "", link.hash);
      select(link.dataset.finish);
    });
  }
  function restore() {
    const finish = fromUrl();
    if (editions.has(finish)) select(finish);
    else if (!finish || finish === "campaign") select("plum");
  }
  addEventListener("hashchange", restore);
  addEventListener("popstate", restore);
})();
