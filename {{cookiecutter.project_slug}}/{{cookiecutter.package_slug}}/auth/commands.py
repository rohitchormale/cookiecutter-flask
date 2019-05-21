"""
This module implements flask-cli commands

@author: {{ cookiecutter.author }}
"""

import click
from flask.cli import AppGroup


auth_cli = AppGroup("auth")

@helpers_cli.command("adduser")
@click.option("--email")
@click.option("--password")
def adduser(email, password):
    pass