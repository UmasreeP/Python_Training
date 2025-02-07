"""
From the given string below,
extract
IP

Expected Output:
------------
123.123.123.123
------------
"""

print("input data:")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
###########################

print("type of input data:")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(type(input_data))

print("#"*40, end="\n\n")
###########################

print("Extract IP: 1-WAY: PARTIAL")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
ip = input_data[0:15]
print(ip)

print("#"*40, end="\n\n")
###########################

print("Extract IP: 2-WAY")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
index_of_1st_space = input_data.find(" ")
ip = input_data[0:index_of_1st_space]
print(ip)

# Example
# >>> # About 'find()' method
# >>> # Feature-1
# >>> s = "WEL COME"
# >>> s.find("E")
# 1
# >>> # Returns index of 1st occurance
# >>>
# >>> # Feature-2
# >>> s = "WEL COME"
# >>> s.find("E", 4) # Start looking from index-4 onwards
# 7
# >>> # Feature-3
# >>> s = "WEL COME"
# >>> s.find("COME")  # Returns index of 'C'
# 4
# >>>
# >>> # Feature-4
# >>> s = "WEL COME"
# >>> s.find("XYZ") # Returns -1 if not found
# -1
# >>> # NOTE: index() method is similar to find, only difference if not found then index will throw error
# >>> # find will return -1

print("#"*40, end="\n\n")
###########################

print("Extract IP: 3-WAY")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = input_data.split()
print("splitted Values:", sp, end="\n\n")

ip = sp[0]
print("ip:", ip)

# Example:
# >>> # About 'split()' method
# >>> # Feature-1
# >>> s = "WEL COME"
# >>> sp = s.split() # split by SPACE
# >>> sp
# ['WEL', 'COME']
# >>>
# >>> # Feature-2
# >>> s = "WEL COME"
# >>> sp = s.split("E")
# >>> sp
# ['W', 'L COM', '']
# >>>
# >>> # Feature-3
# >>> sp = s.split("OM")
# >>> sp
# ['WEL C', 'E']
# >>>

print("#"*40, end="\n\n")
###########################