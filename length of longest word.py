def largestWord(s):
    # Sort the words in increasing
    # order of their lengths
    s = sorted(s, key = len)
    # Print last word
    print(s[-1])
if __name__ == "__main__":
    s=input("Enter the string: ") 
 
    # Split the string into words
    l = list(s.split(" "))
 
    largestWord(l)
