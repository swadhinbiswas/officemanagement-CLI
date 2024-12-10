# Version: 1.0
# Creator:
# Date: 2021-09-26
# Description: Banking System
from src.design.stylr import Style
from src.banking.transction import BankingSystem

from src import app

def bankingSystem():
  bank=BankingSystem()
  stylr = Style()
  stylr.makeheading(text="Welcome to Banking system",title="Banking System",style="bold red",border_style="red")
  stylr.makepanel(text="Choose an option",title="Bank",style="bold green",border_style="green")
  stylr.maketree(text="1. Create account")
  stylr.maketree(text="2. Transfer money")
  stylr.maketree(text="3. Check balance")
  
  stylr.maketree(text="4. All accounts")
  stylr.maketree(text="5. Go back")
  stylr.maketree(text="6. Exit Banking System")
  stylr.maketree(text="7. Deposit money")
  stylr.maketree(text="8. Withdraw money")

  choice = input("Enter your choice: ")
  
  if choice == "1":
    name=input("Enter account holder name: ")
    account_type=input("Enter account type: ")
    employee_id=input("Enter employee id: ")
    try:
      x=bank.create_account(account_name=name,account_type=account_type,employee_id=employee_id)
      stylr.makepanel(text=x['message'],title=f"{x['status']}",style="bold green",border_style="green")
      stylr.makeprint(text=f"Account number: {x['id']}")
     
      bankingSystem()
    except Exception as e:
      print(e)
      bankingSystem()
    
    
  elif choice == "2":
    try:
      sender_account=input("Enter sender account: ")
      receiver_account=input("Enter receiver account: ")
      amount=input("Enter amount: ")
      descriptions=input("Enter descriptions: ")
      transfer=bank.transfer_money(sender_account=sender_account,receiver_account=receiver_account,amount=amount,descriptions=descriptions)
      print({"status":transfer['status'],"message":transfer['message']})
      bankingSystem()
    except Exception as e:
      print(e)
      bankingSystem()
    
  elif choice == "3":
    print("Check balance")
    try:
      account_number=input("Enter account number: ")
      balance=bank.get_account_balance(account_number=account_number)
      print({"status":balance['status'],"message":balance['message']})
      bankingSystem()
    except Exception as e:
      print(e)
      bankingSystem()
    
  elif choice == "4":
    print("All the Account Under Bank")
    
    try:
      stylr.makeheading(text="All the Account Under Bank",title="All the Account Under Bank",style="bold red",border_style="red")
      bank.get_all_accounts()
      # print({"status":accounts['status'],"message":accounts['message']})
      stylr.makepanel(text="Choose an option",title="Bank",style="bold green",border_style="green")
      stylr.maketree(text="1. Go back")
      stylr.maketree(text="2. Exit Banking System")
      
      while True:
        choice = input("Enter your choice: ")
        try:
          if choice == "1":
            stylr.warn(" ⚠️ Going back to Bank menu")
            bankingSystem()
          elif choice == "2":
            print("Exiting...")
            print("Thank you for using our banking system")
            app.app()
          else:
            stylr.warn("Invalid choice. Please try again.")
          
          
        except Exception as e:
          print(e)
    except Exception as e:
      print(e)
      bank.get_all_accounts()

  
  elif choice == "5":
    try:
      stylr.warn(" ⚠️ Going back to main menu")
      app.app()
    except Exception as e:
      print(e)
      app.app()
      
  
  elif choice == "6":
    print("Exiting...")
    print("Thank you for using our banking system")
    app.app()
    
  elif choice == "7":
    stylr.makepanel(text="Deposit Your Money Here",title="Deposit",style="bold green",border_style="green")
    try:
      account_number=input("Enter account number: ")
      amount=input("Enter amount: ")
      deposit=bank.deposit_money(account_number=account_number,amount=amount)
      stylr.makepanel(text=deposit['message'],title=f"{deposit['status']}",style="bold green",border_style="green")
      bank.get_account_balance(account_number=account_number)
    except Exception as e:
      print(e)
      bankingSystem()
    
  elif choice == "8":
    stylr.makepanel(text="Withdraw Your Money Here",title="Withdraw",style="bold green",border_style="green")
    while True:
      account_number=input("Enter account number: ")
      amount=input("Enter amount: ")
      try:
        
        withdraw=bank.withdraw_money(account_number=account_number,amount=amount)
        stylr.makepanel(text=withdraw['message'],title=f"{withdraw['status']}",style="bold green",border_style="green")
        bank.get_account_balance(account_number=account_number)
        
      except Exception as e:
        print(e)
  else:
    stylr.error("Invalid choice. Please try again.")
    bankingSystem()

    
  