height=int(input("Enter the height in cm"))
if (height < 150.0):
    print("Dwarf \n");
elif((height >= 150.0)and(height <= 165.0)):
    print(" Average Height \n")
elif((height > 165.0)and(height <= 195.0)):
    print("Taller \n")
else:
    print("Abnormal height \n")
