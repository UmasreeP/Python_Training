"""
Write variable-argument-static-method to compute average salary of employees.
If we pass 2 or more salaries to methods, it should return the average salary.
"""


class EmployeeClass:

    @staticmethod
    def get_average_salary(*salaries):
        if len(salaries) < 2:
            raise ValueError("Min two salaries must be provided to get the average.")
        return sum(salaries) / len(salaries)


average_salary = EmployeeClass.get_average_salary(10000, 20000, 30000)
print(f"Average Salary: {average_salary}")

# 2 salaries
average_salary = EmployeeClass.get_average_salary(10000, 20000)
print(f"Average Salary: {average_salary}")
