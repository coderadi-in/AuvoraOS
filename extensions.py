'''coderadi'''

# ? Importing flask extensions
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

# ! Building extensions
db = SQLAlchemy()
logger = LoginManager()
upgrader = Migrate()

# * Function to bind extensions
def bind_extensions(server):
    db.init_app(server)
    upgrader.init_app(server, db)
    logger.init_app(server)