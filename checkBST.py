class Node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
		
def checkBST(root):
	if root==None:
		return True
	if(root.left!=None and root.left.value>root.value):
		return False
	if(root.right!=None and root.right.value<root.value):
		return False
	if(checkBST(root.left)!=True or checkBST(root.right)!=True):
		return False
	return True
	
root = Node(20)
root.left = Node(18)
root.right = Node(22)
root.left.left = Node(16)
root.left.right = Node(19)
root.right.left = Node(21)
root.right.right = Node(23)

print checkBST(root)