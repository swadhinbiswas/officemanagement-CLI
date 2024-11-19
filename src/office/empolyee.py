from src.models.employee import Employee
from src.settings.database import Database
from typing import List, Dict, Any,Optional
from sqlalchemy.exc import SQLAlchemyError
from src.Log import logger
from sqlalchemy import update
from datetime import datetime
from src.auth.cheaker import AuthCheaker




class EmployeeClass:
  def __init__(self):
    self.session=Database().get_session()
    self.db=Database().init_db()
    self.cheaker=AuthCheaker()
    
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
      accounts=employee.accounts
      return {"status":"success","message":"Accounts fetched successfully","data":[account.to_dict() for account in accounts]}
    else:
      return {"status":"error","message":"Employee not found"}
    
  def send_money(self,username:str,amount:int,reciever:str)->Dict[str,Any]:
    employee=self.session.query(Employee).filter_by(username=username).first()
    reciever=self.session.query(Employee).filter_by(username=reciever).first()
    try:
      if employee and reciever:
        if amount<=employee.accounts[0].balance:
          employee.accounts[0].balance-=amount
          reciever.accounts[0].balance+=amount
          self.session.commit()
          return {"status":"success","message":"Money sent successfully"}
        else:
          return {"status":"error","message":"Insufficient balance"}
      else:
        return {"status":"error","message":"Employee not found"}
    
    except SQLAlchemyError as e:
      return {"status":"error","message":str(e)}
    
    