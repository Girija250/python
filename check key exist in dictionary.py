my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'kiwi': 3}
value_to_check = 8
if value_to_check in my_dict.values():
    print("The value", value_to_check, "exists in the dictionary.")
else:
    print("The value", value_to_check, "does not exist in the dictionary.")
