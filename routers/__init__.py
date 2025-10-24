'''coderadi'''

# ? Importing routers
from routers.router import router

# * function to bind routers
def bind_routers(server):
    server.register_blueprint(router)