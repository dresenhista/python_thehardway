#Version3.0
#Changes: 
# -> perfect square works now
# -> prime list uses less memory
# -> list doesn't need to be sorted to use remove duplicates
# -> refactoring the code to make it more pythonic



#check if the number in a list is pair or even
def check_parity(x):
	for i in x:
		if i%2==0: # if the rest of the division is 0 then it's pair
			print "%r is pair" %i
		else:
			print "%r is even" %i




#check if the number is prime
def prime_numbers(l):
	
	for x in l:
		divisor = x-1
		multiple = [1, x] # every number is divided by 1 and itself
		while divisor >1:
			if x % divisor == 0: #if the number divides by any other 
				multiple.append(divisor)
				divisor = divisor-1
				break
			else:
				divisor = divisor-1
		if multiple==[1,x]:
			print "Number %r is prime" %x
		else:
			print "Number %r is not prime because it also divides by %r" %(x, multiple[2])
	return multiple



#removing duplicates in a list
def removing_duplicates(x):
	x.sort()
	lenght = len(x)
	newlist = []
	i=0
	while i<lenght:
		item = x[i] #hold the first item
		newlist.append(item)
		j=i+1
		while j<lenght:
			next_item = x[j] # loop around the list +1
			if item==next_item:
				i=i+1 # if it repeats than skip the next one
			j=j+1
		i=i+1
	print newlist
	return newlist
	


#check if the number is a perfect square
def perfect_square(x):
	impar = 0
	status = "Number %r is not perfect square." %x
	for i in range(1,x,2):
		impar += i
		if impar == x:
			status= "Number %r is a perfect square." %x
	print status

