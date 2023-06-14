from sqlalchemy import Column, Integer, BigInteger, String, sql, Boolean, TIMESTAMP

from data.db_gino import BaseModel


class Clients(BaseModel):
    __tablename__ = "clients"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(BigInteger, nullable=False, unique=True)
    username = Column(String)
    access = Column(Boolean, server_default="false")
    binds = Column(Integer, server_default="0")
    limit_binds = Column(Integer)
    subscribe_type = Column(String)
    payment = Column(Integer)
    subscribe = Column(TIMESTAMP)
    vk_token = Column(String)
    block = Column(Boolean, server_default="false")
