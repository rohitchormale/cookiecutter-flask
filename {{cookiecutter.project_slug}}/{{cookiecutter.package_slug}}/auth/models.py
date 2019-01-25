"""
This module implements various models related with User extension


@author: {{ cookiecutter.author }}
"""

from {{cookiecutter.package_slug}} import db
from {{cookiecutter.package_slug}}.helpers import models


class User(models.BaseModel):
    """
    Sample user model
    """

    __tablename__ = "auth_user"

    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)



