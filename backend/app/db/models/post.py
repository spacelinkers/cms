from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
import datetime

from app.db.base_class import Base

class Post(Base):

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    author = Column(String, nullable=False)
    create_at = Column(DateTime, nullable=False, default=datetime.datetime.now())
    is_active = Column(Boolean, default=False)
