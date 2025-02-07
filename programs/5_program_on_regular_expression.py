"""
Get data from log file
then
extract and print
IP
DATE
URL
using regular expression
"""
print("Get data from log file")
print("-"*20)
# ---------------

my_log_file_handle = open(r"../log/web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
###########################

print("Check whether it is IP address line or not, yes or no?")
print("-" * 20)
# ---------------

import re

for each_line in log_file_content:
    # match_result = re.match('\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]', each_line)
    # OR
    match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_line)
    print("Each Line:", each_line)
    print("match_result:", match_result, end="\n\n")

# COMMENT
"""
Regular Expression

IDENTIFIERS
-----------
\d -> to tell any ONE digit between 0 to 9
\D -> to tell any ONE non-digit. Means, Except 0 to 9, any character
. -> to tell any ONE any character
\. -> Exactly DOT
[0-9] -> to tell any ONE digit between 0 to 9
[a2xL] -> It can be any ONE character in this group
            -- It can be 'a'
            OR
            -- It can be '2'
            OR
            -- It can be 'x'
            OR
            -- It can be 'L'
-----------

QUANTIFIER
-----------
\d{3} -> it makes \d 3 times i.e \d\d\d
\d{1,3} -> it makes OR condition i.e (\d|\d\d|\d\d\d)
-----------
"""

# EXAMPLE
"""
'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*' 
    IP followed by ANY-CHARACTER 0 or more times

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}a*' 
     IP followed by character 'a' 0 or more times

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}abc*' 
     IP followed by exact 'ab' followed by character 'c' 0 or more times

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}(abc)*' 
     IP followed by exact 'abc' 0 or more times     

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}[abc]*' 
     IP followed by exact 'a' OR 'b' OR 'c' 0 or more times     

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}(abc)' 
     IP followed by exact 'abc'

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}(abc|xyz)' 
     IP followed by exact 'abc' OR exact xyz

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}(abc|xyz|\d\d)' 
     IP followed by exact 'abc' OR exact xyz OR extat 2 digits

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}abc' 
     IP followed by exact 'abc'

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}[abc]' 
     IP followed by exact 'a' OR 'b' OR 'c'     

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}abc\*' 
     IP followed by exact 'abc' followed by *

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}\(abc\)' 
     IP followed by '(' then followed by exact 'abc' then followed by ')'

'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}[a-zA-Z0-9_?':;]' 
     IP followed by any one character in this [a-zA-Z0-9_?':;] group
"""

print("#" * 40, end="\n\n")
###########################

print("Extract IP")
print("-"*20)
# ---------------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print(ip)

# COMMENT-1
"""
put () to IP address pattern to capture
- this is called grouping
- each group has index starting from-1
"""

# COMMENT-2
"""
MODIFIERS:
----------
* -> use this to make 0 or more times
+ -> use this to make 1 or more times
? -> use this to make 0 or 1 time
----------

"""

print("#"*40, end="\n\n")
###########################

print("Extract IP, DATE")
print("-"*20)
# ---------------

import re

for each_line in log_file_content:
    # match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}) - - \[(\d{2}/[A-Za-z]{3}/\d{4}).*', each_line)
    # OR
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[A-Za-z]{3}/\d{4}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt)

# COMMENT-1
"""
26/Apr/2000

26
---
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits
[0-9]\d # Strictly 2 digits
\d[0-9] # Strictly 2 digits

\d{1,2} # Minimum one digit, maximum 2 digits
[0-9]{1,2} # Minimum one digit, maximum 2 digits
\d?\d # Minimum one digit, maximum 2 digits
[0-9]?[0-9] # Minimum one digit, maximum 2 digits
\d?[0-9] # Minimum one digit, maximum 2 digits
[0-9]?\d # Minimum one digit, maximum 2 digits
###

Apr
---
[A-Z][a-z][a-z]
OR
[A-Za-z]{3}
OR
[A-Z][a-z]{2}
OR
(Jan|Feb|Mar)
###

"""

# EXAMPLE
"""

abc? -> c is optional
(abc)? -> abc is optional
[abc]? -> any one character : a or b or c is which is optional

[0-39] -> any one digit b/n 0 to 3 OR it can 9
    = it can be 0 or 1 or 2 or 3 or 9

31-> [0-3][0-9]

"""



print("#"*40, end="\n\n")
###########################

# Comment
# ---------------
# \s -> ONE Space
# \S -> any character, except space
# \w -> [0-9a-zA-Z_] -> any one character in this group
#   We can use [0-9a-zA-Z_] OR \w
# \W -> [^0-9a-zA-Z_] # any characters Excluding these characters
# [^0-9] -> Any characters excluding digits
###########################