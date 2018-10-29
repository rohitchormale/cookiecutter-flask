"""
This module implements various blueprints and routers of User Extension


@author: {{ cookiecutter.author }}
"""


from flask import Blueprint
from .controllers import *

user_blueprint = Blueprint('user', 'user', url_prefix='/user')
