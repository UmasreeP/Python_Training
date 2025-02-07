"""
- Numbers:
    -- We have option to store numbers like int, float etc
"""

print("Numbers Example")
print("-"*20)
# ---------------

a = 10
# Internally it will create object of builtin class 'int' and store the value
b = 12.5
# Internally it will create object of builtin class 'float' and store the value

c = a + b

print(a, b, c, sep="\n")

d = a - 1
e = a * d
f = a / 2
g = 2 ** 10
h = a // 2
i = a % 2

print(a, b, c, d, e, f, g, h, i, sep="\n")

print("#"*40, end="\n\n")
###########################