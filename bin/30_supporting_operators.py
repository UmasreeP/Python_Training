"""
2 Things
1. support + operator
2. support iteration

In python, for all the operators like +,- etc we have special name
given like + -> __add__, - --> __sub__

If we want to support + then we need to write __add__ method in our class
"""

print("1. support + operator")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, en):
        self.name = en
    def __add__(self, other): # self = e1, other = e2
        concat_result = self.name + other.name
        return concat_result


e1 = Employee("emp-1")
e2 = Employee("emp-2")
# Requirement: if we add 2 employee objects then it should concate both names
add_result = e1 + e2 # "emp-1emp-2"
print("add_result:", add_result)

print("#"*40, end="\n\n")
###########################

print("2. support iteration")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, en):
        self.name = en
    def __add__(self, other): # self = e1, other = e2
        concat_result = self.name + other.name
        return concat_result
    def __iter__(self):
        self.index_no = 0
        return self

    def __next__(self):
        current_index = self.index_no
        if current_index < len(self.name):
            self.index_no = self.index_no + 1
            return self.name[current_index]
        else:
            raise StopIteration

e1 = Employee("emp-1")
e2 = Employee("emp-2")

print("Emp=1 Name:", e1.name)
print("Iterating e1 using for-loop")
for i in e1:
    print("Each char in e1:", i)

print("Emp=2 Name:", e2.name)
print("Iterating e2 using for-loop")
for i in e2:
    print("Each char in e2:", i)
# e
# m
# p
# -
# 2

# To support iteration, we need to implement 2 methods
# 1) __iter__ 2) __next__
# __iter__: It will execute in beginning/before-starting-loop and ONE TIME
# __next__: This will be executed in every iteration

print("#"*40, end="\n\n")
###########################