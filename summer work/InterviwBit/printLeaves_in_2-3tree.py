class Node:
    def __init__(self,l_val,m_val,r_val,left,mid,right):
        self.l_val = l_val
        self.m_val = m_val
        self.r_val = r_val
        self.left = left
        self.mid = mid
        self.right = right
        
def printLeaves(root):
    if(root.left!=None):
        printLeaves(root.left)
    if(root.left==None and root.right==None and root.mid==None):
        print root.l_val
    if(root.mid!=None):
        printLeaves(root.mid)
    if(root.right!=None):
        printLeaves(root.right)
        
root = Node(5,None,27,None,None,None)
root.left = Node(5,None,13,None,None,None)
root.mid = None
root.right = Node(15,None,None,None,None,None)
root.left.left = Node(5,None,8,None,None,None)
root.left.mid = None
root.left.right = Node(10,None,13,None,None,None)
root.right.left = Node(15,None,22,None,None,None)
root.right.mid = None
root.right.right = None
root.left.left.left = Node(5,None,None,None,None,None)
root.left.left.mid = None
root.left.left.right = Node(8,None,None,None,None,None)
root.left.right.left = Node(10,None,None,None,None,None)
root.left.right.mid = None
root.left.right.right = Node(13,None,None,None,None,None)
root.right.left.left = Node(15,None,None,None,None,None)
root.right.left.mid = None
root.right.left.right = Node(22,None,None,None,None,None)

printLeaves(root)