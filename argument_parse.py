				# calculates the fibonacci number entered by user while running the program 
				# https://docs.python.org/3/howto/argparse.html#id1
				# https://docs.python.org/3/library/argparse.html

import argparse

def fib(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a+b
	return a
	
parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("-v","--verbose",action="store_true")  #add a mutually exclusive option argument
group.add_argument("-q","--quite",action="store_true")	#add a mutually exclusive option argument

parser.add_argument("num",help="The fibonacci number you wish to calculate",type=int) #add an argument and defines it

parser.add_argument("list",help="will enter number into list",type=int,nargs='+')

parser.add_argument("-o","--output",help="Opens a file and writes the result in it",action="store_true")

args = parser.parse_args()

result = fib(args.num)

print args.list

if args.verbose:	# here verbose is used to show a specific type of output
	print "Result is:", result
elif args.quite:	# here quite is used to show a specific type of output
	print result
else:
	print "fib(",args.num,") =",result

if args.output:
	f = open("fibonacci.txt", "a")
	f.write(str(result)+"\n")