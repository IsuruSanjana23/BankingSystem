# AccountRepository Usage Examples

from models.account import BankAccount
from repositories.account_repository import AccountRepository

print("=" * 70)
print("ACCOUNT REPOSITORY - USAGE EXAMPLES")
print("=" * 70)

# ========== CREATE ACCOUNTS ==========
print("\n1. CREATING ACCOUNTS...")
print("-" * 70)

account1 = BankAccount(
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

account2 = BankAccount(
    account_number=2,
    customer_id=1,
    name="John Doe",
    dob="1990-01-15",
    email="john@gmail.com",
    phone="071234567",
    address="123 Main Street",
    nic="NIC001",
    account_type="Checking",
    balance=500.00,
    status=True
)

account3 = BankAccount(
    account_number=3,
    customer_id=2,
    name="Jane Smith",
    dob="1995-05-20",
    email="jane@gmail.com",
    phone="072345678",
    address="456 Oak Avenue",
    nic="NIC002",
    account_type="Savings",
    balance=750.00,
    status=True
)

# ========== SAVE ACCOUNTS ==========
print("\n2. SAVING ACCOUNTS...")
print("-" * 70)

AccountRepository.save_account(account1)  # ✓ Account 1 saved
AccountRepository.save_account(account2)  # ✓ Account 2 saved
AccountRepository.save_account(account3)  # ✓ Account 3 saved

# ========== GET SINGLE ACCOUNT ==========
print("\n3. RETRIEVING SINGLE ACCOUNT...")
print("-" * 70)

account = AccountRepository.get_account(1)     # ✓ Account 1 retrieved
if account:
    print(f"  Type: {account['account_type']}")
    print(f"  Balance: {account['balance']}")

not_found = AccountRepository.get_account(999)  # ✗ Account 999 not found

# ========== GET ALL ACCOUNTS ==========
print("\n4. RETRIEVING ALL ACCOUNTS...")
print("-" * 70)

all_accounts = AccountRepository.get_all_accounts()
print(f"  Total accounts: {len(all_accounts)}")
for acc_num, acc_data in all_accounts.items():
    print(f"  - Account {acc_num}: {acc_data['account_type']} (Balance: {acc_data['balance']})")

# ========== GET ACCOUNTS BY CUSTOMER ==========
print("\n5. RETRIEVING ACCOUNTS BY CUSTOMER...")
print("-" * 70)

customer1_accounts = AccountRepository.get_accounts_by_customer(1)
print(f"  Customer 1 has {len(customer1_accounts)} accounts")

customer2_accounts = AccountRepository.get_accounts_by_customer(2)
print(f"  Customer 2 has {len(customer2_accounts)} accounts")

# ========== CHECK IF ACCOUNT EXISTS ==========
print("\n6. CHECKING ACCOUNT EXISTENCE...")
print("-" * 70)

exists_1 = AccountRepository.account_exists(1)    # True
exists_999 = AccountRepository.account_exists(999)  # False

print(f"  Account 1 exists: {exists_1}")
print(f"  Account 999 exists: {exists_999}")

# ========== GET ACCOUNT COUNT ==========
print("\n7. GETTING ACCOUNT COUNT...")
print("-" * 70)

count = AccountRepository.get_account_count()
print(f"  Total accounts in system: {count}")

# ========== GET ACTIVE ACCOUNTS ==========
print("\n8. RETRIEVING ACTIVE ACCOUNTS...")
print("-" * 70)

active = AccountRepository.get_active_accounts()
print(f"  Active accounts: {len(active)}")
for acc_num, acc_data in active.items():
    print(f"  - Account {acc_num}: Status = {acc_data['status']}")

# ========== UPDATE ACCOUNT ==========
print("\n9. UPDATING ACCOUNT...")
print("-" * 70)

updated = AccountRepository.update_account(1, {'balance': 1500.00})  # ✓ Updated
print(f"  Update successful: {updated}")

updated_account = AccountRepository.get_account(1)
print(f"  New balance: {updated_account['balance']}")

# ========== DELETE ACCOUNT (Soft Delete) ==========
print("\n10. DEACTIVATING ACCOUNT...")
print("-" * 70)

deleted = AccountRepository.delete_account(1)  # ✓ Deactivated
print(f"  Deactivation successful: {deleted}")

updated_account = AccountRepository.get_account(1)
print(f"  Account status: {updated_account['status']}")

# ========== FINAL STATE ==========
print("\n11. FINAL STATE...")
print("-" * 70)

print(f"  Total accounts: {AccountRepository.get_account_count()}")
print(f"  Active accounts: {len(AccountRepository.get_active_accounts())}")

print("\n" + "=" * 70)
print("EXAMPLES COMPLETED")
print("=" * 70)

