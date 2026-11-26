import logging
import os
import random
from typing import Tuple

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

try:
    from flask_cors import CORS
except ImportError:  # pragma: no cover - optional when frontend is served from same origin
    CORS = None  # type: ignore

try:
    from openai import OpenAI
except ImportError:  # pragma: no cover - optional when running offline fallback only
    OpenAI = None  # type: ignore

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
if CORS is not None:
    CORS(app)

FALLBACK_QUOTES = {
    "anxious": [
        "Breathe. You're stronger than you think.",
        "Anxiety doesn't define you. Your courage does.",
        "Let go of what you can't control and focus on the next small step.",
        "One step at a time is all it takes.",
        "You've survived 100% of your toughest days.",
    ],
    "sad": [
        "It's okay to not be okay. Give yourself grace today.",
        "Feel it, heal it, and let yourself move forward gently.",
        "Your story isn't over yet—brighter chapters are ahead.",
        "Even the heaviest storms eventually clear.",
        "Be kind to yourself while you recharge.",
    ],
    "tired": [
        "Rest is productive too.",
        "Even the strongest builders need time to recharge.",
        "Small progress is still progress.",
        "You're doing enough. Pause, breathe, and pace yourself.",
        "Take a real break—you've earned it.",
    ],
    "unmotivated": [
        "Action creates momentum. Start with just five minutes.",
        "Consistency beats perfection every single time.",
        "Start where you are. Use what you have. Do what you can.",
        "Motivation often shows up after you begin.",
        "One small completed task can shift your whole day.",
    ],
    "needs focus": [
        "Eliminate one distraction and give this task 20 focused minutes.",
        "Your future self will thank you for the focus you put in today.",
        "One task at a time—finish what matters most first.",
        "Progress, not perfection.",
        "Clear your workspace, pick one goal, and begin.",
    ],
    "seeking creativity": [
        "Create freely. Perfection is the enemy of original ideas.",
        "Inspiration comes from experimenting, not waiting.",
        "Your ideas matter—put the first draft out there.",
        "Messy beginnings lead to breakthroughs.",
        "Let curiosity guide your next experiment.",
    ],
}

DEFAULT_FALLBACK_QUOTES = [
    "Small consistent steps build extraordinary outcomes.",
    "Trust your effort—every day you show up counts.",
    "Focus on progress over perfection today.",
]


def get_fallback_quote(mood: str) -> str:
    quotes = FALLBACK_QUOTES.get(mood.lower(), DEFAULT_FALLBACK_QUOTES)
    return random.choice(quotes)


def generate_with_openai(mood: str) -> Tuple[str, str]:
    """Generate a motivational message with OpenAI, falling back cleanly if unavailable."""
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip() or "gpt-4o-mini"

    if not api_key or OpenAI is None:
        return get_fallback_quote(mood), "fallback"

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an empathetic, concise motivational coach. "
                        "Reply with 1-2 uplifting, practical sentences without surrounding quotes."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Provide a short, powerful motivational message for someone who feels {mood}.",
                },
            ],
            max_tokens=80,
            temperature=0.8,
        )
        content = (response.choices[0].message.content or "").strip()
        if content:
            return content, "openai"
    except Exception as exc:
        logger.warning("OpenAI request failed, using fallback quote: %s", exc)

    return get_fallback_quote(mood), "fallback"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health", methods=["GET"])
def health():
    return jsonify(
        {
            "status": "ok",
            "openai_configured": bool(os.getenv("OPENAI_API_KEY", "").strip()),
        }
    )


@app.route("/generate_motivation", methods=["POST"])
def generate_motivation():
    data = request.get_json(silent=True) or {}
    mood = data.get("mood")

    if not isinstance(mood, str) or not mood.strip():
        return jsonify({"error": "Please provide a valid non-empty 'mood' string."}), 400

    cleaned_mood = mood.strip()[:100]
    message, source = generate_with_openai(cleaned_mood)

    return jsonify(
        {
            "mood": cleaned_mood,
            "motivation": message,
            "source": source,
        }
    )


@app.route("/feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    feedback = (data.get("feedback") or "").strip()

    if not name or not feedback:
        return jsonify({"error": "Both 'name' and 'feedback' are required."}), 400

    logger.info("Feedback received from %s (%d chars)", name[:50], len(feedback))
    return (
        jsonify(
            {
                "status": "received",
                "message": f"Thanks for your feedback, {name[:50]}!",
            }
        ),
        201,
    )


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    port = int(os.getenv("PORT", "5000"))
    app.run(host="127.0.0.1", port=port, debug=debug_mode)
