from models.customer import Customer
from models.account import BankAccount
from models.transaction import Transaction

# Create a customer
customer = Customer(1, "Isuru", "2000:10:23", "isuru@gmail", "071", "No23", "200010")

# Create an account
account = BankAccount(1, 1, "Isuru", "2000:10:23", "isuru@gmail", "071", "No23", "200010", "Savings", 1000, True)

# Create and execute a deposit transaction
trans = Transaction(account, 500, 'DEPOSIT')
result = trans.execute()
print(f"Deposit result: {result}")

# View account transactions
print("\n=== Account Transactions ===")
print(account.transactions)

# View all customers
print("\n=== All Customers ===")
print(Customer.customer_data)

# View all system transactions
print("\n=== All System Transactions ===")
print(BankAccount.transaction_history)
