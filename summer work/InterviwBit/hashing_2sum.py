"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where 
index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. 
Put both these numbers in order in an array and return the array from your function ( Looking at the function 
signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the 
minimum index2, choose the one with minimum index1 out of them.
"""
def twoSum(A, B):
	hashDict = dict()
	n = len(A)
	for i in range(n):
		if A[i] in hashDict:
			return [hashDict[A[i]]+1,i+1]
		elif B-A[i] not in hashDict:
			hashDict[B-A[i]]=i
	return []
	
twoSum([2, 7, 11, 15],9)