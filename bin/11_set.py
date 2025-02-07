"""
- set:
    -- We have option to store multiple values like list of names, list of ids etc
    -- Here we can keep UNIQUE values
    -- No index number to each value
"""

print("set PART-1")
print('Store multiple values')
print("-"*20)
# ---------------

my_set = {10, 10, 10, "python", "python", "python", "java", "java"}
print(my_set)
# OR
my_set = set([10, 10, 10, "python", "python", "python", "java", "java"])
print(my_set)

# Using for/while loop

my_tuple = tuple(my_set)
my_list = list(my_tuple)
print("my_tuple:", my_tuple)
print("my_list:", my_list)

print("#"*40, end="\n\n")
###########################

print("set PART-2")
print("Methods present in 'set' class")
print("-"*20)
# ---------------

print(dir(my_set))
# OR
# print(dir(set))

print("#"*40, end="\n\n")
###########################


print("set PART-3")
print("union, intersection, difference methods")
print("-"*20)
# ---------------

batch_1_list = {"emp-1", "emp-2", "emp-3", "emp-4"}
batch_2_list = {"emp-3", "emp-4", "emp-5", "emp-6"}

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

print("set PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# ---------------

batch_1_set = {"emp-1", "emp-2", "emp-3", "emp-4"}
print("batch_1_set:", batch_1_set, end="\n\n")

# ADD
batch_1_set.add("emp-5")
print("batch_1_set after adding emp-5:", batch_1_set, end="\n\n")
# {"emp-1", "emp-2", "emp-3", "emp-4", "emp-5"}

# REMOVE
batch_1_set.remove("emp-1")
print("batch_1_set after removing emp-1:", batch_1_set, end="\n\n")

batch_1_set.pop()
print("batch_1_set after pop():", batch_1_set, end="\n\n")

# UPDATE
new_set = {"emp-6", "emp-7"}
print("new_set:", new_set)
batch_1_set.update(new_set)
print("batch_1_set after merging newset:", batch_1_set, end="\n\n")
# {'emp-3', 'emp-7', 'emp-6', 'emp-2', 'emp-5'}

# Update: Change emp-7 value to emp-8
batch_1_set.remove("emp-7")
batch_1_set.add("emp-8")
print("batch_1_set after updating emp-7 to emp-8:", batch_1_set, end="\n\n")

print("#"*40, end="\n\n")
###########################