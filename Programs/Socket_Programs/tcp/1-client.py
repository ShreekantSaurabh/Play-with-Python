
import socket
import time

#dip_addr = '127.0.0.1'
dip_addr = socket.gethostname()  #can also be done for local machine.
DTCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

#socket file discriptor/object creation
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Succesfully created")

#connection to hostname on the port, TCP handshake happens here
sockfd.connect((dip_addr, DTCP_PORT))

#To send actual data after handshake
sent_message = sockfd.send(MESSAGE.encode())
print(MESSAGE + " sent to the server")

#Recieving data no more than buffer size at a time
data = sockfd.recv(BUFFER_SIZE)
print(data.decode("ascii") + " recieved from server")

time.sleep(1)

sockfd.close()
