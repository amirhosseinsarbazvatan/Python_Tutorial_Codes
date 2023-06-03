# Random module in python

# Generate random numbers

# Generate random number from 0 to 1
import random
print(random.random())

# Generate random float number from 0 to 10(specific number)
import random
print(random.uniform(0,10))

# Generate random integer number from 0 to 10(specific number)
import random
print(random.randrange(0,10))

# Choice a number from a list of numbers
import random
print(random.choice([1,4,6,8,2,43,12,61,0,2,8,31]))

# Shuffle a list of numbers and change index ofitems 
import random
mylist = [4,8,1,3]
random.shuffle(mylist)
print(mylist)

# Select a sample of list
import random
print(random.sample([1,4,6,8,2,43,12,61,0,2,8,31],3))