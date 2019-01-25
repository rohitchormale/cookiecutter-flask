"""
This module implements various controllers related with User Authentication


@author: {{ cookiecutter.author }}
"""


from flask import flash, redirect, url_for, request, render_template, abort, jsonify, g, make_response
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from flask_httpauth import HTTPBasicAuth
from flask import current_app as app
from {{ cookiecutter.package_slug }} import login_manager, db
from {{ cookiecutter.package_slug }}.helpers.controllers import flash_errors
from .forms import LoginForm, RegisterForm
from .models import User


from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


@login_manager.user_loader
def load_user(id):
    """Load user in login manager after successful authentication"""
    return User.query.get(int(id))


def register():
    """Handle registration request"""
    if current_user.is_authenticated:
        return redirect(url_for('auth.home'))
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        password = generate_password_hash(form.password.data, method="sha256")
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, username=form.username.data,
                    password=password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        app.logger.info("New user registered successfully using form | %s" % user.username)
        return redirect(url_for("auth.home"))
    else:
        app.logger.error("New user registration using form failed")
        flash_errors(form)
    return render_template("register.html", form=form)


def login():
    """Handle login request."""
    if current_user.is_authenticated:
        return redirect(url_for("auth.home"))
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not check_password_hash(user.password, form.password.data):
            flash("Invalid username/password")
            return render_template("login.html", form=form)
        login_user(user)
        app.logger.debug("User login successful | %s" % user.username)
        return redirect(url_for("auth.home"))
    else:
        flash_errors(form)
        app.logger.debug("User login failed")
    return render_template("login.html", form=form)


@login_required
def logout():
    """Handle logout request"""
    logout_user()
    return redirect(url_for("auth.login"))


@login_required
def home():
    """Home page view"""
    return render_template("home.html")


def api_register():
    """API to register admin user"""
    username = request.json.get("username")
    password = request.json.get("password")
    first_name = request.json.get("first_name")
    last_name = request.json.get("last_name")

    if username is None or password is None or first_name is None or last_name is None:
        abort(make_response(jsonify({"msg": "Insufficient data", "type": "-ERR"}), 400))
    if User.query.filter_by(username=username).first() is not None:
        abort(make_response(jsonify({"msg": "User exists", "type": "-ERR"}), 400))

    password = generate_password_hash(password, method="sha256")
    admin = User(username=username, password=password, first_name=first_name, last_name=last_name)
    db.session.add(admin)
    db.session.commit()
    app.logger.info("New user registered successfully using api | %s" % username)
    return jsonify({"msg": "Registration successful", "username": admin.username, "type": "+OK"}), 201


@auth.login_required
def api_get_token():
    """API to get auth token"""
    token = g.user.generate_auth_token()
    app.logger.info("User generated auth token | %s" % g.user)
    return jsonify({"auth_token": token.decode("ascii"), "msg": "Operation successful", "type": "+OK"})


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not check_password_hash(user.password, password):
            return False
    g.user = user
    return True


