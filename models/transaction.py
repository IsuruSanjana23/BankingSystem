import datetime
import random

from models.account import BankAccount

class Transaction(BankAccount):

    def __init__(self, account_number, customer_id, customer_obj, account_type, balance, status, transaction_type, amount):
        super().__init__(account_number, customer_id, customer_obj, account_type, balance, status)
        self.type = transaction_type
        self.amount = amount
        self.time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def transfer(self, target_account_number, amount):
        # Check if target account exists and is active
        target_data = BankAccount.BankAccount_Data.get(target_account_number)
        
        if target_data is None:
            return "Target account not found."
        
        if target_data['status'] == False:
            return "Target account is inactive."
        
        # Check if source account has sufficient funds
        if amount > self.balance:
            return "Insufficient funds. Transfer amount exceeds current balance."

        if self.account_number == target_account_number:
            return (f"Invalid transaction.\n"
                    f"You can't transfer to the same account.\n")
        
        # Withdraw from source account (will automatically record WITHDRAWAL transaction)
        self.withdraw(amount)
        
        # Deposit to target account
        target_data['balance'] += amount
        
        # Record transfer transaction with target account information
        transaction_id = self.record_transaction('TRANSFER', amount, target_account=target_account_number)
        
        return f"Transferred {amount} to account {target_account_number} from {self.account_number}.\nNew balance: {self.balance}\nTransaction ID: {transaction_id}"

t1 = Transaction(2, 1, None, "Savings", 500.00, True, "Deposit", 100)
t2 = Transaction(1003, 3, None, "Savings", 500.00, True, "Deposit", 100)
#print(t1.transfer(2, 100))
#print(t2.transfer(1, 100))

#print(t1.check_balance())


