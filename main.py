'''coderadi'''

# ? Importing libraries
from flask import Flask
from extensions import *

# ? Importing routers
from routers import *

# ! Loading virtual environment [DEVELOPMENT ONLY]
from dotenv import load_dotenv
load_dotenv('.venv/vars.env')

# ! Building server
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# ! Binding extensions
bind_extensions(server)

# ! Binding routers
bind_routers(server)

# | Logger route
@logger.user_loader
def load_user(user_id):
    return User.query.get(user_id)