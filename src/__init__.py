
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object("config.Config")

Bootstrap(app)
db = SQLAlchemy(app)

login_manager = LoginManager(app)

from src import routes