# Chat BOT with Flask and OpenAI

I am learning creating Chat Bot with Flask from different Video Courses, Books, and Websites

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
│   │   └── mainpage.css    # Custom CSS (optional)
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
