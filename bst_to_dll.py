class Node(object):
	def __init__(self,data,left,right):
		self.data = data
		self.right = right
		self.left = left

def convert(root,head):
	if root==None:
		return
	convert(root.left,head)
	if(head==None):
		head = root
		prev = root
	else:
		root.left = prev
		prev.right = root
	prev = root
	convert(root.right,head)
	
root = Node(10,None,None)
root.left = Node(6,None,None)
root.right = Node(14,None,None)
root.left.left = Node(4,None,None)
root.left.right = Node(8,None,None)
root.right.left = Node(12,None,None)
root.right.right = Node(16,None,None)

head = None

global prev
prev = None  		

convert(root,head)