from src.settings.database import Database
from typing import List, Dict, Any,Optional
from  src.models import Accounts,Transactions
from datetime import datetime
import random 
from sqlalchemy.exc import SQLAlchemyError
from src.Log import logger
from src.models import Employee
import enum
from rich.console import Console
from rich.table import Table

class AccountType(enum.Enum):
    SAVINGS = "savings"
    SALARY = "salary"
    BUSINESS = "business"

class BankingSystem:
    def __init__(self):
      self.session=Database().get_session()
      self.db=Database().init_db()
      
      
    def create_account(self,account_name:str,account_type:str,employee_id:int)->Dict[str,Any]:
        x=random.random()
        x=str(x)
        account_numer=x.split('.')[1]
        
        
        try:
          account=Accounts(
            accountnumber=account_numer,
            accout_holdername=account_name,
            accounttype=account_type,
            employee_id=employee_id
            
          )
          print(f"Account number {account_numer}")
          self.session.add(account)
          self.session.commit()
          logger.info(f"""Account created successfully with account number {account_numer},
                      for employee {employee_id},
                      account holder name {account_name} and account type {account_type}""")
          return {"status":"success","message":"Account created successfully","account_number":account_numer}
        except SQLAlchemyError as e:
          self.session.rollback()
          logger.error(f"Error creating account {str(e)}")
          return {"status":"error","message":f"An error occurred: {str(e)}"}
          
    def transfer_money(self, sender_account: int, receiver_account: int, amount: float, descriptions: str | None) -> Dict[str, Any]:
      try:
          self.session.begin_nested()
          sender = self.session.query(Accounts).filter_by(id=sender_account, isactive=1).with_for_update().first()
          receiver = self.session.query(Accounts).filter_by(id=receiver_account, isactive=1).with_for_update().first()

          if not sender or not receiver:
              self.session.rollback()
              logger.error(f"{sender_account} or {receiver_account} account not found")
              return {"status": "error", "message": "Sender or receiver account not found"}

          if sender.balance < amount:
              self.session.rollback()
              logger.error(f"Insufficient balance in account {sender_account}")
              return {"status": "error", "message": "Insufficient balance"}

          transctions = Transactions(
              sender_id=sender_account,
              receiver_id=receiver_account,
              amount=amount,
              descriptions=descriptions
          )
          
          sender.balance -= amount
          receiver.balance += amount
          self.session.add(transctions)
          self.session.commit()
          logger.info(f"Money transferred successfully from account {sender_account} to account {receiver_account}")
          self.session.commit()
          self.session.close()
       
          return {"status": "success", "message": "Transaction successful"} 

      except Exception as e:
          self.session.rollback()
          logger.error(f"Error during money transfer: {e}")
          return {"status": "error", "message": f"An error occurred: {e}"}
        
    def account_transctions(self,account_number:int)->str:
      account=self.session.query(Accounts).filter_by(id=account_number).first()
      if not account:
        logger.error(f"Account not found with account number {account_number}")
        return {"status":"error","message":"Account not found"}
      
       
      return {
            'sent': self.session.query(Transactions).filter_by(sender_id=account.id).all(),
            'received': self.session.query(Transactions).filter_by(receiver_id=account.id).all()
        }
        
    def get_account_balance(self,account_number:int)->Dict[str,Any]:
      account=self.session.query(Accounts).filter_by(id=account_number).first()
      if not account:
        logger.error(f"Account not found with account number {account_number}")
        return {"status":"error","message":"Account not found"}
      return {"status":"success","message":"Account balance fetched successfully","data":account.to_dict()}
    
    def get_all_accounts(self)->List[Dict[str,Any]]:
      accounts=self.session.query(Accounts).all()
      table = Table(title="All Accounts")
      table.add_column("Account Number", style="cyan", no_wrap=True)
      table.add_column("Account Holder Name", style="magenta")
      table.add_column("Account Type", style="green")
      table.add_column("Balance", style="yellow")
      table.add_column("Is Active", style="red")
      for account in accounts:
        table.add_row(str(account.accountnumber), account.accout_holdername, account.accounttype, str(account.balance), str(account.isactive),)
      console = Console()
      console.print(table)
      
    
    def get_account_details(self,account_number:int)->Dict[str,Any]:
      account=self.session.query(Accounts).filter_by(id=account_number).first()
      if not account:
        logger.error(f"Account not found with account number {account_number}")
        return {"status":"error","message":"Account not found"}
      table=Table(title="Account Details")
      table.add_column("Account Number",style="cyan",no_wrap=True)
      table.add_column("Account Holder Name",style="magenta")
      table.add_column("Account Type",style="green")
      table.add_column("Balance",style="yellow")
      table.add_column("Is Active",style="red")
      table.add_row(str(account.accountnumber),account.accout_holdername,account.accounttype,str(account.balance),str(account.isactive))
      console=Console()
      console.print(table)
    
    def delete_account(self,account_number:int)->Dict[str,Any]:
      account=self.session.query(Accounts).filter_by(id=account_number).first()
      if not account:
        logger.error(f"Account not found with account number {account_number}")
        return {"status":"error","message":"Account not found"}
      account.isactive=0
      self.session.commit()
      return {"status":"success","message":"Account deleted successfully"}
    
    def update_account(self,account_number:int,account_name:str,account_type:str)->Dict[str,Any]:
      account=self.session.query(Accounts).filter_by(id=account_number).first()
      if not account:
        logger.error(f"Account not found with account number {account_number}")
        return {"status":"error","message":"Account not found"}
      account.accout_holdername=account_name
      account.accounttype=account_type
      self.session.commit()
      return {"status":"success","message":"Account updated successfully"}
    
    def deposit_money(self,account_number:int,amount:float)->Dict[str,Any]:
      account=self.session.query(Accounts).filter_by(id=account_number).first()
      if not account:
        logger.error(f"Account not found with account number {account_number}")
        return {"status":"error","message":"Account not found"}
      account.balance+=amount
      self.session.commit()
      return {"status":"success","message":"Money deposited successfully"}
    
    def withdraw_money(self,account_number:int,amount:float)->Dict[str,Any]:
      account=self.session.query(Accounts).filter_by(id=account_number).first()
      if not account:
        logger.error(f"Account not found with account number {account_number}")
        return {"status":"error","message":"Account not found"}
      if account.balance<amount:
        logger.error(f"Insufficient balance in account {account_number}")
        return {"status":"error","message":"Insufficient balance"}
      account.balance-=amount
      self.session.commit()
      return {"status":"success","message":"Money withdrawn successfully"}
    
    
    def get_account_by_employee(self,employee_id:int)->List[Dict[str,Any]]:
      accounts=self.session.query(Accounts).filter_by(employee_id=employee_id).all()
      return [account.to_dict() for account in accounts]
    