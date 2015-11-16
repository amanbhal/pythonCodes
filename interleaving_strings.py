def interleaving(string1,string2,string3):
		index1 = 0
		index2 = 0
		index3 = 0 
		condition = True
		while string2[index2]==string3[index3]:
			index2 += 1
			index3 += 1
		if string1.index(string2[index2]) < string1.index(string3[index3]):
			s1 = string2
			s2 = string3
		else:
			s1 = string3
			s2 = string2
		i1 = 0
		i2 = 0
		if(len(string1)!=len(s1)+len(s2)):
			return False
		while condition==True:
			try:
				string1[index1+1]  
			except IndexError: 
				condition = False
			if i1<len(s1) and string1[index1]==s1[i1]:
				i1 += 1
			elif i2<len(s2) and string1[index1]==s2[i2]:
				i2 += 1
			else:
				return False
			index1 +=1
		return True
			
string1 = raw_input("Enter main string\n")
string2 = raw_input("Enter first string\n")
string3 = raw_input("Enter second string\n")
print interleaving(string1,string2,string3)