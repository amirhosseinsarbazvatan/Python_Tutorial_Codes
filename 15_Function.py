# Function in python 

# A function is a block of code which only runs when it is called
# In Python a function is defined using the def keyword

# Function samples:

# Print a number Function

def number():
    print(100)

number()


############################

# Counting Function

def counting(p):
    for i in range(0,p):
        print(i)

counting(12)

############################

# Print statement function

def print_str(name,age):
    print("Name: " + name + "\n" + "Age: " + str(age))

print_str("Amirhossein",12)


############################

# SQRT function
from math import *      # Import math library

def sqrt_func(n):
    return sqrt(n)      # Return just applicable in function and usable for return somethings after run function

print(sqrt_func(4))


############################


# Maximum Function

def max(x,y):
    if x>y:
        print(str(x) + " is gratter than "+ str(y))
    elif x<y:
        print(str(x) + " is lower than " + str(y))
    else:
        print(str(x)+ " is equal to " + str(y))

print("Maximum identifier betwwen two numbers")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

max(num1,num2)
