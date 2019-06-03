from flask import Flask
from config import session_key, app_config, mongo_config
from Controllers import PageRoutes
from Utilities.Database import db

app = Flask(__name__)

# app settings
app.secret_key = session_key
app.static_folder = app_config['ROOT_PATH'] + '/Views/static'
app.template_folder = app_config['ROOT_PATH'].split('Controllers')[0] + '/Views/templates'


# blueprints init
blueprints = [
    PageRoutes.mod
]

# db stuff
app.config['MONGODB_SETTINGS'] = {
    'db': mongo_config['DB'],
    'username': mongo_config['USERNAME'],
    'password': mongo_config['PASSWORD'],
    'host': mongo_config['IP'],
    'port': mongo_config['PORT'],
    'authentication_source': 'admin'
}


for bp in blueprints:
    app.register_blueprint(bp)

db.init_app(app)

if __name__ == '__main__':
    app.run(host="localhost", port=5001, debug=True)
