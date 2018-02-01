class MailSender:
    
#     def __init__(self, a, b):
 #         self.x=20
  #        print "In side MailuSender constructor"
 
     def send_mail(self, message):
        #print "Sending mail with so and so message"
        print("Sending mail to " + self.email)


class Contact:
    # global contact_list
     contact_list = []

     def __init__(self, name , email_id):
          self.name = name
          self.email = email_id
          #global contact_list
          Contact.contact_list.append(self)
          print "Inside Contact constructor"
          #Contact.contact_list.append(self)
          #self.contact_list.append(self)

     def print_all(self):
          for contacts in Contact.contact_list:
               print contacts.name
               print contacts.email


#If few contacts are supplier 

#class Suppliers(Contact): 
#   def order(self):
#        print "If this were a real system we would send "


#class EmailableContact(Contact, MailSender):
#     pass

class EmailableContact(MailSender, Contact):
     pass
class EmailableContact(Contact):
     
      __init__(self, emailid)
          self.MailSender = MailSender()

c1  = Contact("xyz", "abc@gmail.com")
e0 = EmailableContact("Abhay", "Abhay@gmail.com")
print Contact.contact_list
e0.send_mail("Hello e0")

e0.MailSender.Send("jdhkjahdjk")






