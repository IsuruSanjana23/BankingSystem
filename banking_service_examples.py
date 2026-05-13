# Usage Examples for BankingService

from models.customer import Customer
from models.account import BankAccount
from services.banking_service import BankingService

print("=" * 70)
print("BANKING SERVICE - COMPLETE EXAMPLE")
print("=" * 70)

# ========== CREATE ACCOUNTS ==========
print("\n1. CREATING ACCOUNTS...")
print("-" * 70)

account1 = BankingService.create_account(
    account_number=1,
    customer_id=1,
    name="John Doe",
    dob="1990-01-15",
    email="john@gmail.com",
    phone="071234567",
    address="123 Main Street",
    nic="NIC001",
    account_type="Savings",
    balance=1000.00,
    status=True
)

account2 = BankingService.create_account(
    account_number=2,
    customer_id=2,
    name="Jane Smith",
    dob="1995-05-20",
    email="jane@gmail.com",
    phone="072345678",
    address="456 Oak Avenue",
    nic="NIC002",
    account_type="Checking",
    balance=500.00,
    status=True
)

# ========== CHECK BALANCE ==========
print("\n2. CHECKING BALANCES...")
print("-" * 70)

BankingService.check_balance(account1)  # 💰 Current balance: 1000.0
BankingService.check_balance(account2)  # 💰 Current balance: 500.0

# ========== DEPOSIT FUNDS ==========
print("\n3. MAKING DEPOSITS...")
print("-" * 70)

BankingService.deposit(account1, 500)   # ✓ Deposit successful. New balance: 1500.0
BankingService.deposit(account2, 250)   # ✓ Deposit successful. New balance: 750.0

# ========== INVALID DEPOSIT (negative amount) ==========
print("\n4. INVALID DEPOSIT (negative amount)...")
print("-" * 70)

BankingService.deposit(account1, -100)  # ❌ Error: Deposit amount must be greater than zero

# ========== WITHDRAW FUNDS ==========
print("\n5. WITHDRAWING FUNDS...")
print("-" * 70)

BankingService.withdraw(account1, 300)  # ✓ Withdrawal successful. New balance: 1200.0
BankingService.withdraw(account2, 200)  # ✓ Withdrawal successful. New balance: 550.0

# ========== INVALID WITHDRAWAL (insufficient balance) ==========
print("\n6. INVALID WITHDRAWAL (insufficient balance)...")
print("-" * 70)

BankingService.withdraw(account2, 1000)  # ❌ Error: Insufficient balance...

# ========== TRANSFER FUNDS ==========
print("\n7. TRANSFERRING FUNDS...")
print("-" * 70)

BankingService.transfer_funds(account1, account2, 300)  # ✓ Transferred...

# ========== CHECK BALANCES AFTER TRANSFER ==========
print("\n8. CHECKING BALANCES AFTER TRANSFER...")
print("-" * 70)

BankingService.check_balance(account1)  # 💰 Current balance: 900.0
BankingService.check_balance(account2)  # 💰 Current balance: 850.0

# ========== FIND ACCOUNT ==========
print("\n9. FINDING ACCOUNTS...")
print("-" * 70)

found_account = BankingService.find_account(1)    # ✓ Account 1 found
not_found = BankingService.find_account(999)      # ✗ Account 999 not found

# ========== GET TRANSACTION HISTORY ==========
print("\n10. GETTING TRANSACTION HISTORY...")
print("-" * 70)

history = BankingService.get_transaction_history(account1)
if history:
    print(f"\nTransaction details for Account 1:")
    for trans in history:
        print(f"  - Type: {trans['transaction_type']}")
        print(f"    Amount: {trans['amount']}")
        print(f"    Balance After: {trans['balance_after']}")
        print(f"    Time: {trans['timestamp']}")
        print()

# ========== GET ALL ACCOUNTS ==========
print("\n11. ALL ACCOUNTS IN SYSTEM...")
print("-" * 70)

all_accounts = BankingService.get_all_accounts()
print(f"Total accounts: {len(all_accounts)}")
for acc_num, acc_data in all_accounts.items():
    print(f"  Account {acc_num}: Balance = {acc_data['balance']}, Type = {acc_data['account_type']}")

# ========== GET ALL TRANSACTIONS ==========
print("\n12. ALL TRANSACTIONS IN SYSTEM...")
print("-" * 70)

all_trans = BankingService.get_all_transactions()
print(f"Total transactions: {len(all_trans)}")
for trans_id, trans_data in list(all_trans.items())[:5]:  # Show first 5
    print(f"  Transaction {trans_id}: {trans_data['transaction_type']} - Amount: {trans_data['amount']}")

print("\n" + "=" * 70)
print("EXAMPLE COMPLETED")
print("=" * 70)

