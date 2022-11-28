# For loop in python

# Loop is a tool for repeat a procedure 
# For is a loop in python


# Range method return numbers in a period => range(min,max,step)
# Now use range in for loop

for i in range(1,10):       # From 1 to 9 (n-1)
    print(i)

for n in range(11):         # Put one argument in range method means value is max and min is default 0
    print(n)

for m in range(1,10,2):     # Step is jump next number 
    print(m)

mylist = [1,2,3,4,5,6]
for i in mylist:            # For loop can read each items in list
    print(i)


str = "Hello world"
for s in range(5):          # Five times print "Hello world"
    print(str)


text = "Python"
for st in range(5):
    print(text + "!")      # Add a character(!) to string in each loop


# calculate sum of list numbers with for loop

sum = 0
for item in [2,4,8,1,3]:
    sum += item

print(sum)

# calculate multiplication of list numbers with for loop

multiply = 1
for item in [3,4,2]:
    multiply *= item

print(multiply)
