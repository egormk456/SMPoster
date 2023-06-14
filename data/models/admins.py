from sqlalchemy import Column, Integer, BigInteger, String, sql

from data.db_gino import BaseModel


class Admins(BaseModel):
    __tablename__ = "admins"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(BigInteger, nullable=False, unique=True)
    username = Column(String)
