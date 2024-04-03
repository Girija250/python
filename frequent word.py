from collections import defaultdict
string="python is best for coders", "python is fun", "python is easy to learn"
print("The string is :")
print(string)

my_temp = defaultdict(int)

for sub in string:
   for word in sub.split():
      my_temp[word] += 1

result = max(my_temp, key=my_temp.get)

print("The word that has the maximum frequency :")
print(result)
