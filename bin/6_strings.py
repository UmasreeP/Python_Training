"""
- Strings:
    -- We have option to store text-data/collection of characters like name, email-id etc
    -- Automatically index number will be assigned to each character
"""

print("Strings PART-1")
print("How to store the values")
print("-"*20)
# ---------------

a = 'PERSON'
b = "PERSON'S"
c = """PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCHES)"""
d = '''PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCHES)'''
e = 'PERSON\'S'

# In all the above cases, it will create object of builtin class 'str'
# and store the values

print(a, b, c, d, e, sep="\n")

print("#"*40, end="\n\n")
###########################

print("Strings PART-2")
print("How to store the values")
print("-"*20)
# ---------------

a = "C:\newfolder\test.py"
# \n -> to put new line
# \t -> to put tab space
print("Value of a=", a, end="\n\n")

b = r"C:\newfolder\test.py"
# r -> raw string
print("Value of b=", b, end="\n\n")

print("Convert existing string 'a' into raw string:", repr(a), end="\n\n")
# repr() is a string representation of an object, Use repr() for a detailed, developer-focused output of an object.
# Use str() for a simpler, human-readable output.

print("#"*40, end="\n\n")
###########################

print("Strings PART-3")
print("How to store the values")
print("-"*20)
# ---------------

x = 10
y = 20
z = x + y

my_string = f"add of {x} and {y} is {z}"
# f - > format
# f -> replaces {variable_name} with value
print("my_string:", my_string)

print("#"*40, end="\n\n")
###########################

print("Strings PART-4")
print("Indexes: We can access each character using index")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

print("Character at 0th index using positive index:", my_string[0])
print("Character at 0th index using negative index:", my_string[-8], end="\n\n")

# print("Character at 1000th index using positive index:", my_string[1000]) # ERROR

print("#"*40, end="\n\n")
###########################

print("Strings PART-5")
print("Slicing: We can get sub-string")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx also
print("substring from index-1 to 6 using positive index:", my_string[1:6])
print("substring from index-1 to 6 using negative index:", my_string[-7:-2])
print("substring from index-1 to 6 using positive/negative index:", my_string[1:-2])
print("substring from index-1 to 6 using positive/negative index:", my_string[-7:6], end="\n\n")

print("substring from index-1 to END using positive index:", my_string[1:])
print("substring from index-1 to END using negative index:", my_string[-7:], end="\n\n")

print("substring from BEGINNING to 6 using positive index:", my_string[:6])
print("substring from BEGINNING to 6 using negative index:", my_string[:-2], end="\n\n")

print("#"*40, end="\n\n")
###########################

print("Strings PART-6")
print("Providing step value: We can skip characters")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx also
print("substring from index-1 to 6 using positive index with default step value 1 :", my_string[1:6])
print("substring from index-1 to 6 using negative index with default step value 1 :", my_string[-7:-2], end='\n\n')
# default step value = 1: which means from 1 to 6 give me every character

print("substring from index-1 to 6 using positive index with step value 1 :", my_string[1:6:1])
print("substring from index-1 to 6 using negative index with step value 1 :", my_string[-7:-2:1], end='\n\n')
# step value = 1: which means from 1 to 6 give me every character

print("substring from index-1 to 6 using positive index with step value 2 :", my_string[1:6:2])
print("substring from index-1 to 6 using negative index with step value 2 :", my_string[-7:-2:2], end='\n\n')
# step value = 2: which means from 1 to 6 give me every 2nd character

print("#"*40, end="\n\n")
###########################

print("Strings PART-7")
print("Providing -ve step value: Reverse Direction")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 7_strings.xlsx also

# Steps to follow
# Example: 1 to 6 in reverse

# step-1: mention start index = 6
# step-2: mention end index = 1
# step-3: mention negative step value = -1
# IF WE MISS ANY STEP THEN WE WILL GET EMPTY STRING

print("substring from index-6 to 1 using positive index with step value -1:", my_string[6:1:-1])
print("substring from index-6 to 1 using negative index with step value -1:", my_string[-2:-7:-1], end="\n\n")


print("substring from index-6 to 1 using positive index with step value -2:", my_string[6:1:-2])
print("substring from index-6 to 1 using negative index with step value -2:", my_string[-2:-7:-2], end="\n\n")

print("#"*40, end="\n\n")
###########################

print("Strings PART-8")
print("METHODS/VARIABLES present inside 'str' class")
print("-"*20)
# ---------------

print(dir(my_string))
# OR
# print(dir(str))

print("#"*40, end="\n\n")
###########################

# Why __ names?
# ---------------
# __ names are system defined names
# -- names are internally called by some operators like +, - etc
#   or some functions
# Example:
#   If we use + to concat 2 strings then internally it will call __add__
#   If we use len() function to check length, internally it called __len__
###########################

print("Strings PART-8")
print("Learning startswith() method")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

startswith_result = my_string.startswith("WEL") # True/False
print("startswith_result:", startswith_result)

print("#"*40, end="\n\n")
###########################