'''coderadi'''

# ? Importing libraries
from flask import Blueprint, request, jsonify
from extensions import *

# ! Building api router
api = Blueprint('api', __name__, url_prefix='/api')

# * function to load setup
def load_setup() -> OSSetup|None:
    setup = OSSetup.query.get(current_user.id)

    if (not setup):
        return None
    
    return setup

# & LOAD ROUTE
@api.route('/load')
def api_load():
    setup = load_setup()

    if (not setup):
        return jsonify({})

    root = setup.root
    meta = setup.meta

    print({
        'root': root,
        'meta': meta
    })

    return jsonify({
        'root': root,
        'meta': meta
    })

# & SAVE ROUTE
@api.route('/save', methods=['POST'])
def api_save():
    setup = load_setup()
    data = request.get_json()
    root = data.get('root')
    meta = data.get('meta')

    if (setup):
        setup.root = root
        setup.meta = meta
        db.session.commit()