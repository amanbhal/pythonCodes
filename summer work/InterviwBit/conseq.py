"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example: 
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
def longestConsecutive(A):
	hashmap = dict()
	for i in A:
		if i not in hashmap:
			hashmap[i] = 1
	A = sorted(hashmap.keys())
	count = []
	streak = 1
	for i in range(0,len(A)-1):
		if(A[i+1]-A[i]==1):
			streak += 1
		else:
			count.append(streak)
			streak = 1
		if(i+1==len(A)-1):
			count.append(streak)
	try:
		return max(count)
	except ValueError:
		return 1
		
print longestConsecutive([ 97, 86, 67, 19, 107, 9, 8, 49, 23, 46, -4, 22, 72, 4, 57, 111, 20, 52, 99, 2, 113, 81, 7, 5, 21, 0, 47, 54, 76, 117, -2, 102, 34, 12, 103, 69, 36, 51, 105, -3, 33, 91, 37, 11, 48, 106, 109, 45, 58, 77, 104, 60, 75, 90, 3, 62, 16, 119, 85, 63, 87, 43, 74, 13, 95, 94, 56, 28, 55, 66, 92, 79, 27, 42, 70 ])