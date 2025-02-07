"""
Packages: We can keep/organize modules in folders and sub-folders.
These folders and sub-folders are called PACKAGES
"""

print("1-WAY: importing library using 'import'")
print("-"*20)
# ---------------

import mypackage.db.mymodule

print("Course:", mypackage.db.mymodule.course)

add_result = mypackage.db.mymodule.add(10,20)
print("add_result:", add_result)

e1 = mypackage.db.mymodule.Employee()
e1.store_name("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
###########################

print("2-WAY: importing library using 'from-import'")
print("-"*20)
# ---------------

from mypackage.db.mymodule import course, add, Employee

print("Course:", course)

add_result = add(10,20)
print("add_result:", add_result)

e1 = Employee()
e1.store_name("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
###########################

print("1-WAY with short name: importing library using 'import'")
print("-"*20)
# ---------------

import mypackage.db.mymodule as mm

print("Course:", mm.course)

add_result = mm.add(10,20)
print("add_result:", add_result)

e1 = mm.Employee()
e1.store_name("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
###########################

print("2-WAY with short name: importing library using 'from-import'")
print("-"*20)
# ---------------

from mypackage.db.mymodule import course as c, add as a, Employee as E

print("Course:", c)

add_result = a(10,20)
print("add_result:", add_result)

e1 = E()
e1.store_name("emp-1")
print("Employee Name:", e1.get_name())

print("#"*40, end="\n\n")
###########################