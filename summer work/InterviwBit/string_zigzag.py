def convert(string, rows):
	if rows==1:
		return string
	zigzag = ""
	curr = 0
	row = []
	add = -1
	for i in range(0,rows):
		row.append([])
	for i in range(0,len(string)):
		if(curr==0 or curr==rows-1):
			if(add==1):
				add = -1
			else:
				add = 1
		row[curr].append(string[i])
		curr += add
	
	for i in range(0,rows):
		for j in range(0,len(row[i])):
			zigzag += row[i][j]
	
	return zigzag

print convert("kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS",1)	