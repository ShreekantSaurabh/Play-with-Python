class Contact_Manager:
    contact_list = []    #or we can write list()
    def __init__(self, email_id= '', phone_number= ''):
        self.email_id = email_id
        self.phone_number = phone_number
        Contact_Manager.contact_list.append(self)
        
    def print_all(self):
        for i in Contact_Manager.contact_list:
            print(i.email_id)
            print(i.phone_number)
        
#cm1 = Contact_Manager('abc@gmail.com', '9876543210')
#cm2 = Contact_Manager('def@gmail.com', '1234567890')
#cm3 = Contact_Manager('ghi@gmail.com', '2345678901')

cm1.print_all()
#print (Contact_Manager.contact_list[0].email_id)
#print (Contact_Manager.contact_list[1].phone_number)
"""def print_all(self):
    for i in Contact_Manager.contact_list:
        print(i.email_id)
        print(i.phone_number)"""

class Suppliers(Contact_Manager):
    def order(self):
        print ("Supplier")

sup1 = Suppliers('sup1@gmail.com', '001')
sup1.print_all()



    
