from src.settings.database import Database,Base 
from sqlalchemy import Column, Integer, String,DateTime,Table,ForeignKey,Float,Boolean
from decimal import Decimal
from datetime import datetime
from sqlalchemy.orm import relationship
from src.models.employee import Employee



class Accounts(Base):
  __tablename__ = 'accounts'
  id = Column(Integer, primary_key=True)
  accountnumber=Column(String(13),unique=True,nullable=False)
  accout_holdername=Column(String(50),nullable=False)
  accounttype=Column(String(50),nullable=False)
  balance=Column(Float,default=0.0,nullable=False)
  isactive=Column(Boolean,default=True,nullable=False)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(),onupdate=datetime.now())
  employee_id = Column(Integer, ForeignKey('employees.id'))
  employee = relationship("Employee", back_populates="accounts")
  
  sent_transactions = relationship("Transaction", foreign_keys="Transaction.sender_id", back_populates="sender")
  received_transactions = relationship("Transaction", foreign_keys="Transaction.receiver_id", back_populates="receiver")



class Transactions(Base):
  __tablename__='transactions'
  id = Column(Integer, primary_key=True)
  sender_id = Column(Integer, ForeignKey('accounts.id'))
  receiver_id = Column(Integer, ForeignKey('accounts.id'))
  descriptions=Column(String(255),nullable=True)
  amount = Column(Float,nullable=False)
  status=Column(String(50),nullable=False,default='pending')
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(),onupdate=datetime.now())
  sender = relationship("Accounts", foreign_keys=[sender_id], back_populates="sent_transactions")
  receiver = relationship("Accounts", foreign_keys=[receiver_id], back_populates="received_transactions")
  

  