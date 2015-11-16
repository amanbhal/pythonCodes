def enqueue(item):
	queue.append(item)

def dequeue():
	queue.pop(0)
	
def isEmpty():
	try:
		queue[0]
		return False
	except IndexError:
		return True

def size():
	return len(queue)

global queue
queue = []
print isEmpty()
queue = [1,2,3,4,5,6,7]
print size()
dequeue()
dequeue()
enqueue(8)
enqueue(9)
print queue