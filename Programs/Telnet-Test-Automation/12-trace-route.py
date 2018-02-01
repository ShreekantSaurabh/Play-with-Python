from scapy.all import *
target = ["yahoo.com"]
target = ["192.168.1.254"]

result, unans = traceroute(target, maxttl=32)
print (result)
print (unans)

print (traceroute(["www.yahoo.com","www.altavista.com","www.wisenut.com","www.copernic.com"],maxttl=20))
