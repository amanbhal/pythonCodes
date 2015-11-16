import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
msg = raw_input(">>>")
while msg!="exit":
	s.send(msg)
	asd = s.recv(1024)
	print str(asd)
	msg = raw_input(">>>")
	
s.close()                     # Close the socket when done