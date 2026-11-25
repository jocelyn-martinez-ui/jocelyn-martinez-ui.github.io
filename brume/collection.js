(() => {
  "use strict";

  const rows = Array.from(document.querySelectorAll(".register-row"));
  const editions = new Map();
  for (const row of rows) {
    const plates = new Map();
    for (const figure of row.querySelectorAll("figure[data-light]")) {
      const img = figure.querySelector("img");
      plates.set(figure.dataset.light, {
        src: img.getAttribute("src"),
        alt: img.alt,
        lightName: figure.querySelector("strong").textContent,
        note: figure.querySelector("figcaption span").textContent
      });
    }
    editions.set(row.dataset.finish, {
      name: row.querySelector("h3 span").textContent,
      code: row.dataset.code,
      signature: row.dataset.signature,
      plates
    });
  }
  if (!editions.has("ivory")) return;

  const selectors = document.getElementById("selectors");
  const compareSelect = document.getElementById("compare-light");
  const register = document.getElementById("all-studies");
  const primary = document.getElementById("main-photo");
  const photoLink = document.getElementById("view-file");
  const title = document.getElementById("product-title");
  const status = document.getElementById("selection-status");
  const jumpLinks = Array.from(document.querySelectorAll("[data-jump]"));
  const pickLinks = Array.from(document.querySelectorAll("[data-pick]"));
  const comparePhotos = Array.from(document.querySelectorAll("[data-edition]"));
  let selected;

  // Edition fragments point to their static contact sheets until the viewer is ready.
  // After enhancement, those same links bring visitors to the active product above.
  for (const finish of editions.keys()) {
    document.getElementById(finish).removeAttribute("id");
    const target = document.createElement("span");
    target.id = finish;
    target.className = "edition-target";
    target.setAttribute("aria-hidden", "true");
    document.querySelector(".product").prepend(target);
  }

  function readSelection() {
    const url = new URL(location.href);
    const fragment = url.hash.slice(1);
    const finish = editions.has(fragment) ? fragment : url.searchParams.get("finish");
    const name = editions.has(finish) ? finish : "ivory";
    const edition = editions.get(name);
    const light = url.searchParams.get("light");
    return { finish: name, light: edition.plates.has(light) ? light : edition.signature };
  }

  function locationFor(finish, light, section) {
    const url = new URL(location.href);
    url.searchParams.set("light", light);
    if (section) url.searchParams.set("finish", finish);
    else url.searchParams.delete("finish");
    url.hash = section || finish;
    return url;
  }

  function display(announce = false) {
    selected = readSelection();
    const { finish, light } = selected;
    const edition = editions.get(finish);
    const plate = edition.plates.get(light);
    const titleText = edition.name + " / " + plate.lightName;

    primary.setAttribute("src", plate.src);
    primary.alt = plate.alt;
    photoLink.setAttribute("href", plate.src);
    photoLink.setAttribute("aria-label", "Open the full " + edition.name + " " + light + " photograph");
    document.getElementById("current-name").textContent = titleText;
    document.getElementById("current-code").textContent = edition.code;
    document.getElementById("observation").textContent = plate.note;
    for (const input of selectors.querySelectorAll("input")) {
      input.checked = input.value === selected[input.name];
    }
    compareSelect.value = light;

    for (const entry of comparePhotos) {
      const comparePlate = editions.get(entry.dataset.edition).plates.get(light);
      const img = entry.querySelector("img");
      img.setAttribute("src", comparePlate.src);
      img.alt = comparePlate.alt;
    }
    for (const link of pickLinks) {
      const name = link.dataset.pick;
      link.href = locationFor(name, light).href;
      link.setAttribute("aria-label", "Explore " + editions.get(name).name + " in " + light + " light");
    }
    for (const link of jumpLinks) {
      link.href = locationFor(finish, light, link.dataset.jump).href;
    }
    if (announce === "comparison") {
      status.textContent = "Comparing Ivory, Amber and Plum in " + light + " light.";
    } else if (announce) {
      status.textContent = titleText + ". " + plate.note;
    }
  }

  function navigate(url, announce) {
    if (url.href !== location.href) history.pushState(null, "", url);
    display(announce);
  }

  function ordinaryClick(event) {
    return !event.defaultPrevented && event.button === 0 &&
      !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey;
  }

  selectors.addEventListener("change", event => {
    const { name, value } = event.target;
    const finish = name === "finish" ? value : selected.finish;
    const light = name === "light" ? value : selected.light;
    navigate(locationFor(finish, light), true);
  });

  compareSelect.addEventListener("change", () => {
    navigate(locationFor(selected.finish, compareSelect.value, "compare"), "comparison");
  });

  for (const link of pickLinks) {
    link.addEventListener("click", event => {
      if (!ordinaryClick(event)) return;
      event.preventDefault();
      navigate(new URL(link.href), true);
      title.focus({ preventScroll: true });
      document.querySelector(".product").scrollIntoView({ block: "start" });
    });
  }
  for (const link of jumpLinks) {
    link.addEventListener("click", event => {
      if (!ordinaryClick(event)) return;
      event.preventDefault();
      navigate(new URL(link.href), false);
      const section = document.getElementById(link.dataset.jump);
      section.focus({ preventScroll: true });
      section.scrollIntoView({ block: "start" });
    });
  }

  function restore() {
    const fragment = location.hash.slice(1);
    if (fragment === "register" || fragment.startsWith("sheet-")) register.open = true;
    display();
  }

  // Restore the checked radio, comparison panel, photograph and caption together.
  window.addEventListener("popstate", restore);
  window.addEventListener("hashchange", restore);
  window.addEventListener("pageshow", restore);
  register.open = false;
  restore();
  selectors.hidden = false;
  document.getElementById("compare-select-label").hidden = false;
})();
