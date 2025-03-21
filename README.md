# Chat BOT with Flask and OpenAI

I am learning creating Chat Bot with Flask from different Video Courses, Books, and Websites

## UI Preview

![UI Preview](./docs/images/SessionFirstLook.PNG)

## Project Structure

```text
openai-chat-flask/
│
├── app.py                  # Main entry point
├── requirements.txt        # List of dependencies
├── .env                    # Environment variables (e.g., API keys)
├── README.md               # Documentation (optional)
│
├── website/                # Your Flask package
│   ├── __init__.py         # Initializes the Flask app, config, and DB
│   ├── routes.py           # Blueprint for all routes (views & API endpoints)
│   ├── models.py           # (Optional) Database models if using SQLAlchemy
│   ├── static/             # Static files (CSS, JS, images)
│   │   └── globalstyles.css    # Custom CSS (optional)
│   └── templates/          # HTML templates (Jinja2)
│       ├── base.html       # Base template with common layout (navbar, footer)
│       ├── index.html      # Main page template (chat UI)
│       ├── history.html    # (Optional) Chat history template
│       └── response_view.html  # (Optional) Response view template
```

## Project Setup

```powershell
python --version
pip --version

pip install virtualenv
python -m venv .venv
.venv/Scripts/activate
python -m pip install --upgrade pip

pip install flask openai python-dotenv flask_sqlalchemy

pip freeze > requirements.txt
pip install -r .\requirements.txt
```



Based on your feedback, it's best to structure your project for scalability by separating your view (HTML-rendering) routes from your API (JSON-returning) routes. This modular approach will keep your code organized as your project grows.

Below is an example of how you can structure your project using blueprints:

---

### **1. Folder Structure**

```
openai-chat-flask/
│
├── app.py                  # Entry point
├── requirements.txt
├── .env
├── README.md
│
├── website/                # Main package
│   ├── __init__.py         # Create and configure the Flask app, register blueprints
│   ├── models.py           # (Optional) Database models if needed
│   ├── views.py            # Routes that render templates (Home, ST Chat Bot, History, etc.)
│   ├── api.py              # API endpoints (e.g., /api/chat)
│   ├── static/             # Static files (CSS, images, etc.)
│   │   ├── favicon.ico
│   │   └── globalstyles.css
│   └── templates/          # Jinja2 templates
│       ├── base.html
│       ├── home.html
│       ├── stchatbot.html
│       └── history.html
```

---

### **2. Example Code**

#### **2.1. app.py**

This is your application entry point. It simply imports the `create_app()` function from your package and runs the app.

```python
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

#### **2.2. website/__init__.py**

This file initializes your Flask app, configures your settings, initializes your database (if needed), and registers the blueprints from `views.py` and `api.py`.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from dotenv import load_dotenv
import os

load_dotenv()  # Loads environment variables from .env

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    
    # Configure the app
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "SimpleSecretKey")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    
    # Initialize the database
    db.init_app(app)
    
    # Register blueprints
    from .views import views
    from .api import api
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(api, url_prefix="/api")
    
    # Create database if it doesn't exist
    with app.app_context():
        if not path.exists("website/" + DB_NAME):
            db.create_all()
            print("Database Created")
    
    return app
```

#### **2.3. website/views.py**

This file handles your routes that render HTML templates.

```python
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/stchatbot")
def stchatbot():
    return render_template("stchatbot.html")

@views.route("/history")
def history():
    return render_template("history.html")
```

#### **2.4. website/api.py**

This file handles your API endpoints, for example, the chat API that interacts with OpenAI.

```python
from flask import Blueprint, request, jsonify, current_app
import openai
import os

api = Blueprint('api', __name__)

# Ensure OpenAI API key is set via environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Missing OpenAI API Key. Set OPENAI_API_KEY in environment variables.")

# Set the API key globally
openai.api_key = openai_api_key

@api.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            temperature=0.7,
            max_tokens=200
        )
        bot_message = response["choices"][0]["message"]["content"]
        return jsonify({"response": bot_message})
    except Exception as e:
        current_app.logger.error(f"Error in OpenAI API call: {e}")
        return jsonify({"error": "An error occurred while fetching response."}), 500
```

