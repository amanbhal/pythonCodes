class Node:
	def __init__(self,val,next):
		self.val = val
		self.next = next

def detectCycle(A):
	curr = A
	visited = {}
	while(curr!=None and visited.get(curr.val)==None):
		visited[curr.val] = 1
		curr = curr.next
	if(curr==None):
		return curr
	else:
		return curr.val
		
head = Node(1,None)
head.next = Node(2,None)
head.next.next = Node(3,None)
head.next.next.next = Node(4,None)
head.next.next.next.next = Node(5,head.next.next)

print detectCycle(head)