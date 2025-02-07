"""
Problem Statement:

Get data from
1. log_report.json
2. log_report_2.json
3. my_database

and produce single report in
final_report.csv
final_report.xlsx
final_report.json
final_report.xml
"""
print("Get data from log_report.json")
print("-"*20)
# ---------------

import pandas as pd
my_json_data_df_1 = pd.read_json("log_report.json")
print(my_json_data_df_1)

print("#"*40, end="\n\n")
###########################

print("Get data from log_report_2.json")
print("-"*20)
# ---------------

import pandas as pd
my_json_data_df_2 = pd.read_json("log_report_2.json")
print(my_json_data_df_2)

print("#"*40, end="\n\n")
###########################

print("ROTATING: Making rows to column")
print("-"*20)
# ---------------

my_json_data_df_2 = my_json_data_df_2.T # Transpose -> Rotate
print(my_json_data_df_2)

print("#"*40, end="\n\n")
###########################

print("Get data from database")
print("-"*20)
# ---------------

import sqlite3
my_db_connection = sqlite3.connect("my_database.db")

import pandas as pd
my_db_df = pd.read_sql("SELECT * FROM MY_TABLE", my_db_connection)
print(my_db_df)

print("#"*40, end="\n\n")
###########################

print("Merge all: BUT NOT COMING IN REQUIRED FORMAT")
print("-"*20)
# ---------------

# my_json_data_df_1
# my_json_data_df_2
# my_db_df

all_in_one_df = pd.concat([my_json_data_df_1, my_json_data_df_2, my_db_df], axis=0)
print(all_in_one_df)
# axis=0 # horizontal
# axis=1 # vertical

print("#"*40, end="\n\n")
###########################

print("Rename column names in both my_json_data_df_1 and my_json_data_df_2 ")
print("-"*20)
# ---------------

# my_json_data_df_1
# my_json_data_df_2
# my_db_df

print("List of of columns in my_json_data_df_1:", my_json_data_df_1.columns, sep="\n", end="\n\n")
print("List of of columns in my_json_data_df_2:", my_json_data_df_2.columns, sep="\n", end="\n\n")

# Rename all columns
my_json_data_df_1.columns = ["IP", "DATE", "URL"]
my_json_data_df_2.columns = ["IP", "DATE", "URL"]

print("After rename, List of of columns in my_json_data_df_1:", my_json_data_df_1.columns, sep="\n", end="\n\n")
print("After rename, List of of columns in my_json_data_df_2:", my_json_data_df_2.columns, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("Merge all: After providing proper column name")
print("-"*20)
# ---------------

# my_json_data_df_1
# my_json_data_df_2
# my_db_df

all_in_one_df = pd.concat([my_json_data_df_1, my_json_data_df_2, my_db_df], axis=0)
print(all_in_one_df)
# axis=0 # horizontal
# axis=1 # vertical

print("#"*40, end="\n\n")
###########################

print("Any Empty Cells in IP columns")
print("-"*20)
# ---------------

print(all_in_one_df["IP"].isnull())

print("#"*40, end="\n\n")
###########################

print("Any Empty Cells entire data")
print("-"*20)
# ---------------

print(all_in_one_df.isnull())

print("#"*40, end="\n\n")
###########################

print("TOTAL Empty Cells entire data")
print("-"*20)
# ---------------

print(all_in_one_df.isnull().sum())

print("#"*40, end="\n\n")
###########################


print("Fill Empty cells in URL column with 'www.abcxyz.com'")
print("-"*20)
# ---------------

all_in_one_df["URL"] = all_in_one_df["URL"].fillna("www.abcxyz.com")
print(all_in_one_df)

print("#"*40, end="\n\n")
###########################

print("After filling empty cells, TOTAL Empty Cells entire data")
print("-"*20)
# ---------------

print(all_in_one_df.isnull().sum())
all_in_one_df.to_csv("temp.csv", index=None)

print("#"*40, end="\n\n")
###########################

print("Producing final reports")
print("-"*20)
# ---------------

# final_report.csv
all_in_one_df.to_csv("final_report.csv", index=None)

# final_report.xlsx
all_in_one_df.to_excel("final_report.xlsx", index=None)

# final_report.xml
all_in_one_df.to_xml("final_report.xml")

print("""
Created below files, please check

final_report.csv
final_report.xlsx
final_report.xml

""")

print("#"*40, end="\n\n")
###########################

print("Reindex:")
print("-"*20)
# ---------------

all_in_one_df = all_in_one_df.reset_index(drop=True)
# drop=True, delete existing index column
print(all_in_one_df)

print("#"*40, end="\n\n")
###########################

print("Write to json file")
print("-"*20)
# ---------------

all_in_one_df.to_json("final_report_1.json")

all_in_one_df = all_in_one_df.T

all_in_one_df.to_json("final_report_2.json")

print("""
Created 
final_report_1.json 
final_report_2.json
please check
""")

print("#"*40, end="\n\n")
###########################