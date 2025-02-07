"""
Functions: If we want to rewrite/copy-paste same code more than one time
then
instead of rewrite/copy-paste, put that code in a block and reuse
"""

print("WITHOUT using function(rewrite/copy-paste)")
print("-"*20)
# ---------------

a = 10
b = 20
c = a + b
print("Value of c:", c)

a = 10
b = 20
c = a + b
print("Value of c:", c)

a = 10
b = 20
c = a + b
print("Value of c:", c)

a = 10
b = 20
c = a + b
print("Value of c:", c)

a = 10
b = 20
c = a + b
print("Value of c:", c)

print("#"*40, end="\n\n")
###########################

print("USING function(code reusability)")
print("-"*20)
# ---------------


# Function Definition
def my_function():
    a = 10
    b = 20
    c = a + b
    print("Value of c:", c)


my_function()
my_function()
my_function()
my_function()
my_function()

print("#"*40, end="\n\n")
###########################