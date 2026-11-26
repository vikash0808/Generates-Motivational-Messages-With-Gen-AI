# 💡 Daily Motivation Generator (GenAI)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?style=for-the-badge&logo=openai&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

A full-stack Generative AI web application that generates personalized, mood-aware motivational messages using a **Python Flask** backend, the **OpenAI Chat Completions API**, and a clean **HTML/CSS/JavaScript** frontend.

---

## ✨ Features

- **Mood-Aware Prompting:** Tailors AI-generated coaching responses based on the user's selected or entered mood (e.g., *Anxious*, *Sad*, *Tired*, *Unmotivated*, *Needs Focus*, *Seeking Creativity*).
- **REST API Backend:** Exposes `POST /generate_motivation` in Flask with CORS support (`flask-cors`) and JSON responses.
- **Lightweight Frontend:** Uses the browser Fetch API for fast, asynchronous message generation without page reloads.

---

## 📁 Project Structure

```text
Generates-Motivational-Messages-With-Gen-AI/
├── app.py       # Flask backend & OpenAI API integration (/generate_motivation)
├── index.html   # Frontend UI markup
├── script.js    # Fetch API client logic
├── style.css    # Application styling
└── README.md
```

---

## 💻 Getting Started

### Prerequisites
- Python 3.9+
- An OpenAI API key

### Setup & Run
1. Clone the repository:
   ```bash
   git clone https://github.com/vikash0808/Generates-Motivational-Messages-With-Gen-AI.git
   cd Generates-Motivational-Messages-With-Gen-AI
   ```
2. Install dependencies:
   ```bash
   pip install flask flask-cors openai python-dotenv
   ```
3. Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
4. Start the Flask server:
   ```bash
   python app.py
   ```
5. Open `http://127.0.0.1:5000` in your browser.

---

## 🔌 API Reference

### `POST /generate_motivation`
**Request Body:**
```json
{
  "mood": "Needs Focus"
}
```

**Response:**
```json
{
  "motivation": "Pick one small task, start for five minutes, and let momentum carry you forward."
}
```

---

## 👨‍💻 Author

**Vikash Dhillan** — B.Tech Computer Science  
GitHub: [@vikash0808](https://github.com/vikash0808)
