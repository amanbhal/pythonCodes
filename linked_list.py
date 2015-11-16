class Node(object):
	def __init__(self,data,next,previous):
		self.data = data
		self.next = next
		self.previous = previous

def insertion(index,data,head):	
	temp = Node(data,None,None)
	if head==None:
		head = temp
		return head
	start = head
	count = 0
	while count!=index:
		start = start.next
		count += 1
	if start.next == None:
		start.next = temp
		temp.previous = start
	else:
		temp.next = start.next
		start.next.previous = temp
		start.next = temp
		temp.previous = start
	return head
	
def deletion(index,head):
	start = head
	count = 0
	while count!=index:
		start = start.next
		count += 1
	if start.previous==None and start.next!=None:
		head = start.next
		head.previous = None
		del start
	elif start.next==None and start.previous!=None:
		start.previous.next = None
		start.previous = None
		del start
	elif start.next==None and start.previous==None:
		head = None
		del start
	else:
		start.previous.next = start.next
		start.next.previous = start.previous
		del start
	return head
	
head = None
head = insertion(0,2,head)
head = insertion(0,3,head)
head = insertion(1,4,head)
start = head
while start!=None:
	print start.data,
	start = start.next
head = deletion(1,head)
head = deletion(0,head)
head = deletion(1,head)
head = deletion(0,head)
start = head
while start!=None:
	print start.data,
	start = start.next
if start == None:
	print "None"