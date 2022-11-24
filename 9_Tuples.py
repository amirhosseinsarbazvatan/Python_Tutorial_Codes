# Tuples in python


# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable


my_tuple = (1,2,3,4,5,6)
print(my_tuple)
print(type(my_tuple))   # Identify type of tuple

print(my_tuple[2])      # Return value in tuple by index


# Length of tuple
print(len(my_tuple))

# Join and repeat tuples
tuple1 = (1,2,3)
tuple2 =  ("Hello" , "Blue" , 10)

print(tuple1+tuple2)        # + => join
print(tuple1*3)             # * => repeat

# Create Tuple With One Item(just with comma in last item)
one_tuple = (1,)