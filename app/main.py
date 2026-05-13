from models.account import BankAccount
from repositories.account_repository import AccountRepository

account1 = BankAccount(173200120040611,"Isuru","2000:10:23","isuru.sanjana23@gmail.com","0717424472","No23","20001023","Savings",1000,"Active")
#AccountRepository.save_account(account1)
AccountRepository.get_account(173200120040611)