from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_motivation', methods=['POST'])
def generate_motivation():
    data = request.json
    mood = data.get('mood', 'neutral')

    prompt = f"Provide a short, powerful motivational message for someone who feels {mood}."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You're a motivational coach."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60
        )
        message = response['choices'][0]['message']['content'].strip()
        return jsonify({"motivation": message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
