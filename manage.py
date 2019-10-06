from flask import Flask
from config import session_key, app_config, mongo_config, jwt_secret
from Controllers import PageRoutes, ErrorRoutes
from Utilities.Database import db
from flask_jwt_extended import JWTManager


app = Flask(__name__)

# app settings
app.secret_key = session_key
app.static_folder = app_config['ROOT_PATH'] + '/Views/static'
app.template_folder = app_config['ROOT_PATH'].split('Controllers')[0] + '/Views/templates'


# blueprints init
blueprints = [
    PageRoutes.mod,
    ErrorRoutes.mod
]
for bp in blueprints:
    app.register_blueprint(bp)

# db stuff
app.config['MONGODB_SETTINGS'] = {
    'db': mongo_config['DB'],
    'username': mongo_config['USERNAME'],
    'password': mongo_config['PASSWORD'],
    'host': mongo_config['IP'],
    'port': mongo_config['PORT'],
    'authentication_source': 'admin'
}
db.init_app(app)

# jwt stuff
app.config['JWT_SECRET_KEY'] = jwt_secret
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
jwt = JWTManager(app)


if __name__ == '__main__':
    app.run(host="localhost", port=5010, debug=True)
