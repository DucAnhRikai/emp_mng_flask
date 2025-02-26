from flask import Blueprint

from constants.route import ROUTE_CONSTANT

client_employee_routes = Blueprint(
    "client_employee",
    __name__,
    url_prefix=ROUTE_CONSTANT.get("CLIENT").get("EMPLOYEE").get("prefix"),
)
