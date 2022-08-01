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

app.config['SECRET_KEY'] = 'f6f17d71cf013f9d4d4e3c0f2cbbf4e2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Alphabet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    english = db.Column(db.String(20), nullable=False)
    img_name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Alphabet('{self.english}', '{self.img_name}')"

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

@app.route("/matching")
def matching():
    points = 0
    form = AnswerForm()
    if answer == database:
        points = points + 1
        flash(f'Correct Answer! Current Score: {points}')
    else:
        points = points - 1
        flash(f'Incorrect Answer. Current Score: {points}. Retype the correct answer: {database answer}')
        if answer != database:
            flash(f'Incorrect Answer. Retype the correct answer: {database answer}')
        

    return render_template('matching.html')


@app.route("/activities")
def activities():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(26):
        card = Alphabet(english=alphabet[i], img_name=f"{alphabet[i]}.png")
        db.session.add(card)
        db.session.commit()
    return render_template('activities.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

