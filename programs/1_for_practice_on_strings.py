"""
From the given string below,
extract
DATE

Expected Output:
------------
26/Apr/2000
------------
"""

print("input data:")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

start_index = input_data.find("[") + 1
end_index = input_data.find(":", start_index)
date = input_data[start_index:end_index]
print("Date :", date)
print("#"*40, end="\n\n")
###########################

"""
From the given string below,
extract
DATE

Expected Output:
------------
26/Apr/2000
------------
"""

print("input data:")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
###########################


print("Extract DATE")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

index_of_square_bracket = input_data.find("[")
start_index = index_of_square_bracket + 1

end_index = input_data.index(":") # index & find are same.
# Only if not found then index() will throw error and find will return -1

dt = input_data[start_index:end_index]
print(dt)

print("#"*40, end="\n\n")
###########################

print("Extract DATE: 2nd Way")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("Splitted Values:", sp, end="\n\n")

raw_date = sp[3] # '[26/Apr/2000:00:23:48'
print("raw_date:", raw_date, end="\n\n")

# ------------------
# Remove only square bracket
# ------------------
raw_date_1 = raw_date[1:] # '26/Apr/2000:00:23:48'
print("raw_date_1:", raw_date_1, end="\n\n")

raw_date_sp = raw_date.split("[")
print("raw_date_sp:", raw_date_sp)
raw_date_2 = raw_date_sp[-1] # '26/Apr/2000:00:23:48'
print("raw_date_2:", raw_date_2, end="\n\n")

raw_date_3 = raw_date.removeprefix("[") # '26/Apr/2000:00:23:48'
print("raw_date_3:", raw_date_3, end="\n\n")
# ------------------

# Get Date
# ------------------

# 1-way
# raw_date_1 = raw_date[1:] # '26/Apr/2000:00:23:48'
raw_date_1_sp = raw_date_1.split(":")
print("raw_date_1_sp:", raw_date_1_sp)
final_date = raw_date_1_sp[0]
print("1-way final_date:", final_date, end="\n\n")

# 2-way
# raw_date_1 = raw_date[1:] # '26/Apr/2000:00:23:48'
index_of_colon = raw_date_1.index(":")
final_date = raw_date_1[0:index_of_colon]
print("2-way final_date:", final_date, end="\n\n")

# 3-way
input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
final_date = input_data[input_data.index("[")+1 : input_data.index(":")]
print("3-way final_date:", final_date, end="\n\n")
# ------------------

print("#"*40, end="\n\n")
###########################