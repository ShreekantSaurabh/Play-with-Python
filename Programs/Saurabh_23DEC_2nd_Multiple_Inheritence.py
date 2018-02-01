class ContactSearch(list):    
    def search(self, name):
        matched_contact = list()
        for i in self:
            print(id(self))
            if name in i.name:
                matched_contact.append(i)
        
        for i in matched_contact:
            print(i.name)
            
class Contact_Manager:
    #contact_list =     #or we can write list()
    contact_list = ContactSearch()
    
    def __init__(self, name, email_id= ''):
        self.name = name
        self.email_id = email_id
        Contact_Manager.contact_list.append(self)
        
    def print_all(self):
        for i in Contact_Manager.contact_list:
            print(i.name)
            print(i.email_id)
    
    def send(self, message):
        print("Send email to :" + self.email_id)

        
#cm1 = Contact_Manager('abc', 'abc@gmail.com')
#cm2 = Contact_Manager('def', 'def@gmail.com')
#cm3 = Contact_Manager('ghi', 'ghi@gmail.com')
        
class AddressHolder:
    def __init__(self, street = '', city= '', state= '', code= ''):
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        
    
"""
class friend(Contact_Manager, AddressHolder):
    def __init__(self, name, email_id= '', phone_number = '', street = '', city= '', state= '', code= ''):
        Contact_Manager.__init__(self, name, email_id= '')
        self.phone_number = phone_number
        AddressHolder.__init__(self, street = '', city= '', state= '', code= '')
        
"""
class friend(Contact_Manager, AddressHolder):
    def __init__(self, phone_number = '', **kwargs):
        super().__init__(**kwargs)
        self.phone_number = phone_number

f1 = friend(name = "abc", email_id = 'abc@gmail.com', phone_number = '987654321', street = "1st street", city = 'Bangalore', state = 'Karnataka', code = '560034')


    