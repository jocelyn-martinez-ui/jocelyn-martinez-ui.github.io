(() => {
  const viewports = {
    phone: { width: 390, height: 844 },
    desktop: { width: 1280, height: 800 },
  };
  const controls = document.querySelector('#screen-controls');
  const stage = document.querySelector('#stage');
  const sheet = document.querySelector('#sheet');
  const frame = document.querySelector('#live-collection');
  const output = document.querySelector('#dimensions');
  const panning = document.querySelector('#panning');
  const left = document.querySelector('#pan-left');
  const right = document.querySelector('#pan-right');
  const standalone = document.querySelector('#open-collection');
  const collection = new URL(standalone.href);

  function updatePanButtons() {
    left.disabled = stage.scrollLeft <= 1;
    right.disabled = stage.scrollLeft + stage.clientWidth >= stage.scrollWidth - 1;
  }

  function resize() {
    const name = controls.querySelector('[name="viewport"]:checked').value;
    const fit = controls.querySelector('[name="scale"]:checked').value === 'fit';
    const { width, height } = viewports[name];
    const scale = fit ? Math.min(1, stage.clientWidth / width) : 1;

    frame.style.width = width + 'px';
    frame.style.height = height + 'px';
    frame.style.transform = 'scale(' + scale + ')';
    sheet.dataset.viewport = name;
    sheet.style.width = Math.round(width * scale) + 'px';
    sheet.style.height = Math.round(height * scale) + 'px';
    output.textContent = width + ' × ' + height + ' CSS px · ' + Math.round(scale * 100) + '%';
    panning.hidden = sheet.offsetWidth <= stage.clientWidth + 1;
    updatePanButtons();
  }

  function synchronizeLink() {
    // The collection can be explored inside the frame before opening it on its own.
    try {
      const current = new URL(frame.contentWindow.location.href);
      if (current.origin === collection.origin && current.pathname === collection.pathname) {
        standalone.href = current.href;
      }
    } catch {
      // A visitor may have followed an external link inside the preview.
    }
  }

  const initial = window.matchMedia('(max-width: 44rem)').matches ? 'phone' : 'desktop';
  controls.querySelector('[value="' + initial + '"]').checked = true;
  controls.hidden = false;
  controls.addEventListener('change', () => {
    stage.scrollLeft = 0;
    resize();
  });
  stage.addEventListener('scroll', updatePanButtons, { passive: true });
  left.addEventListener('click', () => stage.scrollBy(-stage.clientWidth * .75, 0));
  right.addEventListener('click', () => stage.scrollBy(stage.clientWidth * .75, 0));
  standalone.addEventListener('click', synchronizeLink);
  standalone.addEventListener('contextmenu', synchronizeLink);
  window.addEventListener('resize', resize);
  resize();
})();
