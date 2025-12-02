/* app.js
   Minimal JS to enhance read-along & quiz card
   Lightweight and unobtrusive
*/
// ===========================
// MOBILE NAVBAR TOGGLE
// ===========================
(function(){
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".site-nav");

  if(!toggle || !nav) return;

  toggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("show");
    toggle.setAttribute("aria-expanded", isOpen);
  });
})();


// ===========================
// READ-ALONG AUTO HIGHLIGHT
// ===========================
(function() {
  const readSection = document.querySelector("[data-read-along]");
  if (!readSection) return;

  const lines = Array.from(readSection.querySelectorAll("p"));
  if (lines.length === 0) return;

  let index = 0;

  // Highlight function
  function highlightNextLine() {
    // Remove previous highlights
    lines.forEach(p => p.classList.remove("highlight-line"));

    // Highlight current
    lines[index].classList.add("highlight-line");

    // Move to next line
    index = (index + 1) % lines.length;
  }

  // Start simple interval
  highlightNextLine(); // initial
  setInterval(highlightNextLine, 3500); // every 3.5 seconds
})();


// ===========================
// QUIZ CARD INTERACTION
// ===========================
(function() {
  const quizButtons = document.querySelectorAll("[data-quiz-btn]");
  quizButtons.forEach(btn => {
    btn.addEventListener("click", function(e) {
      e.preventDefault();

      const card = btn.closest(".quiz-card");
      if (!card) return;

      // Add animation class
      card.classList.add("quiz-animate");

      // Optional: temporary text change
      const oldText = btn.textContent;
      btn.textContent = "Loading…";

      // Reset after animation
      setTimeout(() => {
        card.classList.remove("quiz-animate");
        btn.textContent = oldText;
      }, 800);
    });
  });
})();

document.querySelectorAll('.quiz-option').forEach(btn => {
  btn.addEventListener('click', () => {

    // small animation feedback using your "quiz-animate" class
    btn.classList.add('quiz-animate');

    // later we'll add real logic here
    setTimeout(() => {
      btn.classList.remove('quiz-animate');
    }, 600);
  });
});