class contactSearch(list):
    def search(self, name):
        matched_contact = []
        for contacts in self:
            if name in contacts.name:#contacts.name == name:
                matched_contact.append(contacts)
        #return matched_contact
        for contacts in matched_contact:
            print (contacts.name)
    







class ContactManager(object):
    #global contact_list
    contact_list = contactSearch()
    def __init__(self, name , email):
       # global contact_list
        self.name = name
        self.email = email
        #global contact_list
        #ContactManager.contact_list.append(self)
        self.contact_list.append(self)

    def print_all(self):
        for contacts in contact_list:
            print (contacts.name) 
            print (contacts.email)


class frnd(ContactManager):
    def __init__(self,name, email, phno):
        super(ContactManager).__init__(self, name , email)
        self.phone_no = phno




a  = ContactManager("adityain", "aditya@gmail.com")
b  = ContactManager("ananind", "ananda@gmail.com")
c  = ContactManager("abhay", "abhay@gmail.com")
d  = frnd("anand", "apsingh@gmail.com", "9880776543")
