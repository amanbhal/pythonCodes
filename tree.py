class Node(object):
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

node = Node(5,None,None)
node.left = Node(3,None,None)
node.right = Node(2,None,None)
node1 = None
node1 = node
node1.data = 678
print node.data, node.right.data, node.left.data,node1.data,node1.left.data, node1.right.data    
