# import datetime
from Utilities.Database import db
import uuid
from Utilities.Helpers import encode, decode


class User(db.Document):
    email = db.StringField(required=True)
    password = db.BinaryField(required=True)
    #
    meta = {'collection': 'users', 'strict': False}

    def register(self):
        # if doesnt exist, encode password and register
        if not User.objects(email=self.email):
            self.user_id = str(uuid.uuid4())
            self.password = encode(self.password)
            self.save()
            return True
        # does exist, do nothing
        else:
            return False

    def login(self):
        user = User.objects.filter(email=self.email).first()
        # if user doesnt exist return error
        if user and decode(user.password) == self.password:
            return True
        else:
            return False
