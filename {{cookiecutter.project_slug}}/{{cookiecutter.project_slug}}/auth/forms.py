"""
This module implements various forms related with User extension.


@author: {{ cookiecutter.author }}
"""

from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, Length, InputRequired, ValidationError
from . import models as auth_models


class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired(), Length(max=32)])
    last_name = StringField("Last Name", validators=[InputRequired(), Length(max=32)])
    username = StringField("Username", validators=[InputRequired(), Length(max=32)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=5, max=32)])

    def validate_username(self, username):
        admin = auth_models.User.query.filter_by(username=username.data).first()
        if admin is not None:
            raise ValidationError("Please use a different username")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(max=32)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=5, max=32)])


