"""
Get data from web_server.log file

then

Extract
IP
DATE
URL

then

produce below dictionary and write that dictionary to log_report_4.json

Dictionary should be like
----------
{
0:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
1:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
2:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
3:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
4:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
5:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/')
}
----------
"""
print("Get data from web_server.log file")
print("-"*20)
# -------------

my_log_file_handle = open(r"../log/web_server.log", 'r')
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
############################

print("Extract and create dictionary")
print("-"*20)
# -------------
output_dictionary = {}
key = 0
for each_line in log_file_content:
    if each_line.startswith("123"):
        sp = each_line.split()
        # print("sp:", sp)

        ip = sp[0]

        raw_date = sp[3] # '[26/Apr/2000:00:23:48'
        dt = raw_date[1:raw_date.index(":")]

        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        url = raw_url[1:-1]

        each_line_tuple = (ip, dt, url)
        output_dictionary[key] = each_line_tuple
        key = key + 1

print(output_dictionary)

# Example:
#
# >>> D = {}
# >>>
# >>> D[0] = (10,20)
# >>> D[1]=(10,20)
# >>> D
# {0: (10, 20), 1: (10, 20)}

print("#"*40, end="\n\n")
############################

print("write to log_report_4.json")
print("-"*20)
# -------------

my_json_file_handle = open("log_report_4.json", "w")

import json
json.dump(output_dictionary, my_json_file_handle)

my_json_file_handle.close()

print("Created log_report_4.json, please check")

print("#"*40, end="\n\n")
############################