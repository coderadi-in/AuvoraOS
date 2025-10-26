'''coderadi'''

# ? Importing libraries
from flask import Blueprint, render_template, redirect, url_for, flash, request
from extensions import *

# ! Building auth router
auth = Blueprint('auth', __name__, url_prefix='/auth')

# * FUNCTION TO CHECK IF USER IS ALREADY AUTHENTICATED
def check_auth():
    if (current_user.is_authenticated):
        return redirect(url_for('router.dashboard'))
    
# * FUNCTION TO SETUP USER
def setup_user(user: User):
    ossetup = OSSetup.query.filter_by(user_id=user.id).first()
    if (not ossetup):
        new_setup = OSSetup(user_id=user.id)
        db.session.add(new_setup)
        db.session.commit()
    login_user(user)

# & GOOGLE LOGIN ROUTE
@auth.route('/login/google')
def google_login():
    check_auth()
    redirect_uri = url_for('auth.google_authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

# & GOOGLE LOGIN CALLBACK ROUTE
@auth.route('/login/google/callback')
def google_authorize():
    try:
        # Fetch token
        token = oauth.google.authorize_access_token()

        # Check for userinfo in token
        user_info = token.get('userinfo')
        if (not user_info):
            user_info = oauth.google.get('userinfo').json()

        # Check for email in token
        if (not user_info.get('email')):
            flash('Google login failed: No email provided', 'error')
            return redirect(url_for('router.index'))
        
        # Update user in db
        user = User.query.filter_by(email=user_info['email']).first()
        if (not user):
            user = User(
                google_id=user_info.get('sub'),
                name=user_info.get('name', 'User'),
                email=user_info['email'],
                pic=user_info['picture']
            )
            db.session.add(user)
            db.session.commit()

        else:
            if not user.google_id:
                user.google_id = user_info.get('sub')

        # Login user and redirect to dashboard
        setup_user(user)
        flash('Logged in successfully with Google.', 'success')
        return redirect(url_for('router.dashboard'))
    
    except Exception as e:
        print(e)
        flash("Failed to log in with google!", "error")
        return redirect(url_for('router.index'))

# & GITHUB LOGIN ROUTE
@auth.route('/login/github')
def github_login():
    redirect_uri = url_for('auth.github_authorize', _external=True)
    return github.authorize_redirect(redirect_uri)

# & GITHUB LOGIN CALLBACK ROUTE
@auth.route('/login/github/callback')
def github_authorize():
    try:
        token = github.authorize_access_token()
        res = github.get('user')
        user_info = res.json()

        # Fetch primary email
        emails = github.get('user/emails').json()
        primary_email = next((e['email'] for e in emails if e['primary']), None)

        # Check if user exists in DB
        user = User.query.filter_by(email=primary_email).first()
        if (not user):
            user = User(
                github_id=user_info['id'],
                name=user_info['login'],
                email=primary_email,
                pic=user_info['avatar_url']
            )
            db.session.add(user)
            db.session.commit()

        # Login user and redirect to dashboard
        setup_user(user)
        flash("Logged in successfully with GitHub.", "success")
        return redirect(url_for('router.dashboard'))

    except Exception as e:
        print(e)
        flash("Failed to log in with Github!", 'error')
        return redirect(url_for('router.index'))

# & LOGOUT ROUTE
@auth.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('router.index'))