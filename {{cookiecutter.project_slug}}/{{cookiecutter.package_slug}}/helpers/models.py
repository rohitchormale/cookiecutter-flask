"""
Collection of helper functions and classes related with database models


@author: {{ cookiecutter.author }}
"""


from {{cookiecutter.package_slug}} import db


class BaseModel(db.Model):
    """
    Abstract model
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp, onupdate=db.func.current_timestamp)






