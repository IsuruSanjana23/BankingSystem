from models.account import BankAccount
from exceptions.banking_exceptions import BankingException


class AccountRepository:
    """Repository for managing BankAccount data access"""
    
    @staticmethod
    def save_account(account: BankAccount):
        """
        Save an account to the repository
        
        Parameters:
        - account: BankAccount object to save
        
        Returns:
        - True if successful, False otherwise
        """
        try:
            if not account:
                raise ValueError("Invalid account object")
            
            # Account is automatically saved to BankAccount_Data in __init__
            # This method ensures it's properly stored
            BankAccount.BankAccount_Data[account.account_number] = {
                'customer_id': account.customer_id,
                'account_type': account.account_type,
                'balance': account.balance,
                'status': account.status,
                'last_access_at': account.last_access_at
            }
            print(f"✓ Account {account.account_number} saved successfully")
            return True
        
        except Exception as e:
            print(f"✗ Error saving account: {e}")
            return False
    
    @staticmethod
    def get_account(account_number: int):
        """
        Retrieve a single account by account number
        
        Parameters:
        - account_number: Account number to retrieve
        
        Returns:
        - Account data dictionary if found, None otherwise
        """
        try:
            if not account_number:
                raise BankingException.AccountNotFoundError("Account number is required")
            
            # BankAccount_Data is a dictionary where keys are account numbers
            account_data = BankAccount.BankAccount_Data.get(account_number)
            
            if not account_data:
                raise BankingException.AccountNotFoundError(
                    f"Account {account_number} not found"
                )
            
            print(f"✓ Account {account_number} retrieved successfully")
            return account_data
        
        except BankingException.AccountNotFoundError as e:
            e.display()
            return None
        except Exception as e:
            print(f"✗ Error retrieving account: {e}")
            return None
    
    @staticmethod
    def get_all_accounts():
        """
        Retrieve all accounts from the repository
        
        Returns:
        - Dictionary of all accounts
        """
        try:
            accounts = BankAccount.BankAccount_Data
            
            if not accounts:
                print("ℹ No accounts found in repository")
                return {}
            
            print(f"✓ Retrieved {len(accounts)} accounts")
            return accounts
        
        except Exception as e:
            print(f"✗ Error retrieving accounts: {e}")
            return {}
    
    @staticmethod
    def get_accounts_by_customer(customer_id: int):
        """
        Get all accounts for a specific customer
        
        Parameters:
        - customer_id: Customer ID to search for
        
        Returns:
        - Dictionary of accounts belonging to the customer
        """
        try:
            if not customer_id:
                raise ValueError("Customer ID is required")
            
            customer_accounts = {}
            
            for account_num, account_data in BankAccount.BankAccount_Data.items():
                if account_data['customer_id'] == customer_id:
                    customer_accounts[account_num] = account_data
            
            if not customer_accounts:
                print(f"ℹ No accounts found for customer {customer_id}")
                return {}
            
            print(f"✓ Found {len(customer_accounts)} accounts for customer {customer_id}")
            return customer_accounts
        
        except Exception as e:
            print(f"✗ Error retrieving customer accounts: {e}")
            return {}
    
    @staticmethod
    def update_account(account_number: int, account_data: dict):
        """
        Update account information
        
        Parameters:
        - account_number: Account number to update
        - account_data: Dictionary with updated data
        
        Returns:
        - True if successful, False otherwise
        """
        try:
            if not account_number or not account_data:
                raise ValueError("Account number and data are required")
            
            if account_number not in BankAccount.BankAccount_Data:
                raise BankingException.AccountNotFoundError(
                    f"Account {account_number} not found"
                )
            
            # Update the account data
            for key, value in account_data.items():
                if key in BankAccount.BankAccount_Data[account_number]:
                    BankAccount.BankAccount_Data[account_number][key] = value
            
            print(f"✓ Account {account_number} updated successfully")
            return True
        
        except BankingException.AccountNotFoundError as e:
            e.display()
            return False
        except Exception as e:
            print(f"✗ Error updating account: {e}")
            return False
    
    @staticmethod
    def delete_account(account_number: int):
        """
        Delete an account (set status to inactive)
        
        Parameters:
        - account_number: Account number to delete
        
        Returns:
        - True if successful, False otherwise
        """
        try:
            if not account_number:
                raise ValueError("Account number is required")
            
            if account_number not in BankAccount.BankAccount_Data:
                raise BankingException.AccountNotFoundError(
                    f"Account {account_number} not found"
                )
            
            # Soft delete - set status to inactive
            BankAccount.BankAccount_Data[account_number]['status'] = False
            print(f"✓ Account {account_number} has been deactivated")
            return True
        
        except BankingException.AccountNotFoundError as e:
            e.display()
            return False
        except Exception as e:
            print(f"✗ Error deleting account: {e}")
            return False
    
    @staticmethod
    def account_exists(account_number: int):
        """
        Check if an account exists
        
        Parameters:
        - account_number: Account number to check
        
        Returns:
        - True if exists, False otherwise
        """
        return account_number in BankAccount.BankAccount_Data
    
    @staticmethod
    def get_account_count():
        """
        Get total number of accounts
        
        Returns:
        - Integer count of accounts
        """
        return len(BankAccount.BankAccount_Data)
    
    @staticmethod
    def get_active_accounts():
        """
        Get all active accounts
        
        Returns:
        - Dictionary of active accounts
        """
        try:
            active_accounts = {}
            
            for account_num, account_data in BankAccount.BankAccount_Data.items():
                if account_data['status'] == True:
                    active_accounts[account_num] = account_data
            
            print(f"✓ Found {len(active_accounts)} active accounts")
            return active_accounts
        
        except Exception as e:
            print(f"✗ Error retrieving active accounts: {e}")
            return {}
