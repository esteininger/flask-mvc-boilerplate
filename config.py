import os

appConfig = {
    'ROOT_PATH': os.path.dirname(os.path.abspath(__file__))
}

mongoConfig = {
    'IP': '',
    'PORT': ,
    'USERNAME': '',
    'PASSWORD': '',
    'DATABASE': ''
}

sqlConfig = {
    'IP': '',
    'USERNAME': '',
    'PASSWORD': '',
    'DATABASE': ''
}

cloudinaryConfig = {
    'NAME' : '',
    'KEY' : '',
    'SECRET' : ''
}

emailConfig = {
    'ADDRESS' : '',
    'PASSWORD' : '',
    'SMTP': '',
    'PORT': 
}

sessionKey = ''
secretKey = ''
sentryDSN = ''
serverName = ''

def getMode():
    server = str(os.path.realpath('.'))
    if serverName in server:
        return 'test'
    else:
        return 'live'
