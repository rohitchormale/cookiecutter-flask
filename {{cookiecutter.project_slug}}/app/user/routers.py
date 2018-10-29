"""
This module implements various blueprints and routers for different controllers related with authentication


@author: Rohit Chormale
"""


from flask import Blueprint
from .controllers import *

user_blueprint = Blueprint('user', 'user', url_prefix='/user')
