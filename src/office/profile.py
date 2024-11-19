from src.models.employee import Employee
from src.settings.database import Database
from typing import List, Dict, Any,Optional
from sqlalchemy.exc import SQLAlchemyError
from src.Log import logger
from sqlalchemy import update
from datetime import datetime
from src.auth.cheaker import AuthCheaker
from src.design.stylr import Style
from PIL import Image
from image import DrawImage
from rich.panel import Panel
from rich.layout import Layout
from rich.console import Console

class Profile:
  def __init__(self):
    self.session=Database().get_session()
    self.db=Database().init_db()
    self.cheaker=AuthCheaker()
    self.style=Style()
    self.console=Console()
  
  def get_profile(self,username:str)->Dict[str,Any]:
    employee=self.session.query(Employee).filter_by(username=username).first()
    if employee:
      return {
        "name":employee.name,
        "username":employee.username,
        "email":employee.email,
        "depertment":employee.depertment,
        "phone":employee.phone,
        "address":employee.address,
        "profile_picture":employee.profile_picture,
        "status":"success"
        
      }
    else:
      return {"status":"error","message":"Employee not found"}
  
  def printprofile(self):
    profile=self.get_profile()
    name=profile["name"]
    username=profile["username"]
    email=profile["email"]
    depertment=profile["depertment"]
    phone=profile["phone"]
    address=profile["address"]
    profile_picture=profile["profile_picture"]
    status=profile["status"]
  
    panel = Panel(f"""Name: {name}\nUsername: {username} \nEmail: {email} \n Depertment: {depertment} \n Phone: {phone} \n Address: {address} \n Status: {status}""", title="Profile", style="bold green", border_style="red",title_align="center",expand=True)
  
    self.style.makeheading(text=panel,title="Profile",style="bold green",border_style="red")
    image=Image.open(profile_picture)
    image2=DrawImage.from_file(image)
    layout=Layout()
    layout.split_row(
        Layout(image2.draw_image(),name="picture"),
        Layout(self.console.print(panel),name="Biodata", ratio=1)
        
    )
    
    


profile={
  "name":"admin",
  "username":"admin",
  "email":"admin",
  "depertment":"admin",
  "phone":"admin",
  "address":"admin",
  "profile_picture":"admin",
  "status":"success",
  "phone":"admin",
  "address":"admin",
  "profile_picture":"admin",
}
from rich.table import Table
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.tree import Tree
from rich.prompt import Prompt
from rich.live import Live

student_table=Table(header_style="bold red",style="bold red")
student_table.add_column("Name")
student_table.add_column("Year")
student_table.add_column("Time")
student_table.add_row("admin","admin","admin")
student_table.add_row("admin","admin","admin")
student_table.add_row("admin","admin","admin")


# student = Panel(student_table, title="Student", style="bold red", border_style="red",title_align="center")
# print(student)
# layout = Layout()
# makeheading=Layout()
# makeheading.split_row(
#     Layout(student_table,name="Student"),
#     Layout(name="main", ratio=1),
#     Layout(name="footer"),
# )
# print(makeheading)


  