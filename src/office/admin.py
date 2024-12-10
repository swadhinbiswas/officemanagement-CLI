from src.models.adminmodel import Admin
from src.settings.database import Database
from typing import List, Dict, Any,Optional
from sqlalchemy.exc import SQLAlchemyError
from src.Log import logger
from sqlalchemy import update
from datetime import datetime

class AdminClass:
  def __init__(self):
    self.session=Database().get_session()
    self.db=Database().init_db()
    
  def create_admin(self,username:str,password:str,email:str)->Dict[str,Any]:
    admin=Admin(
      username=username,
      password=password,
      email=email,
      
    )
    self.session.add(admin)
    self.session.commit()
    logger.info(f"""Admin created successfully with username {username},
                email {email}""")
    return {"status":"success","message":"Admin created successfully","data":admin.to_dict()}
  
  def update_admin(self,username:str,update_data)->Dict[str,Any]:
    
    admin=self.session.query(Admin).filter_by(username=username).first()
    if admin:
     valid_fields=["phone","name","address","profile_picture"]
     invalid_keys = set(update_data.keys()) - set(valid_fields)
     if invalid_keys:
        return {"status":"error","message":f"Invalid keys {invalid_keys} in update data"}
      
     update_data['updated_at']=datetime.now()
     
     stmp=update(Admin).where(Admin.username==username).values(update_data)
     self.session.execute(stmp)
     self.session.commit()
     return {"status":"success","message":"Admin updated successfully"}
    else:
      return {"status":"error","message":"Admin not found"}
    

    


  


