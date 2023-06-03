# Datetime module in python

# Time and Date functions in python

# Display current date and time
import datetime
print(datetime.datetime.now())

# Display current day of week
import datetime
print(datetime.datetime.now().strftime("%A"))
print(datetime.datetime.now().strftime("%a"))

# Display current month
import datetime
print(datetime.datetime.now().strftime("%B"))
print(datetime.datetime.now().strftime("%b"))

# Display current year
import datetime
print(datetime.datetime.now().strftime("%Y"))
print(datetime.datetime.now().strftime("%y"))

# Display current time and hour
import datetime
print(datetime.datetime.now().strftime("%r"))

# Display current date
import datetime
print(datetime.datetime.now().strftime("%x"))