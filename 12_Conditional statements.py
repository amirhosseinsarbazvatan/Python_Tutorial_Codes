# Conditional statements in python


# Conditions can be used in several ways, most commonly in "if statements" and loops
# Result of conditions will be True|False

# If condition samples:


if 1 == 1:
    print("1==1 is True")

############################

if 10 > 5:
    print("Yes")

############################

my_list = [1,2,3,4]
if 5 in my_list:
    print("Correct")        # Don't have any result because condition is False

############################

# Else : The else keyword catches anything which isn't caught by the preceding conditions

my_list = [1,2,3,4]
if 5 in my_list:
    print("Correct") 
else:
    print("Not found!")


# Elif : The elif keyword is pythons way of saying, if the previous conditions were not true, then try this condition

x = 6
y = 4

if x > y:
    print(str(x) + " is gratter")
elif x < y:
    print(str(y) + " is gratter")
else:
    print("equal")
