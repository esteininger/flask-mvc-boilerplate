from flask import Blueprint, render_template
from config import appConfig

mod = Blueprint('error_routes', __name__)

@mod.app_errorhandler(404)
def error404(e):
   return '404', 404

@mod.app_errorhandler(500)
def error500(e):
   return '500', 500
