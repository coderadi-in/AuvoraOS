'''coderadi'''

# ? Importing libraries
from flask import Blueprint, render_template, redirect, url_for, flash, request
from extensions import *

# ! Building new-widgets router
new = Blueprint('new', __name__, url_prefix='/new')

# & NEW FOLDER ROUTE
@new.route('/folder/', methods=['POST'])
def new_folder():
    folder_name = request.form.get('folder-name')

    