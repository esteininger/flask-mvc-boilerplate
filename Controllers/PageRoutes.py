from flask import Blueprint, render_template, make_response, redirect
from Utilities.Helpers import redirect_if_jwt_invalid
from flask_jwt_extended import unset_jwt_cookies


mod = Blueprint('page_routes', __name__)


@mod.route('/')
def home():
    return render_template("index.html")


@mod.route('/protected')
@redirect_if_jwt_invalid
def protected():
    return render_template("index.html")


@mod.route('/login')
def login():
    return render_template("login.html")


@mod.route('/logout')
def login_page():
    resp = make_response(redirect('/login'))
    unset_jwt_cookies(resp)
    return resp
