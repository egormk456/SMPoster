from sqlalchemy import Column, BigInteger, String, sql

from data.db_gino import BaseModel


class InviteLinks(BaseModel):
    __tablename__ = "invite_links"
    query: sql.select

    id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(String(length=250), nullable=False)
    url = Column(String(length=250))
