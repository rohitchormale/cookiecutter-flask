"""
This module implements flask-cli commands

@author: {{ cookiecutter.author }}
"""

import click
from flask.cli import AppGroup


helpers_cli = AppGroup("helpers")

@helpers_cli.command("startapp")
@click.option("name")
def startapp(name):
    # TODO - implement command
    print("This command is not implemented yet")
