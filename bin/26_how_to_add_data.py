"""
How to add data?

In this section,
1. CLASS VARIABLES
2. INSTANCE VARIABLES
"""

print("Defining our own class")
print("-"*20)
# ---------------


class Employee:
    pass


print("#"*40, end="\n\n")
###########################

print("Creating 2 objects")
print("-"*20)
# ---------------

e1 = Employee()
# This will create object and store in e1
e2 = Employee()
# This will create object and store in e2

print("#"*40, end="\n\n")
###########################

print("Total we have 3 objects")
print("-"*20)
# ---------------

# CLASS OBJECT: 'Employee' By default, AUTOMATICALLY, one object in the name of class
#           will be created.
# INSTANCE OBJECTS: e1 & e2 which we created

print("#"*40, end="\n\n")
###########################

print("Store the data")
print("-"*20)
# ---------------

Employee.company_name = "XYZ Company"
# It will create NEW variable 'company_name' inside object
#   then it will store the value
e1.name = "emp-1"
# It will create NEW variable 'name' inside object
#   then it will store the value
e2.name = "emp-2"
# It will create NEW variable 'name' inside object
#   then it will store the value

print("#"*40, end="\n\n")
###########################

print("DATA present in each object")
print("-"*20)
# ---------------

print("DATA present in class object 'Employee':", Employee.company_name)
print("DATA present in instance object 'e1':", e1.name)
print("DATA present in instance object 'e2':", e2.name)

print("#"*40, end="\n\n")
###########################

print("METHODS/VARIABLES present in each object")
print("-"*20)
# ---------------

print("METHODS/VARIABLES present in class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES present in instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES present in instance object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

# About CLASS object 'Employee':
# ---------------
# - CLASS object 'Employee' is common space for all objects
# - DATA which is common for all the objects, that data we can store
#   in class object
###########################