import bcrypt
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, event, func
from sqlalchemy.orm import relationship

from db.db import db


class Employee(db.Model):
    __tablename__ = "employees"

    # schema
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=True)

    username = Column(String(20), unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String(50), nullable=False, default="")
    birthday = Column(DateTime, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    # one-to-many
    dpm_create = relationship("Department", back_populates="emp_create")
    dpm_update = relationship("Department", back_populates="emp_update")

    # many-to-one
    role = relationship("Role", back_populates="employees")

    def __repr__(self):
        return f"<Employee {self.id}>"


@event.listens_for(Employee, "before_insert")
def beforeInsertUser(_mapper, _connection, target):
    if not target.password:
        raise ValueError("Password can't be empty!")
    target.password = bcrypt.hashpw(target.password.encode("utf-8"), bcrypt.gensalt())
