# website/views/home.py
from flask import Blueprint, render_template

# Define the blueprint for views
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
