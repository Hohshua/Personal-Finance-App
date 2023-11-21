from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DateField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo

class HomeForm(FlaskForm):
    submit = SubmitField('submit')
    