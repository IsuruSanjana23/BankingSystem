import datetime
import random


class Customer:

    customer_data = {}

    def __init__(self,customer_id,name,dob,email,phone,address,nic):
        self.customer_id = customer_id
        self.name = name
        self.dob = dob
        self.email = email
        self.phone = phone
        self.address = address
        self.nic = nic
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        number = random.randint(100000,999999)
        Customer.customer_data[number] = {
            'customer_id': customer_id,
            'name': name,
            'dob': dob,
            'email': email,
            'phone': phone,
            'address': address,
            'nic': nic,
            'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }



#c1 = Customer(1,"Isuru","2000:10:23" , "isuru@gmail","071" , "No23" , "200010")
#c2 = Customer(1,"Isuru","2000:10:23" , "isuru@gmail","071" , "No23" , "200010")

#print(c1.customer_data)