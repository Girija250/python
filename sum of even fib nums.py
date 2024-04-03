a = 1
b = 1
c = 0
Sum = 0
while c<50:
    c = a + b
    if c%2==0:
        Sum+=c
    a = b
    b = c
print(Sum)
