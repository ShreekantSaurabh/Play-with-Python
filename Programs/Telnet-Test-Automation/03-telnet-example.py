import getpass
import telnetlib

HOST = "localhost"
user = "bhagavan"
password = "jnjnuh"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
print((tn.read_all().decode('ascii')))

tn.write(b"ls -l\n")
print((tn.read_all().decode('ascii')))

tn.write(b"exit\n")

print((tn.read_all().decode('ascii')))
