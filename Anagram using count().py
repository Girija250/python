from collections import Counter

def are_anagrams(str1, str2):
    # Count occurrences of each character in both strings
    count_str1 = Counter(str1)
    count_str2 = Counter(str2)
    
    # Check if the counts of characters are the same
    return count_str1 == count_str2

# Example usage:
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
