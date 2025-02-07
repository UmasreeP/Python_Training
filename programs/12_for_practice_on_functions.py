"""
Write a function called 'log_process_function'

which takes one argument 'log_file_path'

function should read log file content
then
function should extract info
then
function should keep extract info in dictionary
then
function should return extract info in dictionary

Expected Output:
-------------
Example:
extracted_data = log_process_function("C:\python_training\web_server.log")
print(extracted_data)

It should print below dictionary:
{
0:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
1:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
2:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
3:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
4:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
5:('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
}
-------------
"""

def log_process_function(log_file_path):
    my_log_file_handle = open(log_file_path, "r")
    my_log_file_content = my_log_file_handle.readlines()
    my_dict = {}
    key = 0
    for eachline in my_log_file_content:
        if eachline.startswith("123"):
            # print("Each line is :", eachline)
            raw_string = eachline.split()
            ip = raw_string[0]
            dt_start_index = eachline.find("[")+1
            dt_end_index = eachline.find(":")
            dt = eachline[dt_start_index:dt_end_index]
            raw_url = raw_string[10]
            url = raw_url[1:-2]
            my_dict[key] = (ip, dt, url)
            key = key+1
            # print(ip, dt, url, end ="/n/n")

    return my_dict

print("Extracted Data")
print("-" * 20)
# ---------------
extracted_data = log_process_function("../log/web_server.log")
print(extracted_data, end="/n/n")
print("#"*40, end="\n\n")
###########################