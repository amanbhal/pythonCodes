no = int(raw_input())
arr = []
for x in range(no):
	i = int(raw_input())
	arr.append(i)

print arr
	
maxi = max(arr)
ind = arr.index(maxi)
if ind==0:
	print 0
else:
	mini = min(arr[:ind])
	diff = maxi - mini
	print diff