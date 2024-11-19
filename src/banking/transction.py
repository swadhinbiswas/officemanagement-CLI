from src.settings.database import Database
from typing import List, Dict, Any,Optional
from models.accounts import Accounts,Transactions
from datetime import datetime
import random 
from sqlalchemy.exc import SQLAlchemyError
from src.Log import logger
from models.employee import Employee
import enum

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
        account_numer=x.split('.')[1]
        
        try:
          account=Accounts(
            accountnumber=account_numer,
            accout_holdername=account_name,
            accounttype=account_type,
            employee_id=employee_id
            
          )
          self.session.add(account)
          self.session.commit()
          logger.info(f"""Account created successfully with account number {account_numer},
                      for employee {employee_id},
                      account holder name {account_name} and account type {account_type}""")
          return {"status":"success","message":"Account created successfully","data":account.to_dict()}
        except SQLAlchemyError as e:
          self.session.rollback()
          logger.error(f"Error creating account {str(e)}")
          return {"status":"error",
                  "message":"Error creating account"}
          
    def transfer_money(self,sender_account:int,receiver_account:int,amount:float,descriptions:str|None)->Dict[str,Any]:
      try:
        self.session.begin_nested()
        sender=self.session.query(Accounts).filter_by(id=sender_account,
                                                      isactive=1).with_for_update().first()
        reciver=self.session.query(Accounts).filter_by(id=receiver_account,
                                                       isactive=1).with_for_update().first()
        if not sender or not reciver:
          self.session.rollback()
          logger.error(f"{sender_account} or {receiver_account} account not found")
          return {"status":"error","message":"Sender or receiver account not found"}
        if sender.balance<amount:
          self.session.rollback()
          logger.error(f"Insufficient balance in account {sender_account}")
          return {"status":"error","message":"Insufficient balance"}
        transctions=Transactions(
          sender_id=sender_account,
          receiver_id=receiver_account,
          amount=amount,
          descriptions=descriptions
        )
        
        self.session.add(transctions)
        sender.balance-=amount
        reciver.balance+=amount
        transctions.status="success"
        self.session.commit()
        logger.info(f"Money transfered successfully from account {sender_account} to account {receiver_account}")
        return {"status":"success","message":"Money transfered successfully"}
      except SQLAlchemyError as e:
        self.session.rollback()
        logger.error(f"Error transfering money {str(e)}")
        return {"status":"error","message":"Error transfering money"}
      
    def account_transctions(self,account_number:int)->str:
      account=self.session.query(Accounts).filter_by(id=account_number).first()
      if not account:
        logger.error(f"Account not found with account number {account_number}")
        return {"status":"error","message":"Account not found"}
      
       
      return {
            'sent': self.session.query(Transactions).filter_by(sender_id=account.id).all(),
            'received': self.session.query(Transactions).filter_by(receiver_id=account.id).all()
        }
        
       
      
        

          
       
      
  
  
  
  