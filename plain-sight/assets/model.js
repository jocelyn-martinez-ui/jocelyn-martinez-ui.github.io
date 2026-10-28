/* Small shared state model. The browser and Node tests use the same rules. */
(function (root, factory) {
  const model = factory();
  if (typeof module === 'object' && module.exports) module.exports = model;
  else root.PlainSightModel = model;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const series = ['all', 'gestures', 'arrangements', 'in-between'];
  function readState(search, sources, pageCount = 24) {
    const q = new URLSearchParams(search);
    const source = sources.find(item => item.id === q.get('source')) || sources[0];
    const crop = source.crops.find(item => item.id === q.get('crop')) || source.crops[0];
    const rawPage = Number(q.get('page') || 1);
    return {
      series: series.includes(q.get('series')) ? q.get('series') : 'all',
      source, crop,
      look: sources.find(item => item.id === q.get('look')) || null,
      page: Number.isInteger(rawPage) ? Math.min(pageCount, Math.max(1, rawPage)) : 1
    };
  }
  function filterSources(sources, selected) {
    return sources.filter(item => selected === 'all' || item.series === selected);
  }
  function stepIndex(index, delta, length) { return Math.min(length - 1, Math.max(0, index + delta)); }
  function query(search, values) {
    const q = new URLSearchParams(search);
    for (const [key, value] of Object.entries(values)) {
      if (value === null || value === undefined || value === '' || value === 'all') q.delete(key);
      else q.set(key, String(value));
    }
    return q.size ? '?' + q.toString() : '';
  }
  return {readState, filterSources, stepIndex, query};
});
