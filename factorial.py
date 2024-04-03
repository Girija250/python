'''def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num =2
result = factorial(num)
print("The factorial of", num, "is", result)
##using for loop
# Python Program to find the factors of a number

# This function computes the factor of the argument passed'''
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num =6

print_factors(num)
