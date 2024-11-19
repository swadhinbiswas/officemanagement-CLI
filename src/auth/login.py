from src.models.adminmodel import Admin
from src.settings.database import Database
from typing import List, Dict, Any,Optional
from sqlalchemy.exc import SQLAlchemyError
from src.Log import logger
from src.auth.cheaker import AuthCheaker






class LoginClass:
  def __init__(self):
    self.session=Database().get_session()
    self.db=Database().init_db()
    self.cheaker=AuthCheaker()
    
    
  def login(self,username:str,password:str)->bool:
    if self.cheaker.cheak_user(username, password):
      logger.info(f"User {username} login successfully")
      return True
    else:
      logger.error(f"User {username} login failed")
      return False
  
  