'''coderadi'''

# ? Importing libraries
from flask import Blueprint, render_template, redirect, url_for, request
from extensions import *

# ! Building base router
router = Blueprint('router', __name__)

# & BASE ROUTE
@router.route('/')
def index():
    if (current_user.is_authenticated):
        return redirect(url_for('router.dashboard'))
    return render_template('pages/index.html')

# & DASHBOARD ROUTE
@router.route('/dashboard')
@login_required
def dashboard():
    setup = OSSetup.query.filter_by(user_id=current_user.id).first()
    
    apps = InstalledApp.query.filter(
        (InstalledApp.system_app == True) |
        (InstalledApp.user_id == current_user.id)
    ).all()
    
    return render_template('pages/dash.html', data={
        'setup': setup,
        'apps': apps
    })