#### **2.5. website/templates/base.html**

Your base template provides a consistent layout (header, navbar, footer) for all pages.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{% block title %}Single Turn Chatbot with OpenAI{% endblock %}</title>
  
  <!-- Google Fonts: Inter -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
  
  <!-- Favicon -->
  <link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon" />
  
  <!-- Tailwind CSS CDN -->
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  
  <!-- Custom Global Styles -->
  <link rel="stylesheet" href="{{ url_for('static', filename='globalstyles.css') }}">
</head>
<body class="flex flex-col min-h-screen bg-gray-50 text-gray-900 font-inter">
  
  <!-- Navbar -->
  <nav class="bg-indigo-400 text-white shadow-md">
    <div class="container mx-auto px-4 py-2 flex justify-between items-center">
      <a href="/"
         class="text-2xl font-bold px-4 py-1 rounded transition-colors duration-200 hover:bg-indigo-500 hover:text-white">
         AI Assistant
      </a>
      <div class="space-x-4">
        <a href="/stchatbot" class="px-4 py-2 rounded transition-colors duration-200 hover:bg-indigo-500 hover:text-white font-bold">
          ST Chat Bot
        </a>
        <a href="/history" class="px-4 py-2 rounded transition-colors duration-200 hover:bg-indigo-500 hover:text-white font-bold">
          Search History
        </a>
        <button class="bg-purple-400 hover:bg-purple-600 px-3 py-1 rounded transition-colors duration-200 font-bold">
          Logout
        </button>
      </div>
    </div>
  </nav>
  
  <!-- Main Content -->
  <main class="container mx-auto p-4 flex-grow">
    {% block content %}{% endblock %}
  </main>
  
  <!-- Sticky Footer -->
  <footer class="bg-gray-800 text-white text-center p-2 text-md border-t border-gray-100">
    © 2025 Chatbot - Built with Flask & OpenAI
  </footer>
  
</body>
</html>
```

#### **2.6. Templates for Each Page**

- **home.html:**  
  Displays general information about the app.
  
  ```html
  {% extends "base.html" %}
  {% block title %}Home{% endblock %}
  {% block content %}
  <div class="max-w-3xl mx-auto bg-white p-6 rounded-lg shadow">
      <h2 class="text-2xl font-bold mb-4">Welcome to the Single Turn Chat BOT</h2>
      <p class="mb-4">
          This application demonstrates a single-turn chat with Azure OpenAI.
          You can ask a question, and it will respond once per query.
      </p>
      <p class="mb-4"><strong>Features:</strong></p>
      <ul class="list-disc list-inside mb-4">
          <li>Single Turn Chat Bot (GPT-based)</li>
          <li>Search History to revisit previous queries</li>
          <li>Simple, responsive UI</li>
      </ul>
      <p class="mb-4">
          Use the navigation bar above to explore the chatbot or view your search history.
      </p>
  </div>
  {% endblock %}
  ```

- **stchatbot.html:**  
  Contains the chat interface.
  
  *(Use your chat UI code here.)*
  
- **history.html:**  
  A placeholder for search history.
  
  ```html
  {% extends "base.html" %}
  {% block title %}Search History{% endblock %}
  {% block content %}
  <div class="max-w-3xl mx-auto bg-white p-6 rounded-lg shadow">
      <h2 class="text-2xl font-bold mb-4">Search History</h2>
      <p>Coming soon...</p>
  </div>
  {% endblock %}
  ```

---

### **3. Final Steps**

1. **Activate your virtual environment:**
   ```bash
   .\.venv\Scripts\activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run your app:**
   ```bash
   python app.py
   ```
4. **Test each route:**
   - Home: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
   - ST Chat Bot: [http://127.0.0.1:5000/stchatbot](http://127.0.0.1:5000/stchatbot)
   - Search History: [http://127.0.0.1:5000/history](http://127.0.0.1:5000/history)

---

This modular, blueprint-based approach will keep your code organized and scalable as the project grows. Let me know if you have any questions or need further adjustments!