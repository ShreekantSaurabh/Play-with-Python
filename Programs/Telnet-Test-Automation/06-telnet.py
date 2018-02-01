import telnetlib
import time
import sys

HOST = "192.168.1.253"
USER = "bhagavan"
PASSWORD = "jnjnuh"

telnet = telnetlib.Telnet(HOST)
print("After telnet")

telnet.read_until("login: ")
telnet.write(USER + "\n")
print("After user")

telnet.read_until("Password: ")
telnet.write(PASSWORD + "\n")
data = telnet.read_until("~$")
print("Login successful")

#telnet.write("stdbuf -i0 -o0 -e0 ls -l\n")

#telnet.write("ls -l\n")
#print "After ls"
#data = telnet.read_until("total")
#print "got total"

telnet.write("service apache2 status\n")
print("After service")
data = telnet.read_until("apache2")
data = telnet.read_very_eager()

if (data.find("not running") > 0):
    print("Service is not running")
    print("starting service")
    telnet.write("sudo service apache2 start\n")
    telnet.read_until("[sudo] password ")
    data = telnet.read_very_eager()

    telnet.write("jnjnuh\n")
    data = telnet.read_until("*")
    time.sleep(5)
    data = telnet.read_very_eager()

    if (data.find("failed") > 0):
        print("Service start failed")
    else:
        print("Service start SUCCESS")

if (data.find("unrecognized") > 0):
    print("Service is not INSTALLED")

telnet.write("exit\n")
print(data)

'''
telnet.write("exit\n")

telnet.read_very_eager()
#print telnet.read_all()

telnet.write("ps -aLl\n")
print "After ps"
print telnet.read_very_eager()
#print telnet.read_all()

telnet.write("netstat -alnp\n")
print "After netstat"
#print telnet.read_all()
print telnet.read_very_eager()

print "After read"
time.sleep(5)
telnet.write("exit\n")

print telnet.read_all()

'''
