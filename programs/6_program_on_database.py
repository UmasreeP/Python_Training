"""
Get data from web_server.log
then
extract info using regular expression
then
send extracted data to database
"""

"""
How to communicate with database in python?

python-program  <-- using library--> any databases(SQL/No-SQL)

Example:
python-program  <-- using library (cx-oracle)--> Oracle database
python-program  <-- using library (mysql.connector)--> MySQL database
python-program  <-- using library (sqlite3)--> SQLite database
"""

"""
We need ONE database.
- We can use SQLite database
- SQLite database will not run any database server
- it is severless database
- It will just create one database file, on that database file
    we can execute SQL query
"""

"""
How to create and communicate with SQLite database?

2 ways
1-way: Using SQLite database software
2-way: WITHOUT Using SQLite database software,
        using python library 'sqlite3', we can create database
        as well we can interact with database
"""

print("Create database and table")
print("-"*20)
# ---------------

import sqlite3

print("Create database 'my_database.db'")
my_db_connection = sqlite3.connect("my_database.db")
print("Done\n")

print("Create cursor object, in order to execute SQL query")
my_db_dursor = my_db_connection.cursor()
print("Done\n")

print("Creating table if not present")
my_query = """
CREATE TABLE IF NOT EXISTS MY_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100)
)
"""
my_db_dursor.execute(my_query)
print("Done\n")


print("#"*40, end="\n\n")
###########################

print("Get data from log file")
print("-"*20)
# ---------------

my_log_file_handle = open(r"../log/web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
###########################

print("Extract IP, DATE and write to database")
print("-"*20)
# ---------------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[A-Za-z]{3}/\d{4}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}', '{dt}')"
        print("Executing Query:", my_query)
        my_db_dursor.execute(my_query)
        print("One record inserted\n")

my_db_connection.commit()
print("All records inserted to database")

print("#"*40, end="\n\n")
###########################

print("Getting data from database")
print("-"*20)
# ---------------

my_query = "SELECT * FROM MY_TABLE"
my_db_dursor.execute(my_query)
my_db_result = my_db_dursor.fetchall()
print(my_db_result)
my_db_connection.close()
print("DB Connection closed")

print("#"*40, end="\n\n")
###########################