from models.account import BankAccount
from models.transaction import Transaction
from exceptions.banking_exceptions import BankingException

class BankingService:
    """Service layer for banking operations"""
    
    @staticmethod
    def create_account(account_number, customer_id, name, dob, email, phone, address, nic, account_type, balance, status):
        """
        Create a new bank account
        
        Parameters:
        - account_number: Unique account number
        - customer_id: Customer ID
        - name: Customer name
        - dob: Date of birth
        - email: Email address
        - phone: Phone number
        - address: Address
        - nic: National ID number
        - account_type: Type of account (Savings, Checking, etc.)
        - balance: Initial balance
        - status: Account status (True/False)
        
        Returns:
        - BankAccount object if successful, None if failed
        """
        try:
            account = BankAccount(
                account_number=account_number,
                customer_id=customer_id,
                name=name,
                dob=dob,
                email=email,
                phone=phone,
                address=address,
                nic=nic,
                account_type=account_type,
                balance=balance,
                status=status
            )
            print(f"✓ Account {account_number} created successfully for {name}")
            return account
        except Exception as e:
            print(f"✗ Error creating account: {e}")
            return None
    
    @staticmethod
    def deposit(account: BankAccount, amount: float):
        """
        Deposit funds into an account
        
        Parameters:
        - account: BankAccount object
        - amount: Amount to deposit
        
        Returns:
        - New balance if successful, None if failed
        """
        try:
            result = account.deposit(amount)
            if result:
                print(f"✓ Deposit successful. New balance: {result}")
            return result
        except BankingException.InsufficientAmountError as e:
            e.display()
            return None
        except Exception as e:
            print(f"✗ Error during deposit: {e}")
            return None
    
    @staticmethod
    def withdraw(account: BankAccount, amount: float):
        """
        Withdraw funds from an account
        
        Parameters:
        - account: BankAccount object
        - amount: Amount to withdraw
        
        Returns:
        - New balance if successful, None if failed
        """
        try:
            result = account.withdraw(amount)
            if result:
                print(f"✓ Withdrawal successful. New balance: {result}")
            return result
        except BankingException.InsufficientAmountError as e:
            e.display()
            return None
        except BankingException.InsufficientBalanceError as e:
            e.display()
            return None
        except Exception as e:
            print(f"✗ Error during withdrawal: {e}")
            return None
    
    @staticmethod
    def find_account(account_number):
        """
        Find an account by account number
        
        Parameters:
        - account_number: Account number to search for
        
        Returns:
        - Account data dictionary if found, None if not found
        """
        try:
            account = BankAccount.get_account(account_number)
            if account:
                print(f"✓ Account {account_number} found")
                return account
            else:
                raise BankingException.AccountNotFoundError(
                    f"Account {account_number} not found"
                )
        except BankingException.AccountNotFoundError as e:
            e.display()
            return None
        except Exception as e:
            print(f"✗ Error finding account: {e}")
            return None
    
    @staticmethod
    def transfer_funds(from_account: BankAccount, to_account: BankAccount, amount: float):
        """
        Transfer funds between two accounts
        
        Parameters:
        - from_account: Source BankAccount object
        - to_account: Target BankAccount object
        - amount: Amount to transfer
        
        Returns:
        - Success message if successful, None if failed
        """
        try:
            trans = Transaction(from_account, amount, 'TRANSFER')
            result = trans.transfer(to_account, amount)
            if result:
                print(f"✓ {result}")
            return result
        except Exception as e:
            print(f"✗ Error during transfer: {e}")
            return None
    
    @staticmethod
    def check_balance(account: BankAccount):
        """
        Check account balance
        
        Parameters:
        - account: BankAccount object
        
        Returns:
        - Current balance
        """
        try:
            balance = account.check_balance()
            print(f"💰 Current balance: {balance}")
            return balance
        except Exception as e:
            print(f"✗ Error checking balance: {e}")
            return None
    
    @staticmethod
    def get_transaction_history(account: BankAccount):
        """
        Get transaction history for an account
        
        Parameters:
        - account: BankAccount object
        
        Returns:
        - List of transactions
        """
        try:
            history = account.get_transaction_history()
            print(f"✓ Found {len(history)} transactions")
            return history
        except Exception as e:
            print(f"✗ Error retrieving transaction history: {e}")
            return None
    
    @staticmethod
    def get_all_accounts():
        """
        Get all bank accounts in the system
        
        Returns:
        - Dictionary of all accounts
        """
        return BankAccount.BankAccount_Data
    
    @staticmethod
    def get_all_transactions():
        """
        Get all transactions in the system
        
        Returns:
        - Dictionary of all transactions
        """
        return BankAccount.transaction_history
    
