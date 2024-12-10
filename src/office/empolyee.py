
from src.settings.database import Database
from typing import List, Dict, Any,Optional
from sqlalchemy.exc import SQLAlchemyError
from src.Log import logger
from sqlalchemy import update
from datetime import datetime
from src.auth.cheaker import AuthCheaker
from src.models import Task
from src.models import Employee
from rich.console import Console
from rich.table import Table
from src.design.stylr import Style

console=Console()
class EmployeeClass:
  def __init__(self):
    self.session=Database().get_session()
    self.db=Database().init_db()
    self.cheaker=AuthCheaker()
    self.console=Console()
    self.style=Style()
    
  def create_employee(self,username:str,password:str,email:str,depertment:str|None,phone:str|None,name:str|None,address:str|None,profile_picture:str|None)->Dict[str,Any]:
    if not self.cheaker.email_cheaker(email):
      return {"status":"error","message":"Invalid email"}
    if not self.cheaker.username_cheaker(username):
      return {"status":"error","message":"Invalid username"}
    if self.cheaker.user_exist(username):
      return {"status":"error","message":"User already exist"}
    if self.cheaker.email_exist(email):
      return {"status":"error","message":"Email already exist"}
    hased_passowrd=self.cheaker.password_hased(password)
    
    employee=Employee(
      username=username,
      password=hased_passowrd,
      email=email,
      depertment=depertment,
      phone=phone,
      name=name,
      address=address,
      profile_picture=profile_picture
      
    )
    self.session.add(employee)
    self.session.commit()
    logger.info(f"""Employee created successfully with username {username},
                email {email}""")
    return {"status":"success","message":"Employee created successfully","data":employee.to_dict()}
  
  
  def get_accounts(self,username:str)->Dict[str,Any]:
    employee=self.session.query(Employee).filter_by(username=username).first()
    if employee:

      table=Table(title="Profile")
      table.add_column("username")
      table.add_column("email")
      table.add_column("depertment")
      table.add_column("phone")
      table.add_column("address")
      table.add_column("profile_picture")
      table.add_column("role")
      table.add_column("created_at")
      table.add_column("updated_at")
      
      table.add_row(employee.username,employee.email,employee.depertment,employee.phone,employee.address,employee.profile_picture,employee.role,employee.created_at,employee.updated_at)
     
      console.print(table)
      
      
    else:
      self.style.warn("Employee not found")
      
    
  def send_money(self,username:str,amount:int,reciever:str)->Dict[str,Any]:
    employee=self.session.query(Employee).filter_by(username=username).first()
    reciever=self.session.query(Employee).filter_by(username=reciever).first()
    try:
      if employee and reciever:
        if amount<=employee.accounts[0].balance:
          employee.accounts[0].balance-=amount
          reciever.accounts[0].balance+=amount
          self.session.commit()
          
        else:
          return {"status":"error","message":"Insufficient balance"}
      else:
        return {"status":"error","message":"Employee not found"}
    
    except SQLAlchemyError as e:
      return {"status":"error","message":str(e)}
    
  def addTask(self,username:str,deadline:str,status:str,priority:str,category:str,sub_category:str,title:str,description:str,assignees:List[str])->Dict[str,Any]:
    employee=self.session.query(Employee).filter_by(username=username).first()
    if employee:
      task=Task(
        deadline=deadline,  

        status=status,
        priority=priority,
        category=category,
        sub_category=sub_category,
        title=title,
        description=description,
        creator=employee,
        assignees=[self.session.query(Employee).filter_by(username=assignee).first() for assignee in assignees]
      )
      self.session.add(task)
      self.session.commit()
      logger.info(f"""Task created successfully with id : {task.id},
                  deadline : {deadline}
                  status : {status}
                  priority : {priority}
                  category : {category}
                  sub_category : {sub_category}
                  title : {title}
                  description : {description}
                  assignees {assignees}
                  
                  """)
      self.console.print(f"Task created successfully with id {task.id}")
      
      
      
    else:
      self.style.warn("Employee not found")
      return {"status":"error","message":"Employee not found"}
  
  def getTask(self,username:str)->Dict[str,Any]:
    employee=self.session.query(Employee).filter_by(username=username).first()
    if employee:
      tasks=employee.assigned_tasks
      if tasks:
        table=Table(title="Tasks")
        table.add_column("id")
        table.add_column("deadline")
        table.add_column("status")
        table.add_column("priority")
        table.add_column("category")
        table.add_column("sub_category")
        table.add_column("title")
        table.add_column("description")
        table.add_column("created_at")
        table.add_column("updated_at")
        for task in tasks:
          table.add_row(task.id,task.deadline,task.status,task.priority,task.category,task.sub_category,task.title,task.description,task.created_at,task.updated_at)
        console.print(table)
      else:
       self.style.warn("No tasks found")
    else:
     self.style.warn("Employee not found")
    
  def getAlltask(self)->Dict[str,Any]:
    tasks=self.session.query(Task).all()
    if tasks:
      table=Table(title="Tasks")
      table.add_column("id")
      table.add_column("deadline")
      table.add_column("status")
      table.add_column("priority")
      table.add_column("category")
      table.add_column("sub_category")
      table.add_column("title")
      table.add_column("description")
      table.add_column("created_at")
      table.add_column("updated_at")
      for task in tasks:
        table.add_row(task.id,task.deadline,task.status,task.priority,task.category,task.sub_category,task.title,task.description,task.created_at,task.updated_at)
      console.print(table)
    else:
      self.style.warn("No tasks found")
  
  def updateTask(self,username:str,task_id:int,update_data:Dict[str,Any])->Dict[str,Any]:
    employee=self.session.query(Employee).filter_by(username=username).first()
    if employee:
      task=self.session.query(Task).filter_by(id=task_id).first()
      if task:
        valid_fields=["deadline","status","priority","category","sub_category","title","description"]
        invalid_keys = set(update_data.keys()) - set(valid_fields)
        if invalid_keys:
          return {"status":"error","message":f"Invalid keys {invalid_keys} in update data"}
        
        update_data['updated_at']=datetime.now()
        
        stmp=update(Task).where(Task.id==task_id).values(update_data)
        self.session.execute(stmp)
        self.session.commit()
        return {"status":"success","message":"Task updated successfully"}
      else:
        return {"status":"error","message":"Task not found"}
    else:
      return {"status":"error","message":"Employee not found"}
    
    