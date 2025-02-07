"""
while-loop: Execute loop based on condition
"""

print("while-loop example")
print("-"*20)
# ---------------

x = 0
while x < 5:
    print("Value of x is:", x)
    x = x + 1

print("#"*40, end="\n\n")
###########################

print("while-loop example to iterate list/tuple or other collections")
print("-"*20)
# ---------------

my_list = ["Java", "Perl", "Python", "C"]
print("my_list:", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    print("Each Value in my_list:", my_list[index_no])
    index_no = index_no + 1

print("#"*40, end="\n\n")
###########################

# ---------------
# Can we iterate collections which is not having index numbers
#   like set, frozenset etc?
# ---------------
# - Convert to list/tuple
# - Now, iterate list/tuple
###########################

# ---------------
# 2 Cases
# ---------------
# Case-1: 'break-statement' How to end while-loop in between
# Case-2: 'continue-statement' How to skip current iteration and go for next iteration
###########################

print("# Case-1: 'break-statement' How to end while-loop in between")
print("-"*20)
# ---------------

# Requirement: If key 'course' found then no need to proceed for other elements

# Example-1:
#
# >>> all_keys = my_dictionary.keys()
#
# >>> type(all_keys)
# <class 'dict_keys'>
# >>>
#
# >>> all_keys_in_list = list(all_keys)
# >>> all_keys_in_list
# ['duration', 'course', 'mode']
# >>>

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

all_keys = my_dictionary.keys()
all_keys_in_list = list(all_keys)
print("all_keys_in_list:", all_keys_in_list, end="\n\n")

index_no = 0
while index_no < len(all_keys_in_list):
    key = all_keys_in_list[index_no]
    if key == "course":
        break
    print("Each Key:", key)
    print("Each Value:", my_dictionary[key])
    index_no = index_no + 1

# for k in my_dictionary: # iterate key
#     if k == "course":
#         break
#     print("Each Key:", k)
#     print("Each Value:", my_dictionary[k], end="\n\n")

print("#"*40, end="\n\n")
###########################

print("# Case-2: 'continue-statement' How to skip current iteration and go for next iteration")
print("-"*20)
# ---------------

# Requirement: If key 'course' found then DON'T print, skip the iteration

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

all_keys = my_dictionary.keys()
all_keys_in_list = list(all_keys)
print("all_keys_in_list:", all_keys_in_list, end="\n\n")

index_no = 0
while index_no < len(all_keys_in_list):
    key = all_keys_in_list[index_no]
    if key == "course":
        index_no = index_no + 1
        continue
    print("Each Key:", key)
    print("Each Value:", my_dictionary[key])
    index_no = index_no + 1

# for k in my_dictionary: # iterate key
#     if k == "course":
#         continue
#     print("Each Key:", k)
#     print("Each Value:", my_dictionary[k], end="\n\n")

print("#"*40, end="\n\n")
###########################

print("while-else block")
print("-"*20)
# ---------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

all_keys = my_dictionary.keys()
all_keys_in_list = list(all_keys)
print("all_keys_in_list:", all_keys_in_list, end="\n\n")

index_no = 0
while index_no < len(all_keys_in_list):
    key = all_keys_in_list[index_no]
    if key == "course":
        index_no = index_no + 1
        continue
    print("Each Key:", key)
    print("Each Value:", my_dictionary[key])
    index_no = index_no + 1
else:
    print("After completing while-loop, else-block will execute")
    print("We want to empty the dictionary after completing while-loop because work done")
    my_dictionary.clear()
    print(f"my_dict after clearing is {my_dictionary}")


# for k in my_dictionary: # iterate key
#     if k == "course":
#         continue
#     print("Each Key:", k)
#     print("Each Value:", my_dictionary[k], end="\n\n")
# else:
#     print("After completing for-loop, else-block will execute")
#     print("We want to empty the dictionary after completing for-loop because work done")
#     my_dictionary.clear()


print("#"*40, end="\n\n")
###########################