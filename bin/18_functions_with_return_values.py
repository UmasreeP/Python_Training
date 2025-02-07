"""
2 cases
Case-1: How to access values outside the function
Case-2: How to pass values to variables present inside the function

Here,
Case-1: How to access values outside the function
"""

print("Function with 1 return values")
print("-"*20)
# ---------------

# 2 Steps we need to follow
# Step-1: use 'return' statement inside function to specify values
# Step-2: Assign function call to some variable to receive return value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1: use 'return' statement inside function to specify values
    return name


# Step-2: Assign function call to some variable to receive return value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################

print("Function with more than 1 return values: TUPLE")
print("-"*20)
# ---------------

# 2 Steps we need to follow
# Step-1: use 'return' statement inside function to specify values
# Step-2: Assign function call to some variable to receive return value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1: use 'return' statement inside function to specify values
    return (name, company)


# Step-2: Assign function call to some variable to receive return value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################

print("Function with more than 1 return values: LIST")
print("-"*20)
# ---------------

# 2 Steps we need to follow
# Step-1: use 'return' statement inside function to specify values
# Step-2: Assign function call to some variable to receive return value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1: use 'return' statement inside function to specify values
    return [name, company]


# Step-2: Assign function call to some variable to receive return value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################

print("Function with more than 1 return values: DICTIONARY")
print("-"*20)
# ---------------

# 2 Steps we need to follow
# Step-1: use 'return' statement inside function to specify values
# Step-2: Assign function call to some variable to receive return value

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1: use 'return' statement inside function to specify values
    return {"name": name, "company": company}

# Step-2: Assign function call to some variable to receive return value
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################