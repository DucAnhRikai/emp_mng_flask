from flask import Blueprint

from constants.route import ROUTE_CONSTANT
from routes.employee.admin import admin_employee_routes

admin_routes = Blueprint(
    "admin", __name__, url_prefix=ROUTE_CONSTANT.get("ADMIN").get("prefix")
)

admin_routes.register_blueprint(admin_employee_routes)
