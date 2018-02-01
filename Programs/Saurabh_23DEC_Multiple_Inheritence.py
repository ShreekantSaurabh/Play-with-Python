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
    
    def __init__(self, name, email_id= '', phone_number= ''):
        self.name = name
        self.email_id = email_id
        self.phone_number = phone_number
        Contact_Manager.contact_list.append(self)
        
    def print_all(self):
        for i in Contact_Manager.contact_list:
            print(i.name)
            print(i.email_id)
            print(i.phone_number)
    
    def send(self, message):
        print("Send email to :" + self.email_id)

        
#cm1 = Contact_Manager('abc', 'abc@gmail.com', '9876543210')
#cm2 = Contact_Manager('def', 'def@gmail.com', '1234567890')
#cm3 = Contact_Manager('ghi', 'ghi@gmail.com', '2345678901')

#Contact_Manager.contact_list.search('a')
#print(id(cm1))

class Suppliers(Contact_Manager):
    def order(self):
        print ("Supplier")
    
    #Function Overriding ie. child class will get preference.
    #print_all() is present at both parent and child class
    def print_all(self):
        for i in Contact_Manager.contact_list:
            print(i.name)
            print(i.email_id)
            #print(i.phone_number)
        

#sup1 = Suppliers('sup1', 'sup1@gmail.com', '001')
#sup1.print_all()


#cm1 = Contact_Manager('abc', 'abc@gmail.com', '9876543210')
#cm2 = Contact_Manager('def', 'def@gmail.com', '1234567890')
#cm3 = Contact_Manager('ghi', 'ghi@gmail.com', '2345678901')
#cm1.send()
            



    