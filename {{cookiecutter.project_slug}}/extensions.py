"""
To avoid cyclic imports, instantiate extensions here.
Use this module to access them elsewhere in project, instead using `__init__.py`
"""


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from .models import *


from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()


from flask_cors import CORS
cors = CORS(resources={r"/api/*": {"origins": "*"}})


from flask_login import LoginManager
login_manager = LoginManager()



