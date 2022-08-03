from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class AnswerForm(FlaskForm):
    answer = StringField(validators = [DataRequired()])
    submit = SubmitField('Submit')

class UserForm(FlaskForm):
    name = StringField('Username',
                           validators=[DataRequired(), Length(min=2)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    suggestion = StringField('Do you have any suggestions for our website? Please enter below:')
    new_info = StringField('Is there any information you would like to share that we do not already have on the website? Please provide a link to a new resource or describe it below:')
    
    submit = SubmitField('Submit Input Request')
