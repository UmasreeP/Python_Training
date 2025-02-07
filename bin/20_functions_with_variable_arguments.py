"""
Functions with Variable Arguments
1. Functions with Variable POSITIONAL Arguments
2. Functions with Variable KEYWORD Arguments
"""

print("1. Functions with Variable POSITIONAL Arguments")
print("-"*20)
# ---------------

def add(*a):
    print("Received All Values In Tuple:", a)

add()
add(10)
add(10, 20, 30, 40, 50, 60)

print("#"*40, end="\n\n")
###########################

print("2. Functions with Variable KEYWORD Arguments")
print("-"*20)
# ---------------

def employee_profile(**employee_details):
    print("Received all values in dictionary:", employee_details)


employee_profile()
employee_profile(name="emp-1")
employee_profile(name="emp-2", email="a@b.com")
employee_profile(name="emp-3", email="c@d.com", phone="1111111")

print("#"*40, end="\n\n")
###########################

print("Functions with list/dictionary args")
print("-"*20)
# ---------------

def add(a, b):
    print("Value of a:", a)
    print("Value of b:", b)
    return a, b


L = [10, 20]
D = {"A":10, "B":20}
received_values = add(L,D)
print("received values are: ", received_values)

print("#"*40, end="\n\n")
###########################