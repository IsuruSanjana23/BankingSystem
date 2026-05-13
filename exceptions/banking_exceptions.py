class BankingException(Exception):
    """Base exception class for banking operations"""
    
    class InsufficientBalanceError(Exception):
        """Raised when an account has insufficient balance for a transaction."""
        def __init__(self, message="Insufficient balance for the transaction."):
            self.message = message
            super().__init__(self.message)
        
        def display(self):
            """Display the error message"""
            print(f"❌ Error: {self.message}")
            return self.message

    class InsufficientAmountError(Exception):
        """Raised when deposit/withdrawal amount is invalid."""
        def __init__(self, message="Invalid amount for transaction."):
            self.message = message
            super().__init__(self.message)

        def display(self):
            """Display the error message"""
            print(f"❌ Error: {self.message}")
            return self.message
    
    class AccountNotFoundError(Exception):
        """Raised when an account cannot be found."""
        def __init__(self, message="Account not found."):
            self.message = message
            super().__init__(self.message)
            
        def display(self):
            """Display the error message"""
            print(f"❌ Error: {self.message}")
            return self.message
    
    class AccountInactiveError(Exception):
        """Raised when trying to use an inactive account."""
        def __init__(self, message="Account is inactive."):
            self.message = message
            super().__init__(self.message)
            
        def display(self):
            """Display the error message"""
            print(f"❌ Error: {self.message}")
            return self.message
    
    class InvalidTransactionError(Exception):
        """Raised for invalid transactions."""
        def __init__(self, message="Invalid transaction."):
            self.message = message
            super().__init__(self.message)
            
        def display(self):
            """Display the error message"""
            print(f"❌ Error: {self.message}")
            return self.message
