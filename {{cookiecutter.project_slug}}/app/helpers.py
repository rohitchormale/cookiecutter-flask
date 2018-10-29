"""
Collection of helper functions and classes


@author: {{ cookiecutter.author }}
"""


from flask import flash
def flash_errors(form):
    """Generate flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')


