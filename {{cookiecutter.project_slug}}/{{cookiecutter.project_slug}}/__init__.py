"""
App init module


@author: {{ cookiecutter.author }}
"""


from flask import Flask, redirect, render_template, jsonify
import logging
import logging.handlers


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_login import LoginManager
login_manager = LoginManager()

from flask_cors import CORS
cors = CORS(resources={r"/api/*": {"origins": "*"}})

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()


def create_app():
    """Initiate flask app"""
    app = Flask(__name__, instance_relative_config=True, static_folder="ui/static", template_folder="ui/templates")
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    # login
    handler = logging.handlers.RotatingFileHandler(app.config["LOG_FILE"], maxBytes=app.config["LOG_SIZE"])
    handler.setLevel(app.config["LOG_LEVEL"])
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s [%(pathname)s at %(lineno)s]: %(message)s", "%Y-%m-%d %H:%M:%S"))
    app.logger.addHandler(handler)

    # init flask-extensions
    cors.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    db.init_app(app)

    # push required elements in app-context
    with app.app_context():
        from .auth.routes import auth_blueprint
        app.register_blueprint(auth_blueprint)

        from .auth.routes import auth_api_blueprint
        app.register_blueprint(auth_api_blueprint)
        csrf.exempt(auth_api_blueprint)

        db.create_all()

        # register common views
        @app.route("/")
        def home():
            """Handle root resource request"""
            return redirect("/admin/home")

        @app.errorhandler(404)
        def page_not_found(e):
            """Handle error gracefully"""
            return jsonify({"msg": "Resource not found. Visit API docs for more info.", "type": "+OK", "return": None})
            # return render_template("404.html"), 404

        @app.errorhandler(500)
        def internal_server_error(e):
            """Handle internal server error gracefully"""
            return jsonify({"msg": "Internal server error. Please contact support.", "type": "+OK", "return": None})
            # return render_template("500.html"), 500

    return app

