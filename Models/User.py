# import datetime
from Utilities.Database import db


class User(db.Document):
    name = db.StringField(required=True)
    meta = {'collection': 'users', 'strict': False}
