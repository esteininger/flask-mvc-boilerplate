from time import time
from flask import jsonify
from Utilities.Monitoring import sentryLogger
from config import getMode

def success_response(data, code=200):
	return jsonify({
		"ok": True,
		"code": code,
		"timestamp": time(),
		"response": data
	})

def error_response(msg, code=400):

	if getMode() == 'live':
		sentryLogger(error=msg)

	return jsonify({
		"ok": False,
		"code": code,
		"timestamp": time(),
		"message": str(msg)
	}),500

def check_json(json, keys):
	for key in keys:
		if key not in json:
			return key
	return None
