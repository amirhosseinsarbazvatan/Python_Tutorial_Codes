# Sets in python

# Sets are used to store multiple items in a single variable
# A set is a collection which is unordered and unindexed

my_set = {1,2,3,4}
print(my_set)         # Each time print a set, set show items with defferent indexes (Sets is unordered)
print(type(my_set))   # Identify type of set

# Empty set
set_empty = ()

# Length of set
print(len(my_set))

# Add method in set
my_set.add(12)
print(my_set)


# Update method in set
my_set.update({21,14,15,12})
print(my_set)       # Don't add 12 beacause this item exists in set(not unique)



# Discard, Remove, and POP methods in set
my_set.pop()        
print(my_set)       # Remove first item 

my_set.remove(3)
print(my_set)       # Remove current item

my_set.discard(12)
print(my_set)       # Remove current item


# Membershipment in set
set_countries = {"Germany", "UAE" , "India", "Netherland"}
print("Spain" in set_countries)     # Return True | False
print("India" in set_countries)


# Sets in math

# Union
set_number1 = {1,2,3,4,5}   
set_number2 = {3,4,5,6,7}
print(set_number1.union(set_number2))

# Intersection
print(set_number1.intersection(set_number2))

# Differnce
print(set_number1.difference(set_number2))

# Symmetric_difference
print(set_number1.symmetric_difference(set_number2))
