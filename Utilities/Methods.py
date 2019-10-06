from time import time
from flask import jsonify, request
import traceback


def success_response(data, code=200):
    return jsonify({
        "ok": True,
        "code": code,
        "endpoint": request.path,
        "timestamp": time(),
        "count": len(data),
        "response": data
    })


def error_response(msg, code=400):
    data = {
        "ok": False,
        "code": code,
        "timestamp": time(),
        "message": str(msg)
    }
    log_error(data=data, traceback=traceback.print_exc())
    return jsonify(data), 500


def check_json(json, keys):
    for key in keys:
        if key not in json:
            return key
    return None


def log_error(data, traceback):
    pass
