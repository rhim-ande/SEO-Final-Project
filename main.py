from flask import Flask, render_template, url_for, flash, redirect, request
#from forms import RegistrationForm, LoginForm, GameForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import UserMixin, login_user
#from flask_login import LoginManager, login_required, current_user, logout_user
import requests

app = Flask(__name__)
proxied = FlaskBehindProxy(app)

app.config['SECRET_KEY'] = '78de1af656d14fd39ee8e9ca98fd5989'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

@app.route("/")
@app.route("/homepage")
def home():
    return render_template('home.html')

@app.route("/news")
def news():
    return render_template('news.html')

@app.route("/history")
def history():
    return render_template('history.html')

@app.route("/resources")
def resources():
    return render_template('resources.html')

@app.route("/game")
def game():
    return render_template('game.html')

@app.route("/flashcards")
def flashcards():
    return render_template('flashcards.html')

@app.route("/flash_categories")
def flash_categories():
    return render_template('flash_categories.html')

@app.route("/activities")
def activities():
    return render_template('activities.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

