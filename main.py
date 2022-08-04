from flask import Flask, render_template, url_for, flash, redirect, request
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
from forms import UserForm, AnswerForm
import requests

from gbooks import get_books
from gnews import get_articles
import os
apikey = os.environ.get('gn_apikey')

from card_lists import get_basics, get_alphabet, get_foods, get_basl


app = Flask(__name__)
proxied = FlaskBehindProxy(app)

app.config['SECRET_KEY'] = 'f6f17d71cf013f9d4d4e3c0f2cbbf4e2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    suggestion = db.Column(db.String(), nullable=False)
    resource = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Input('{self.name}', '{self.email}')"

@app.route("/")
@app.route("/homepage")
def home():
    return render_template('home.html')

@app.route("/news")
def news():
    articles = get_articles(apikey)
    return render_template('news.html', art1=articles[0][0], art2=articles[1][0], art3=articles[2][0], art4=articles[3][0], d1=articles[0][1], d2=articles[1][1], d3=articles[2][1], d4=articles[3][1], link1=articles[0][2], link2=articles[1][2], link3=articles[2][2], link4=articles[3][2])

@app.route("/input", methods=['GET', 'POST'])
def input():
    form = UserForm()
    if form.validate_on_submit():
        input = Input(name = form.name.data, email=form.email.data, suggestion=form.suggestion.data, resource=form.new_info.data)
        db.session.add(input)
        db.session.commit()
        flash('Thank you for submitting an improvement form!', 'success')
    return render_template('input.html', form=form)

@app.route("/history")
def history():
    books = get_books()
    return render_template('history.html', book1=books[0][0], book2=books[1][0], book3=books[2][0], url1=books[0][1], url2=books[1][1], url3=books[2][1])

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

#visited = [False] * 26
@app.route("/game/<index><points><visited>", methods=['GET', 'POST'])
def game(index, points, visited):
    index = int(index)
    visited = int(visited)
    '''if index == 0 and points == 0:
        for v in visited:
            v = False'''
    #figure out how/when to reset the "visited" thingy
    #make visited a number instead of a list so that it can just be compared to index 
    # if visited > index don't increase points when they get it right 
    # pass visited parameter back and forth just like the index parameter 
    # increase visited when answered is True
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
            if not visited > index:
                points += 1
                visited += 1
            answered = True
        else:
            flash(f'Incorrect', 'success')

    return render_template('matching.html', form=form, asl=img_string, index=index, points=points, visited=visited)

@app.route("/game_result<points><cat>")
def game_result(points, cat):
    percentage = 0
    total = 0
    if cat == "alphabet":
        percentage = (26 - points)/26 * 100
        total = 26
    if cat == "basics" or cat == "foods":
        percentage = (20 - points)/20 * 100
        total = 20
    if cat == "basl":
        percentage = (10 - points)/10 * 100
        total = 10

    return render_template('game_result.html', percentage=percentage, points=points, total=total)

@app.route("/flash_categories")
def flash_categories():
    return render_template('flash_categories.html')

@app.route("/activities")
def activities():
    return render_template('activities.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

