'''coderadi'''

# ? Importing routers
from routers.router import router
from routers.auth import auth

# * function to bind routers
def bind_routers(server):
    server.register_blueprint(router)
    server.register_blueprint(auth)