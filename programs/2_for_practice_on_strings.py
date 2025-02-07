"""
From the given string below,
extract
PICS

Expected Output:
------------
wpaper.gif
------------
"""

print("input data:")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)
start_index = input_data.find("/pics/") + len("/pics/")
end_index = input_data.find(" HTTP", start_index)
pic_url = input_data[start_index:end_index]
print("image url is :", pic_url)

print("#"*40, end="\n\n")
###########################

