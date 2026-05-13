import datetime
import random
from models.account import BankAccount
from exceptions.banking_exceptions import BankingException

class Transaction:
    """Execute transactions on BankAccount objects"""

    def __init__(self, account: BankAccount, amount: float, transaction_type: str):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type.upper()  # Normalize to uppercase
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def execute(self):
        """Execute the transaction"""
        if self.transaction_type == 'DEPOSIT':
            return self.account.deposit(self.amount)
        elif self.transaction_type == 'WITHDRAWAL':
            return self.account.withdraw(self.amount)
        else:
            return f"Unknown transaction type: {self.transaction_type}"
    
    def transfer(self, target_account: BankAccount, amount: float):
        """Transfer funds to another account"""
        try:
            if amount <= 0:
                raise BankingException.InsufficientAmountError("Transfer amount must be greater than zero")
            
            if not target_account:
                raise BankingException.AccountNotFoundError("Target account not found")
            
            if not target_account.status:
                raise BankingException.AccountInactiveError("Target account is inactive")
            
            if self.account.account_number == target_account.account_number:
                raise BankingException.InvalidTransactionError("Cannot transfer to the same account")
            
            # Withdraw from source
            self.account.withdraw(amount)
            
            # Deposit to target
            target_account.deposit(amount)
            
            return f"✓ Transferred {amount} from account {self.account.account_number} to account {target_account.account_number}"
        
        except BankingException.InsufficientAmountError as e:
            e.display()
            return None
        except BankingException.AccountNotFoundError as e:
            e.display()
            return None
        except BankingException.AccountInactiveError as e:
            e.display()
            return None
        except BankingException.InvalidTransactionError as e:
            e.display()
            return None
