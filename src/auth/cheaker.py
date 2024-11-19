import re 
from werkzeug.security import generate_password_hash
from src.models.employee import Employee
from src.settings.database import Database
from sqlalchemy.exc import SQLAlchemyError
from src.Log import logger
from typing import Dict,Any,Optional
from src.models.adminmodel import Admin

class AuthCheaker:
    def __init__(self):
        self.email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        self.username_regex =re.compile(r'^[a-zA-Z0-9_]{3,50}$')

    def email_cheaker(self, email)->bool:
        return bool(self.email_regex.match(email))
      
    def password_hased(self,password:str)->str:
        return generate_password_hash(password)
    
    def username_cheaker(self,username:str)->bool:
        return bool(self.username_regex.match(username))
      
    def cheak_user(self,username:str,password:str)->bool:
     
        session=Database().get_session()
        user=session.query(Employee).filter_by(username=username).first() or session.query(Admin).filter_by(username=username).first()
        if user:
          password_hash=user.password
          hashed_password=generate_password_hash(password)
          if password_hash==hashed_password and user:
            return True
          else:
            return False
    def user_exist(self,username:str)->bool:
        session=Database().get_session()
        user=session.query(Employee).filter_by(username=username).first() or session.query(Admin).filter_by(username=username).first()
        if user:
          return True
        else:
          return False
    def email_exist(self,email:str)->bool:
        session=Database().get_session()
        user=session.query(Employee).filter_by(email=email).first() or session.query(Admin).filter_by(email=email).first()
        if user:
          return True
        else:
          return False

        
      
        
      
        

   
    
    
    
    
 