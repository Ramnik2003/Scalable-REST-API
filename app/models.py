from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")

class DBTask(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    owner = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)