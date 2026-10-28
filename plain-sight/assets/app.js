/* Progressive enhancement. Static content and ordinary links remain the fallback. */
(() => {
  'use strict';
  const dataNode = document.getElementById('collection-data');
  const model = window.PlainSightModel;
  if (!dataNode || !model) return;
  const sources = JSON.parse(dataNode.textContent);
  const pageData = document.getElementById('publication-data');
  const pages = pageData ? JSON.parse(pageData.textContent) : [];
  const $ = selector => document.querySelector(selector);
  const all = selector => [...document.querySelectorAll(selector)];
  const state = () => model.readState(location.search, sources, pages.length || 24);
  const text = (selector, value) => { const node = $(selector); if (node) node.textContent = value; };
  const navigate = (values, mode = 'push', hash = location.hash, meta = history.state) => {
    const next = location.pathname + model.query(location.search, values) + hash;
    if (next !== location.pathname + location.search + location.hash) history[mode + 'State'](meta, '', next);
    sync();
  };
  const unmodified = event => event.button === 0 && !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey;
  const setImage = (image, item) => {
    image.alt = item.alt;
    image.width = item.width;
    image.height = item.height;
    image.src = 'assets/images/' + item.id + '.webp';
    image.srcset = 'assets/thumbs/' + item.id + '.webp 480w, assets/images/' + item.id + '.webp ' + item.width + 'w';
  };

  const toggle = $('[data-nav-toggle]');
  const nav = $('#site-nav');
  const setMenu = open => {
    toggle?.setAttribute('aria-expanded', String(open));
    if (toggle) toggle.textContent = open ? 'Close −' : 'Menu +';
    nav?.classList.toggle('is-open', open);
  };
  toggle?.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
  nav?.addEventListener('click', event => { if (event.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true' && !$('#look-dialog')?.open) {
      setMenu(false); toggle.focus();
    }
  });
  // Only collapse navigation after the controlling handlers exist.
  document.documentElement.classList.add('js');

  function renderIndex() {
    const grid = $('#source-grid');
    if (!grid) return;
    const selected = state().series;
    const filtered = model.filterSources(sources, selected);
    all('[data-source-card]').forEach(card => { card.hidden = !filtered.some(item => item.id === card.dataset.sourceCard); });
    all('[data-filter]').forEach(link => link.setAttribute('aria-current', String(link.dataset.filter === selected)));
    grid.classList.toggle('is-filtered', selected !== 'all');
    text('#source-count', filtered.length + ' original source' + (filtered.length === 1 ? '' : 's'));
  }
  all('[data-filter]').forEach(link => link.addEventListener('click', event => {
    if (!unmodified(event)) return;
    event.preventDefault();
    navigate({series:link.dataset.filter}, 'push', '#work');
  }));

  let renderedSource = null;
  function renderTable() {
    if (!$('#light-table')) return;
    const {source, crop} = state();
    all('[data-select-source]').forEach(link => link.setAttribute('aria-current', String(link.dataset.selectSource === source.id)));
    const select = $('#crop-select');
    if (renderedSource !== source.id) {
      select.replaceChildren(...source.crops.map(item => {
        const option = document.createElement('option'); option.value = item.id; option.textContent = item.title; return option;
      }));
      renderedSource = source.id;
    }
    select.value = crop.id;
    for (const [kind, item] of [['source', source], ['crop', crop]]) {
      const frame = $('#' + kind + '-frame');
      setImage(frame.querySelector('img'), item);
      frame.style.setProperty('--image-width', Math.min(500, 360 * item.width / item.height) + 'px');
      text('#' + kind + '-caption', item.alt);
      text('#' + kind + '-title', item.title);
      text('#' + kind + '-note', item.note);
    }
    text('#source-identity', 'SOURCE ' + source.number);
    text('#crop-identity', 'FROM SOURCE ' + source.number + ' / CROP ' + (source.crops.indexOf(crop) + 1));
    text('#source-meta', 'SOURCE ' + source.number + ' / ' + source.seriesName.toUpperCase());
    text('#table-status', 'Source ' + source.number + ', ' + source.title + '. Comparing: ' + crop.title + '.');
    $('#table-look').dataset.look = source.id;
    $('#table-look').href = 'light-table.html' + model.query(location.search, {look:source.id});
    $('#table-study').href = source.series + '.html';
    $('#table-study').textContent = 'Return to ' + source.seriesName + ' ↗';
    $('#crop-publication').href = 'publication.html?page=' + crop.page + '#reader';
    $('#table-error').hidden = true;
  }
  all('[data-select-source]').forEach(link => link.addEventListener('click', event => {
    if (!unmodified(event)) return;
    event.preventDefault(); navigate({source:link.dataset.selectSource, crop:null});
  }));
  $('#crop-select')?.addEventListener('change', event => navigate({crop:event.target.value}));
  $('#guide-toggle')?.addEventListener('change', event => all('[data-guides]').forEach(guide => { guide.hidden = !event.target.checked; }));
  all('.inspection-frame img').forEach(image => image.addEventListener('error', () => { $('#table-error').hidden = false; }));

  const viewer = $('#look-dialog');
  let origin = null;
  let lastLook = null;
  function viewerSequence(item) {
    const currentPage = document.body.dataset.page;
    let scope = ['gestures','arrangements','in-between'].includes(currentPage) ? currentPage : (currentPage === 'index' ? state().series : 'all');
    const list = model.filterSources(sources, scope);
    return list.some(source => source.id === item.id) ? list : sources;
  }
  function renderViewer() {
    if (!viewer || typeof viewer.showModal !== 'function') return;
    const item = state().look;
    if (!item) {
      if (viewer.open) { viewer.close(); origin?.focus({preventScroll:true}); }
      lastLook = null; return;
    }
    const list = viewerSequence(item);
    const index = list.findIndex(source => source.id === item.id);
    if (lastLook !== item.id) {
      setImage($('#viewer-image'), item);
      $('#viewer-image').sizes = '(max-width: 760px) 90vw, 70vw';
      text('#viewer-title', item.title);
      text('#viewer-series', 'SOURCE ' + item.number + ' / ' + item.seriesName);
      text('#viewer-note', item.note);
      $('#viewer-inspect').href = 'light-table.html?source=' + item.id;
      $('#viewer-direct').href = 'assets/images/' + item.id + '.webp';
      $('#viewer-error').hidden = true;
      text('#viewer-status', (index + 1) + ' of ' + list.length + ' original sources');
      $('[data-viewer-prev]').disabled = index === 0;
      $('[data-viewer-next]').disabled = index === list.length - 1;
      lastLook = item.id;
    }
    if (!viewer.open) viewer.showModal();
  }
  document.addEventListener('click', event => {
    const link = event.target.closest('[data-look]');
    if (!link || !unmodified(event) || typeof viewer?.showModal !== 'function') return;
    if (!sources.some(source => source.id === link.dataset.look)) return;
    event.preventDefault(); origin = link;
    navigate({look:link.dataset.look}, 'push', location.hash, {...history.state,psLook:true});
  });
  function closeViewer() {
    if (history.state?.psLook) history.back();
    else navigate({look:null}, 'replace');
  }
  function stepViewer(delta) {
    const item = state().look;
    if (!item) return;
    const list = viewerSequence(item);
    const next = model.stepIndex(list.indexOf(item), delta, list.length);
    navigate({look:list[next].id}, 'replace');
  }
  $('[data-close-viewer]')?.addEventListener('click', closeViewer);
  $('[data-viewer-prev]')?.addEventListener('click', () => stepViewer(-1));
  $('[data-viewer-next]')?.addEventListener('click', () => stepViewer(1));
  viewer?.addEventListener('cancel', event => { event.preventDefault(); closeViewer(); });
  viewer?.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') { event.preventDefault(); stepViewer(event.key === 'ArrowLeft' ? -1 : 1); }
  });
  $('#viewer-image')?.addEventListener('error', () => { $('#viewer-error').hidden = false; });

  let lastPage = null;
  function renderPublication() {
    if (!pages.length) return;
    const selected = state().page;
    const item = pages[selected - 1];
    if (selected !== lastPage) {
      const image = $('#publication-image');
      image.src = 'assets/publication/page-' + String(selected).padStart(2,'0') + '.webp';
      image.alt = 'Page ' + selected + ': ' + item.description;
      text('#page-position','PAGE ' + String(selected).padStart(2,'0') + ' / ' + pages.length);
      text('#page-title',item.title); text('#page-description',item.description); text('#page-transcript',item.text);
      $('#page-source').href = item.sourceId ? 'light-table.html?source=' + item.sourceId : 'light-table.html';
      $('#page-source').textContent = item.sourceId ? 'Inspect this image’s framing ↗' : 'Inspect the source images ↗';
      $('#page-select').value = String(selected);
      $('[data-page-prev]').disabled = selected === 1;
      $('[data-page-next]').disabled = selected === pages.length;
      $('#publication-error').hidden = true;
      $('#page-mat').classList.remove('is-zoomed');
      $('#page-zoom').setAttribute('aria-pressed','false');
      $('#page-zoom').textContent = 'Enlarge page';
      all('.publication-thumbs [data-page-link]').forEach(link => link.setAttribute('aria-current',String(Number(link.dataset.pageLink) === selected)));
      lastPage = selected;
    }
  }
  const selectPage = value => navigate({page:value}, 'push', '#reader');
  all('[data-page-link]').forEach(link => link.addEventListener('click', event => {
    if (!unmodified(event)) return;
    event.preventDefault(); selectPage(Number(link.dataset.pageLink));
    $('#reader').scrollIntoView({block:'start',behavior:'instant'});
    if (link.closest('.publication-thumbs')) $('#page-select').focus({preventScroll:true});
  }));
  $('[data-page-prev]')?.addEventListener('click', () => selectPage(state().page - 1));
  $('[data-page-next]')?.addEventListener('click', () => selectPage(state().page + 1));
  $('#page-select')?.addEventListener('change', event => selectPage(Number(event.target.value)));
  $('#page-zoom')?.addEventListener('click', event => {
    const zoomed = $('#page-mat').classList.toggle('is-zoomed');
    event.currentTarget.setAttribute('aria-pressed',String(zoomed));
    event.currentTarget.textContent = zoomed ? 'Fit page' : 'Enlarge page';
  });
  $('#publication-image')?.addEventListener('error', () => { $('#publication-error').hidden = false; });

  const copy = $('[data-copy-email]');
  if (copy) {
    copy.hidden = false;
    copy.addEventListener('click', async () => {
      try {
        if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText('jocelyn.wisteria@gmail.com');
        text('#copy-status','Email address copied. Nothing has been sent.');
      } catch {
        text('#copy-status','Automatic copying is unavailable. Select and copy the email address above, or use the email link.');
      }
    });
  }
  const motion = $('#motion-toggle');
  if (motion) {
    const preference = matchMedia('(prefers-reduced-motion: reduce)');
    const applyMotionPreference = () => {
      if (preference.matches) { $('#motion-scene').classList.remove('is-playing'); motion.setAttribute('aria-pressed','false'); }
      motion.disabled = preference.matches;
      motion.textContent = preference.matches ? 'Motion reduced' : ($('#motion-scene').classList.contains('is-playing') ? 'Pause motion' : 'Play motion');
      text('#motion-status',preference.matches ? 'Your reduced-motion preference is respected. The static composition is shown.' : ($('#motion-scene').classList.contains('is-playing') ? 'Motion is playing. You can pause it at any time.' : 'Motion is paused.'));
    };
    motion.addEventListener('click', () => { if (preference.matches) return; const playing=$('#motion-scene').classList.toggle('is-playing'); motion.setAttribute('aria-pressed',String(playing)); applyMotionPreference(); });
    preference.addEventListener('change',applyMotionPreference); applyMotionPreference();
  }
  function sync() { renderIndex(); renderTable(); renderPublication(); renderViewer(); }
  window.addEventListener('popstate', sync);
  sync();
})();
