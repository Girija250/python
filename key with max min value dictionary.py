my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'kiwi': 3}
max_key = max(my_dict, key=my_dict.get)
min_key = min(my_dict, key=my_dict.get)
print("Key with maximum value:", max_key)
print("Key with minimum value:", min_key)
