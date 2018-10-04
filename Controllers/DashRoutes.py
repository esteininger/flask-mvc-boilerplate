from flask import Blueprint, request, render_template, abort, session, redirect
from Models.User import User

mod = Blueprint('dash_routes', __name__)

@mod.route('/')
@mod.route('/home')
def homePage():
	return render_template("index.html")
