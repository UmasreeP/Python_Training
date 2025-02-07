"""
Finally create below ﬁles,


1.	Create new python ﬁle called ‘EmployeeModule.py’, Inside this ﬁle keep ONLY
a.	EmployeeClass
b.	my_company_decorator

2.	Create another new python ﬁle called ‘NewEmployeeModule.py’, Inside this ﬁle keep ONLY

a.	NewEmployeeClass which is created in Task-6

NOTE: Since NewEmployeeClass is inheriting from ‘EmployeeClass’, import necessary module


3.		Create new python ﬁle called ‘main_program.py’, In this ﬁle import ‘NewEmployeeClass’ and test the following


  1: Create instance
E1 = NewEmployeeClass(‘emp-1’, 123, 1000)


  2: Add tax details E1.set_emp_tax(100)

  3: Access all methods
print(“Employee Name:”, E1.get_emp_name()) print(“Employee Salary:”, E1.get_emp_salary()) print(“Employee ID:”, E1.get_emp_id()) print(“Employee ID:”, E1.get_emp_tax())

4.	Average Salary
avg_sal = E1.get_avg_salary(1000, 2000, 3000) print(“avg_sal:”, avg_sal)   output=2000

5.	Iterate for x in E1:
print(“Each Char: ”, x)


6.	Get old salary
print(“Employee Old Salary :”, E1.get_old_salary())


"""