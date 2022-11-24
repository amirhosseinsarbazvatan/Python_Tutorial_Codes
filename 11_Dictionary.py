# Dictionary in python

# Dictionaries are used to store data values in key:value pairs
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates

my_dict = {"Pen" : 3, "Eraser" : 5, "Pencil" : 1 , "Notebook" : 10}
print(my_dict)         
print(type(my_dict))   


# Empty dictionary
dict_empty = {}

# Construct a dict
dict_new = {}
dict_new["a"] = 1
dict_new["b"] = 2
dict_new["c"] = 3
dict_new["d"] = 4

print(dict_new)

# Delete dictionary
del dict_new

# Length method in dictionary
print(len(my_dict))     # Show number of key-values in dictionary

# Show all keys in dictionary
print(my_dict.keys())

# Show all keys in dictionary
print(my_dict.values())

# Show all items(keys,values) in dictionary
print(my_dict.items())

# Exist or not exist a key in dictionary
print(my_dict.__contains__("Pen"))      # The result will be True | False  