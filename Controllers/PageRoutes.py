from flask import Blueprint, render_template

mod = Blueprint('page_routes', __name__)


@mod.route('/')
@mod.route('/home')
def home():
	return render_template("index.html")
