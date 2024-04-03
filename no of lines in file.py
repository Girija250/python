
with open('tutebox.txt','r') as file:
   cnt = 0
   for line in file: 
      cnt += 1
print(f"The counting of number of lines is: {cnt}")
