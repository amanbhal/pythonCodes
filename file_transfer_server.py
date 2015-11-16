import threading
import socket
import os

host = '127.0.0.1'
port = 5002
log = {}	#to keep a track of file transfers

def fileTrans(addr,sock):
	file = sock.recv(1024)
	log[addr]=file
	if os.path.isfile(file):
		sock.send("TRANSFERRING " + str(os.path.getsize(file)))
		userResponse = sock.recv(1024)
		if userResponse=="OK":
			with open(file, 'rb') as f:
				bytesToSend = f.read(1024)
				sock.send(bytesToSend)
				while bytesToSend!="":
					bytesToSend = f.read(1024)
					sock.send(bytesToSend)
		else:
			sock.send("TRANSFER CANCELLED")
	else:
		sock.send("ERR")
	sock.close()

s = socket.socket()
s.bind((host,port))
s.listen(5)
print "SERVER STARTED"

while True:
	c, addr = s.accept()
	t = threading.Thread(target=fileTrans,args=(addr,c))
	t.start()

print log
s.close()