from sqlalchemy import Column, Integer, String, DateTime
from Utilities.Database import AlchemyEncoder, sqlDB as db
from Utilities.Methods import *
from dateutil import parser

class UserModel(db.Model):
	__tablename__ = 'Experiments'
	id = db.Column(Integer, primary_key=True)
	username = db.Column(String(64), unique=True)
	start_date = db.Column(DateTime)
	end_date = db.Column(DateTime)

	def __repr__(self):
		return '<Username %r>' % (self.username)

class UserService:
	def __init__(self, username):
		self.USERNAME = username
		self.AlchemyEncoder = AlchemyEncoder()
		pass

	def retrieve(self):
		try:
			query = UserModel.query.filter(UserModel.username == self.USERNAME).all()
			return self.AlchemyEncoder.toJson(query)

		except Exception as e:
			return error_response(e)
