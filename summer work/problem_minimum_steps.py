import math
def coverPoints(A, B):
	steps = 0
	for i in range(0,len(A)-1):
		x1 = A[i]
		y1 = B[i]
		x2 = A[i+1]
		y2 = B[i+1]
		X = math.fabs(x1-x2)
		Y = math.fabs(y1-y2)
		x = x1
		y = y1
		while(X>0 and Y>0):
			if(x2>x1 and y2>y1):
				x += 1
				y += 1
			elif(x2<x1 and y2>y1):
				x -= 1
				y += 1
			elif(x2>x1 and y2<y1):
				x += 1
				y -= 1
			else:
				x -= 1
				y -= 1
			X = math.fabs(x-x2)
			Y = math.fabs(y-y2)
			steps += 1
			
		if (X == 0):
			steps += math.fabs(y-y2)
		else:
			steps += math.fabs(x-x2)
		print steps
	print steps
		
A = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
B = [ 4, -15, -10, -3, -13, 12, 8, -8 ]
coverPoints(A,B)