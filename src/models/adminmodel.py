from src.settings.database import Database,Base # Ensure this import is correct and the Database class is defined in the specified module
from sqlalchemy import Column, Integer, String,DateTime
from datetime import datetime




class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    username = Column(String(13), unique=True, nullable=False)
    password = Column(String(100),nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    phone = Column(String(13),nullable=True)
    name= Column(String(100),nullable=True)
    address = Column(String(200),nullable=True)
    profile_picture = Column(String(255),nullable=True)
    role = Column(String,default='admin')
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    
  
