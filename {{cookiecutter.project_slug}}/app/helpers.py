"""
Collection of helpers functions and classes

@author: Rohit Chormale
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


# import random
# import string
# def generate_uuid(length):
#     """Generate uuid of given length by using lowercase and uppercase letters and digits without any special characters"""
#     return ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in xrange(length)])


# import json
# import datetime
# from bson.objectid import ObjectId
# class JSONEncoder(json.JSONEncoder):
#     """Encode datetime object and Mongo object-id as string"""
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         if isinstance(o, datetime.datetime):
#             return str(o)
#         return json.JSONEncoder.default(self, o)



