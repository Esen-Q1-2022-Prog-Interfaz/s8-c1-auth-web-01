from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth
from flask_bcrypt import Bcrypt
from utils.loginManagerService import login_manager

app = Flask(__name__)

app.config.from_object("config.BaseConfig")
print(app.config)

SQLAlchemy(app)
Bcrypt(app)
login_manager.init_app(app)

app.register_blueprint(auth)
