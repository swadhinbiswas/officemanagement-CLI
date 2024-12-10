from src.design.stylr import Style
from src.banking.bank import bankingSystem as banking_system
from src.chatroom import Chatroom
from src.office import OfficeManagement

stylr = Style()

def app():
  stylr.makeheading(text="Welcome to office management system",title="Office Management System",style="bold red",border_style="red")
  stylr.makepanel(text="Choose an option",title="Choose an option",style="bold green",border_style="green")
  stylr.maketree(text="1. Banking System",style="bold green")
  stylr.maketree(text="2. Chatroom",style="bold green")
  stylr.maketree(text="3. Task Management System",style="bold green")
  stylr.maketree(text="3. Employee Management System",style="bold green")
  stylr.maketree(text="4. Leave Management System",style="bold green")
  stylr.maketree(text="5. Payroll Management System",style="red")
  stylr.maketree(text="6. Exit",style="bold red")
  choice = input("Enter your choice :  ")
  while True:
    if choice == "1":
      banking_system()
    elif choice == "2":
      chatroom = Chatroom()
      stylr.makepanel(text="Choose an option",title="Chatroom",style="bold green",border_style="green")
      stylr.maketree(text="1. Create Chatroom",style="bold green")
      stylr.maketree(text="2. Join Chatroom",style="bold green")
      while True:
        choice = input("Enter your choice :  ")
        if choice == "1":
          chatroom.create_chatroom()
        elif choice == "2":
          chatroom.join_chatroom()
          app()
          
        else:
          print("Invalid choice. Please try again.")
    elif choice == "3":
      office_management = OfficeManagement()
      office_management.employee_management_system()
      
    elif choice == "4":
      office_management = OfficeManagement()
      office_management.employee_management_system()
    
    elif choice == "5":
      office_management = OfficeManagement()
      office_management.employee_management_system()
    elif choice == "6":
      
      print("Thank you for using our office management system")
      stylr.warn(" ⚠️ Exiting...")
      stylr.makepanel(text="Dev: Swadhin",title="Thank you",style="bold green",border_style="green")
      
      exit()
    else:
      print("Invalid choice. Please try again.")


  # elif choice == "4":
  #   employee_management_system()
  # elif choice == "5":
  #   leave_management_system()
  # elif choice == "6":
  #   payroll_management_system()
  # elif choice == "7":
  #   exit()
  # else:
  #   print("Invalid choice. Please try again.")
  #   app()
  
