from sqlalchemy import Column, Integer, String, DateTime
from app.core.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique = True, index = True, nullable = False)
    hashed_password = Column(String, nullable = False)
    created_at = Column(DateTime(timezone=True), server_default = func.now())
    applications = relationship('Application', back_populates = 'user')