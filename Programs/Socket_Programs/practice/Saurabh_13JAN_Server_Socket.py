import socket
import time

#create socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Succesfully created")

#Get local Machine name
host = socket.gethostname()

port = 9999

#bind to the port
serversocket.bind((host, port))

#queue to 5 request
serversocket.listen(5)

while True:
    #establish a connection 
    clientsocket, addr = serversocket.accept()
    
    print("Got a connection from %s " %str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
    
    



