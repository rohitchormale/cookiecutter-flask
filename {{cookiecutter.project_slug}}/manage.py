"""
Development server can be started using this module.
"""
from app import app
app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])