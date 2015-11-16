class Node(object):
	def __init__(self,data,link):
		self.data = data
		self.link = link
		
class Block(object):
	def __init__(self,head,next,nodeCount):
		self.head = head
		self.next = next
		self.nodeCount = nodeCount
		
def newBlock():
	block = Block(None,None,0)
	return block
	
def newNode(value):
	temp = Node(value,None)
	return temp
	
def searchElement(nodeNumber,firstBlock):
		#find the block
		j = (nodeNumber-1)/blockSize
		k = nodeNumber%blockSize
		if(k==0):
			k = blockSize
		
		block = firstBlock
		while(j):
			block = block.next
			j = j-1
		blockNode = block.head
		
		k = block.nodeCount + 1 - k		#because links are in reverse direction
		while(k):
			blockNode = blockNode.link
			k = k-1
		return block,blockNode
		
def main():
	global blockSize
	blockSize = 3
	node1 = newNode(10)
	node2 = newNode(156)
	node3 = newNode(30)
	node3.link = node2
	node2.link = node1
	node1.link = node3
	block2 = Block(node1,None,3)
	node4 = newNode(70)
	node5 = newNode(3)
	node6 = newNode(45)
	node6.link = node5
	node5.link = node4
	node4.link = node6
	block1 = Block(node4,block2,3)
	foundBlock, foundNode = searchElement(5,block1)
	print foundNode.data
	
	
main()