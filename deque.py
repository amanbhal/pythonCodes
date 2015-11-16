def addFront(item):
	deque.insert(0,item)

def addRear(item):
	deque.append(item)
	
def removeFront():
	deque.pop(0)
		
def removeRear():
	deque.pop(-1)

def isEmpty():
	return deque==[]
	
def size():
	return len(deque)
	
global deque
deque = [1,2,3,4,5,6]
removeFront()
removeRear()
removeFront()
removeFront()
removeFront()
removeFront()
print isEmpty()
addRear(7)
addFront(8)
print size()
print deque