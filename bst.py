class Node(object):
	def __init__(self,data,left,right):
		self.data = data
		self.left = left
		self.right = right

def bst(node,data):
	if node==None:
		return Node(data,None,None)
	else:
		if data <= node.data:
			temp = bst(node.left,data)
			node.left = temp
		else:
			temp = bst(node.right,data)
			node.right = temp
		return node
		
def inorder(node):
	if node.left==None and node.right==None:
		print node.data
	else:
		inorder(node.left)
		print node.data
		inorder(node.right)
	
#global root
root = None
root = bst(root,20)
root = bst(root,8)
root = bst(root,22)
root = bst(root,4)
root = bst(root,12)

inorder(root)