"""
Write a class named ‘EmployeeClass’ which is having 	init	() method with 3 arguments emp_name, emp_id, emp_salary
   Example:
E1 = EmployeeClass(‘emp-1’, 100, 1000)

"""


class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary


# Creating Object
E1 = EmployeeClass('emp-1', 100, 1000)

print(f"Employee Name: {E1.emp_name}, ID: {E1.emp_id}, Salary: {E1.emp_salary}")
