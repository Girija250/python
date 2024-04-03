max=int(input(" Please Enter the Maximum Value : "))
even_sum= 0
odd_sum= 0
 
for num in range(1,max+1):
    if(num%2==0):
        even_sum= even_sum+num
    else:
        odd_sum= odd_sum+num
 
print("The Sum of Even Numbers from 1 to {0} = {1}".format(num,even_sum))
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(num,odd_sum))
