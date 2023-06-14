from sqlalchemy import Column, Integer, BigInteger, String, sql, ARRAY, Boolean, ForeignKey

from data.db_gino import BaseModel


class Binds(BaseModel):
    __tablename__ = "binds"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    owner_id = Column(ForeignKey("clients.user_id", ondelete='CASCADE'))
    tg_channels_names = Column(ARRAY(String), server_default="{}")
    tg_channels_ids = Column(ARRAY(String), server_default="{}")
    tg_channels_urls = Column(ARRAY(String), server_default="{}")
    vk_groups_names = Column(ARRAY(String), server_default="{}")
    vk_groups_ids = Column(ARRAY(String), server_default="{}")
    vk_groups_urls = Column(ARRAY(String), server_default="{}")
    qty = Column(BigInteger)
    tags = Column(String)
    opt_text = Column(String)
    excl_tags = Column(String)
    url = Column(Integer)
    on = Column(Boolean, server_default="true")
