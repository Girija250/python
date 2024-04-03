import math
num = float(input(" Enter a number: "))
sqRoot = math.pow(num, 0.5)
print("The square root of a given number {0} = {1}".format(num, sqRoot)) 



##using newton rahson method
def newtonsqrt(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    return approx
print(newtonsqrt(64))

















