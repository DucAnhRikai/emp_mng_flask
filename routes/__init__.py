from routes.admin import admin_routes
from routes.client import client_routes


def init_routes(app):
    print("[ROUTES]: Initializing!")

    app.register_blueprint(admin_routes)
    app.register_blueprint(client_routes)
    print("[ROUTES]: Initialized!")
