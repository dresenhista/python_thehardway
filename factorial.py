def factorial(x):
	
	if x<0:
		print "Factorial can't be calculated for negative numbers."
	elif x==0:
		print "0"
	else:
		factorial = x	
		while x>1:
			x = x-1
			factorial = x*factorial
	print factorial
	return factorial

number = raw_input("> ")
number = int(number)
factorial(number)