# Example usage of the Banking System with Exception Handling

from models.customer import Customer
from models.account import BankAccount
from models.transaction import Transaction
from exceptions.banking_exceptions import BankingException

print("=" * 60)
print("BANKING SYSTEM - EXCEPTION HANDLING EXAMPLES")
print("=" * 60)

# Create customers
print("\n1. Creating Customers...")
try:
    customer1 = Customer(1, "John Doe", "1990-01-15", "john@gmail.com", "071234567", "123 Main St", "NIC001")
    customer2 = Customer(2, "Jane Smith", "1995-05-20", "jane@gmail.com", "072345678", "456 Oak Ave", "NIC002")
    print("✓ Customers created successfully")
except Exception as e:
    print(f"✗ Error creating customer: {e}")

# Create accounts
print("\n2. Creating Bank Accounts...")
try:
    account1 = BankAccount(1, 1, "John Doe", "1990-01-15", "john@gmail.com", "071234567", "123 Main St", "NIC001", "Savings", 1000, True)
    account2 = BankAccount(2, 2, "Jane Smith", "1995-05-20", "jane@gmail.com", "072345678", "456 Oak Ave", "NIC002", "Checking", 500, True)
    print("✓ Accounts created successfully")
    print(f"  - Account 1 balance: {account1.check_balance()}")
    print(f"  - Account 2 balance: {account2.check_balance()}")
except Exception as e:
    print(f"✗ Error creating account: {e}")

# Example 1: Valid Deposit
print("\n3. Valid Deposit Transaction...")
try:
    trans1 = Transaction(account1, 500, 'DEPOSIT')
    result = trans1.execute()
    print(f"✓ New balance: {result}")
except BankingException.InsufficientAmountError as e:
    e.display()
except Exception as e:
    print(f"✗ Error: {e}")

# Example 2: Invalid Deposit (negative amount)
print("\n4. Invalid Deposit (negative amount)...")
try:
    trans2 = Transaction(account1, -100, 'DEPOSIT')
    result = trans2.execute()
    if result is None:
        print("  Transaction failed")
except Exception as e:
    print(f"✗ Error: {e}")

# Example 3: Valid Withdrawal
print("\n5. Valid Withdrawal Transaction...")
try:
    trans3 = Transaction(account1, 200, 'WITHDRAWAL')
    result = trans3.execute()
    print(f"✓ New balance: {result}")
except Exception as e:
    print(f"✗ Error: {e}")

# Example 4: Invalid Withdrawal (insufficient balance)
print("\n6. Invalid Withdrawal (insufficient balance)...")
try:
    trans4 = Transaction(account2, 1000, 'WITHDRAWAL')
    result = trans4.execute()
    if result is None:
        print("  Transaction failed - insufficient balance")
except Exception as e:
    print(f"✗ Error: {e}")

# Example 5: Valid Transfer
print("\n7. Valid Transfer Transaction...")
try:
    trans5 = Transaction(account1, 300, 'TRANSFER')
    result = trans5.transfer(account2, 300)
    print(f"✓ {result}")
    print(f"  - Account 1 new balance: {account1.check_balance()}")
    print(f"  - Account 2 new balance: {account2.check_balance()}")
except Exception as e:
    print(f"✗ Error: {e}")

# Example 6: Invalid Transfer (self-transfer)
print("\n8. Invalid Transfer (self-transfer)...")
try:
    trans6 = Transaction(account1, 100, 'TRANSFER')
    result = trans6.transfer(account1, 100)
    if result is None:
        print("  Transfer failed - cannot transfer to same account")
except Exception as e:
    print(f"✗ Error: {e}")

# Example 7: View Transaction History
print("\n9. Transaction History for Account 1:")
print("-" * 60)
history = account1.get_transaction_history()
if history:
    for trans in history:
        print(f"  Type: {trans['transaction_type']}")
        print(f"  Amount: {trans['amount']}")
        print(f"  Balance After: {trans['balance_after']}")
        print(f"  Timestamp: {trans['timestamp']}")
        print("-" * 60)
else:
    print("  No transactions found")

print("\n" + "=" * 60)
print("EXAMPLES COMPLETED")
print("=" * 60)

