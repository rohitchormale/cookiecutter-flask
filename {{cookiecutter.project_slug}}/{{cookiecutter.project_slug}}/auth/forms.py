"""
This module implements various forms related with User extension.


@author: {{ cookiecutter.author }}
"""

from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, length, InputRequired


