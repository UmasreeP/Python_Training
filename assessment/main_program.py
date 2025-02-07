from NewEmployeeModule import NewEmployeeClass

E1 = NewEmployeeClass("emp-1", 123, 1000)

E1.set_tax(0.1)  # Set the tax (10%)

print("Employee Name:", E1.get_emp_name())
print("Employee Salary:", E1.get_emp_salary())
print("Employee ID:", E1.get_emp_id())
print("Employee Tax:", E1.get_tax()) # Corrected method name

avg_sal = E1.get_avg_salary(1000, 2000, 3000)
print("avg_sal:", avg_sal)

for x in E1:
    print("Each Char:", x)

print("Employee Old Salary :", E1.get_old_salary())

# E2 = NewEmployeeClass("TestEmp", 200, 50000)
# E2.set_tax(0.2)
# print("Employee Name:", E2.get_emp_name())
# print("Employee Salary:", E2.get_emp_salary())
# print("Employee ID:", E2.get_emp_id())
# print("Employee Tax:", E2.get_tax()) # Corrected method name