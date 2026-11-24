(() => {
  const project = document.querySelector('#which');
  const frame = document.querySelector('#comparison-view');
  const version = document.querySelectorAll('input[name="edition"]');
  const width = document.querySelector('#width');
  const link = document.querySelector('#open-edition');
  function render() {
    const option = project.selectedOptions[0];
    const earlier = version[0].checked;
    const url = earlier ? 'before/' + option.value + '.html' : option.dataset.current;
    const title = (earlier ? 'Earlier ' : 'Revised ') + option.textContent + ' opening';
    frame.title = title;
    if (frame.getAttribute('src') !== url) frame.setAttribute('src', url);
    frame.style.width = 'min(100%, ' + width.value + 'px)';
    link.href = url;
    link.textContent = 'Open ' + title;
    document.querySelector('#comparison-note').textContent = option.dataset.note;
  }
  document.querySelector('.comparison-controls').addEventListener('change', render);
  render();
})();
