from flask import Flask, render_template, url_for, flash, redirect, request
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
from forms import UserForm, AnswerForm
import requests
from card_lists import get_basics, get_alphabet, get_foods, get_basl

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

@app.route("/alphabet/<index>")
#pass index variable to find english and asl in lists 
def alphabet(index):
    index = int(index)
    cards = get_alphabet()
    al = cards[0]#['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    images = cards[1]#['A.PNG', 'B.PNG', 'C.PNG', 'D.PNG', 'E.PNG', 'F.PNG', 'G.PNG', 'H.PNG', 'I.PNG', 'J.PNG', 'K.PNG', 'L.PNG', 'M.PNG', 'N.PNG', 'O.PNG', 'P.PNG', 'Q.PNG', 'R.PNG', 'S.PNG', 'T.PNG', 'U.PNG', 'V.PNG', 'W.PNG', 'X.PNG', 'Y.PNG', 'Z.PNG']
    #image string for html file 
    img_string = f"../static/alphabet/{images[index]}"
    return render_template('alphabet.html', card=al[index], asl=img_string, index=index)

@app.route("/basics/<index>")
def basics(index):
    index = int(index)
    cards = get_basics()
    bas = cards[0]
    images = cards[1]
    img_string = f"../static/basics/{images[index]}"
    return render_template('basics.html', card=bas[index], asl=img_string, index=index)    

@app.route("/foods/<index>")
def foods(index):
    index = int(index)
    cards = get_foods()
    food = cards[0]
    images = cards[1]
    img_string = f"../static/foods/{images[index]}"
    return render_template('foods.html', card=food[index], asl=img_string, index=index)    

@app.route("/basl/<index>")
def basl(index):
    index = int(index)
    cards = get_basl()
    ba = cards[0]
    images = cards[1]
    img_string = f"../static/basl/{images[index]}"
    return render_template('basl.html', card=ba[index], asl=img_string, index=index)    

@app.route("/game/<index><points>", methods=['GET', 'POST'])
def game(index, points):
    index = int(index)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    images = ['A.PNG', 'B.PNG', 'C.PNG', 'D.PNG', 'E.PNG', 'F.PNG', 'G.PNG', 'H.PNG', 'I.PNG', 'J.PNG', 'K.PNG', 'L.PNG', 'M.PNG', 'N.PNG', 'O.PNG', 'P.PNG', 'Q.PNG', 'R.PNG', 'S.PNG', 'T.PNG', 'U.PNG', 'V.PNG', 'W.PNG', 'X.PNG', 'Y.PNG', 'Z.PNG']
    #keep track of points as they go, display points at the end of game 
    #let them go to previous cards and change answers
    #display a percentage of answers for them to find
    points = int(points)
    form = AnswerForm()
    img_string = f"../static/alphabet/{images[index]}"
    answered = False
    if form.validate_on_submit():
        answer = form.answer.data
        if answer.lower() == alphabet[index].lower():
            flash(f'Correct', 'success')
            points += 1
            answered = True
        else:
            flash(f'Incorrect', 'success')

    return render_template('matching.html', form=form, asl=img_string, index=index, answered=answered, points=points)

@app.route("/flash_categories")
def flash_categories():
    return render_template('flash_categories.html')

@app.route("/activities")
def activities():
    return render_template('activities.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

