import socket
from termcolor import colored

def scan(target, ports):
	print('\n' + '[+] Starting Scanning ' + str(target))
	for port in range (1,ports):
		scan_port(target, port)
		
def get_banner(s):
	return s.recv(1024)	
	
def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.settimeout(0.3)
		sock.connect((ipaddress, port))
		
		try:
			banner = get_banner(sock)
			print('[+] Open Port ' + str(port) + ' :' + str(banner.decode().strip('\n')))
		except:
			print('[+] Open port ' + str(port))
		sock.close()
	
	except:
		pass
		
targets = input('[+] Enter Target IP: ')
ports = int(input('[+] Enter number of ports to scan: '))

flag = 0

if ',' in targets:
	print(colored(('\n [*] Scanning multiple targets [*]\n'), 'green'))
	for ip_add in targets.split(','):
		"""if (isinstance(ip_add.strip(' '), str)):
			try:
				ip_add_new = socket.gethostbyname(ip_add)
				scan(ip_add_new,ports)
			except socket.gaierror as e:
				print("[+] Error resolving hostname: " + ip_add.strip(' '))
		else:"""
		scan(ip_add.strip(' '), ports)
else:
	scan(targets,ports)

