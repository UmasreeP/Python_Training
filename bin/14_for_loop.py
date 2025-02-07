"""
for-loop: Iterate any collection of values like strings, list, tuple etc
"""

print("Iterate strings")
print("-"*20)
# ---------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

for i in my_string:
    print("Value of i:", i)

print("#"*40, end="\n\n")
###########################

print("Iterate list")
print("-"*20)
# ---------------

my_list = ["Python", "Java", "C++"]
print("my_list:", my_list, end="\n\n")

for i in my_list:
    print("Each value in list:", i)

print("#"*40, end="\n\n")
###########################

print("Iterate dictionary")
print("-"*20)
# ---------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

for k in my_dictionary: # iterate key
    print("Each Key:", k)
    print("Each Value:", my_dictionary[k], end="\n\n")

print("#"*40, end="\n\n")
###########################

# ---------------
# 2 Cases
# ---------------
# Case-1: 'break-statement' How to end for-loop in between
# Case-2: 'continue-statement' How to skip current iteration and go for next iteration
###########################

print("# Case-1: 'break-statement' How to end for-loop in between")
print("-"*20)
# ---------------

# Requirement: If key 'course' found then no need to proceed for other elements

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

for k in my_dictionary: # iterate key
    if k == "course":
        break
    print("Each Key:", k)
    print("Each Value:", my_dictionary[k], end="\n\n")

print("#"*40, end="\n\n")
###########################

print("# Case-2: 'continue-statement' How to skip current iteration and go for next iteration")
print("-"*20)
# ---------------

# Requirement: If key 'course' found then DON'T print, skip the iteration

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

for k in my_dictionary: # iterate key
    if k == "course":
        continue
    print("Each Key:", k)
    print("Each Value:", my_dictionary[k], end="\n\n")

print("#"*40, end="\n\n")
###########################

print("for-else block")
print("-"*20)
# ---------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

for k in my_dictionary: # iterate key
    if k == "course":
        continue
    print("Each Key:", k)
    print("Each Value:", my_dictionary[k], end="\n\n")
else:
    print("After completing for-loop, else-block will execute")
    print("We want to empty the dictionary after completing for-loop because work done")
    my_dictionary.clear()
    print("my_dictionary after clear is: ", my_dictionary)
    print(f"my dist after clear is {my_dictionary}")

# Behavior of 'else' block
# - If for-block forcebilly ended using 'break' then 'else-block' will not execute
# - Which means, after successful execution of for-block, if we want to do
#   something then we can use else block

# Example:
#   We are keep on writing to DB/File in for-block
#   after sucessful writing if we want to save then that save logic will
#   come in else-block.
#   If writing is unsuccessful then 'break' the loop so that 'else-block' will
#   not execute, so it will not save

print("#"*40, end="\n\n")
###########################