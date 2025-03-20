# website/routes.py
from flask import Blueprint, render_template, request, jsonify
import openai
import os

routes = Blueprint('routes', __name__)

# Set your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


@routes.route("/")
def home():
    return render_template("index.html")


@routes.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Use the new OpenAI ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_message = response["choices"][0]["message"]["content"]
        return jsonify({"response": bot_message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
