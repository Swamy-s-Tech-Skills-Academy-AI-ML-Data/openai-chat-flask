# website/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)

    # Basic configuration
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "SimpleSecretKey")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"

    # Initialize database
    db.init_app(app)

    # Register blueprint(s)
    from .routes import routes  # Import the blueprint from routes.py
    app.register_blueprint(routes, url_prefix="/")

    # Create the database if it doesn't exist
    create_database(app)

    return app


def create_database(app):
    # Ensure database is created inside the app context.
    from os import path
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Database Created")
