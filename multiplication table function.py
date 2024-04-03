def print_table(num): 
    for i in range(1,11): 
        print(num,' x ', i, ' = ',num*i) 
num = int(input("Please Enter a number to print its multiplication table:"))
print_table(num)
