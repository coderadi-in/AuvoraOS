'''coderadi'''

# ? Importing flask extensions
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from authlib.integrations.flask_client import OAuth

# ? Importing libraries
import os

# & DATASET OF INSTALLED APPS
installed_apps = [
    {
        "app_id": "file_manager",
        "app_title": "File manager",
        "app_icon": "/static/assets/icons/apps/file_manager.png",
        "pinned": True,
    },
    {
        "app_id": "settings",
        "app_title": "Settings",
        "app_icon": "/static/assets/icons/apps/settings.png",
        "pinned": True,
    },
]

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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    google_id = db.Column(db.String(50))
    github_id = db.Column(db.String(50))
    pic = db.Column(db.String(100))
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20))

# | OS Setup database model
class OSSetup(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    bg = db.Column(db.String(100))
    theme = db.Column(db.String(5), default='light')
    pinned_apps = db.Column(db.JSON, default=lambda: ['settings', 'file_manager'])

# | Installed App database model
class InstalledApp(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_id = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer)
    icon = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    app_data = db.Column(db.Float, default=0.00)
    system_app = db.Column(db.Boolean, default=False)
    pinned = db.Column(db.Boolean, default=False)