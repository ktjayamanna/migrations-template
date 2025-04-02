from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .engine import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    phone_number = Column(String, unique=True, nullable=True)

    urls = relationship("Url", back_populates="owner")

class Url(Base):
    __tablename__ = "urls"

    url_id = Column(Integer, primary_key=True, index=True)
    shortened_url = Column(String, unique=True, nullable=False)
    original_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    expire_at = Column(DateTime, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.user_id"))

    owner = relationship("User", back_populates="urls")
