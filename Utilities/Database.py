from config import mongoConfig, sqlConfig
from pymongo import MongoClient, GEO2D
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

##sql alchemy init var
sqlDB = SQLAlchemy()

def mongoDBConnect():
	client = MongoClient('mongodb://{}:{}@{}'.format(mongoConfig['USERNAME'], mongoConfig['PASSWORD'], mongoConfig['IP']), mongoConfig['PORT'])
	db_session = client[mongoConfig['DATABASE']]
	return db_session

class AlchemyEncoder(json.JSONEncoder):

	def default(self, obj):
		if isinstance(obj.__class__, DeclarativeMeta):
			# an SQLAlchemy class
			fields = {}
			for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
				data = obj.__getattribute__(field)
				try:
					# this will fail on non-encodable values, like other classes
					json.dumps(data)
					fields[field] = data
				except TypeError:
					fields[field] = None
			# a json-encodable dict
			return fields

		return json.JSONEncoder.default(self, obj)

	def toJson(self, query):
		jsonQuery = json.dumps(query, cls=AlchemyEncoder)
		return jsonify(json.loads(jsonQuery))
