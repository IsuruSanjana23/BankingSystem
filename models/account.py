
import datetime
import random


class BankAccount:

    BankAccount_Data = {}
    transaction_history = {}  # Store all transactions

    def __init__(self,account_number,customer_id,customer_obj,account_type,balance,status):
        self.account_number = account_number
        self.customer_id = customer_id
        self.customer_obj = customer_obj
        self.account_type = account_type
        self.balance = balance
        self.status = status
        self.last_access_at = datetime.datetime.now()

        # Add account data to the class variable
        BankAccount.BankAccount_Data[account_number] = {
            'customer_id': customer_id,
            'account_type': account_type,
            'balance': balance,
            'status': status,
            'last_access_at': self.last_access_at
        }

    def check_balance(self):
        return self.balance
    
    def record_transaction(self, transaction_type, amount, target_account=None):
        """Record a transaction in the transaction history"""
        transaction_id = random.randint(100000, 999999)
        
        BankAccount.transaction_history[transaction_id] = {
            'transaction_id': transaction_id,
            'transaction_type': transaction_type,
            'amount': amount,
            'from_account': self.account_number,
            'to_account': target_account if target_account else self.account_number,
            'customer_id': self.customer_id,
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'balance_after': self.balance
        }
        return transaction_id
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            # Update the dictionary
            BankAccount.BankAccount_Data[self.account_number]['balance'] = self.balance
            # Record transaction
            self.record_transaction('DEPOSIT', amount)
            return self.balance
        else:
            return "Invalid amount. Deposit must be greater than zero."
    
    def withdraw(self, amount):
        if amount < 0:
            return "Invalid amount. Withdraw must be greater than zero."
        elif amount > self.balance:
            return "Insufficient funds. Withdraw amount exceeds current balance."
        else:
            self.balance -= amount
            # Update the dictionary
            BankAccount.BankAccount_Data[self.account_number]['balance'] = self.balance
            # Record transaction
            self.record_transaction('WITHDRAWAL', amount)
            return self.balance
    
    @classmethod
    def get_account(cls, account_number):
        """Retrieve an account from BankAccount_Data"""
        return cls.BankAccount_Data.get(account_number)
    
    def get_transaction_history(self):
        """Get all transactions for this account"""
        account_transactions = []
        for trans_id, trans_data in BankAccount.transaction_history.items():
            if trans_data['from_account'] == self.account_number or trans_data['to_account'] == self.account_number:
                account_transactions.append(trans_data)
        return account_transactions
    
    @classmethod
    def get_all_transactions(cls):
        """Get all transactions in the system"""
        return cls.transaction_history


#acc1 = BankAccount(1,1,Customer,"Savings",100.00,True)
#acc2 = BankAccount(2,2,"Savings",1500.00,True)
#acc3 = BankAccount(1003,3,"Savings",2500.00,True)
"""
print(acc1.check_balance())
print(acc1.deposit(100))
print(acc1.withdraw(100))
"""