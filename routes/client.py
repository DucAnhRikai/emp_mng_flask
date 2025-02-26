from flask import Blueprint

from constants.route import ROUTE_CONSTANT
from routes.employee.client import client_employee_routes

client_routes = Blueprint(
    "client", __name__, url_prefix=ROUTE_CONSTANT.get("CLIENT").get("prefix")
)

client_routes.register_blueprint(client_employee_routes)
