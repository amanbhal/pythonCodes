def prettyJSON(A):
	A = A.replace(" ","")
	B = list(A)
	#print B
	indent = ['\t']
	enter = '\n'
	result = ""
	result += B[0]+enter+''.join(indent)
	for i in range(1,len(B)):
		if(B[i]=='{' or B[i]=='['):
			result += enter+''.join(indent)+B[i]+enter
			indent.append('\t')
			result += ''.join(indent)
		elif(B[i]=='}' or B[i]==']'):
			indent = indent[:len(indent)-1]
			result += enter+''.join(indent)+B[i]+enter+''.join(indent)
		elif(B[i]==','):
			result += B[i]+enter+''.join(indent)
		else:
			result += B[i]
	return result
	
	
print prettyJSON('{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}')