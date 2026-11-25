// A plain list of linked sheets remains available if scripts are disabled.
(() => {
  const story = document.getElementById('carousel');
  if (!story) return;

  const menu = story.querySelector('.frame-map');
  const controls = Array.from(menu.querySelectorAll('[data-choose]'));
  const panels = controls.map(control => document.getElementById(control.hash.slice(1)));
  if (!controls.length || panels.some(panel => !panel)) return;

  function select(index) {
    controls.forEach((control, position) => {
      const active = index === position;
      control.setAttribute('aria-selected', String(active));
      control.tabIndex = active ? 0 : -1;
      panels[position].hidden = !active;
    });
  }

  function choose(index) {
    select(index);
    history.replaceState(history.state, '', controls[index].hash);
  }

  function restore() {
    const index = controls.findIndex(control => control.hash === location.hash);
    select(index < 0 ? 0 : index);
  }

  menu.setAttribute('role', 'tablist');
  menu.setAttribute('aria-label', 'Editorial story frames');
  story.querySelector('.frame-list').setAttribute('role', 'presentation');
  controls.forEach((control, index) => {
    control.setAttribute('role', 'tab');
    control.setAttribute('aria-controls', panels[index].id);
    panels[index].setAttribute('role', 'tabpanel');
    panels[index].setAttribute('aria-labelledby', control.id);
    control.addEventListener('click', event => {
      if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      choose(index);
    });
    control.addEventListener('keydown', event => {
      const last = controls.length - 1;
      const next = {
        ArrowLeft: (index + last) % controls.length,
        ArrowUp: (index + last) % controls.length,
        ArrowRight: (index + 1) % controls.length,
        ArrowDown: (index + 1) % controls.length,
        Home: 0,
        End: last,
        ' ': index,
      }[event.key];
      if (next === undefined) return;
      event.preventDefault();
      choose(next);
      controls[next].focus();
    });
  });
  window.addEventListener('hashchange', restore);
  restore();
  story.classList.add('sequence-upgraded');
})();
