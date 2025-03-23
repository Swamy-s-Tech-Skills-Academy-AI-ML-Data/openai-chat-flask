# Chat BOT with Flask and OpenAI

I am learning creating Chat Bot with Flask from different Video Courses, Books, and Websites

## UI Preview

![UI Preview](./docs/images/SessionFirstLook.PNG)

## Project Structure

```text
openai-chat-flask/
├── app.py                  # Application entry point
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (e.g., API keys, secret key)
├── README.md               # Project documentation
└── website/                # Main Flask package
    ├── __init__.py         # App factory: creates the Flask app, configures DB, registers blueprints
    ├── data/               # Database-related code
    │   ├── __init__.py     # (Optional) Expose models as a package
    │   └── models.py       # SQLAlchemy models (e.g., ChatHistory)
    ├── api/                # API endpoints (return JSON responses)
    │   ├── __init__.py     # Initializes the API blueprint (simply imports blueprint from chat.py)
    │   └── chat.py         # Defines the chat API route that interacts with OpenAI
    ├── views/              # View routes (render templates)
    │   ├── __init__.py     # Initializes the views blueprint (imports blueprint from home.py)
    │   └── home.py         # Contains routes for Home, ST Chat Bot, and History pages
    ├── static/             # Static assets (CSS, images, etc.)
    │   ├── favicon.ico
    │   └── globalstyles.css
    └── templates/          # Jinja2 templates
        ├── base.html       # Base layout (includes navbar and footer via includes)
        ├── navbar.html     # Navbar HTML (included in base.html)
        ├── Footer.html     # (Optional) Footer HTML (could be included in base.html)
        ├── home.html       # Home page (overview of the application)
        ├── stchatbot.html  # Single Turn Chat Bot page (chat interface)
        └── history.html    # Search History page (placeholder or chat history)
```

## Project Setup

```powershell
python --version
pip --version
(.venv) PS D:\STSAALMLDT\openai-chat-flask> python --version
Python 3.12.5
(.venv) PS D:\STSAALMLDT\openai-chat-flask> pip --version
pip 25.0.1 from D:\STSAALMLDT\openai-chat-flask\.venv\Lib\site-packages\pip (python 3.12)
(.venv) PS D:\STSAALMLDT\openai-chat-flask>

pip install virtualenv
python -m venv .venv
.venv/Scripts/activate
python -m pip install --upgrade pip

pip install flask openai python-dotenv flask_sqlalchemy

pip freeze > requirements.txt
pip install -r .\requirements.txt
```

---
