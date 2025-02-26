from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import Relationship

from db.db import db


class Role(db.Model):
    __tablename__ = "roles"

    # schema
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20), nullable=False, default="")

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    # one-to-many
    employees = Relationship("Employee", back_populates="role")

    def __repr__(self):
        return f"<Roles {self.usernaidme}>"
