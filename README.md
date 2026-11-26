# 💡 Daily Motivation Generator (GenAI)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=for-the-badge&logo=openai&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

A full-stack Generative AI web application that generates personalized, mood-aware motivational messages using a **Python Flask** backend, the **OpenAI Chat Completions API (`openai>=1.0`)**, and a responsive **HTML/CSS/JavaScript** frontend — with automatic offline fallback when no API key is configured.

---

## ✨ Features

- **Real OpenAI Integration + Offline Fallback:** Generates tailored motivational messages via `POST /generate_motivation` using OpenAI (`gpt-4o-mini` by default), and gracefully falls back to a curated mood-based quote bank if `OPENAI_API_KEY` is missing or unreachable.
- **Mood-Aware Coaching:** Supports *Anxious*, *Sad*, *Tired*, *Unmotivated*, *Needs Focus*, and *Seeking Creativity*.
- **Persistent UI State:** Saves message history and Light/Dark theme preference in browser `localStorage`.
- **Feedback API & Health Check:** Includes `POST /feedback` and `GET /health` endpoints plus automated unit tests (`tests/test_app.py`).

---

## 📁 Project Structure

```text
Generates-Motivational-Messages-With-Gen-AI/
├── app.py                  # Flask backend, OpenAI v1 integration & fallback logic
├── templates/
│   └── index.html          # Jinja2 HTML template
├── static/
│   ├── style.css           # Responsive Light/Dark mode styles
│   └── script.js           # Fetch API client, localStorage history & theme toggle
├── tests/
│   └── test_app.py         # Automated Flask endpoint & mocked OpenAI tests
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .gitignore
└── README.md
```

---

## 💻 Getting Started

### Prerequisites
- Python 3.9+
- *(Optional)* An OpenAI API key — the app still runs cleanly in Offline Fallback Mode without one.

### Setup & Run
1. Clone the repository:
   ```bash
   git clone https://github.com/vikash0808/Generates-Motivational-Messages-With-Gen-AI.git
   cd Generates-Motivational-Messages-With-Gen-AI
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux / macOS:
   source venv/bin/activate

   pip install -r requirements.txt
   ```
3. Configure environment variables:
   ```bash
   cp .env.example .env
   ```
   Set `OPENAI_API_KEY` inside `.env` (or leave it empty to test Offline Fallback Mode).
4. Start the Flask server:
   ```bash
   python app.py
   ```
5. Open `http://127.0.0.1:5000` in your browser.

### Run Tests
```bash
python -m unittest discover -s tests -v
```

---

## 🔌 API Reference

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Renders the web application (`templates/index.html`) |
| `/health` | `GET` | Returns server status and whether `OPENAI_API_KEY` is configured |
| `/generate_motivation` | `POST` | Body: `{"mood": "needs focus"}` → returns `{"mood", "motivation", "source"}` |
| `/feedback` | `POST` | Body: `{"name": "...", "feedback": "..."}` → returns confirmation (`201`) |

---

## 👨‍💻 Author

**Vikash Dhillan** — B.Tech Computer Science  
GitHub: [@vikash0808](https://github.com/vikash0808)
