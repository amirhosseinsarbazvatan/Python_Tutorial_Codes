# Work with files in python


# For write path in python use two tupes:
# Raw string => r"C:\Users\pc\Desktop\test.txt"
# Two slash => "C:\\Users\\pc\\Desktop\\test.txt"


# Read, write and modify files in python

# Read file 
with open(r"C:\Users\pc\Desktop\test.txt", encoding="utf-8", mode="r") as file:     # with open(path,encoding,mode)
    print(file.read())
    file.close()        # Close file 


# Write file
with open(r"C:\Users\pc\Desktop\test.txt", encoding="utf-8", mode="w") as file:     
    file.write("Java")      # Clear file and write new content
    file.close()   


# Append file
with open(r"C:\Users\pc\Desktop\test.txt", encoding="utf-8", mode="a") as file:     
    file.write("\t Python is simple!")      # Clear file and write new content
    file.close() 


with open(r"C:\Users\pc\Desktop\test.txt", encoding="utf-8", mode="r") as file:     
    print(file.read())
    file.close()        