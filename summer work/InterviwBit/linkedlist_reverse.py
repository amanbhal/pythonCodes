class Node:
	def __init__(self,data,next):
		self.data = data
		self.next = next
		
def reverseLinkedList(head,a,b):
	count = 0
	curr = head
	if(a==1):
		prev_start = Node(0,head)
	
	while(curr!=None):
		count += 1
		if(count==a-1):
			prev_start = curr
		if(count==a):
			start = curr
		if(count==b-1):
			prev_end = curr
		if(count==b):
			end = curr
		curr = curr.next

	while(start!=end):
		prev_start.next = start.next
		start.next = end.next
		end.next = start
		start = prev_start.next
	if(a==1):
			head = prev_start.next
	print "Final list: ",
	while(head!=None):
		print head.data,
		head = head.next

head = Node(1,None)
head.next = Node(2,None)
head.next.next = Node(3,None)
#head.next.next.next = Node(4,None)
#head.next.next.next.next = Node(5,None)

print "Initial list: ",
curr = head
while(curr!=None):
	print curr.data,
	curr = curr.next
print '\n'

reverseLinkedList(head,1,2)