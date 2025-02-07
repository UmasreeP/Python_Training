"""
Write new class called ‘NewEmployeeClass’ which is inheriting from ‘EmployeeClass’ and provide below functionality.
1)	Add 2 instance-methods to set and get tax
2)	Override get_emp_salary method to return (salary-tax)
3)	Also write one more method called get_old_salary where inside this method,
try to access super class method ‘get_emp_salary’ and return the super class method returned value.

"""

class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    def get_emp_name(self):
        return self.emp_name

    def get_emp_id(self):
        return self.emp_id

    def get_emp_salary(self):
        return self.emp_salary


class NewEmployeeClass(EmployeeClass):  # New class inheriting from EmployeeClass
    def __init__(self, emp_name, emp_id, emp_salary):
        super().__init__(emp_name, emp_id, emp_salary)  # Call superclass constructor
        self.tax = 0  # Initialize tax to 0

    def set_tax(self, tax_rate):
        self.tax = self.emp_salary * tax_rate #tax in rupees

    def get_tax(self):
        return self.tax

    def get_emp_salary(self):  # Override get_emp_salary
        return self.emp_salary - self.tax

    def get_old_salary(self):
        return super().get_emp_salary()  # Access superclass method


emp = NewEmployeeClass('emp-1', 100, 1000)

emp.set_tax(0.1) #10% tax
print("Salary after tax:", emp.get_emp_salary())    # Output: 900
print("Tax amount:", emp.get_tax()) # Output: 100
print("Original salary:", emp.get_old_salary()) # Output: 1000