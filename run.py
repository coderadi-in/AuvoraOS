'''coderadi'''

# ? Importing main file
from main import *

# ! Initializing database
with server.app_context():
    db.create_all()

# ! Running server
if __name__ == '__main__':
    server.run(debug=True)