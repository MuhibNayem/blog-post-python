from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    published = Column(Boolean, default=True)
    rating = Column(Integer, nullable=True)
    owner_id = Column(String, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")
