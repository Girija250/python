import math
def pascaltriangle(rows):
  for i in range(rows):
    print(" "*(rows-i-1)+ " ".join(str(math.comb(i,j)) for j in range(i+1)))
rows=int(input("Enter rows:"))
pascaltriangle(rows)
    
