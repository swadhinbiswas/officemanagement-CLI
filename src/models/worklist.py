from src.settings.database import Database,Base # Ensure this import is correct and the Database class is defined in the specified module
from sqlalchemy import Column, Integer, String,DateTime,Table,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship



task_assignments = Table(
    'task_assignments',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('tasks.id'), primary_key=True),
    Column('employee_id', Integer, ForeignKey('employees.id'), primary_key=True),
    Column('assignment_type', String(50), nullable=False), 
    Column('created_at', DateTime, default=datetime.now),
    Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)
)

class Task(Base):
  __table__name__ = 'tasks'
  id = Column(Integer, primary_key=True)
  creator_id:int = Column(Integer,nullable=False)
  assignee_id:int = relationship('Employee')
  deadline = Column(DateTime,nullable=False)
  status = Column(String(100),nullable=False)
  priority = Column(String(100),nullable=False)
  category = Column(String(100),nullable=False)
  sub_category = Column(String(100),nullable=False)
  title = Column(String(100),nullable=False)
  description = Column(String(255),nullable=False)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
  creator=relationship('Admin',foreign_keys=[creator_id],back_populates='created_tasks')
  assinees=relationship('Employee',
                        secondary=task_assignments,
                        back_populates='assigned_tasks',

                       primaryjoin="Task.id==task_assignments.c.task_id",
                       secondaryjoin="Employee.id==task_assignments.c.employee_id"
  )
  




class ClientList(Base):
  __tablename__='clientlist'
  id = Column(Integer, primary_key=True)
  name = Column(String(100),nullable=False)
  email = Column(String(50), unique=True, nullable=False)
  phone = Column(String(13),nullable=True)
  address = Column(String(200),nullable=True)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
  services=relationship('Service',back_populates='client')
  
  
  
  

class Services(Base):
  __tablename__ = 'services'
  id = Column(Integer, primary_key=True)
  client_id = Column(Integer,ForeignKey('clientlist.id'))
  service_type = Column(String(100),nullable=False)
  service_description = Column(String(255),nullable=False)
  service_status = Column(String(100),nullable=False)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
  client=relationship('ClientList',back_populates='services')
  price=relationship('Price',back_populates='service')



class Price(Base):
  id= Column(Integer,primary_key=True)
  service_id = Column(Integer,ForeignKey('services.id'))
  amount = Column(Integer,nullable=False)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
  service=relationship('Services',back_populates='price')

  