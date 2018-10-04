from functools import wraps
from flask import request, url_for, session, redirect

def loginRequired(fn):
    @wraps(fn)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('dash_routes.loginPage'))

        return fn(*args, **kwargs)
    return decorated_function
