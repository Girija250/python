number = input("Enter a series of numbers: ")
even_sum = 0
for element in number:
    if int(element) % 2 == 0:
        even_sum += int(element)
print("Sum of even digits: " + str(even_sum))
