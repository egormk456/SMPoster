from sqlalchemy import Column, Integer, String, sql, ForeignKey

from data.db_gino import BaseModel


class PostsMediaGroup(BaseModel):
    __tablename__ = "posts_media_group"
    query: sql.select

    id = Column(Integer, primary_key=True, nullable=False)
    owner_id = Column(ForeignKey("clients.user_id", ondelete='CASCADE'))
    tg_channel_name = Column(String)
    tg_channel_id = Column(String)
    media_group_id = Column(String)
    count_files = Column(Integer, server_default="1")
