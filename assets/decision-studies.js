/* Portfolio specimens use local examples. Their links reconstruct the selected
   example in the full prototype; no community or service records are touched. */
(() => {
  'use strict';
  const sheet = document.querySelector('.decision-opening');
  if (!sheet) return;
  const find = selector => sheet.querySelector(selector);
  const listed = selector => [...sheet.querySelectorAll(selector)];
  const sample = find('[data-primary-sample]');

  function changeSample(key, value) {
    const target = new URL(sample.href);
    target.searchParams.set(key, value);
    sample.href = target.href;
  }

  if (sheet.classList.contains('decision-psychic')) {
    const titles = {
      discussion: ['Has anyone revisited an old reading?', 'A public question invites other members to reply. This fictional thread has no rating.'],
      review: ['My first session with a sample reader', 'A firsthand review belongs with the reader’s catalogue entry, where a member can add a dated follow-up.']
    };
    const choices = listed('[data-intent]');
    for (const choice of choices) {
      choice.addEventListener('click', () => {
        const [heading, copy] = titles[choice.dataset.intent];
        for (const item of choices) item.setAttribute('aria-pressed', String(item === choice));
        find('[data-intent-heading]').textContent = heading;
        find('[data-intent-copy]').textContent = copy;
      });
    }
  }

  if (sheet.classList.contains('decision-afterform')) {
    const versions = {
      request: ['Match the surrounding cloth as closely as practical.', 'Customer request · Awaiting assessment'],
      proposal: ['Reinforce the wider worn area. A visible difference in the finish may remain.', 'Studio proposal · Awaiting customer approval']
    };
    const choices = listed('[data-tag]');
    for (const choice of choices) {
      choice.addEventListener('click', () => {
        const [instruction, status] = versions[choice.dataset.tag];
        for (const item of choices) item.setAttribute('aria-pressed', String(item === choice));
        find('[data-tag-instruction]').textContent = instruction;
        find('[data-tag-status]').textContent = status;
      });
    }
  }

  if (sheet.classList.contains('decision-interval')) {
    let early = false;
    const change = find('[data-change-session]');
    change.addEventListener('click', () => {
      early = !early;
      find('[data-first-time]').textContent = early ? '11:00' : '11:20';
      find('[data-first-name]').textContent = early ? 'Deep listening' : 'Objects in motion';
      find('[data-first-room]').textContent = early ? 'Until 11:45 · Room 01, Listening room' : 'Until 12:10 · Room 02, Studio';
      find('[data-break-value]').textContent = early ? '45' : '20';
      find('[data-break-result]').textContent = early ? '15 minutes to spare' : '10 minutes short';
      change.textContent = early ? 'Return to Objects in motion' : 'Try Deep listening instead';
      changeSample('planPair', early ? 'long' : 'short');
    });
  }

  if (sheet.classList.contains('decision-aurea')) {
    const second = find('#case-second-scent');
    const scents = {
      sol: {name:'Sol Mist', image:'assets/aurea-sol-mist.webp', alt:'Sol Mist citrus fragrance study', notes:['Bergamot, mandarin','Neroli, green tea','Soft cedar, clean musk'], summary:'Bergamot is shared in the opening.'},
      santal: {name:'Santal Dusk', image:'assets/aurea-santal-dusk.webp', alt:'Santal Dusk woody fragrance study', notes:['Cardamom, black pepper','Iris, violet leaf','Sandalwood, amber'], summary:'No shared notes in this pair.'}
    };
    second.addEventListener('change', () => {
      const scent = scents[second.value];
      if (!scent) return;
      const picture = find('[data-second-image]');
      picture.src = scent.image;
      picture.alt = scent.alt;
      find('[data-second-name]').textContent = scent.name;
      listed('[data-note]').forEach((node, index) => { node.textContent = scent.notes[index]; });
      find('[data-note-result]').textContent = scent.summary;
      changeSample('pair', second.value);
    });
  }

  if (sheet.classList.contains('decision-loopline')) {
    find('[data-save-window]').addEventListener('click', () => {
      const time = find('#case-pickup').value;
      find('[data-window-result]').textContent = time + ' preference saved. The partner has yet to accept.';
      changeSample('window', time);
    });
  }

  if (sheet.classList.contains('decision-novella')) {
    const reveal = find('[data-reveal-title]');
    reveal.addEventListener('click', () => {
      const book = find('#case-novella-book');
      book.hidden = !book.hidden;
      find('[data-read-excerpt]').hidden = book.hidden;
      reveal.textContent = book.hidden ? 'Reveal the book' : 'Hide the title';
      reveal.setAttribute('aria-expanded', String(!book.hidden));
    });
  }

  if (sheet.classList.contains('decision-nutriva')) {
    let tomatoesAtHome = true;
    const toggle = find('[data-toggle-tomatoes]');
    toggle.addEventListener('click', () => {
      tomatoesAtHome = !tomatoesAtHome;
      find('[data-pantry-state]').textContent = tomatoesAtHome ? 'Tomatoes at home' : 'Tomatoes missing';
      find('[data-shopping-state]').textContent = tomatoesAtHome ? '0 ingredients' : '1 ingredient · Tomatoes for tomato pasta';
      toggle.textContent = tomatoesAtHome ? 'Remove tomatoes from pantry' : 'Put tomatoes back';
      changeSample('tomatoes', tomatoesAtHome ? 'home' : 'missing');
    });
  }
})();
