import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 5001
server = ('127.0.0.1',5000)
s.bind((host,port))

msg = raw_input(">>>")

while msg!="exit":
	s.sendto(msg,server)
	data, addr = s.recvfrom(1024)
	print addr,":",data
	msg = raw_input(">>>")
s.close()