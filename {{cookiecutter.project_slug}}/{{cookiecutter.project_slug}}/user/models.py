"""
This module implements various models related with User extension


@author: {{ cookiecutter.author }}
"""


from {{cookiecutter.project_slug}} import db


class BaseModel(db.Model):
    """
    Abstract model
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp, onupdate=db.func.current_timestamp)



