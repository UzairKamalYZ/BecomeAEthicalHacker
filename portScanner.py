import sys
import socket
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("not enough arguments")
	sys.exit()

try:
	for port in range(50,90):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		print("checking port {}".format(port))
		if result == 0:
			print("port {} is opne".format(port))
		s.close()
except  KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resovled")
	sys.exit()
except socket.error:
	print("Couldn't connect to server")
	sys.exit()
							
