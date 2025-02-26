import importlib
import pkgutil

from flask import Blueprint, Flask

from configs.base import PORT
from configs.db import DB_URI
from db.db import db
from routes import init_routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Database initialize
db.init_app(app)

# App config prefix
api = Blueprint("api", __name__, url_prefix="/api")


# Dynamically import all models in the `db.models` package
def import_models(package_name):
    package = importlib.import_module(package_name)
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"{package_name}.{module_name}")


import_models("db.models")

with app.app_context():
    db.create_all()


@api.route("/ping")
def pong():
    return {"success": True, "message": "Pong"}


init_routes(app=app)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(port=PORT, debug=True)
