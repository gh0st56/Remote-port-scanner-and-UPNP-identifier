import socket
import sys
import errno
import re

arg1 = sys.argv[1]
arg2 = sys.argv[2]
ports = list(range(15 ,500))

upnpreq = \
	b'M-SEARCH * HTTP/1.1\r\n' \
    b'HOST: 239.255.255.250:1900\r\n' \
    b'ST:upnp:rootdevice\r\n' \
    b'MX:2\r\n' \
    b'MAN:"ssdp:discover"\r\n' \
    b'\r\n'

def Banner():
	banner = """
	 _                 _____                 
	| |               /  ___|                
	| |     __ _ _ __ \ `--.  ___ __ _ _ __  
	| |    / _` | '_ \ `--. \/ __/ _` | '_ \ 
	| |___| (_| | | | /\__/ / (_| (_| | | | |
	\_____/\__,_|_| |_\____/ \___\__,_|_| |_|
        [*] Created By: André Lorenci(gh0sst)
	10/13/2019
                                         """                                                                                                                               
	print(banner)
	
def remote_ports():
    for port in ports:
        try:
            if port == 80:
                continue
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((arg1, port))
            resp = sock.recv(1024)
            port = str(port)
            sock.close()
            print("[+] port "+port+" open")
            print("\t--"+str(resp)+"\r\n")
        except socket.error:
            sock.close()
        if port == "250":
            print("Still scanning...")
def Upnp_scan():
	local_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	local_sock.settimeout(3)
	local_sock.sendto(upnpreq, ('239.255.255.250', 1900))
	try:
		while True:
			response = local_sock.recvfrom(1020)
			response = str(response)
			print("[+] UPNP service found: "+response+"\r\n")
	except socket.timeout:
		pass

if arg2 == "--rs":
	Banner()
	print("Starting remote scanner...\r\n")
	remote_ports()
if arg1 == "localhost" and arg2 == "--ls":
	Banner()
	print("UPNP service scanner...\r\n")
	Upnp_scan()

	
    
