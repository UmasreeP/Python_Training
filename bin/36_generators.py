"""
Generators: We can create object whenever we want
"""

print("WITHOUT Using Generators")
print("-"*20)
# ---------------


def my_square_function(my_list):
    result = []
    for i in my_list:
        result.append(i*i)
    return result


L = [10, 20, 30, 40]
square_result = my_square_function(L)
print("square_result:", square_result, end="\n\n")

# OUR REQUIREMENT HERE Is, process one value at a time,
# BUT function is keeping all sqaured in list which is occupying memory
# SO, is it possible to give one squared value at a time whenever we ask

for j in square_result:
    print("Each Squared value:", j)

print("#"*40, end="\n\n")
###########################

print("USING Generators")
print("-"*20)
# ---------------


def my_square_function(my_list):
    for i in my_list:
        yield i*i


L = [10, 20, 30, 40]
square_result = my_square_function(L)
print("square_result:", square_result, end="\n\n")

# OUR REQUIREMENT HERE Is, process one value at a time,
# BUT function is keeping all sqaured in list which is occupying memory
# SO, is it possible to give one squared value at a time whenever we ask

for j in square_result:
    print("Each Squared value:", j)

print("#"*40, end="\n\n")
###########################

print("Another way to create Generators Object: Using TUPLE COMPREHENSION")
print("-"*20)
# ---------------

L = [10, 20, 30, 40]
# LIST/TUPLE/DICTIONARY/SET COMPREHENSION: We can write expression(one liner)

my_squared_list = [i*i for i in L]
print("my_squared_list:", my_squared_list, end="\n\n")

my_squared_tuple = (i*i for i in L)
print("my_squared_tuple: IT IS GENERATOR:", my_squared_tuple, end="\n\n")

print("Iterating generator object my_squared_tuple:")
for i in my_squared_tuple:
    print("Value:", i)

print("#"*40, end="\n\n")
###########################

print("Set and Dictionary Comprehension")
print("-"*20)
# ---------------

keys = ["A", "B"]
values = [10, 20]

# zip(keys, values) = [('A', 10), ('B', 20)]
D = {i[0]:i[1] for i in zip(keys, values)}
print("Dictionary:", D)

squared_values_set = {i*i for i in values}
print('squared_values_set:', squared_values_set)

# zip Example:
#
# >>> keys = ["A", "B"]
# >>> values = [10, 20]
# >>>
# >>> paired = [('A', 10), ('B', 20)]
# >>> dict(paired)
# {'A': 10, 'B': 20}
# >>>
# >>> z = zip(keys, values)
# >>> list(z)
# [('A', 10), ('B', 20)]

print("#"*40, end="\n\n")
###########################