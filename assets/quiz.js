// Shared quiz component.
//
// Multiple choice: <div class="mcq" data-answer="L2" data-why="…"> containing
// <button data-choice="L2">…</button> elements. The first click locks the question
// and shows whether it was right and why. Buttons are shuffled on load so the
// answer's position carries no information, except for ordered scales (N/P/L/F,
// levels 0–3, options labelled a/b/c), whose natural order is kept.
//
// Recall: <div class="recall"> containing a <textarea> and a <div class="model">
// with the model answer. The model answer stays hidden until the learner has written
// something and presses "Compare".
//
// Every <section class="drill"> gets a running score in its <p class="score">.

(function () {
  const style = document.createElement("style");
  style.textContent = `
    .drill { background: var(--wash); padding: 1rem 1.2rem 1.2rem; margin: 1.4rem 0; }
    .drill .score { font: 600 0.8rem system-ui, sans-serif; color: var(--muted); text-align: right; margin: 0; }
    .mcq { margin: 1.1rem 0; padding-top: 0.9rem; border-top: 1px solid var(--rule); }
    .mcq.first { border-top: none; }
    .mcq .q { margin: 0 0 0.5rem; }
    .mcq button {
      font: 0.95rem system-ui, sans-serif; margin: 0 0.4rem 0.4rem 0; padding: 0.35rem 0.8rem;
      border: 1px solid var(--ink); background: var(--paper); color: var(--ink); cursor: pointer; border-radius: 3px;
    }
    .mcq button:disabled { cursor: default; opacity: 0.55; }
    .mcq button.right { background: var(--good); color: white; border-color: var(--good); opacity: 1; }
    .mcq button.wrong { background: var(--bad); color: white; border-color: var(--bad); opacity: 1; }
    .mcq .why { font-size: 0.92rem; margin: 0.3rem 0 0; }
    .mcq .why:focus { outline: none; }
    .mcq .why b.right { color: var(--good); }
    .mcq .why b.wrong { color: var(--bad); }
    .recall textarea { width: 100%; min-height: 5rem; font: 0.95rem/1.5 system-ui, sans-serif; padding: 0.5rem; border: 1px solid var(--rule); }
    .recall button { font: 0.95rem system-ui, sans-serif; margin-top: 0.4rem; padding: 0.35rem 0.8rem; cursor: pointer; }
    .recall .model { display: none; margin-top: 0.6rem; border-left: 3px solid var(--good); padding-left: 0.8rem; }
    .recall .model.shown { display: block; }
  `;
  document.head.appendChild(style);

  const ordered = (choices) =>
    choices.every((c) => ["N", "P", "L", "F"].includes(c)) || choices.every((c) => /^[0-9a-z]$/.test(c));

  function shuffle(q) {
    const buttons = [...q.querySelectorAll("button[data-choice]")];
    if (ordered(buttons.map((b) => b.dataset.choice))) return;
    const parent = buttons[0].parentNode;
    const anchor = buttons[buttons.length - 1].nextSibling;
    for (let i = buttons.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [buttons[i], buttons[j]] = [buttons[j], buttons[i]];
    }
    buttons.forEach((b) => parent.insertBefore(b, anchor));
  }

  function updateScore(drill) {
    const score = drill.querySelector(".score");
    if (!score) return;
    const all = drill.querySelectorAll(".mcq").length;
    const done = drill.querySelectorAll(".mcq[data-done]").length;
    const right = drill.querySelectorAll('.mcq[data-done="right"]').length;
    score.textContent = done === 0 ? `${all} questions` : `${right} of ${done} right · ${all - done} to go`;
  }

  document.querySelectorAll(".drill").forEach((drill) => {
    const first = drill.querySelector(".mcq");
    if (first) first.classList.add("first");
  });

  document.querySelectorAll(".mcq").forEach((q) => {
    shuffle(q);
    const why = document.createElement("p");
    why.className = "why";
    why.setAttribute("aria-live", "polite");
    why.tabIndex = -1;
    q.appendChild(why);
    q.querySelectorAll("button[data-choice]").forEach((b) => {
      b.addEventListener("click", () => {
        const right = b.dataset.choice === q.dataset.answer;
        q.dataset.done = right ? "right" : "wrong";
        q.querySelectorAll("button[data-choice]").forEach((other) => {
          other.disabled = true;
          if (other.dataset.choice === q.dataset.answer) {
            other.classList.add("right");
            other.textContent = "✓ " + other.textContent;
          }
        });
        if (!right) {
          b.classList.add("wrong");
          b.textContent = "✗ " + b.textContent;
        }
        why.innerHTML = `<b class="${right ? "right" : "wrong"}">${right ? "Right." : "Not quite."}</b> ${q.dataset.why || ""}`;
        why.focus();
        const drill = q.closest(".drill");
        if (drill) updateScore(drill);
      });
    });
  });

  document.querySelectorAll(".recall").forEach((r) => {
    const text = r.querySelector("textarea");
    const model = r.querySelector(".model");
    const prompt = r.querySelector("p");
    if (prompt) text.setAttribute("aria-label", prompt.textContent);
    const button = document.createElement("button");
    button.textContent = "Compare with the model answer";
    button.addEventListener("click", () => {
      if (!text.value.trim()) {
        text.placeholder = "Write your answer first — the retrieval is the exercise.";
        text.focus();
        return;
      }
      model.classList.add("shown");
    });
    text.after(button);
  });

  document.querySelectorAll(".drill").forEach(updateScore);
})();
