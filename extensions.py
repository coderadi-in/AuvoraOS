'''coderadi'''

# ? Importing flask extensions
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from authlib.integrations.flask_client import OAuth

# ? Importing libraries
import os

# ! Building extensions
db = SQLAlchemy()
logger = LoginManager()
upgrader = Migrate()
oauth = OAuth()

# * Function to bind extensions
def bind_extensions(server):
    db.init_app(server)
    upgrader.init_app(server, db)
    logger.init_app(server)
    oauth.init_app(server)

# & GITHUB OAUTH CONFIGURATION
github = oauth.register(
    name='github',
    client_id=os.getenv("GITHUB_ID"),
    client_secret=os.getenv("GITHUB_SECRET"),
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'read:user user:email'},
)

# & GOOGLE OAUTH CONFIGURATION
google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_ID'),
    client_secret=os.getenv('GOOGLE_SECRET'),
    access_token_url='https://oauth2.googleapis.com/token',
    authorize_url='https://accounts.google.com/o/oauth2/v2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v3/',
    client_kwargs={
        'scope': 'openid email profile',
        'prompt': 'select_account',
    },
    jwks_uri='https://www.googleapis.com/oauth2/v3/certs',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
)

# | User database model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String)
    github_id = db.Column(db.String)
    pic = db.Column(db.String)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20))