from sqlalchemy import Column, Integer, sql, String, TIMESTAMP, ForeignKey

from data.db_gino import BaseModel


class Payments(BaseModel):
    __tablename__ = "payments"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey("clients.user_id", ondelete='CASCADE'))
    date_p = Column(TIMESTAMP)
    type_p = Column(String)
    amount_p = Column(Integer)
