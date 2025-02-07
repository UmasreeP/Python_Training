"""
How to get or create objects
- Answer: Using CLASSES, we can create n number of objects

In this section,
1. CLASS OBJECT
2. INSTANCE OBJECTS
"""

print("Defining our own class")
print("-"*20)
# ---------------


class Employee:
    pass

# pass: This is DUMMPY keyword
# pass: to keep any block like if, for, while, function etc empty, we can pass

# Eventhough above class is empty,
#   -- we can create objects
#   -- we can store data

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


print("DATA present in each object")
print("-"*20)
# ---------------

print("DATA present in class object 'Employee':", Employee)
print("DATA present in instance object 'e1':", e1)
print("DATA present in instance object 'e2':", e2)

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

# About 'object' class
# ---------------
# - It is a MASTER class
# - It has basic methods like creating object, initializing object etc
# - By default, whatever there in object class will come to
#   each and every class which we create: INHERITANCE
#   OR
#   if we want say in other way,
#   all the classes are inherited from 'object' class
###########################