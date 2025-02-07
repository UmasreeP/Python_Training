"""
Write instance methods to get emp_name, emp_id, emp_salary
Expected output: E1.get_emp_name() Should print:
‘emp-1’
E1.get_emp_id() Should print: 100
E1.get_emp_salary() Should print:
1000
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
# Creating Object
E1 = EmployeeClass('emp-1', 100, 1000)
print("Emp Name is :", E1.get_emp_name())
print("Emp ID is :", E1.get_emp_id())
print("Emp Salary is :", E1.get_emp_salary())

