import threading
import time

maxconnections = 2
pool_sema = threading.BoundedSemaphore(value=maxconnections) # allows more than one thread lock at a time.

def timer(name,delay,repeat):
	print "Timer : " + name + " started."
	pool_sema.acquire()
	print name + " acquired lock"
	while repeat>0:
		time.sleep(delay)
		print name, time.ctime(time.time())
		repeat -= 1
	pool_sema.release()
	print name + " released lock"
	print "Timer : " + name + " completed."

t1 = threading.Thread(target=timer,args=("Thread_1",2,4))
t2 = threading.Thread(target=timer,args=('Thread_2',3,4))
t3 = threading.Thread(target=timer,args=('Thread_3',1,2))

t1.start()
t2.start()
t3.start()

print "Program completed."