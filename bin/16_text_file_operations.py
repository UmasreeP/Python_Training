"""
Read/Write with text files like .txt, .log etc
"""

"""
We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect
"""

"""
We have functions for all 3 steps
Step-1: Connect to file
    - open() function
Step-2: Read/Write
    - FOR WRITING: 1) write 2) writelines 3) print-function
    - FOR READING: 1) read 2) readlines 3) readline
Step-3: Disconnect
    - close()
"""

print("All write operations")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
# my_out_file_handle = open("provide file name or file path here", "provide mode here")
my_out_file_handle = open("my_out_file.txt", "w")
# mode 'w': Write Only, It will create new file, it will ERASE the existing content
# mode 'r': Read Only, It will NOT create new file
# mode 'a': Append Only, It will create new file only if it is not present

# Step-2: Write
# ---------------
# Our Data
x = 10
y = "python"

# 1) write -> it will take only one string
my_out_file_handle.write(str(x)+"\n")
my_out_file_handle.write(y+"\n")

# 2) writelines -> it takes collection of values like list/tuple etc
my_data_in_list = [str(x)+"\n", y+"\n"]
my_out_file_handle.writelines(my_data_in_list)

# 3) print-function
print(x, y, 20, "java", sep="\n" ,file=my_out_file_handle) # this will write to file
# Here no need of converting to string

# Step-3: Disconnect
# ---------------
my_out_file_handle.close()

print("""
All write operations are completed.
Please check 'my_out_file.txt'
""")

print("#"*40, end="\n\n")
###########################

print("Reading from my_out_file.txt file using 'read()'")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# ---------------
file_content = my_file_handle.read()
# read() will return entire file content in ONE string
print("file_content:", file_content, end="\n\n")
print("file_content in RAW FORMAT:", repr(file_content), end="\n\n")

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
###########################

print("Reading from my_out_file.txt file using 'readlines()'")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# ---------------
file_content = my_file_handle.readlines()
# readlines() will return entire file content in list
print("file_content:", file_content, end="\n\n")


# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
###########################

print("Reading from my_out_file.txt file using 'readline()'")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# ---------------
file_content = my_file_handle.readline()
# readline() will return one line
print("file_content:", file_content, end="\n\n")


# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
###########################

print("Reading from my_out_file.txt file using 'read line by line using for-loop'")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# ---------------
for each_line in my_file_handle:
    print("Each Line:", each_line)

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
###########################