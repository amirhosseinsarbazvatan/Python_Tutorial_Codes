# OS module in python

# Operating system functions in python

# Display operating system name
import os
print(os.name)      # nt is equal to windows

# Run a file in os like open an image
import os
os.system(r"C:\Users\pc\Desktop\image.jpg")

# Generate a real random number 
import os
os.urandom(10)

# Run anythings in os like run a application and software
import os
os.startfile(r"C:\Users\pc\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code")

# Get current directory
import os 
print(os.getcwd())

# Get list of contents in directory
import os
print(os.listdir(r"C:\Users\pc\Desktop\Python_Code"))
print(os.listdir("."))      # Get current directory

# Change directory
import os
os.chdir(r"C:\Users\pc\Desktop\Python_Code\New Folder")

# Get information about a directory or file
import os
print(os.stat(r"C:\Users\pc\Desktop\Python_Code"))

# Get created time of directory or file
import os 
print(os.path.getctime(r"C:\Users\pc\Desktop\Python_Code"))

# Get accessed time of directory or file
import os 
print(os.path.getatime(r"C:\Users\pc\Desktop\Python_Code"))

# Get modified time of directory or file
import os 
print(os.path.getmtime(r"C:\Users\pc\Desktop\Python_Code"))

# Get created time of directory or file by datetime and readable format
import os
import datetime
print(datetime.datetime.fromtimestamp(os.path.getctime(r"C:\Users\pc\Desktop\Python_Code")))

# Get accessed time of directory or file by datetime and readable format
import os
import datetime
print(datetime.datetime.fromtimestamp(os.path.getctime(r"C:\Users\pc\Desktop\Python_Code")))

# Get modified time of directory or file by datetime and readable format
import os
import datetime
print(datetime.datetime.fromtimestamp(os.path.getctime(r"C:\Users\pc\Desktop\Python_Code")))

# Exist a file or directory in os (True | False)
import os 
print(os.path.exists(r"C:\Users\pc\Desktop\Python_Code"))

# Is directory? (True | False)
import os 
print(os.path.isdir(r"C:\Users\pc\Desktop\Python_Code"))

# Is file? (True | False)
import os 
print(os.path.isfile(r"C:\Users\pc\Desktop\Python_Code"))

# Get real path of file or directory
import os 
print(os.path.realpath(r"C:\Users\pc\Desktop\Python_Code"))

# Get absolute path of file or directory
import os 
print(os.path.abspath(r"C:\Users\pc\Desktop\Python_Code"))

# Create all intermediate-level directories
import os
os.makedirs(r"C:\Users\pc\Desktop\Python_Code\new\test")

# Create a directory
import os
os.mkdir(r"C:\Users\pc\Desktop\Python_Code1")

# Remove all intermediate-level directories
import os
os.removedirs(r"C:\Users\pc\Desktop\Python_Code\new\test")

# Remove a directory
import os
os.rmdir(r"C:\Users\pc\Desktop\New Folder(11)")


# Two exercises for os module 

# 1 : Classify directory and files in a path
import os
for item in os.listdir(r"C:\Users\pc\Desktop\Python_Code"):
    if os.path.isfile(item):
        print(item + " is File")
    elif os.path.isdir(item):
        print(item + "is Dirtectory")


# 2 : Get comprehensive information about a file or directory with best format 
import os, datetime
print("Item exists: " + str(os.path.exists(r"C:\Users\pc\Desktop\Python_Code\24_OS module.py")))
print("Item is a file: " + str(os.path.isfile(r"C:\Users\pc\Desktop\Python_Code\24_OS module.py")))
print("Item is a directory: " + str(os.path.isdir(r"C:\Users\pc\Desktop\Python_Code\24_OS module.py")))
print("Item path: " + str(os.path.realpath(r"C:\Users\pc\Desktop\Python_Code\24_OS module.py")))
print("Item path and name: " + str(os.path.split(os.path.realpath(r"C:\Users\pc\Desktop\Python_Code\24_OS module.py"))))
print("Item created: " + str(datetime.datetime.fromtimestamp(os.path.getctime(r"C:\Users\pc\Desktop\Python_Code\24_OS module.py"))))
print("Item last accessed: " + str(datetime.datetime.fromtimestamp(os.path.getatime(r"C:\Users\pc\Desktop\Python_Code\24_OS module.py"))))
print("Item last modified: " + str(datetime.datetime.fromtimestamp(os.path.getmtime(r"C:\Users\pc\Desktop\Python_Code\24_OS module.py"))))