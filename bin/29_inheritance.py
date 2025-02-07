"""
Inheritance:
1. multilevel inheritance
2. multiple inheritance
"""

print("1. multilevel inheritance")
print("-"*20)
# ---------------


# Assume, Below class is already present
class Salary:
    def store_salary(self, sal):
        self.salary = sal
    def get_salary(self):
        return self.salary

# Client new requirement: Add below functionality to existing class
# 'Salary'
# 1. store_tax method
# 2. get_tax method
# 3. modify get_salary() method to return (salary-tax)
# 4. get_old_tax_scheme_salary

# New class 'Employee', inherited from 'Salary' class
# 'Employee' -> sub-class/child-class
# 'Salary' -> super-class/parent-class


class Employee(Salary):
    # 1. store_tax method
    def store_tax(self, tx):
        self.tax = tx

    # 2. get_tax method
    def get_tax(self):
        return self.tax

    # 3. modify get_salary() method to return (salary-tax)
    # POLYMORPHISM: WE can use same name as super class class method name
    def get_salary(self): # This will override superclass method
        return (self.salary - self.tax)

    # 4. get_old_tax_scheme_salary
    # Here, we need to access super class get_salary method
    def get_old_tax_scheme_salary(self):
        # 1-WAY
        sal = super().get_salary()
        # 2-WAY
        sal = Salary.get_salary(self)
        return sal

print("#"*40, end="\n\n")
###########################

print("Create objects and access the methods")
print("-"*20)
# ---------------

e1 = Employee()
e1.store_salary(20000)
e1.store_tax(2000)


print("Salary:", e1.get_salary())
print("Tax:", e1.get_tax())
print("Old Salary:", e1.get_old_tax_scheme_salary())

print("#"*40, end="\n\n")
###########################

print("1. multilevel inheritance: Method Resolution Order")
print("Other way: In what sequence, it will look for methods")
print("-"*20)
# ---------------

print(Employee.mro())

print("#"*40, end="\n\n")
###########################

print("2. multiple inheritance: Method Resolution Order")
print("Other way: In what sequence, it will look for methods")
print("-"*20)
# ---------------

class A:
    pass

class B:
    pass

class C(A,B):
    pass

print(C.mro())

print("#"*40, end="\n\n")
###########################