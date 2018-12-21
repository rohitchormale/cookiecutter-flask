"""
Add variable config here. Do NOT commit this file in vcs.
"""

# Development  server
DEBUG = True
HOST = "0.0.0.0"
PORT = 8080
# change secret key
SECRET_KEY = "my-secret-key"


# Database
SQLALCHEMY_DATABASE_URI = "sqlite:///{{cookiecutter.project_slug}}.sqlite3"
# SQLALCHEMY_DATABASE_URI = "mysql:/user:passwd@127.0.0.1:3307/"



