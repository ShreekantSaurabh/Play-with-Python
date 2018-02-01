class Contact:
    all_contacts = []
   
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)
        print ("Contacts")



class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        print ("Address Holder")


class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone
        print ("In Frinds")



f0 = Friend("Ramesh Caurasia", street = "main road", state = "Dehi", code = "50123", name = "Abhay", email = "Abhay22@gmail.com")
f1 = Friend("Ramesh Caurasia")
print (Contact.all_contacts)
print (Contact.all_contacts[0].street )
print (f1.phone)

