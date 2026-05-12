# Bank System Project

A comprehensive Python-based banking system that manages customers, accounts, transactions, and transfers with full transaction tracking and audit trails.

---

## 📁 Project Structure

```
BankSystem/
├── main.py                    # Main entry point
├── models/
│   ├── __init__.py           # Package initializer
│   ├── customer.py           # Customer model
│   ├── account.py            # Bank account model
│   └── transaction.py        # Transaction model
├── services/
│   └── admin.py              # Admin service for user management
├── repositories/             # Data access layer (placeholder)
├── exceptions/               # Custom exceptions (placeholder)
├── utils/                    # Utility functions (placeholder)
├── data/                     # Data storage (placeholder)
└── README.md                 # Project documentation
```

---

## 🎯 Core Components

### 1. Customer Model (`models/customer.py`)

Manages customer profiles and personal information.

**Features:**
- Create customer records with complete details
- Auto-generate unique customer record IDs
- Store customers in `customer_data` dictionary
- Track creation timestamps
- Persistent storage of customer information

**Usage:**
```python
from models.customer import Customer

# Create a new customer
customer = Customer(
    customer_id=1,
    name="John Doe",
    dob="1990-01-15",
    email="john@gmail.com",
    phone="071234567",
    address="123 Main Street",
    nic="199001"
)

# View all customers
print(Customer.customer_data)
```

**Data Structure:**
```python
{
    135548: {
        'customer_id': 1,
        'name': 'John Doe',
        'dob': '1990-01-15',
        'email': 'john@gmail.com',
        'phone': '071234567',
        'address': '123 Main Street',
        'nic': '199001',
        'created_at': '2026-05-12 14:49:27'
    }
}
```

---

### 2. Bank Account Model (`models/account.py`)

Handles account creation, management, and transactions.

**Features:**
- Create multiple account types (Savings, Checking, etc.)
- Link accounts to customers
- Balance management with validation
- Automatic transaction recording
- Transaction history tracking
- Account data persistence

**Methods:**

| Method | Description |
|--------|-------------|
| `check_balance()` | Returns current account balance |
| `deposit(amount)` | Add funds to account (auto-records) |
| `withdraw(amount)` | Withdraw funds with validation (auto-records) |
| `record_transaction()` | Manually record a transaction |
| `get_transaction_history()` | Get all transactions for this account |
| `get_all_transactions()` | Get all system transactions (class method) |

**Usage:**
```python
from models.customer import Customer
from models.account import BankAccount

# Create customer
customer = Customer(1, "Jane Doe", "1995-05-20", "jane@gmail.com", "072", "456 Oak Ave", "199505")

# Create account
account = BankAccount(
    account_number=1,
    customer_id=1,
    customer_obj=customer,
    account_type="Savings",
    balance=1000.00,
    status=True
)

# Perform operations
print(account.check_balance())          # Output: 1000.0
print(account.deposit(500))              # Output: 1500.0 (auto-recorded)
print(account.withdraw(200))             # Output: 1300.0 (auto-recorded)

# View transaction history
print(account.get_transaction_history())
```

**Data Structure:**
```python
BankAccount.BankAccount_Data = {
    1: {
        'customer_id': 1,
        'account_type': 'Savings',
        'balance': 1300.0,
        'status': True,
        'last_access_at': datetime_object
    }
}

BankAccount.transaction_history = {
    567890: {
        'transaction_id': 567890,
        'transaction_type': 'DEPOSIT',
        'amount': 500.0,
        'from_account': 1,
        'to_account': 1,
        'customer_id': 1,
        'timestamp': '2026-05-12 14:49:27',
        'balance_after': 1500.0
    }
}
```

---

### 3. Transaction Model (`models/transaction.py`)

Extends BankAccount to handle transfers and complex transactions.

**Features:**
- Inherit all account functionality
- Transfer funds between accounts
- Validate transfer operations
- Prevent self-transfers
- Auto-record all transfer transactions
- Generate unique transaction IDs

