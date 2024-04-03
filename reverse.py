num =int(input("Enter the number"))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

#string
def reverse(string):
    string = [string[i] for i in range(len(string)-1, -1, -1)]
    return "".join(string)
 
s = "Geeksforgeeks"
 
print("The original string  is : ", s)
 
print("The reversed string(using reversed) is : ", reverse(s))
