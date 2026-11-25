import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";
import vm from "node:vm";

const base = new URL("../", import.meta.url);
const markup = readFileSync(new URL("collection.html", base), "utf8");
const controller = readFileSync(new URL("collection.js", base), "utf8");
const gallery = [...markup.matchAll(/<section class="register-row" data-finish="([^"]+)" data-code="([^"]+)" data-signature="([^"]+)"[^>]*>([\s\S]*?)<\/section>/g)];
const finishes = ["ivory", "amber", "plum"];
const lights = ["morning", "afternoon", "evening"];
const publicURL = "https://example.test/brume/collection.html";

function fixtureElement(initial = {}) {
  return {
    events: {},
    addEventListener(event, listener) { this.events[event] = listener; },
    setAttribute(name, value) { this[name] = value; },
    getAttribute(name) { return this[name]; },
    removeAttribute(name) { delete this[name]; },
    scrollIntoView() {},
    focus() {},
    ...initial
  };
}

// Exercise the real URL and rendering code against the shipped contact sheet.
// The fixture handles only the few document operations the controller uses.
function openAt(suffix) {
  const location = new URL(publicURL + suffix);
  const byId = new Map([...markup.matchAll(/\bid="([^"]+)"/g)].map(([, id]) => [id, fixtureElement({id})]));
  const radios = [...markup.matchAll(/type="radio" name="(finish|light)" value="([^"]+)"/g)]
    .map(([, name, value]) => fixtureElement({name, value}));
  byId.get("selectors").querySelectorAll = () => radios;
  const rows = gallery.map(([, finish, code, signature, inner]) => {
    const figures = [...inner.matchAll(/<figure data-light="([^"]+)">([\s\S]*?)<\/figure>/g)]
      .map(([, light, content]) => {
        const img = fixtureElement({
          src: content.match(/src="([^"]+)"/)[1],
          alt: content.match(/alt="([^"]+)"/)[1]
        });
        const parts = {
          img,
          strong: {textContent: content.match(/<strong>([^<]+)<\/strong>/)[1]},
          "figcaption span": {textContent: content.match(/<span>([^<]+)<\/span>/)[1]}
        };
        return fixtureElement({dataset: {light}, querySelector: selector => parts[selector]});
      });
    return fixtureElement({
      dataset: {finish, code, signature},
      querySelector: () => ({textContent: inner.match(/<span id="[^"]+">([^<]+)<\/span>/)[1]}),
      querySelectorAll: () => figures
    });
  });
  const comparison = finishes.map(edition => {
    const img = fixtureElement();
    return fixtureElement({dataset: {edition}, querySelector: () => img});
  });
  const jumps = ["main", "compare", "materials"].map(jump => fixtureElement({dataset: {jump}}));
  const picks = finishes.map(pick => fixtureElement({dataset: {pick}}));
  const groups = {".register-row": rows, "[data-edition]": comparison, "[data-jump]": jumps, "[data-pick]": picks};
  const document = {
    querySelectorAll: selector => groups[selector],
    querySelector: () => ({prepend(node) { byId.set(node.id, node); }}),
    getElementById: id => byId.get(id),
    createElement: () => fixtureElement()
  };
  const window = fixtureElement();
  const history = {pushState(_data, _unused, url) { location.href = url.href; }};
  vm.runInNewContext(controller, {URL, location, document, history, window});
  return {byId, radios, comparison, jumps, picks, location, window};
}

test("the script-free register links every unique finished WebP and opens by default", () => {
  assert.match(markup, /<details id="all-studies" open>/);
  assert.match(markup, /<noscript>[\s\S]*?href="#register"[\s\S]*?<\/noscript>/);
  assert.deepEqual(gallery.map(row => row[1]), finishes);
  const imageBodies = new Set();
  for (const [, finish, , , inner] of gallery) {
    assert.match(inner, new RegExp('<span id="' + finish + '">'));
    for (const time of lights) {
      const path = 'images/register/' + finish + '-' + time + '.webp';
      assert.ok(inner.includes('href="' + path + '"'));
      assert.ok(inner.includes('src="' + path + '"'));
      const bytes = readFileSync(new URL(path, base));
      assert.equal(bytes.toString("ascii", 8, 12), "WEBP");
      imageBodies.add(bytes.toString("base64"));
    }
  }
  assert.equal(imageBodies.size, 9);
});

test("each shared URL restores the photograph, native radio choices and matching comparison light", () => {
  for (const finish of finishes) {
    for (const light of lights) {
      const ui = openAt("?light=" + light + "#" + finish);
      const expected = "images/register/" + finish + "-" + light + ".webp";
      assert.equal(ui.byId.get("main-photo").src, expected);
      assert.equal(ui.byId.get("view-file").href, expected);
      assert.deepEqual(ui.radios.filter(input => input.checked).map(input => input.value), [finish, light]);
      for (const row of ui.comparison) assert.ok(row.querySelector("img").src.endsWith("-" + light + ".webp"));
    }
  }
});

test("bare finish fragments and invalid light names fall back to the finish's photographed signature", () => {
  for (const [, finish, , signature] of gallery) {
    for (const query of ["", "?light=invalid"]) {
      const ui = openAt(query + "#" + finish);
      assert.equal(ui.byId.get("compare-light").value, signature);
    }
  }
});

test("changing room light preserves the finish in links and after history restoration", () => {
  const ui = openAt("?light=evening#plum");
  ui.byId.get("selectors").events.change({target: {name: "light", value: "morning"}});
  assert.equal(ui.location.href, publicURL + "?light=morning#plum");
  for (const link of ui.jumps) {
    assert.equal(new URL(link.href).searchParams.get("finish"), "plum");
    assert.equal(new URL(link.href).searchParams.get("light"), "morning");
  }
  ui.location.href = publicURL + "?light=evening&finish=plum#compare";
  ui.window.events.popstate();
  assert.equal(ui.byId.get("current-name").textContent, "Plum / Evening");
  assert.equal(ui.byId.get("compare-light").value, "evening");
});
