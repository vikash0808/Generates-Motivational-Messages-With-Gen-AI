const outputDiv = document.getElementById('output');
const historyList = document.getElementById('history-list');

const motivationQuotes = {
  anxious: [
    "Breathe. You’re stronger than you think.",
    "Anxiety doesn’t define you. Your courage does.",
    "Let go of what you can't control.",
    "One step at a time is all it takes.",
    "You’ve survived 100% of your worst days."
  ],
  sad: [
    "It’s okay to not be okay.",
    "Feel it, heal it, let it go.",
    "Your story isn’t over yet.",
    "After rain comes sunshine.",
    "Tears are proof you’re healing."
  ],
  tired: [
    "Rest is productive too.",
    "Even the strongest need a break.",
    "Small progress is still progress.",
    "You’re doing enough. Just breathe.",
    "Take a break. You’ve earned it."
  ],
  unmotivated: [
    "Discipline beats motivation.",
    "Action creates momentum. Start now.",
    "Consistency > Perfection.",
    "Start where you are. Use what you have.",
    "Motivation comes from motion."
  ],
  "needs focus": [
    "Eliminate distractions. Focus.",
    "Your future self will thank you.",
    "One task at a time.",
    "Progress, not perfection.",
    "You’ve got this!"
  ],
  "seeking creativity": [
    "Create freely. Perfection is the enemy.",
    "Inspiration comes from action.",
    "Your ideas matter. Express them.",
    "Messy beginnings lead to brilliance.",
    "Let curiosity guide you."
  ]
};

function getMotivation() {
  const mood = document.getElementById('mood').value;
  const quotes = motivationQuotes[mood];
  if (quotes && quotes.length > 0) {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    const quote = quotes[randomIndex];
    outputDiv.textContent = `"${quote}"`;
    addToHistory(quote);
  } else {
    outputDiv.textContent = "No quotes available for this mood.";
  }
}

function addToHistory(message) {
  const li = document.createElement('li');
  li.textContent = message;
  historyList.prepend(li);
}

function toggleTheme() {
  document.body.classList.toggle('dark-mode');
}

function submitFeedback(event) {
  event.preventDefault();
  const name = document.getElementById('name').value;
  const feedback = document.getElementById('feedback').value;
  document.getElementById('feedback-response').textContent = `Thanks for your feedback, ${name}!`;
  document.getElementById('name').value = '';
  document.getElementById('feedback').value = '';
}
