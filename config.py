import os

app_config = {
    'ROOT_PATH': os.path.dirname(os.path.abspath(__file__))
}

mongo_config = {
    'IP': '',
    'PORT': ,
    'USERNAME': '',
    'PASSWORD': '',
    'DATABASE': ''
    # 'DATABASE': 'meports'
}


emailConfig = {
    'ADDRESS' : '',
    'PASSWORD' : '',
    'SMTP': 'smtp.gmail.com',
    'PORT': 587
}

sessionKey = ''
secretKey = ''
dev_computer_name = ''

def getMode():
    server = str(os.path.realpath('.'))
    if dev_computer_name in server:
        return 'test'
    else:
        return 'live'
