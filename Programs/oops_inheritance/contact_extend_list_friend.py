class contactSearch(list):
    def search(self, name):
        #matched_contact = []
        matched_contact = list()
        for contacts in self:
            if name in contacts.name:               #contacts.name == name:
                matched_contact.append(contacts)
        #return matched_contact
        for contacts in matched_contact:
            print (contacts.name)
 


class ContactManager:
    #gloextend_list.py_list
    contact_list = contactSearch()
    def __init__(self, name , email):
       # global contact_list
        self.name = name
        self.email = email
        #global contact_list
        #ContactManager.contact_list.append(self)
        ContactManager.contact_list.append(self)

    def print_all(self):
        for contacts in ContactManager.contact_list:
            print (contacts.name) 
            print (contacts.email)



class Friend(ContactManager):    
    def __init__(self, name, email, phone):        
        self.name = name        
        self.email = email        
        self.phone = phone


class office_friend(ContactManager):
    def __init__(self, name , email, phone):
        #super(ContactManager).__init__(name , email)
        #super(ContactManager, self).__init__(name , email)
        ContactManager.__init__(self, name, email)
        self.phone = phone
        #self.address = address


a  = ContactManager("aditya", "aditya@gmail.com")
b  = ContactManager("anand", "ananda@gmail.com")
c  = ContactManager("abhay", "abhay@gmail.com")
d  = Friend("ram","ram@samsung.com", "9148569992")
e  = office_friend("ramesh", "ramesh@samsung.com", "76677744")
#a.print_all()

ContactManager.contact_list.search("a")


#for contacts in matched_contact:
 #    print contacts.name


