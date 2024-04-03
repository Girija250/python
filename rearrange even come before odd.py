def rearrange_even_odd(nums):
    nums.sort(key=lambda x: x % 2)
    return nums

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rearranged_numbers = rearrange_even_odd(numbers)
print(rearranged_numbers)
