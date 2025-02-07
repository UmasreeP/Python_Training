"""
How to add methods?

Requirement:
1. add method to store employee name
2. add method to get employee name
3. add method to store company name
4. add method to get company name
5. add method to check employee_name_startswith
6. add method to compute_average_salary
"""

print("Developing our own class")
print("-"*20)
# ---------------


class Employee:
    """
        Requirement:
        1. add method to store employee name
        2. add method to get employee name
        3. add method to store company name
        4. add method to get company name
        5. add method to check employee_name_startswith
        6. add method to compute_average_salary
    """
    # 1. add method to store employee name
    def store_employee_name(self, en):
        self.name = en

    # 2. add method to get employee name
    def get_employee_name(self):
        return self.name

    # 3. add method to store company name
    @classmethod
    def store_company_name(cls, cn):
        cls.company_name = cn

    # 4. add method to get company name
    @classmethod
    def get_company_name(cls):
        return cls.company_name

    # 5. add method to check employee_name_startswith
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

    # 6. add method to compute_average_salary
    # Requirement: If we pass 2 numbers, it should return average
    @staticmethod
    def compute_average_salary(sal1, sal2):
        return (sal1+sal2)/2

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

# CLASS OBJECT
# -------
Employee.store_company_name("XYZ Company")
# Object 'Employee' will be passed to 'cls'

e1.store_company_name("XYZ Company")
# @classmethod will take care of passing class objecy 'Employee' to 'cls'
# even if we call this method using e1, e2 etc
###########

# INSTANCE OBJECT: e1
# -------
e1.store_employee_name("emp-1")
# object 'e1' will be passed to 'self'

# THIS WILL BE ERROR: WE CAN'T CALL
# Employee.store_employee_name("emp-1")

# THIS WILL WORK
Employee.store_employee_name(e1, "emppppp-1") # self=e1, en="empppp-1"
###########

# INSTANCE OBJECT: e2
# -------
e2.store_employee_name("emp-2")
# object 'e2' will be passed to 'self'

# THIS WILL BE ERROR: WE CAN'T CALL
# Employee.store_employee_name("emp-2")

# THIS WILL WORK
Employee.store_employee_name(e2, "emppppp-2") # self=e2, en="empppp-2"
###########

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