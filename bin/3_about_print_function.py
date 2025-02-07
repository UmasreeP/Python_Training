"""
About 'print' function
"""

print("print function with 'sep' argument")
print("-"*20)
# ---------------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d) # By Default, In output, it will print each value separated by space
print(a, b, c, d, sep="\t\t")
print(a, b, c, d, sep="XYZ")

print("#"*40, end="\n\n")
###########################


print("print function with 'end' argument")
print("-"*20)
# ---------------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d) # Default end="\n", Which means in output, after printing all the values, put \n
print(a, b, c, d, end="\n\n")
print(a, b, c, d, end="\n")
print(a, b, c, d, end="XYZ\n")

# We can also pass 'file' parameter to print-function
# - this we will discuss during file operations

print("#"*40, end="\n\n")
###########################