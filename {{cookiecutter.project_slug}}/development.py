"""
Development server

@author: {{ cookiecutter.author }}
"""
from {{cookiecutter.package_slug}} import create_app
app = create_app()
app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])
