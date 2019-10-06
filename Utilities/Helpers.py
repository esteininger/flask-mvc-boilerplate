# -*- coding: utf-8 -*-
import re
import unidecode
from config import secret_key
from Crypto.Cipher import XOR
import base64
from functools import wraps

from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from flask_jwt_extended.view_decorators import _decode_jwt_from_request

from .Methods import success_response

from flask import redirect


def auth_response(username):
    resp = success_response({'login': True})
    # Create the tokens we will be sending back to the user
    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)
    #
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
        # if the grab worked and the identity key is in the dict then proceed
        if jwt_data and 'identity' in jwt_data:
            return view_function(*args, **kwargs)
        else:
            return redirect('login', code=302)

    return wrapper


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text)


def encode(plaintext):
    cipher = XOR.new(secret_key)
    return base64.b64encode(cipher.encrypt(plaintext))


def decode(encoded_text):
    cipher = XOR.new(secret_key)
    return cipher.decrypt(base64.b64decode(encoded_text)).decode("utf-8")
