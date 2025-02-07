from EmployeeModule import EmployeeClass  # Import

class NewEmployeeClass(EmployeeClass):
    def __init__(self, emp_name, emp_id, emp_salary):
        super().__init__(emp_name, emp_id, emp_salary)
        self.tax = 0

    def set_tax(self, tax_rate): #tax in rupees
        self.tax = self.emp_salary * tax_rate

    def get_tax(self):
        return self.tax

    def get_emp_salary(self):
        return self.emp_salary - self.tax

    def get_old_salary(self):
        return super().get_emp_salary()

    def get_avg_salary(self, *salaries):  # method for average salary
        if len(salaries) < 2:
            raise ValueError("Min two salaries must be provided to get the average.")
        return sum(salaries) / len(salaries)

    def __iter__(self): # make the class iterable
        return iter(self.emp_name)