"""
- Frozenset:
    -- We have option to store multiple values like list of names, list of ids etc
    -- Here we can keep UNIQUE values
    -- No index number to each value
"""

print("frozenset PART-1")
print('Store multiple values')
print("-"*20)
# ---------------

my_fs = frozenset([10, 10, 10, "python", "python", "python", "java", "java"])
print(my_fs)

# Using for/while loop

my_tuple = tuple(my_fs)
my_list = list(my_tuple)
print("my_tuple:", my_tuple)
print("my_list:", my_list)

print("#"*40, end="\n\n")
###########################

print("frozenset PART-2")
print("Methods present in 'frozenset' class")
print("-"*20)
# ---------------

print(dir(my_fs))
# OR
# print(dir(frozenset))

print("#"*40, end="\n\n")
###########################


print("frozenset PART-3")
print("union, intersection, difference methods")
print("-"*20)
# ---------------

batch_1_list = frozenset(["emp-1", "emp-2", "emp-3", "emp-4"])
batch_2_list = frozenset(["emp-3", "emp-4", "emp-5", "emp-6"])

print("batch_1_list:", batch_1_list)
print("batch_2_list:", batch_2_list, end="\n\n")

all_employees = batch_1_list.union(batch_2_list)
print("all_employees:", all_employees)

employee_only_in_batch_1 = batch_1_list.difference(batch_2_list)
print("employee_only_in_batch_1:", employee_only_in_batch_1)

employees_present_in_both = batch_1_list.intersection(batch_2_list)
print("employees_present_in_both:", employees_present_in_both)

print("#"*40, end="\n\n")
###########################