// All actions and checkbox IDs use the walking guide's existing session model.
(() => {
  const observations = [
    ['Find a starting point.', 'Look along the pavement. Where do the storefronts, trees, or the rhythm of the windows first draw your eye?'],
    ['Read the buildings.', 'Follow a roofline. Where do the shape, color, or spacing of the windows change from one building to the next?'],
    ['Notice a small detail.', 'Look above the shop windows. Choose a brick pattern, a carved letter, or a change in the shape of an opening.']
  ];
  const requirements = [
    ['Historical sources', 'Historical claims have traceable sources.'],
    ['Images and permissions', 'Image permissions and descriptions are reviewed.'],
    ['Route access', 'Route access, distance, and conditions are documented.']
  ];

  function routeList(stops, active, currentIndex = -1) {
    return `<ol class="hg-route-list">${active.map((id, position) => `<li${position === currentIndex ? ' aria-current="step"' : ''}>
      <span aria-hidden="true">${String(position + 1).padStart(2, '0')}</span><strong>${stops[id]}</strong>
      ${position === currentIndex ? '<em>Current stop</em>' : ''}</li>`).join('')}</ol>`;
  }

  function photo() {
    return `<figure class="hg-context-image"><img src="../assets/holland-place.webp" width="1800" height="1205" alt="Upper windows and brick storefronts along a downtown Holland street"><figcaption>Downtown Holland · Context photograph · <a href="../image-credits.html" target="_top">Andrew Jameson</a></figcaption></figure>`;
  }

  function builder(stops, chosen, button) {
    const selected = Array.from(chosen).sort((a,b) => a-b);
    const count = selected.length;
    return `<header class="hg-view-heading"><p class="hg-label">Holland / Build a walk</p><h1>Choose your stories.</h1>
      <p>Pick the observations you want to take with you. You’ll see their order before you begin.</p></header>
      <div class="hg-builder-grid"><section class="hg-choice-sheet"><h2>Stories to include</h2>
        ${stops.map((name,id) => `<label class="hg-choice"><input type="checkbox" data-stop="${id}" ${chosen.has(id) ? 'checked' : ''}><span><b>${name}</b><small>${observations[id][0]}</small></span></label>`).join('')}
        <p class="hg-selection" role="status">${count ? count + (count === 1 ? ' story selected.' : ' stories selected.') : 'Choose at least one story to continue.'}</p>
        ${button('Review my selected stories','preview-custom',false,count ? '' : 'disabled')}</section>
      <aside class="hg-trail-sheet"><p class="hg-label">Your field guide</p><h2>In walking order</h2>
        ${count ? routeList(stops, selected) : '<p>Your selected stories will appear here.</p>'}
        <p class="hg-fine">Illustrative story sequence. Distances and access conditions require local verification.</p></aside></div>`;
  }

  function walk(stops, active, step, paused, button) {
    const number = String(step + 1).padStart(2, '0');
    const id = active[step];
    return `<div class="hg-live-layout"><section class="hg-live-stop">
      <div class="hg-live-top"><p class="hg-label">Your field guide / Holland</p><strong>${paused ? 'Walk paused' : 'Walk in progress'}</strong></div>
      <div class="hg-live-ticket"><div class="hg-ticket-no"><span>STOP</span><b>${number}</b><span>OF ${String(active.length).padStart(2,'0')}</span></div>
        <div><p class="hg-label">Stop ${step + 1} of ${active.length}</p><h1>${stops[id]}</h1><p>${paused ? 'Your place is kept for this visit. Resume when you’re ready.' : observations[id][0]}</p></div></div>
      <div class="hg-walk-controls"><div class="hg-walk-primary">${button(paused ? 'Resume my walk' : 'Read this story',paused ? 'pause' : 'view:story')}${paused ? '' : button('Pause my walk','pause',true)}</div>
      <div class="hg-walk-secondary">${button('Previous stop','previous-stop',true,step === 0 || paused ? 'disabled' : '')}${button(step === active.length - 1 ? 'Finish walk' : 'Next stop','next-stop',true,paused ? 'disabled' : '')}</div></div>
      <details class="hg-route-disclosure"><summary>My selected stops</summary>${routeList(stops, active, step)}</details>
      <div class="hg-live-foot">${button('Help & text size','view:tools',true)}<span>Manual progression · Sample route</span></div>
      </section>${photo()}</div>`;
  }

  function story(stops, active, step, largeText, button, back) {
    const id = active[step];
    return `${back('view:walk','Back to my walk')}<div class="hg-reading-grid"><article class="hg-reading-copy">
      <p class="hg-label">Observation / Stop ${step + 1} of ${active.length}</p><h1>${stops[id]}</h1><p class="hg-reading-lead">${observations[id][0]}</p>
      <p>${observations[id][1]}</p><p class="hg-fine">An original observation prompt in an illustrative walking sequence.</p>
      <div class="hg-walk-primary">${button('Return to my walk','view:walk')}${button(largeText ? 'Standard text' : 'Larger text','large-text',true,'aria-pressed="'+largeText+'"')}</div></article>${photo()}</div>`;
  }

  function editor(checks, ready, button) {
    const outstanding = requirements.filter((item,index) => !checks[index]);
    return `<header class="hg-view-heading"><p class="hg-label">Content studio / Downtown stories</p><h1>Is the route ready?</h1>
      <p>Gather the evidence before sending a route to the next reviewer.</p></header>
      <nav class="hg-studio-nav" aria-label="Content studio">${button('Tour management','view:cms')}${button('Story library','view:stops',true)}${button('Visual archive','view:archive',true)}</nav>
      <div class="hg-builder-grid"><section class="hg-choice-sheet"><h2>Review requirements</h2>
        ${requirements.map(([name,note],id) => `<label class="hg-choice"><input type="checkbox" data-editorial-check="${id}" ${checks[id] ? 'checked' : ''}><span><b>${name}</b><small>${note}</small></span></label>`).join('')}
        <p class="hg-selection" role="status">${checks.filter(Boolean).length} of ${requirements.length} review requirements acknowledged.</p>
        ${button(ready ? 'Return sample to draft' : 'Mark sample ready for review','hw-publish:0',false,outstanding.length ? 'disabled' : '')}</section>
        <aside class="hg-trail-sheet hg-editor-sheet"><p class="hg-label">Editorial status</p><h2>${ready ? 'Ready for review' : 'Draft'}</h2>
        ${outstanding.length ? `<p>Still needs review</p><ul>${outstanding.map(([name])=>`<li>${name}</li>`).join('')}</ul>`
          : `<p>${ready ? 'All three checks are recorded. Removing one reopens the draft.' : 'All three checks are recorded. You can send this sample to review.'}</p>`}
        <p class="hg-fine">Illustrative checklist. Readiness is local to this visit and does not publish a visitor route.</p>
      </aside></div>`;
  }

  globalThis.HollandFieldGuide = {builder, walk, story, editor};
})();
