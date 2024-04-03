my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'kiwi': 3}
key_to_remove = 'banana'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print("Key", key_to_remove, "removed from the dictionary.")
else:
    print("Key", key_to_remove, "not found in the dictionary.")
print("Updated dictionary:", my_dict)
