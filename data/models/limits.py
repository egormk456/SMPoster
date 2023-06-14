from sqlalchemy import Column, Integer, sql

from data.db_gino import BaseModel


class Limits(BaseModel):
    __tablename__ = "limits"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    standard_pay = Column(Integer)
    add_pay = Column(Integer)
    bind_limit = Column(Integer)
