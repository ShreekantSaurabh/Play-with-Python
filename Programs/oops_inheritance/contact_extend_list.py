class contactSearch(list):
    def search(self, name):
        #matched_contact = []
        matched_contact = list()
        for i in self:
            if name in i.name:#contacts.name == name:
                matched_contact.append(i)
        #return matched_contact
        for contacts in matched_contact:
            print contacts
    
class ContactManager:
    #global contact_list
    contact_list = contactSearch() #list()
    def __init__(self, name , email):
       # global contact_list
        self.name = name
        self.email = email
        #global contact_list
        #ContactManager.contact_list.append(self)
        ContactManager.contact_list.append(self)

    def print_all(self):
        for contacts in ContactManager.contact_list:
            print contacts.name 
            print contacts.email


a  = ContactManager("aditya", "aditya@gmail.com")
b  = ContactManager("anand", "ananda@gmail.com")
c  = ContactManager("abhay", "abhay@gmail.com")
#a.print_all()

ContactManager.contact_list.search("a")


#for contacts in matched_contact:
 #    print contacts.name


