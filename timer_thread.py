import threading
import time

tLock = threading.Lock() 	#when one lock is acquired nobody else can acquire that lock until it is released

def timer(name,delay,repeat):
	print "Timer : " + name + " started."
	tLock.acquire()
	print name + " acquired lock"
	while repeat>0:
		time.sleep(delay)
		print name, time.ctime(time.time())
		repeat -= 1
	tLock.release()
	print name + " released lock"
	print "Timer : " + name + " completed."

t1 = threading.Thread(target=timer,args=("Thread_1",2,4))
t2 = threading.Thread(target=timer,args=('Thread_2',3,4))

t1.start()
t2.start()

print "Program completed."