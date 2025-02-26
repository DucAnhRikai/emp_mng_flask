from flask import Blueprint

from constants.route import ROUTE_CONSTANT

admin_employee_routes = Blueprint(
    "admin_employee",
    __name__,
    url_prefix=ROUTE_CONSTANT.get("ADMIN").get("EMPLOYEE").get("prefix"),
)
