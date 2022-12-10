# Lists in python


# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary
# List items are ordered, changeable, and allow duplicate values

mylist = [1,2,3,4]
print(mylist)

string_list = ["python","java","javascript","C++"]
print(string_list)

# Return item in list by index
print(mylist[0])             # Return first item in list

print(string_list[1])        # Return second item in list

# Replace items in list 
nums = [7,5,3,1]
nums[2]=60
print(nums)

# Concatenation and Repeat in lists
print(nums + [77,88,99])    

print([1,2,3] * 3)

# Membershipment in list
names = ["Jack", "Marry", "Patrik"]
print("Jack" in names)
print("Sum" in names)

# Append method in list
num1 = [1,2,3,4]
num1.append(5)
print(num1)

# Insert method in list
num1.insert(1,6)      # insert(index,value)
print(num1)

# Len method in list
print(len(num1))

# Count method in list
print(num1.count(1))      

# Index method in list
n = ["a" , "b" , "c" , "d"]
print(n.index("b"))

# Extend method in list
n = ["a" , "b" , "c" , "d"]
print(n.extend([11,12,13,14]))

# Reverse method in list
num2 = [1,2,3,4]
print(num2.reverse())

# Remove/POP method in list
num2 = [1,2,3,4]
num2.remove(2)      # remove(value)     => Remove base on value in list
num2.pop(0)         # pop(index)        => Remove base on list item index
print(num2)
