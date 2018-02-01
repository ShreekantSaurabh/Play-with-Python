import sys
import telnetlib

def get_process_status_by_name(service, HOST, user, password, ps_cmd):
	tn = telnetlib.Telnet(HOST)

	tn.read_until(bytes("login: ", 'UTF-8'))
	print("Prompted login")

	user = bytes(user+"\n", 'UTF-8')
	tn.write(user)
	print("Sent username :%s" % (user))

	tn.read_until(bytes("Password: ", 'UTF-8'))
	print("Prompted Password")

	if password:
		tn.write(bytes((password + "\n"), "UTF-8"))

	print("Sent password :%s" % ("*************"))

	tn.read_until(bytes(":~$ ", "UTF-8"))

	print ("Got Shell prompt")

	tn.write(bytes((ps_cmd + "\n"), "UTF-8"))
	print("Sent command :%s" % (ps_cmd))

	tn.read_until(bytes("CMD", 'UTF-8'))

	tn.write(bytes("exit\n", "UTF-8"))

	output =  tn.read_all()
	print ("==========")
	#print (output)
	print ("==========")

	if (output.find(bytes(service, "UTF-8")) >= 0):
		print("Service %s is ***Running***" % (service))
	else:
		print("Service %s is ***NOT Running***" % (service))

	print ("==========")

def get_hostname_by_ip(ip_addr, user, password):
	cmd = "hostname"

	tn = telnetlib.Telnet(ip_addr)

	tn.read_until("login: ")
	print("-->Prompted for username")

	tn.write(user + "\n")
	print("-->Sent username :%s" % (user))

	tn.read_until("Password: ")
	print("-->Prompted for Password")

	tn.write(password + "\n")
	print("-->Sent password :%s" % ("*************"))

	tn.read_until(":~$ ")
	print ("-->Got Shell prompt")

	tn.write(cmd + "\n")
	print("-->Sent command :%s" % (cmd))
	output = tn.read_until("com")
	print ("-->Hostname :%s" % output)

	tn.write("exit\n")

	output =  tn.read_all()
	print ("==========")
	print (output)
	print ("==========")

def get_sys_uptime_by_ip(ip_addr, user, password):
	cmd = "uptime"

	tn = telnetlib.Telnet(ip_addr)

	tn.read_until("login: ")
	print("-->Prompted for username")

	tn.write(user + "\n")
	print("-->Sent username :%s" % (user))

	tn.read_until("Password: ")
	print("-->Prompted for Password")

	tn.write(password + "\n")
	print("-->Sent password :%s" % ("*************"))

	tn.read_until(":~$ ")
	print ("-->Got Shell prompt")

	tn.write(cmd + "\n")
	print("-->Sent command :%s" % (cmd))

	tn.read_until("up")
	tn.write("exit\n")

	output =  tn.read_all()
	print ("==========")
	print (output)
	print ("==========")

HOST = "localhost"
user = "bhagavan"
password = "jnjnuh"
ps_cmd = "ps -Al"
service = "mytestprog"

def main():
	#get_sys_uptime_by_ip("127.0.0.1", "bhagavan", "jnjnuh")
	#get_process_status_by_name(service, HOST, user, password, ps_cmd)
	get_hostname_by_ip("127.0.0.1", "bhagavan", "jnjnuh")

if (__name__ == "__main__"):
        main()

exit(1)

