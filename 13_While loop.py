# While loop in python

# Loop is a tool for repeat a procedure 
# While is a loop in python

x = 1
while x < 10:
    print(x)    
    x = x+1


x = 1
while x < 5:
    print("Python")    
    x = x+1


n = 1
while n < 5:
    print(str(n)+")"+"World")
    n = n+1

# Calculate sqrt a set of numbers with while loop
from math import *
y = 0
while y < 10:
    print(y , "\t" , sqrt(y))
    y = y + 1 


# Break => stop loop
x = 1
while x < 10:
    print(x)    
    x = x+1
    if x == 5:      # Loop break when counter reach 4
        break
    
# Continue => skip a step in loop
x = 1
while x < 10:
    print(x)    
    x = x+1
    if x == 5:      # Loop skip 5 and go on
        continue