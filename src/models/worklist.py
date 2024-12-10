from src.settings.database import Base # Ensure this import is correct and the Base class is defined in the specified module
from sqlalchemy import Column, Integer, String,DateTime,Table,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

task_assignments = Table(
    'task_assignments',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('tasks.id'), primary_key=True),
    Column('employee_id', Integer, ForeignKey('employees.id'), primary_key=True),
    Column('assignment_type', String(50), nullable=False),
    Column('created_at', DateTime, default=datetime.now),
    Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)
    
)


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
  created_tasks = relationship('Task', back_populates='creator') 
  assigned_tasks = relationship('Task', secondary=task_assignments, back_populates='assignees') 
  accounts=relationship('Accounts',back_populates='employee',cascade='all,delete-orphan')
  chatrooms = relationship('Chatroom', secondary='chatroom_members', back_populates='members') 
  
  
  

class Task(Base):
  __tablename__ = 'tasks'
  __allow_unmapped__ = True
  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  creator_id = Column(Integer, ForeignKey('employees.id'), nullable=False)  # Assuming creator is also an Employee
  deadline = Column(DateTime,nullable=False)
  status = Column(String(100),nullable=False)
  priority = Column(String(100),nullable=False)
  category = Column(String(100),nullable=False)
  sub_category = Column(String(100),nullable=False)
  title = Column(String(100),nullable=False)
  description = Column(String(255),nullable=False)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
  creator=relationship('Employee', foreign_keys=[creator_id], back_populates='created_tasks')
  assignees=relationship('Employee',
                        secondary=task_assignments,
                        back_populates='assigned_tasks',
                        primaryjoin="Task.id==task_assignments.c.task_id",
                        secondaryjoin="Employee.id==task_assignments.c.employee_id"
  )
  assignee: Mapped["Employee"] = relationship("Employee", foreign_keys=[creator_id], overlaps="created_tasks,creator") 




# class ClientList(Base):
#   __tablename__='clientlist'
#   id = Column(Integer, primary_key=True)
#   name = Column(String(100),nullable=False)
#   email = Column(String(50), unique=True, nullable=False)
#   phone = Column(String(13),nullable=True)
#   address = Column(String(200),nullable=True)
#   created_at = Column(DateTime, default=datetime.now())
#   updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
#   services = relationship("Service", back_populates="client_lists") 
  
  
  
  

# class Services(Base):
#   __tablename__ = 'services'
#   id = Column(Integer, primary_key=True)
#   client_id = Column(Integer,ForeignKey('clientlist.id'))
#   service_type = Column(String(100),nullable=False)
#   service_description = Column(String(255),nullable=False)
#   service_status = Column(String(100),nullable=False)
#   created_at = Column(DateTime, default=datetime.now())
#   updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
#   client_lists=relationship('ClientList',back_populates='services')
#   price=relationship('Price',back_populates='service')



# class Price(Base):
#   __tablename__='price'
#   id= Column(Integer,primary_key=True)
#   service_id = Column(Integer,ForeignKey('services.id'))
#   amount = Column(Integer,nullable=False)
#   created_at = Column(DateTime, default=datetime.now())
#   updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
#   service=relationship('Services',back_populates='price')

  