"""
Add variable config here. Do NOT commit this file in vcs.
"""


import os
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


#####################
# Development Server
####################

DEBUG = True
HOST = "0.0.0.0"
PORT = 8080


###########
# Database
###########

SQLALCHEMY_DATABASE_URI = "sqlite:///{{cookiecutter.project_slug}}.sqlite3"
# SQLALCHEMY_DATABASE_URI = "mysql:/user:passwd@127.0.0.1:3307/"


###########
# Logging
##########

import logging
LOG_FILE = os.path.join(BASE_DIR, "log", "{{cookiecutter.project_slug}}.log")
LOG_SIZE = 1024*1024
LOG_LEVEL = logging.DEBUG


########
# Auth
########

# change secret key
SECRET_KEY = "my-secret-key"





