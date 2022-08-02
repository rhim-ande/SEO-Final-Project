from flask import Flask, render_template, url_for, flash, redirect, request
#from forms import RegistrationForm, LoginForm, GameForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import UserMixin, login_user
#from flask_login import LoginManager, login_required, current_user, logout_user
from form2 import UserForm
import requests

app = Flask(__name__)
proxied = FlaskBehindProxy(app)

app.config['SECRET_KEY'] = 'f6f17d71cf013f9d4d4e3c0f2cbbf4e2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Alphabet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    english = db.Column(db.String(), nullable=False)
    img_name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Alphabet('{self.english}', '{self.img_name}')"

'''
class UserInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suggestion = db.Column(db.String(), nullable=False) '''

@app.route("/")
@app.route("/homepage")
def home():
    return render_template('home.html')

@app.route("/news")
def news():
    return render_template('news.html')

@app.route("/input")
def input():
    form = UserForm()
    return render_template('input.html', form=form)

@app.route("/history")
def history():
    return render_template('history.html')

@app.route("/resources")
def resources():
    return render_template('resources.html')

@app.route("/game")
def game():
    return render_template('game.html')

@app.route("/alphabet/<index>")
#pass index variable to find english and asl in lists 
def alphabet(index):
    index = int(index)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    images = ['A.PNG', 'B.PNG', 'C.PNG', 'D.PNG', 'E.PNG', 'F.PNG', 'G.PNG', 'H.PNG', 'I.PNG', 'J.PNG', 'K.PNG', 'L.PNG', 'M.PNG', 'N.PNG', 'O.PNG', 'P.PNG', 'Q.PNG', 'R.PNG', 'S.PNG', 'T.PNG', 'U.PNG', 'V.PNG', 'W.PNG', 'X.PNG', 'Y.PNG', 'Z.PNG']
    #image string for html file 
    img_string = f"../static/alphabet/{images[index]}"
    return render_template('alphabet.html', card=alphabet[index], asl=img_string, index=index)

@app.route("/basics/<index>")
def basics(index):
    index = int(index)
    basics = ['where', 'why', 'how', 'when', 'which', 'what', 'you', 'us', 'me', 'them', 'parents', 'person', 'family', 'community', 'blue', 'yellow', 'orange', 'red', 'green', 'purple']
    images = ['where.PNG', 'why.PNG', 'how.PNG', 'when.PNG', 'which.PNG', 'what.PNG', 'you.PNG', 'us.PNG', 'me.PNG', 'them.PNG', 'parents.PNG', 'person.PNG', 'family.PNG', 'community.PNG', 'blue.PNG', 'yellow.PNG', 'orange.PNG', 'red.PNG', 'green.PNG', 'purple.PNG']
    img_string = f"../static/basics/{images[index]}"
    return render_template('basics.html', card=basics[index], asl=img_string, index=index)    

@app.route("/foods/<index>")
def foods(index):
    index = int(index)
    foods = ['orange', 'pineapple', 'banana', 'apple', 'grapes', 'sour', 'sweet', 'spicy', 'disgust', 'tasty', 'cookies', 'sandwich', 'cake', 'soup', 'pancakes', 'snack', 'lunch', 'breakfast', 'dessert', 'dinner']
    images =['orange.PNG', 'pineapple.PNG', 'banana.PNG', 'apple.PNG', 'grapes.PNG', 'sour.PNG', 'sweet.PNG', 'spicy.PNG', 'disgust.PNG', 'tasty.PNG', 'cookies.PNG', 'sandwich.PNG', 'cake.PNG', 'soup.PNG', 'pancakes.PNG', 'snack.PNG', 'lunch.PNG', 'breakfast.PNG', 'dessert.PNG', 'dinner.PNG']
    img_string = f"../static/foods/{images[index]}"
    return render_template('foods.html', card=foods[index], asl=img_string, index=index)    

@app.route("/flash_categories")
def flash_categories():
    return render_template('flash_categories.html')

@app.route("/activities")
def activities():
    return render_template('activities.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

