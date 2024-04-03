file = open("C:\data.txt", "r")

# Read the content of file
data = file.read()

# Get the length of the data
number_of_characters = len(data)

print('Number of characters in text file :', number_of_characters)
