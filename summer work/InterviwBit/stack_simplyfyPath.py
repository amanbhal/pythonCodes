from collections import deque
def simplifyPath(A):
	B = A.split('/')
	#print B
	C = deque()
	for i in B:
		try:
			if(i=='.' or i==''):
				pass
			elif(i=='..'):
				C.pop()
			else:
				C.append(i)
		except IndexError:
			pass
	result = ""
	while(len(C)!=0):
		if(C[0]==''):
			C.popleft()
		else:
			result += '/'+C.popleft()
	
	if(result==''):
		return '/'
	else:
		return result
print simplifyPath("/./.././ykt/xhp/nka/eyo/blr/emm/xxm/fuv/bjg/./qbd/./../pir/dhu/./../../wrm/grm/ach/jsy/dic/ggz/smq/mhl/./../yte/hou/ucd/vnn/fpf/cnb/ouf/hqq/upz/akr/./pzo/../llb/./tud/olc/zns/fiv/./eeu/fex/rhi/pnm/../../kke/./eng/bow/uvz/jmz/hwb/./././ids/dwj/aqu/erf/./koz/..")    