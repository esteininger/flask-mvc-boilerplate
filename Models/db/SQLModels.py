from sqlalchemy import Column, Integer, String
import json
from Database import Base
from sqlalchemy.ext.declarative import DeclarativeMeta

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


class DummyTable(Base):
    __tablename__ = 'Reflections'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=False)
    entrydate = Column(String(255), unique=False)

    def __repr__(self):
        return '<Username %r>' % (self.username)
