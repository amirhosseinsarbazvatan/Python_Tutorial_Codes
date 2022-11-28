# Exception handling in python

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
  print(x)                          # x variable not defined and error occured
except:
  print("An exception occurred")    # Print specific statement instead of error alert



try:
    x=10
    y=0
    print(x/y)                      # Numbers can not divided by zero
except ZeroDivisionError:           # Except specific error for exception
    print("Divided by zero!")



try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
finally:
    print("Finally run")            # Finally run anyway


# Use Try/Except in simple mathematic operation 

def divide():
  try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(x/y)
  except ZeroDivisionError:
    print("Divided by zero!!!")
  finally:
    divide()

divide()
