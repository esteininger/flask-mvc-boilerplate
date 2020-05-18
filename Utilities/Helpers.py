import re
import unidecode
import json

from config import crypto_key
from cryptography.fernet import Fernet
from functools import wraps

from flask_jwt_extended import create_access_token, set_access_cookies, set_refresh_cookies, create_refresh_token
from flask_jwt_extended.view_decorators import _decode_jwt_from_request
from datetime import datetime, timedelta

from .Methods import success_response

from flask import redirect, render_template


def auth_response(username):
    resp = success_response({'login': True})
    expires = timedelta(days=5)
    # Create the tokens we will be sending back to the user
    access_token = create_access_token(identity=username, expires_delta=expires)
    refresh_token = create_refresh_token(identity=username)

    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp


def redirect_if_jwt_invalid(view_function):
    @wraps(view_function)
    def wrapper(*args, **kwargs):
        # attempt to grab the jwt from request
        try:
            jwt_data = _decode_jwt_from_request(request_type='access')
        except:
            jwt_data = None

        jwt_data_json = json.dumps(jwt_data)

        # if the grab worked and the identity key is in the dict then proceed
        if jwt_data_json and 'identity' in jwt_data_json:
            return view_function(*args, **kwargs)
        else:
            return redirect('login', code=302)

    return wrapper


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text)


def encode(plaintext):
    cipher_suite = Fernet(crypto_key)
    cipher_text = cipher_suite.encrypt(str.encode(plaintext))
    return cipher_text


def decode(encoded_text, array=False):
    cipher_suite = Fernet(crypto_key)

    if array:
        encoded_text = bytes(encoded_text)

    return cipher_suite.decrypt(encoded_text).decode("utf-8")
