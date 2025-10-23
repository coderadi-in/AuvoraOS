'''coderadi'''

# ? Importing libraries
from flask import Flask
from extensions import *

# ! Building server
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coderadi.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = 'coderadi.vOS'

# ! Binding extensions
bind_extensions(server)