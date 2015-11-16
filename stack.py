def push(data):
	stack.append(data)

def pop1():
	stack.pop(-1)

def peek():
	print stack[-1]

def isEmpty():
	try:
		stack[0]
		print "Stack is not empty"
	except IndexError:
		print "Stack is empty"
		
def size():
	print "Size of stack is: ", len(stack)

global stack
stack = []
isEmpty()
push(6)
push(7)
push(8)
push(9)
size()
pop1()
peek()
size()
print stack
