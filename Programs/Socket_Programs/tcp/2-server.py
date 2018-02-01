#!/usr/bin/env python
import socket
import time

MY_IFACE = ''      # if it is '' empty then it will consider all ports present for communication
#MY_IFACE = socket.gethostname()   #can also be done to get its name
TCP_PORT = 5005
BUFFER_SIZE = 20 

#socket file discriptor/object creation
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Succesfully created")

#bind hostname to the port
sockfd.bind((MY_IFACE, TCP_PORT))

#queue to 5 request
sockfd.listen(5)

#new file descriptors gets created after establish a connection using accept()
newfd, addr = sockfd.accept()
print('Got new Connection from address:', addr)

data = newfd.recv(BUFFER_SIZE)
print("received data from client:", data.decode())

newfd.send(data.upper())  # echo/ send the data to client

newfd.close()
sockfd.close()

