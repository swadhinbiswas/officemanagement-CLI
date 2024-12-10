from src.settings.database import Database,Base
from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship, backref



class Message(Base):
  __tablename__ = 'messages'
  id = Column(Integer, primary_key=True)
  sender_id = Column(Integer,nullable=False)
  receiver_id = Column(Integer,nullable=False)
  message = Column(String(255),nullable=False)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
  


chatroom_members = Table('chatroom_members', Base.metadata,
    Column('chatroom_id', Integer, ForeignKey('chatrooms.id'), primary_key=True),
    Column('employee_id', Integer, ForeignKey('employees.id'), primary_key=True)
)

class Chatroom(Base):
  __tablename__ = 'chatrooms'
  id = Column(Integer, primary_key=True)
  name = Column(String(100),nullable=False)
  description = Column(String(255),nullable=False)
  creator=Column(Integer,nullable=False)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
  members=relationship('Employee',secondary='chatroom_members',back_populates='chatrooms')
  