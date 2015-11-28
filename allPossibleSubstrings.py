from math import factorial
def substrings(A,sol):	#all substrings
	while(len(sol)!=calculate(len(A))):
		for string in sol:
			for char in A:
				if(char not in string):
					sol.append(string+char)
	print "All possible substrings are:",
	for i in sol:
		print i,
	print ""
	print"-----------------------------------"
			
def uniqueSubstrings(A):	#unique substrings
	sol = []
	for i in range(len(A)):
		sol.append(A[i])
		for j in range(len(sol)):
			if(A[i]!=sol[j]):
				sol.append(sol[j]+A[i])
		
	print "Unique substrings are:",
	for i in sol:
		print i,
	print ""
	print "------------------------------------"
	
def calculate(n):
	result = 0
	for i in range(1,n+1):
		result += (factorial(n)/factorial(n-i))
	return result
		
A = "abc"
A = list(A)
sol = []
uniqueSubstrings(A)
for i in A:
	sol.append(i)
substrings(A,sol)