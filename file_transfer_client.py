import threading
import socket

host = '127.0.0.1'
port = 5002

s = socket.socket()
s.connect((host,port))

file = raw_input("Enter filename:\t")
while file!="exit":
	s.send(file)
	output = s.recv(1024)
	print output
	filesize = long(output[13:])
	if output[:12]=="TRANSFERRING":
		input = raw_input("Type 'OK' to proceed and 'CANCEL' to cancel file transfer:\t")
		s.send(input)
		f = open('new_'+file, 'wb')
		data = s.recv(1024)
		totalRecv = len(data)
		f.write(data)
		while totalRecv<filesize:
			data = s.recv(1024)
			totalRecv += len(data)
			f.write(data)
			print str((totalRecv/float(filesize))*100) + "% complete"
		print "Download Complete"
		file = raw_input("Enter filename:\t")
	else:
		print "File does not exist."

s.close()