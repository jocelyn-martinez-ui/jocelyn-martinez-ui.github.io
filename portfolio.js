(() => {
  const chips = [...document.querySelectorAll('[data-mood]')];
  const save = document.querySelector('#save-demo');
  const status = document.querySelector('#demo-status');
  if (!save || !status) return;
  let mood = 'Soft & floral';
  chips.forEach(chip => chip.addEventListener('click', () => {
    mood = chip.dataset.mood;
    chips.forEach(item => item.setAttribute('aria-pressed', String(item === chip)));
    save.setAttribute('aria-pressed', 'false');
    save.textContent = 'Save selection';
    status.textContent = `Selected: ${mood}.`;
  }));
  save.addEventListener('click', () => {
    const saved = save.getAttribute('aria-pressed') !== 'true';
    save.setAttribute('aria-pressed', String(saved));
    save.textContent = saved ? 'Saved ✓' : 'Save selection';
    status.textContent = saved ? `${mood} saved in this demonstration.` : `${mood} removed from the saved selection.`;
  });
})();