**Methods:**

| Method | Description |
|--------|-------------|
| `transfer(target_account, amount)` | Transfer funds to another account |

**Usage:**
```python
from models.transaction import Transaction

# Create transaction account
t1 = Transaction(
    account_number=3,
    customer_id=3,
    customer_obj=None,
    account_type="Checking",
    balance=2000.00,
    status=True,
    transaction_type="Transfer",
    amount=0
)

# Create target account
t2 = Transaction(4, 4, None, "Savings", 500.00, True, "Transfer", 0)

# Transfer funds
result = t1.transfer(target_account_number=4, amount=300)
print(result)
# Output:
# Transferred 300 to account 4 from account 3.
# New balance: 1700.0
# Transaction ID: 847392
```

**Transaction Recording:**
- ✅ DEPOSIT - When funds are added to an account
- ✅ WITHDRAWAL - When funds are withdrawn from an account
- ✅ TRANSFER - When funds move between accounts

---

### 4. Admin Service (`services/admin.py`)

Administrative interface for customer management.

**Features:**
- Create new customers
- View all customers
- Search for specific customers
- User authentication (username/password)

**Methods:**

| Method | Description |
|--------|-------------|
| `create_user()` | Create new customer profile |
| `view_all_customers()` | Display all customers with details |
| `get_customer()` | Search customer by ID |

**Usage:**
```python
from services.admin import Admin

# Create admin
admin = Admin(username="Isuru", password="Isuru")

# Create customers
user1 = admin.create_user(
    customer_id=12,
    name="Sanjana",
    dob="2000:10:23",
    email="sanjana@gmail.com",
    phone="071",
    address="No23",
    nic="200010"
)

# View all customers
admin.view_all_customers()

# Search for specific customer
customer = admin.get_customer(customer_id=12)
if customer:
    print(f"Found: {customer['name']} - {customer['email']}")
```

---

## 📊 Transaction Types

### 1. Deposit Transaction
```python
account.deposit(500)
# Records:
# - Type: DEPOSIT
# - Amount: 500
# - Balance After: 1500.0
# - Timestamp: 2026-05-12 14:49:27
```

### 2. Withdrawal Transaction
```python
account.withdraw(100)
# Records:
# - Type: WITHDRAWAL
# - Amount: 100
# - Balance After: 1400.0
# - Timestamp: 2026-05-12 14:49:27
```

### 3. Transfer Transaction
```python
account.transfer(target_account_number=2, amount=200)
# Records:
# - Type: TRANSFER
# - Amount: 200
# - From Account: 1
# - To Account: 2
# - Balance After: 1200.0
# - Timestamp: 2026-05-12 14:49:27
# - Transaction ID: 567890
```

---

## 🔄 Complete Workflow Example

```python
from models.customer import Customer
from models.account import BankAccount
from models.transaction import Transaction
from services.admin import Admin

# Step 1: Create Admin
admin = Admin("Isuru", "Isuru")

# Step 2: Create Customers
c1 = admin.create_user(1, "John", "1990-01-01", "john@gmail.com", "071", "123 St", "NIC123")
c2 = admin.create_user(2, "Jane", "1995-05-15", "jane@gmail.com", "072", "456 St", "NIC456")

# Step 3: Create Accounts
acc1 = BankAccount(1, 1, c1, "Savings", 1000.00, True)
acc2 = BankAccount(2, 2, c2, "Checking", 500.00, True)

# Step 4: Perform Transactions
print(acc1.deposit(500))              # ✓ DEPOSIT recorded: 1500.0
print(acc1.withdraw(100))             # ✓ WITHDRAWAL recorded: 1400.0

# Step 5: Transfer Money
t1 = Transaction(1, 1, c1, "Savings", 1400.00, True, "Transfer", 0)
result = t1.transfer(2, 200)          # ✓ WITHDRAWAL + TRANSFER recorded
print(result)

# Step 6: View History
print(acc1.get_transaction_history())  # All transactions for acc1
print(BankAccount.get_all_transactions())  # All system transactions

# Step 7: View All Customers
admin.view_all_customers()
```

