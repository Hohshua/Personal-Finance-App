from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DateField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo
from .server import access_token

class HomeForm(FlaskForm):
    enable_display = False
    if access_token is not None:
        enable_display = True
    