from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from app.core.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
class Application(Base):
    __tablename__ = 'applications'
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    company_name = Column(String, nullable = False)
    role = Column(String, nullable = True)
    status = Column(String, default = 'pending')
    description = Column(Text, nullable = True)
    user = relationship("User", back_populates = "applications")
    applied_at = Column(DateTime(timezone = True), server_default = func.now())
    