import datetime
import socket
import time
#from local_machine_info import print_machine_info

start_time = time.time()

print "Vrijeme pokretanja novog programa: "
print datetime.datetime.now()
print "Program se izvodi na ovom racunalu:"
#print_machine_info()

print "--------------------------------------------"
print "Molim vas unesite adresu hosta koju zelite testirati:"
target = raw_input(">> ")
targetIP = socket.gethostbyname(target)
print "Skeniram host %s, IP adresu: %s" % (target, targetIP)
print "Unesite od kojeg do kojeg porta zelite napraviti skeniranje? "
start = raw_input("Pocetni port >> ")
end = raw_input("Zavrsni port >> ")

for PortNumber in range(int(start),int(end)+1):
	tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "Skeniram port: %d" % PortNumber
	result = tcp_sock.connect_ex((targetIP,PortNumber))
	if result == 0:
		print "Port %d je otvoren" % PortNumber
	tcp_sock.close()

elapse_time = time.time() - start_time

print "Skeniranje portova zavrseno!!!"
print " Trajanje %s " % elapse_time