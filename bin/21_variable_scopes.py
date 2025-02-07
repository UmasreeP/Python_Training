"""
4 Scopes
Scope-1: Local Scope
Scope-2: Enclosed Scope
Scope-3: Global Scope

Scope-4: Builtin Scope :
    - If no where that name/variable found in the file,
     then it will go and check in builtins
"""

print("Scope-1: Local Scope")
print("-"*20)
# ---------------

def my_function():
    x = 100 # Local variable, We can't access outside the function
    print("Inside function, value of x:", x)

my_function()


print("#"*40, end="\n\n")
###########################

