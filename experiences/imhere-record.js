// The faculty form and student history share the same attendance state in experience.js.
(() => {
  function correction({student, from, to, reason, request, escape, back, button}) {
    const studentLabel = 'Student ' + String(student + 1).padStart(2, '0');
    return `${back('cancel-correction','Back to the record')}
      <header class="ir-form-title"><p class="ir-label">Faculty review / Session 04</p>
        <h1>Correct an attendance record.</h1>
        <p>${studentLabel} · DES 101 · Introduction to Design</p></header>
      <div class="ir-form-layout">
        <form id="correction-form" class="ir-form" novalidate>
          <div class="ir-form-status">
            <div><span>Current record</span><strong>${escape(from)}</strong></div>
            <b aria-hidden="true">→</b>
            <div><span>Proposed record</span><strong>${escape(to)}</strong></div>
          </div>
          <p class="ir-request"><b>Student’s request</b> ${escape(request || 'No additional context supplied.')}</p>
          <label for="ir-reason">Reason for this correction</label>
          <p id="correction-help">What did you review, and why does it support the new status? The student can read this explanation.</p>
          <textarea id="ir-reason" name="reason" rows="3" maxlength="500" required aria-describedby="correction-help correction-error">${escape(reason)}</textarea>
          <div class="ir-field-meta"><span>Use attendance context only.</span><span id="reason-count">${reason.length}/500</span></div>
          <p id="correction-error" class="error" role="alert"></p>
          <div class="ir-form-actions"><button class="button" type="submit">Save explained correction</button>${button('Keep current record','cancel-correction',true,'type="button"')}</div>
        </form>
        <aside class="ir-sheet ir-preview" aria-labelledby="ir-preview-title">
          <div class="ir-sheet-top"><span>ImHere <b>/</b> Student history</span><span>Draft</span></div>
          <div class="ir-sheet-body"><p class="ir-label">Preview of shared record</p><h2 id="ir-preview-title">What the student will see</h2>
            <ol class="ir-timeline"><li><div class="ir-item-head"><span class="ir-node" aria-hidden="true"></span><strong>Faculty correction</strong></div>
              <p class="ir-status-pair">${escape(from)} <span aria-label="changed to">→</span> ${escape(to)}</p>
              <p id="ir-reason-preview" class="ir-preview-quote">${reason.trim() ? escape(reason.trim()) : 'Your explanation will appear here as you type.'}</p>
            </li></ol>
          </div><div class="ir-sheet-base"><span>${studentLabel}</span><span>Updates on save</span></div>
        </aside>
      </div>`;
  }

  function history(changes, escape) {
    return `<section class="ir-sheet ir-history" aria-label="Student correction history">
      <div class="ir-sheet-top"><span>ImHere <b>/</b> Student history</span><span>DES 101</span></div>
      <div class="ir-sheet-body"><p class="ir-label">Session 04 · Changes this visit</p><h2>Correction history</h2>
        <ol class="ir-timeline">${changes.map(change => {
          const undo = change.by === 'Faculty undo';
          return `<li><div class="ir-item-head"><span class="ir-node${undo ? ' ir-node-outline' : ''}" aria-hidden="true"></span><strong>${undo ? 'Correction undone' : escape(change.by)}</strong></div>
            <p class="ir-status-pair">${escape(change.from)} <span aria-label="changed to">→</span> ${escape(change.to)}</p><p>${escape(change.reason)}</p></li>`;
        }).join('')}</ol>
      </div></section>`;
  }

  function updatePreview(value) {
    const preview = document.getElementById('ir-reason-preview');
    if (preview) preview.textContent = value.trim() || 'Your explanation will appear here as you type.';
  }

  globalThis.ImHereRecord = {correction, history, updatePreview};
})();
