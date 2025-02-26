from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, event, func
from sqlalchemy.orm import Relationship

from db.db import db


class Department(db.Model):
    __tablename__ = "departments"

    # schema
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(10), nullable=False, unique=True)
    name = Column(String(50), nullable=False, default="")

    created_by = Column(Integer, ForeignKey("employees.id"), nullable=False)
    updated_by = Column(Integer, ForeignKey("employees.id"), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    # many-to-one
    emp_create = Relationship("Employee", back_populates="dpm_create")
    emp_update = Relationship("Employee", back_populates="dpm_update")

    def __repr__(self):
        return f"<Department {self.code}>"


@event.listens_for(Department, "before_insert")
def beforeInsert(_mapper, _connection, target):
    target.code = str(target.code).capitalize()
