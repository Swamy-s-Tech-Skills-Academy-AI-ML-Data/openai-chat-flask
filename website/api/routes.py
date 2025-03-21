# File: routes.py
from flask import Blueprint, render_template, request, jsonify, current_app
import openai
import os

routes = Blueprint('routes', __name__)

# Ensure API key is set
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError(
        "Missing OpenAI API Key. Set OPENAI_API_KEY in environment variables.")

# Set the API key globally for the OpenAI package
openai.api_key = openai_api_key


@routes.route("/")
def home():
    return render_template("home.html")


@routes.route("/stchatbot")
def stchatbot():
    return render_template("stchatbot.html")


@routes.route("/history")
def history():
    return render_template("history.html")


@routes.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()

    # Validate user input
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Create an OpenAI client instance
        client = openai.OpenAI(api_key=openai_api_key)

        # Call OpenAI's ChatCompletion API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            temperature=0.7,  # Adjust randomness
            max_tokens=200  # Limit response length
        )

        bot_message = response.choices[0].message.content

        return jsonify({"response": bot_message})

    except openai.OpenAIError as oe:
        current_app.logger.error(f"OpenAI API error: {oe}")
        return jsonify({"error": "OpenAI API error occurred."}), 500
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500
