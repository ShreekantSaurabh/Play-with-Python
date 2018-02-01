class Contact:
     #global contact_list
     contact_list = []

     def __init__(self, name , email_id):
          self.name = name
          self.email = email_id
          #global contact_list
          Contact.contact_list.append(self)
          #Contact.contact_list.append(self)
          #self.contact_list.append(self)

     def print_all(self):
          for contacts in Contact.contact_list:
               print contacts.name
               print contacts.email



class mailSender():
    def Send_mail(self, message):
        print "sending mail to " + self.email




#class EmailableConatct:
 #   pass



class EmailableContact(Contact, mailSender):
    pass


obj = EmailableContact("aditya", "aditya.singh@gmail.com")
obj.Send_mail("Hello Aditya")

print Contact.contact_list
