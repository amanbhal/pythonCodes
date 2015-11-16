import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	#override the default for tcp
host = '127.0.0.1'
port = 5000
s.bind((host,port))

print "Server Started"

while True:
	data, addr = s.recvfrom(1024)
	if not data:
		break
	print addr,":",data
	msg = raw_input(">>>")
	s.sendto(data,addr)

c.close()