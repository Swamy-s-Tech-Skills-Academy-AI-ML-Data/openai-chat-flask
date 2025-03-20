# Chat BOT with Flask and OpenAI

I am learning creating Chat Bot with Flask from different Video Courses, Books, and Websites

## Project Structure

```text
openai-chat-flask/
│── .venv/                # Virtual environment
│── app.py                # Main Flask file
│── requirements.txt
│── templates/
│   ├── base.html
│   └── index.html        # Main chat page
│── static/
│   ├── style.css         # (Optional) Additional styling
│── .env                  # (Optional) for API keys
```

## Project Setup

```powershell
python --version
pip --version

pip install virtualenv
python -m venv .venv
.venv/Scripts/activate
python -m pip install --upgrade pip

# pip install Flask python-dotenv openai Flask-SQLAlchemy requests SQLAlchemy

pip install flask openai python-dotenv flask_sqlalchemy

pip freeze > requirements.txt
pip install -r .\requirements.txt
```
