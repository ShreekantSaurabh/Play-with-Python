import json

servers_list = [ 
 {
   "system_name": "localhost",
   "username": "bhagavan",
   "password": "jnjnuh",
   "service": "apache2"
 },
 {
   "system_name": "192.168.1.1",
   "username": "bhagavan",
   "password": "jnjnuh",
   "service": "nginx"
 },
 {
   "system_name": "127.0.0.1",
   "username": "bhagavan",
   "password": "jnjnuh",
   "service": "ftpd"
 }
]
print(servers_list)
print(servers_list[0])
print(servers_list[0]["system_name"])
print(servers_list[0]["username"])
print(servers_list[0]["password"])

for server in servers_list:
    #print server["system_name"]
    #print server["username"]
    #print server["password"]
    print((server['system_name'], server['username'], server['password'], server['service']))
'''
'''

print ("")

with open('servers.json') as data_file:    
    data = json.load(data_file)

for server in data:
    print((server['system_name'], server['username'], server['password'],  server['service']))
