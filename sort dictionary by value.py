my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'kiwi': 3}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by values:")
print(sorted_dict)
