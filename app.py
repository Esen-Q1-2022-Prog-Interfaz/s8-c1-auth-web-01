from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Bcrypt(app)

app.register_blueprint(auth)
