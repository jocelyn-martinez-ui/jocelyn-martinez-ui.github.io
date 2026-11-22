(() => {
  'use strict';

  const strip = document.querySelector('[data-sample-tabs]');
  if (strip) {
    const tabs = Array.from(strip.querySelectorAll('[data-panel]'));
    const panels = tabs.map(tab => document.getElementById(tab.dataset.panel));
    function select(index, moveFocus = false) {
      tabs.forEach((tab, position) => {
        const selected = position === index;
        tab.setAttribute('aria-selected', String(selected));
        tab.tabIndex = selected ? 0 : -1;
        panels[position].hidden = !selected;
      });
      if (moveFocus) tabs[index].focus();
    }
    strip.setAttribute('role', 'tablist');
    tabs.forEach((tab, index) => {
      tab.setAttribute('role', 'tab');
      tab.setAttribute('aria-controls', panels[index].id);
      panels[index].setAttribute('role', 'tabpanel');
      panels[index].setAttribute('aria-labelledby', tab.id);
      tab.addEventListener('click', event => {
        if (event.metaKey || event.ctrlKey || event.altKey || event.shiftKey) return;
        event.preventDefault();
        select(index);
      });
      tab.addEventListener('keydown', event => {
        const next = {
          ArrowRight: (index + 1) % tabs.length,
          ArrowLeft: (index + tabs.length - 1) % tabs.length,
          Home: 0, End: tabs.length - 1
        }[event.key];
        if (next === undefined) return;
        event.preventDefault();
        select(next, true);
      });
    });
    select(0);
  }

  const input = document.querySelector('#project-search');
  if (input) {
    const groups = Array.from(document.querySelectorAll('.index-group'));
    const count = document.querySelector('#project-count');
    const empty = document.querySelector('#index-empty');
    function normalize(text) {
      return text.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    }
    function filter() {
      const words = normalize(input.value).trim().split(/\s+/).filter(Boolean);
      let total = 0;
      groups.forEach(group => {
        let visible = 0;
        group.querySelectorAll('.project-row').forEach(row => {
          const text = normalize(group.querySelector('h2').textContent + ' ' + row.textContent + ' ' + (row.dataset.terms || ''));
          row.hidden = !words.every(word => text.includes(word));
          if (!row.hidden) visible++;
        });
        group.hidden = visible === 0;
        total += visible;
      });
      count.textContent = total === 1 ? '1 project' : total + ' projects';
      empty.hidden = total > 0;
    }
    input.closest('.index-search').hidden = false;
    count.hidden = false;
    input.addEventListener('input', filter);
    document.querySelector('#clear-search').addEventListener('click', () => {
      input.value = '';
      filter();
      input.focus();
    });
    document.querySelectorAll('.index-jumps a').forEach(link => link.addEventListener('click', () => {
      input.value = '';
      filter();
    }));
    window.addEventListener('pageshow', filter);
    filter();
  }
})();
