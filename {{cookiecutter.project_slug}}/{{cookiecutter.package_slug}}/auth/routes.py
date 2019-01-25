"""
This module implements various blueprints and routers of User extension


@author: {{ cookiecutter.author }}
"""


from flask import Blueprint
from .controllers import *

# auth routes
auth_blueprint = Blueprint("auth", "auth", url_prefix="/auth")


# auth api routes
auth_api_blueprint = Blueprint("auth_api", "auth_api", url_prefix="/api/auth")



