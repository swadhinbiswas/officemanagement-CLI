from src.settings.database import Database,Base # Ensure this import is correct and the Database class is defined in the specified module
from sqlalchemy import Column, Integer, String,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from src.models.accounts import Accounts



class Employee(Base):
  __tablename__ = 'employees'
  id = Column(Integer, primary_key=True)
  username = Column(String(13), unique=True, nullable=False)
  password = Column(String(100),nullable=False)
  depertment = Column(String(100),nullable=True)
  email = Column(String(50), unique=True, nullable=False)
  phone = Column(String(13),nullable=True)
  name= Column(String(100),nullable=True)
  address = Column(String(200),nullable=True)
  profile_picture = Column(String(255),nullable=True)
  role = Column(String,default='employee')
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
  accounts=relationship('Accounts',back_populates='employee',cascade='all,delete-orphan')
  
  