---

## ✨ Key Features

| Feature | Status | Description |
|---------|--------|-------------|
| Customer Management | ✅ | Create and manage customer profiles |
| Account Creation | ✅ | Create multiple account types |
| Balance Management | ✅ | Check, deposit, withdraw with validation |
| Fund Transfers | ✅ | Transfer between accounts with validation |
| Transaction Recording | ✅ | Auto-record all operations |
| Transaction History | ✅ | View per-account and system-wide history |
| Customer-Account Link | ✅ | Accounts linked to customer objects |
| Admin Interface | ✅ | User management via admin service |
| Data Validation | ✅ | Validate amounts and account status |
| Error Handling | ✅ | Comprehensive error messages |

---

## 🔒 Validation & Error Handling

**Deposit Validation:**
- ❌ Rejects negative or zero amounts
- ✅ Adds funds and records transaction

**Withdrawal Validation:**
- ❌ Rejects negative amounts
- ❌ Rejects if amount exceeds balance
- ✅ Deducts funds and records transaction

**Transfer Validation:**
- ❌ Rejects if target account doesn't exist
- ❌ Rejects if target account is inactive
- ❌ Rejects if insufficient funds
- ❌ Rejects self-transfers
- ✅ Transfers funds and records transactions

---

## 📋 Data Storage

All data is stored in class variables (dictionaries) that persist during runtime:

- `Customer.customer_data` - All customer records
- `BankAccount.BankAccount_Data` - All account records
- `BankAccount.transaction_history` - All transactions

**Note:** Currently uses in-memory storage. Can be extended to:
- File-based storage (JSON, CSV)
- Database (SQLite, MySQL, PostgreSQL)
- Cloud storage (AWS, Firebase)

---

## 🚀 Getting Started

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd BankSystem
```

2. No external dependencies required (uses only Python standard library)

### Running the Project

```bash
# Run main application
python main.py

# Run admin service
python services/admin.py

# Run individual models
python models/customer.py
python models/account.py
python models/transaction.py
```

---

## 📝 File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Main application entry point |
| `models/customer.py` | Customer model and class |
| `models/account.py` | Bank account model and class |
| `models/transaction.py` | Transaction model extending BankAccount |
| `services/admin.py` | Admin service for user management |
| `models/__init__.py` | Package initializer |

---

## 🔮 Future Enhancements

- [ ] Database persistence (SQLite/MySQL)
- [ ] User authentication system
- [ ] Account statements and reports
- [ ] Interest calculation for savings accounts
- [ ] Overdraft protection
- [ ] Multi-currency support
- [ ] Loan management system
- [ ] Investment accounts
- [ ] Bill payment integration
- [ ] Mobile app interface
- [ ] API endpoints (REST/GraphQL)
- [ ] Analytics dashboard

---

## 📞 Support

For issues or questions about the project, please contact the development team.

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Development Status

**Current Version:** 1.0  
**Status:** ✅ Complete and Functional  
**Last Updated:** May 12, 2026

---

## 📚 Documentation

### How to Create a Customer
```python
customer = Customer(1, "John", "1990-01-01", "john@gmail.com", "071", "123 St", "NIC123")
```

### How to Create an Account
```python
account = BankAccount(1, 1, customer, "Savings", 1000.00, True)
```

### How to Perform Transactions
```python
account.deposit(500)      # Add funds
account.withdraw(100)     # Remove funds
```

### How to Transfer Money
```python
transaction = Transaction(1, 1, customer, "Savings", 1000.00, True, "Transfer", 0)
transaction.transfer(2, 200)  # Transfer to account 2
```

### How to View History
```python
account.get_transaction_history()    # Account transactions
BankAccount.get_all_transactions()   # All system transactions
```

---

**Happy Banking! 🏦**

