"""
Exceptions Handling:
"""
# print("WITHOUT handling Exceptions:")
# print("-"*20)
# # ---------------
#
# a = 10
# b = 0
# result = a / b # Program will terminate abruptly HERE
# print("result:", result)
#
# print("#"*40, end="\n\n")
# ###########################
#


print("Handling Exceptions using (try/except):")
print("-"*20)
# ---------------

try:
    a = 10
    b = 0
    result = a / b # Program will NOT terminate, instead control will be passed to 'except' block
    print("result:", result) # This line will never execute
except:
    print("Reached except block")
    print("Some error in try")
    print("Here, we are writing code to solve problem occurred in try block")

print("#"*40, end="\n\n")
###########################

"""
Exceptions Handling:
"""
# print("WITHOUT handling Exceptions:")
# print("-"*20)
# # ---------------
#
# a = 10
# b = 0
# result = a / b # Program will terminate abruptly HERE
# print("result:", result)
#
# print("#"*40, end="\n\n")
# ###########################
#


print("Handling Exceptions using (try/except):")
print("-"*20)
# ---------------

try:
    a = 10
    b = 0
    result = a / b # Program will NOT terminate, instead control will be passed to 'except' block
    print("result:", result) # This line will never execute
except:
    print("Reached except block")
    print("Some error in try")
    print("Here, we are writing code to solve problem occurred in try block")

print("#"*40, end="\n\n")
###########################
print("try-except with class names")
print("-"*20)
# ---------------

# Exception classes
# - We need to have exception class for each error type
#   then we can handle using try-except
#   else we can't handle so program will terminate abruptly
#
# - Few exception classes are present in builtins
#
# - 'Exception' is super class for all the exception classes

try:
    a = 10
    b = 0
    L = []
    print("1st Value:", L[1]) # INDEX NOT PRESENT, SO ERROR
    # Program will NOT terminate, instead control will be passed to 'except' block
    result = a / XYZ # This line will never execute
    print("result:", result) # This line will never execute
except ZeroDivisionError: # 1-WAY: This is 1-way to specify class name
    print("This is ZDE block")
except NameError as ne: # 2-WAY: This is 2nd way to specify class name, here we are storing error object in 'ne'
    print("This is NE and value of 'ne' is:", ne)
except Exception as e:
    print("This is some other error and error details are :", e)
    print("type of error :", type(e))

print("#"*40, end="\n\n")
###########################

print("Using try-except-else-finally blocks")
print("-"*20)
# ---------------

try:
    print("\nReached try block")
    my_file_handle = open(r"D:\nadjsad\dnfdf.txt", "w") # Error path not found

    # WE ARE NOT HANDLING BELOW CODE ERROR IN BELOW EXCEPT BLOCK
    # my_file_handle.write(10) # Error, We need to pass string '10'
    # my_file_handle.write("Hello")
    # my_file_handle.close()
except Exception as e:
    print("\nReached except block")
    print("This except block strictly to handle open() function error:")
    print("Error Message:", e)
else:
    print("\nReached else block")
    try:
        my_file_handle.write(10) # Error, We need to pass string '10'
        my_file_handle.write("Hello")
    except Exception as e:
        print("Got error while writing and details are:", e)
        print("type of error:", type(e))
finally:
    print("\nReached finally block")
    try:
        my_file_handle.close()
        print("file handle closed")
    except Exception as e:
        print("Not able to close file handle, Because:", e)


# About 'finally' block
# If ERROR/NO-ERROR in try/except/else block, BUT finally block will execute
#   in both the condition

# About 'else' block
# - if try block success then 'else' will execute and 'except' will be skipped
# - if try block failed then 'except' will execute and 'else' will be skipped

print("#"*40, end="\n\n")
###########################

print("User defined exception class example-1")
print("-"*20)
# ---------------

# Mandatory Step: Our class should be subclass of 'Exception' class
# OR if some classes like builtin-exception-classes are already subclass
# of Exception then we can use that class as well to create our exception class

class MyError(Exception):
    pass
# - pass -> empty block
# - Even though it is empty block, this is valid class
#   so we can make use this class to handle using try-except

try:
    x = 10
    if x == 10:
        raise MyError
        #raise ZeroDivisionError

    if x > 10:
        raise MyError

    if x < 10:
        raise MyError

except MyError:
    print("Reached MyError Except Block")


print("#"*40, end="\n\n")
###########################

print("User defined exception class example-2")
print("-"*20)
# ---------------

# Requirement: pass some message while raising error


class MyError(Exception):
    def __init__(self, msg):
        self.error_message = msg


try:
    x = 10

    if x == 10:
        raise MyError("Here value of x is 10 so raising MyError")

    if x > 10:
        raise MyError("Here value of x is gt 10 so raising MyError")

    if x < 10:
        raise MyError("Here value of x is lt 10 so raising MyError")

except MyError as me:
    print("Reached MyError Except Block and Details:", me.error_message)


print("#"*40, end="\n\n")
###########################