import socket
import time

#create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Succesfully created")

#Get local Machine name
host = socket.gethostname()

port = 9999

#connection to hostname on the port
s.connect((host, port))

#Recieve no more than 1024 byte
tm = s.recv(1024)

s.close()


print("The time got from the server is %s" % tm.decode("ascii"))