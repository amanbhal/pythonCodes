# A is an integer between 1 to 3999

def intToRoman(A):
	roman = ""
	divisors = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
	print sorted(divisors.keys(),reverse=True)
	for key in sorted(divisors.keys(),reverse=True):
		while (A > 0):
			if(A/key >= 1):
				roman += divisors[key]
				A -= key
			else:
				break
	return roman
		
print intToRoman(919)