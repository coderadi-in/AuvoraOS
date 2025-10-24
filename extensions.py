'''coderadi'''

# ? Importing flask extensions
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

# ? Importing libraries
import os

# ! Building extensions
db = SQLAlchemy()
logger = LoginManager()
upgrader = Migrate()

# * Function to bind extensions
def bind_extensions(server):
    db.init_app(server)
    upgrader.init_app(server, db)
    logger.init_app(server)

# | User database model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20))