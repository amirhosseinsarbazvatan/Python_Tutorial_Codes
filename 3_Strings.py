# String in python


# Define string value and print it
x = "Hello word"
print(x)

# Ignore a string or statement as comment(#,''' ''')
# This is a comment
''' this is a comment '''

str = "hello"

# String methods

# Capitalize first character
print(str.capitalize())

# Uppercase all characteries
print(str.upper())

# Lowercase all characteries
print(str.lower())

# Find a character index in string
print(str.find("o"))

# Replace new string to old one
print(str.replace("Hello" , "Hi"))
print(str)

# Center justify
print(str.center(10, "-"))

# Right justify
print(str.rjust(2,"."))

# Left justify
print(str.ljust(2,"."))

# Remove space in first and last of string
str1 = "      World"
print(str1.strip())

# Ends with a specific character(True|False)
print(str.endswith("o"))

# Start with a specific character(True|False)
print(str.startswith("o"))

# All string must be String
print(str.isalpha())

# All string must be numbers
print(str.isdigit())



# Scape Characters

# \t => tab
# \n => next line


