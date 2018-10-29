from flask import Flask, redirect, render_template
from flask_wtf.csrf import CSRFProtect
# from .helpers import JSONEncoder


# init flask app
app = Flask(__name__, instance_relative_config=True, template_folder="ui/templates", static_folder="ui/static")
app.config.from_object("config")
app.config.from_pyfile("config.py")
# app.json_encoder = JSONEncoder
csrf = CSRFProtect(app)


# blueprint registrations
from app.user.routers import user_blueprint
app.register_blueprint(user_blueprint)


# common routes to change easily in future
@app.route("/")
def home():
    """Handle root resource request"""
    return redirect("/user/login")


@app.errorhandler(404)
def page_not_found(e):
    """Handle error gracefully"""
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handle internal server error gracefully"""
    return render_template("500.html"), 500