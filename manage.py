from flask import Flask
from Controllers import DashRoutes, ErrorRoutes
import os
from config import appConfig, sessionKey, getMode, sqlConfig
from Utilities.Database import sqlDB as db
from Utilities.Monitoring import sentryLogger

app = Flask(__name__)

#app settings
app.secret_key = sessionKey
app.static_folder = appConfig['ROOT_PATH'] + '/Views/static'
app.template_folder = appConfig['ROOT_PATH'].split('Controllers')[0] + '/Views/templates'

#Mysql db init
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(sqlConfig['USERNAME'], sqlConfig['PASSWORD'], sqlConfig['IP'], sqlConfig['DATABASE'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

#blueprints init
blueprints = (
    DashRoutes.mod,
    ErrorRoutes.mod
)

for bp in blueprints:
    app.register_blueprint(bp)

#sentry init
if getMode() == 'live':
    sentryLogger()

if __name__ == '__main__':
    app.run(host="localhost", debug=True)
