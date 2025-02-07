"""
- Tuple:
    -- We have option to store multiple values like list of names, list of ids etc
    -- Here we can keep DUPLICATE values
    -- Automatically index number will be assigned to each value
"""

print("Tuple PART-1")
print("Store multiple values")
print("-"*20)
# ---------------

my_tuple = (10, 12.5, "python", (100, 200))
print("my_tuple:", my_tuple)
# Internally it will create object of tuple class and store the values

print("#"*40, end="\n\n")
###########################

print("Tuple PART-2")
print("Indexes are similar to strings")
print("-"*20)
# ---------------

print("1st Value:", my_tuple[0])
print("2nd Value:", my_tuple[1])

print("#"*40, end="\n\n")
###########################

print("Tuple PART-3")
print("Methods present inside 'tuple' class")
print("-"*20)
# ---------------

print(dir(my_tuple))
# OR
# print(dir(tuple))

print("#"*40, end="\n\n")
###########################

print("Tuple PART-4")
print("Index and Count Methods")
print("-"*20)
# ---------------

my_tuple = (10, 12.5, "python", (100, 200))
print("my_tuple:", my_tuple)

index_of_python = my_tuple.index("python")
count_of_python = my_tuple.count("python")

print("index_of_python:", index_of_python)
print("count_of_python:", count_of_python)

print("#"*40, end="\n\n")
###########################

