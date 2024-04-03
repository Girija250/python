size=int(input("Enter the no of rows: "))
for i in range(1,size+1):
    print(("*"*(2*i-1)).center(2*size-1))
for i in range(size-1,0,-1):
    print(("*"*(2*i-1)).center(2*size-1))
