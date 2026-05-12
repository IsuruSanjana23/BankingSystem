from models.customer import Customer

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def create_user(customer_id, name, dob, email, phone, address, nic):
        """Create a new customer and return the customer object"""
        new_user = Customer(customer_id, name, dob, email, phone, address, nic)
        print(f"✓ {name} USER CREATED")
        print(f"  Customer ID: {customer_id}")
        print(f"  Email: {email}")
        print(f"  Phone: {phone}\n")
        return new_user
    
    @staticmethod
    def view_all_customers():
        """Display all customers in the system"""
        if not Customer.customer_data:
            print("No customers found.")
            return
        
        print("=== ALL CUSTOMERS ===")
        for key, customer in Customer.customer_data.items():
            print(f"ID: {key}")
            print(f"  Customer ID: {customer['customer_id']}")
            print(f"  Name: {customer['name']}")
            print(f"  Email: {customer['email']}")
            print(f"  Phone: {customer['phone']}")
            print(f"  Address: {customer['address']}")
            print(f"  NIC: {customer['nic']}")
            print(f"  Created: {customer['created_at']}\n")
    
    @staticmethod
    def get_customer(customer_id):
        """Search for a customer by customer_id"""
        for key, customer in Customer.customer_data.items():
            if customer['customer_id'] == customer_id:
                return customer
        return None


# Example Usage
admin = Admin("Isuru", "Isuru")

# Create users
user1 = admin.create_user(12, "Sanjana", "2000:10:23", "sanjana@gmail.com", "071", "No23", "200010")
user2 = admin.create_user(13, "John", "1995:05:15", "john@gmail.com", "072", "No45", "199505")

# View all customers
admin.view_all_customers()

# Get specific customer
customer = admin.get_customer(12)
if customer:
    print(f"Found: {customer['name']} - {customer['email']}")

