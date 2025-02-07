"""
Here,
Scope-2: Enclosed Scope
"""

print("Scope-2: Enclosed Scope: CASE-1")
print("-"*20)
# ---------------


def my_function_1():
    x = 100 # Enclosed Scope: Current function and Nested functions can access

    def my_function_2():
        print("In function_2, accessing function_1 variable x and its value:", x) # 100

    my_function_2()
    print("In function_1, variable x value:", x) # 100


my_function_1()


print("#"*40, end="\n\n")
###########################

print("Scope-2: Enclosed Scope: CASE-2")
print("-"*20)
# ---------------


def my_function_1():

    x = 100 # Enclosed Scope: Current function and Nested functions can access

    def my_function_2():
        # x = 2000 # It will create local variable
        nonlocal x # This will refer enclosed scope variable
        x = 1000 # This will change value of enclosed scope variable
        print("In function_2, accessing function_1 variable x and its value:", x) # 1000


    my_function_2()
    print("In function_1, variable x value:", x)  # 1000


my_function_1()


print("#"*40, end="\n\n")
###########################