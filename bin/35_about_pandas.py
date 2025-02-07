"""
About pandas library
- This library is mainly for tabular data processing like csv, xlsx, database

- pandas library has many functions and classes in it
- Few function names are: 1) read_csv 2) read_excel 3) read_sql many more
- Few class names are : 1) DataFrame class 2) Series class many more

DataFrame class is MAIN class here
DataFrame class is written for work with tabular data
few methods like sum(), mean() avg(), std() many more
few methods like to_csv, to_excel, to_sql many more
few methods like groupby etc
"""

print("In pandas library")
print("-"*20)
# ---------------

import pandas as pd
print(dir(pd))

print("#"*40, end="\n\n")
###########################

print("In DataFrame class")
print("-"*20)
# ---------------

import pandas as pd
print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
###########################

print("DataFrame class example-1")
print("-"*20)
# ---------------

my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130,140,150, 160]])
print(my_df)

print("#"*40, end="\n\n")
###########################

print("DataFrame class example-2")
print("-"*20)
# ---------------

my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130,140,150, 160]],
                     index=["r1", "r2", "r3", "r4"],
                     columns=["c1", "c2", "c3", "c4"]
                     )
print(my_df)

print("#"*40, end="\n\n")
###########################