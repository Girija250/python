def sum(x,y):
     if(y==0):
        return x;
     else:
        return(1+sum(x,y-1));
x=20
y=10
print("Sum of two numbers are: ",sum(x,y))
