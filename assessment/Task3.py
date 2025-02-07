"""
Write decorator function outside the above class, decorator function name will be ‘my_company_decorator’.
Use this decorator on top of all 3 get-methods deﬁned inside the class.
Details of the decorator has been provided below these examples. Please check

Expected output:

E1.get_emp_name() Should print:

Company Name Is: “XYZ Company” ‘emp-1’
Address: XYZ Address

E1.get_emp_id() Should print:

Company Name Is: “XYZ Company” 100
Address: XYZ Address

E1.get_emp_salary() Should print:

Company Name Is: “XYZ Company” 1000
Address: XYZ Address

Decorator Requirement: As we observed above, all get methods are using some common functionality which is
Company Name Is: “XYZ Company” Address: XYZ Address
Write a decorator for this common functionality and make use in all get methods

"""

class EmployeeClass:
    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    def my_company_decorator(func):
        def wrapper(self, *args, **kwargs):
            print('Company Name Is: "XYZ Company"', end=' ')
            result = func(self, *args, **kwargs)
            print('\nAddress: XYZ Address')
            return result
        return wrapper

    @my_company_decorator
    def get_emp_name(self):
        print(f"'{self.emp_name}'", end=' ')
    @my_company_decorator
    def get_emp_id(self):
        print(self.emp_id, end=' ')
    @my_company_decorator
    def get_emp_salary(self):
        print(self.emp_salary, end=' ')
# Creating Object
E1 = EmployeeClass('emp-1', 100, 1000)
E1.get_emp_name()
E1.get_emp_id()
E1.get_emp_salary()