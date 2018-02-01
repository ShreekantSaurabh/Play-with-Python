import json
import telnetlib
import time
import sys
from scapy.all import *

if sys.version_info[0] == 2:
	import thread as thread
else:
	import _thread as thread

import threading
from threading import Thread, current_thread
import os
from multiprocessing import Process, Lock

def get_task_id():
	return current_thread().name

def my_debug_print (debug):
	print("\t" + get_task_id() + ":" + debug)

def print_output(data):
	data = str(data)

	my_debug_print ("----------")
	for line in data.split('\n'):
		my_debug_print(line)
	my_debug_print ("----------")

def make_connection(host):
    #print(get_task_id(), end=' ') 
    try:
        telnet = telnetlib.Telnet(host)
        print("Telnetting to server '%s' success..." % host)
        return telnet
    except:
        print("Could not connect to server '%s'" % host)
        return None 

def get_trace_route_by_ip(host):
	#target = ["192.168.1.254"]
	target = ["yahoo.com"]
	result, unans = traceroute(target, maxttl=5)
	print (result)
	print ("")
	print (unans)

	return result

def start_service_by_name(host, username, password, service):
	'''	
	print ("host     :", host)
	print ("username :", username)
	print ("password :", password)
	print ("serivce  :", service)
	print ("host     :", host)
	'''	

	telnet = make_connection(host)

	if (telnet == None):
		get_trace_route_by_ip(host)
		return
	telnet.read_until("login: ".encode('ascii'))

	username = bytes(username+"\n", 'UTF-8')
	telnet.write(username)

	telnet.read_until("Password: ".encode('ascii'))

	password = bytes(password + "\n", 'UTF-8')
	telnet.write(password)

	data = telnet.read_until("~$".encode('ascii'))
	my_debug_print ("Logging into server '%s' is successful..." % host)

	my_debug_print ("Checking '%s' status..." % service)

	cmd = "service " + service + " status\n"
	telnet.write(bytes(cmd, 'UTF-8'))

	data = telnet.read_until("*".encode('ascii'))
	data = telnet.read_very_eager()
	#print "service status :'%s'" % data

	if (data.find("not".encode('ascii')) > 0):
		my_debug_print("Service '%s' is not running..." % service)
		my_debug_print("Trying to start service...")

		telnet.write(bytes("sudo service apache2 start\n", 'UTF-8'))
		telnet.read_until("[sudo] password ".encode('ascii'))
		data = telnet.read_very_eager()

		password = (password + bytes("\n", 'UTF-8'))
		telnet.write(password)

		data = telnet.read_until("*".encode('ascii'))
		time.sleep(5)
		data = telnet.read_very_eager()

		if (data.find("failed".encode('ascii')) > 0):
			my_debug_print ("Service start failed, reason...")
			print_output(data)
		else:
			my_debug_print( "Service start SUCCESS")
	else:
		my_debug_print("Service '%s' is already running..." % service)

	telnet.write(bytes("exit\n", 'UTF-8'))

def main():
	#with open('servers.json', encoding="utf-8") as data_file:    
	with open('servers.json') as data_file:    
		data = json.load(data_file)


	for server in data:
		start_service_by_name(server['system_name'], server['username'], server['password'],  server['service'])
		print("")
		return

if (__name__ == "__main__"):
	main()
