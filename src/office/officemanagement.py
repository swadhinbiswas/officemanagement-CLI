from src.office import EmployeeClass
from src.design.stylr import Style
from src import app
style=Style()

class OfficeManagement:
  
  def __init__(self):
    self.employee=EmployeeClass()
  
  def employee_management_system(self):
    style.makeheading(text="Employee Management System",title="System",style="bold green",border_style="red")
    style.makepanel(text="Choose an option",title="Choice",style="bold green",border_style="green")
    style.maketree(text="1. Create Employee",style="bold green")
    style.maketree(text="2. Get Accounts",style="bold green")
    style.maketree(text="3. Send Money",style="bold green")
    style.maketree(text="4. Create Task",style="bold green")
    style.maketree(text="5. Get Task",style="bold green")
    style.maketree(text="6. Update Task",style="bold green")
    style.maketree(text="7. Get All Task",style="bold green")
    style.maketree(text="9. Exit System ",style="bold red")
    while True:
      choice=input("Enter your choice : ")
      if choice=="1":
        try:
          
          username=input("Enter username : ")
          password=input("Enter password : ")
          email=input("Enter email : ")
          depertment=input("Enter depertment : ")
          phone=input("Enter phone : ")
          name=input("Enter name : ")
          address=input("Enter address : ")
          profile_picture=input("Enter profile_picture : ")
          print(self.employee.create_employee(username=username,password=password,email=email,depertment=depertment,phone=phone,name=name,address=address,profile_picture=profile_picture))
        except Exception as e:
          print(e)
      elif choice=="2":
        try:
          username=input("Enter username : ")
          self.employee.get_accounts(username=username)
        except Exception as e:
          print(e)
          self.employee_management_system()
      elif choice=="3":
        username=input("Enter username : ")
        amount=int(input("Enter amount : "))
        reciever=input("Enter reciverusrname : ")
        print(self.employee.send_money(username=username,amount=amount,reciever=reciever))
        
      elif choice=="4":
        try:
          username=input("Enter username : ")
          deadline=input("Enter dadline : ")
          status=input("Enter status : ")
          priority=input("Enter priority : ")
          category=input("Enter category : ")
          sub_category=input("Enter sub_category : ")
          title=input("Enter title : ")
          description=input("Enter description : ")
          assignees=input("Enter assignees : ")
          
          self.employee.addTask(username=username,deadline=deadline,status=status,priority=priority,category=category,sub_category=sub_category,title=title,description=description,assignees=assignees)
          style.success("Task created successfully")
          self.employee_management_system()
        except Exception as e:
          print(e)
          self.employee_management_system()
      elif choice=="5":
        try:
          username=input("Enter username : ")
          self.employee.getTask(username=username)
          
        except Exception as e:
          print(e)
          self.employee_management_system()
          
      elif choice=="6":
        try:
          username=input("Enter username : ")
          task_id=input("Enter task_id : ")
          status=input("Enter status : ")
          priority=input("Enter priority : ")
          category=input("Enter category : ")
          sub_category=input("Enter sub_category : ")
          title=input("Enter title : ")
          description=input("Enter description : ")
          assignees=input("Enter assignees : ")
          self.employee.updateTask(username=username,task_id=task_id,status=status,priority=priority,category=category,sub_category=sub_category,title=title,description=description,assignees=assignees)
          style.success("Task updated successfully")
          self.employee_management_system()
        except Exception as e:
          print(e)
          self.employee_management_system()
          
      elif choice=="7":
        try:
          username=input("Enter username : ")
          self.employee.getAlltask(username=username)
        except Exception as e:
          print(e)
          self.employee_management_system()
      elif choice=="9":
        print("Exiting Employee Management System")
        app.app()
        
      else:
        print("Invalid choice")
    
    
 

        
      
        


   