def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = sum(map(lambda char: 1 if char in vowels else 0, string))
    return count

input_string = input("Enter a string: ")
print("Number of vowels:", count_vowels(input_string))
