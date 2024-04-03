from functools import reduce

def longest_word_length(sentence):
    words = sentence.split()
    return reduce(lambda x, y: x if len(x) > len(y) else y, words)

sentence = input("Enter a sentence: ")
longest_word = longest_word_length(sentence)
print("Length of the longest word:", len(longest_word))
