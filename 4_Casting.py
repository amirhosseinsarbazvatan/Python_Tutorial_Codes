# Cast a value in python


# Casting means Convert type of value to another type

f = 12.5
print(int(f))         # int(float) => integer result (12)

i = 12
print(float(i))       # float(int) => float result (12.0)


num = 12
print(str(num))       # str(numeric value) => string result

x = 5
# print(x + "_")        # This statement make error because x is not a string and can't merge with a string, Now use casting for solve it:
print(str(x) + "_")