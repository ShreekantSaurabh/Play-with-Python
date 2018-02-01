import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Succesfully created")
except socket.error as err:
    print("socket creation failed with error" + err)
    
port = 80

host_ip = socket.getaddrinfo("www.google.com")

s.connect(host_ip, port)

print("The socket has succesfully connected to google")

