class Contact:
    # global contact_list
     contact_list = list()     #[]

     def __init__(self, name , email_id):
          self.name = name
          self.email = email_id
          #global contact_list
          Contact.contact_list.append(self)
          #Contact.contact_list.append(self)
          #self.contact_list.append(self)

     def print_all(self):
          for contacts in Contact.contact_list: 
               print(contacts.name)
               print(contacts.email)


#If few contacts are supplier 

class Suppliers(Contact):
    def order(self):
        print( "If this were a real system we would send ")

c1 =  Contact("aditya", "aditya.singh@learnbay.in")
s1 = Suppliers("Anand", "anand.singh@learnbay.in")
s1.order()
c1.print_all()


