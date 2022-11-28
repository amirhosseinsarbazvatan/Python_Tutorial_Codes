# Lambda in python

# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression


x = lambda x : x + 10                 # With same variable name 
print(x(5))


x = lambda n : n + 10                 # With different variable name 
print(x(5))


multiply = lambda a,b : a*b           # Use lambda in any math operations 
print(multiply(4,2))


sum = lambda a,b,c : a+b+c            # No limitation for arguments
print(sum(2,5,7))


sum = lambda a,b,c : a**2 * (b/c)     # Use lambda in mathematical expressions(Polynomials) 
print(sum(2,5,7))


def my_function(n):                    # Use lambda in function 
    return lambda a : a * n

result = my_function(2)

print(result(11))