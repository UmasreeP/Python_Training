"""
Overriding 'object' class(super-class) methods

Constructor: __new__
Initializer: __init__
When we create object, both methods will execute

Case-1
Here, We are planning OVERRIDE __init__ method to store employee name

Case-2
Also trying, directly declaring variables inside the class
"""

print("Developing our own class")
print("-"*20)
# ---------------


class Employee:
    """
        Case-1
        Here, We are planning OVERRIDE __init__ method to store employee name

        Case-2
        Also trying, directly declaring variables inside the class

    """
    # Case-1
    # Here, We are planning OVERRIDE __init__ method to store employee name
    def __init__(self, en):
        self.name = en

    # Case-2
    # Also trying, directly declaring variables inside the class
    company_name = "XYZ Company"

    def get_employee_name(self):
        return self.name

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    def employee_name_startswith(self, prefix):
        # 1-WAY
        employee_name = self.name
        # OR
        # 2-WAY
        employee_name = self.get_employee_name()
        # employee_name -> string
        if employee_name.startswith(prefix):
            return True
        else:
            return False

    @staticmethod
    def compute_average_salary(sal1, sal2):
        return (sal1+sal2)/2

print("#"*40, end="\n\n")
###########################

print("Creating 2 objects")
print("-"*20)
# ---------------

e1 = Employee("emp-1") # call __init__
# This will create object and store in e1
e2 = Employee("emp-2") # call __init__
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

print("DATA present in class object 'Employee':", Employee.get_company_name())
# object 'Employee' will be passed to 'cls'
print("DATA present in instance object 'e1':", e1.get_employee_name())
# object 'e1' will be passed to 'self'
print("DATA present in instance object 'e2':", e2.get_employee_name())
# object 'e1' will be passed to 'self'

print("Employee-1 name startswith 'emp':", e1.employee_name_startswith("emp"))
# object 'e1' will be passed to 'self', "emp"

s1 = 10000
s2 = 20000
avg_salary = e1.compute_average_salary(s1, s2) # THIS WILL WORK
# OR
avg_salary = Employee.compute_average_salary(s1, s2) # THIS WILL ALSO WORK
# for CLASS METHOD: object 'Employee' will be passed to 'cls'
# for INSTANCE METHOD: object 'e1' or 'e2' will be passed to 'self'
# for STATIC METHOD: NO object will be passed internally,
#       only whatever we are passing, that will be passed to method

print("avg_salary:", avg_salary)

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