def vowelConsonant(string):
   if not string.isalpha():
      return 'Neither'
   if string.lower() in 'aeiou':
      return 'Vowel'
   else:
      return 'Consonant'
string = input('Enter any string: ')
for ch in string:
   print(ch,'is',vowelConsonant(ch),end=', ')
