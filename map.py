# Python program to demonstrate working
# of map.

# Return double of n
import functools
def addition(n):
	return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = functools.map(addition, numbers)
print(list(result))

'''# import counter class from collections module
#from collections import Counter

# Creation of a Counter Class object using 
# string as an iterable data container
x = Counter("geeksforgeeks")

# printing the elements of counter object
for i in x.elements():
	print ( i, end = " ")'''
