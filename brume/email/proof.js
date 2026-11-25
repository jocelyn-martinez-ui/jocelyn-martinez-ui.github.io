(() => {
  'use strict';
  const links = [...document.querySelectorAll('.letter-choice')];
  const frame = document.getElementById('letter-proof');
  const mat = document.getElementById('frame-mat');
  const surface = mat.parentElement;
  const radios = [...document.querySelectorAll('input[name="width"]')];
  const imagesOff = document.getElementById('hide-images');
  const status = document.getElementById('proof-status');
  let activeLink;
  let shownFile = frame.getAttribute('src');
  let heightObserver;
  let sizingFrame = 0;
  const selected = location.hash.slice(1);
  const narrowScreen = window.matchMedia('(max-width: 760px)').matches;
  radios.find(radio => radio.value === (narrowScreen ? '360' : '640')).checked = true;

  function sizeFrame() {
    cancelAnimationFrame(sizingFrame);
    sizingFrame = requestAnimationFrame(() => {
      const page = frame.contentDocument?.getElementById('proof-page');
      if (!page) return;
      const selectedWidth = Number(radios.find(radio => radio.checked).value);
      const padding = getComputedStyle(surface);
      const available = surface.clientWidth - parseFloat(padding.paddingLeft) - parseFloat(padding.paddingRight);
      if (!available) return;
      const width = selectedWidth === 360 ? Math.min(360, Math.floor(available)) : selectedWidth;
      const scale = Math.min(1, available / width);
      frame.style.width = `${width}px`;
      const height = Math.max(1, Math.ceil(page.getBoundingClientRect().height));
      frame.style.height = `${height}px`;
      frame.style.transform = `scale(${scale})`;
      mat.classList.add('is-sized');
      mat.style.width = `${width * scale}px`;
      mat.style.height = `${Math.ceil(height * scale)}px`;
    });
  }

  function setImageMode() {
    const documentInside = frame.contentDocument;
    const page = documentInside?.getElementById('proof-page');
    if (!page) return;
    page.querySelectorAll('img').forEach(image => {
      if (!('proofDisplay' in image.dataset)) image.dataset.proofDisplay = image.style.display;
      image.style.display = imagesOff.checked ? 'none' : image.dataset.proofDisplay;
      if (!image.alt) return;
      if (!image.nextElementSibling?.classList.contains('image-description')) {
        const alt = documentInside.createElement('p');
        alt.className = 'image-description';
        alt.textContent = image.alt;
        alt.style.cssText = 'margin:0;padding:16px 24px;font:16px/1.45 Arial,sans-serif;background:#e8e8dc;color:#30372b;border:1px dashed #88907e';
        image.after(alt);
      }
      image.nextElementSibling.hidden = !imagesOff.checked;
    });
    sizeFrame();
  }

  function prepareFrame() {
    heightObserver?.disconnect();
    const page = frame.contentDocument?.getElementById('proof-page');
    if (!page) return;
    frame.contentDocument.documentElement.style.overflow = 'hidden';
    setImageMode();
    if ('ResizeObserver' in window) {
      heightObserver = new ResizeObserver(sizeFrame);
      heightObserver.observe(page);
    }
    sizeFrame();
  }

  function activate(link) {
    if (!link || link === activeLink) return;
    activeLink = link;
    links.forEach(other => {
      if (other === link) other.setAttribute('aria-current', 'true');
      else other.removeAttribute('aria-current');
    });
    const file = link.getAttribute('href');
    const stem = file.replace(/\.html$/, '');
    const subject = link.dataset.subject;
    document.getElementById('subject').textContent = subject;
    document.getElementById('preheader').textContent = link.dataset.preheader;
    document.getElementById('web-file').href = file;
    document.getElementById('text-file').href = `${stem}.txt`;
    document.getElementById('source-file').href = `sources/${stem}.eml`;
    frame.title = `Email preview: ${subject}`;
    if (shownFile !== file) {
      // The outer page owns history so one Back action always restores one letter.
      shownFile = file;
      frame.contentWindow.location.replace(link.href);
    }
    status.textContent = `Showing ${subject}`;
  }

  links.forEach(link => link.addEventListener('click', event => {
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) return;
    event.preventDefault();
    activate(link);
    if (location.hash.slice(1) !== link.dataset.letter) history.pushState(null, '', `#${link.dataset.letter}`);
  }));
  function selectFromLocation() {
    activate(links.find(link => link.dataset.letter === location.hash.slice(1)) || links[0]);
  }
  window.addEventListener('hashchange', selectFromLocation);
  window.addEventListener('popstate', selectFromLocation);
  frame.addEventListener('load', prepareFrame);
  imagesOff.addEventListener('change', setImageMode);
  radios.forEach(radio => radio.addEventListener('change', sizeFrame));
  if ('ResizeObserver' in window) new ResizeObserver(sizeFrame).observe(surface);
  else window.addEventListener('resize', sizeFrame);

  document.querySelectorAll('.proof-controls, .enhanced-only').forEach(el => { el.hidden = false; });
  activate(links.find(link => link.dataset.letter === selected) || links[0]);
  prepareFrame();
})();
