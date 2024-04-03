nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12, 13]
]
max_sublist = max(nested_list, key=lambda sublist: max(sublist))
sum_max_sublist = sum(max_sublist)

print("Nested List:", nested_list)
print("Sublist with largest element:", max_sublist)
print("Sum of the sublist with largest element:", sum_max_sublist)
