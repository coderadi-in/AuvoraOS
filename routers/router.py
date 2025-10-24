'''coderadi'''

# ? Importing libraries
from flask import Blueprint, render_template, redirect, url_for, request
from extensions import *

# ! Building base router
router = Blueprint('router', __name__)

# & Base route
@router.route('/')
def index():
    if (current_user.is_authenticated):
        return redirect(url_for('router.dashboard'))
    return render_template('index.html')