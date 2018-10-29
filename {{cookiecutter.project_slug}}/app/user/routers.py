"""
This module implements various blueprints and routers of User extension


@author: {{ cookiecutter.author }}
"""


from flask import Blueprint
from .controllers import *


user_blueprint = Blueprint("user", "user", url_prefix="/user")
user_blueprint.add_url_rule("test", "test", test, methods=["GET",])

