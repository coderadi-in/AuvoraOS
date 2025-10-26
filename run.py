'''coderadi'''

# ? Importing main file
from main import *

# ! Initializing database
with server.app_context():
    db.create_all()

# & SETUP BASIC DB STORAGE
with server.app_context():
    for app in installed_apps:
        if (not InstalledApp.query.filter_by(app_id=app['app_id']).first()):
            print("Adding 1 app...")
            new_app = InstalledApp(
                app_id=app['app_id'],
                icon=app['app_icon'],
                title=app['app_title'],
                system_app=True,
                pinned=app['pinned'],
            )
            db.session.add(new_app)
            db.session.commit()

# ! Running server
if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0')