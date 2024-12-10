from src.design.stylr import Style
from src.banking.bank import bankingSystem as banking_system
from src.chatroom import chatroom

stylr = Style()
def app():
  stylr.makeheading(text="Welcome to office management system",title="Office Management System",style="bold red",border_style="red")
  stylr.makepanel(text="Choose an option",title="Choose an option",style="bold green",border_style="green")
  stylr.maketree(text="1. Banking System",guide_style="bold green")
  stylr.maketree(text="2. Chatroom",style="bold green")
  stylr.maketree(text="3. Task Management System",style="bold green")
  stylr.maketree(text="3. Employee Management System",style="bold green")
  stylr.maketree(text="4. Leave Management System",style="bold green")
  stylr.maketree(text="5. Payroll Management System",style="bold green")
  stylr.maketree(text="3. Exit",style="bold red")
  choice = input("Enter your choice :  ")
  
  if choice == "1":
    banking_system()
  elif choice == "2":
    chatroom()
  
  # elif choice == "3":
  #   task_management_system()
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
  
