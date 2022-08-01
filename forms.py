from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class AnswerForm(FlaskForm):
    answer = StringField(validators = [DataRequired()])
    sumbit = SubmitField('Submit')
