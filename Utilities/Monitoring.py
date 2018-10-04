from raven import Client
from config import sentryDSN

def sentryLogger(**kwargs):
    client = Client(sentryDSN)
    client.context.merge(kwargs)
