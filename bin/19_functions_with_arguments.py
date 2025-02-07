"""
Here,
Case-2: How to pass values to variables present inside the function

3 ways to pass values to variables present inside the function
1-way: we can pass only values or in arg_name=value format
    Called POSITIONAL or KEYWORD argument function
2-way: we can RESTRICT to pass only values
    Called ONLY POSITIONAL argument function
3-way: we can RESTRICT to pass values in arg_name=value format
    Called KEYWORD argument function
"""

print("""
1-way: we can pass only values or in arg_name=value format
    Called POSITIONAL or KEYWORD argument function
""")
print("-"*20)
# ---------------

# name, company are called POSITIONAL or KEYWORD arguments
def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################

print("""
2-way: we can RESTRICT to pass only values
    Called ONLY POSITIONAL argument function
""")
print("-"*20)
# ---------------

# / -> is just syntax to tell only positional argument function
# / -> we are not counting this as argument
# / -> we are not passing any values to /

# name, company are called POSITIONAL arguments
''' Commenting this as I have a lower python version which doesn't support positional arguments
def employee(name, company, /):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# PASSING VALUES WILL WORK
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# USING ARGUMENT NAME WILL NOT WORK HERE
# received_value = employee(name="emp-1", company="comp-1")
# print("received_value:", received_value)
'''

print("#"*40, end="\n\n")
###########################

print("""
3-way: we can RESTRICT to pass values in arg_name=value format
    Called KEYWORD argument function
""")
print("-"*20)
# ---------------

# * -> is just syntax to tell only keyword argument function
# * -> we are not counting this as argument
# * -> we are not passing any values to *

# name, company are called KEYWORD arguments
def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# PASSING VALUES WILL NOT WORK HERE
# received_value = employee("emp-1", "comp-1")
# print("received_value:", received_value)

# USING ARGUMENT NAME IS MANDATORY HERE
received_value = employee(company="comp-1", name="emp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################