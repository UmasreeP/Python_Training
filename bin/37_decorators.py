"""
Decorators: If we are writing more than one function,
In all the functions, few statements/logic are common,
then how to reuse that common logic/code?
"""
print("WITHOUT using Decorators")
print("-"*20)
# ---------------

def add1(a, b):
    print("Result is")
    print(a+b)
    print("End of the result")

def add2(a, b):
    print("Result is")
    print(a+b+a)
    print("End of the result")

def sub1(a, b):
    print("Result is")
    print(a-b)
    print("End of the result")

def sub2(a, b):
    print("Result is")
    print(a-b-a)
    print("End of the result")


add1(10, 20)
add2(10, 20)
sub1(10, 20)
sub2(10, 20)

print("#"*40, end="\n\n")
###########################

print("USING Decorators: PARTIAL IMPLEMENTATION")
print("-"*20)
# ---------------


# Function using DECORATOR DESIGN PATTERN
def my_decorator(my_func): # my_func = add2
    def decorated_function(x, y):
        print("Result is")
        my_func(x,y) # add2(10,20)
        print("End of the result")
    return decorated_function


def add1(a, b):
    print(a+b)

nested_function_reference = my_decorator(add1)
# nested_function_reference having reference to 'decorated_function'
nested_function_reference(10,20)

def sub1(a, b):
    print(a-b)

nested_function_reference = my_decorator(sub1)
# nested_function_reference having reference to 'decorated_function'
nested_function_reference(10,20)

def add2(a, b):
    print(a+b+a)

nested_function_reference = my_decorator(add2)
# nested_function_reference having reference to 'decorated_function'
nested_function_reference(10,20)

print("#"*40, end="\n\n")
###########################

print("USING Decorators: FINAL IMPLEMENTATION")
print("-"*20)
# ---------------


# Function using DECORATOR DESIGN PATTERN
def my_decorator(my_func): # my_func = add2
    def decorated_function(x, y):
        print("Result is")
        my_func(x,y) # add2(10,20)
        print("End of the result")
    return decorated_function

@my_decorator
def add1(a, b):
    print(a+b)

add1(10,20)

# @my_decorator will take care of executing below 2 steps
# nested_function_reference = my_decorator(add1)
# nested_function_reference(10,20)
@my_decorator
def sub1(a, b):
    print(a-b)

sub1(10,20)
# @my_decorator will take care of executing below 2 steps
# nested_function_reference = my_decorator(sub1)
# nested_function_reference(10,20)
@my_decorator
def add2(a, b):
    print(a+b+a)

add2(10, 20)
# @my_decorator will take care of executing below 2 steps
# nested_function_reference = my_decorator(add2)
# nested_function_reference(10,20)

print("#"*40, end="\n\n")
###########################