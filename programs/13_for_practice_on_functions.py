"""
Write a function called 'log_process_function'

which takes one argument 'log_file_path'

function should read log file content
then
function should extract ONLY IP
then
function should keep extract IP in list
then
function should return extract info in list

Expected Output:
-------------
Example:
extracted_data = log_process_function("C:\python_training\web_server.log")
print(extracted_data)

It should print below list:
['123.123.123.123', '123.123.123.123', '123.123.123.123', '123.123.123.123', '123.123.123.123', '123.123.123.123']
-------------
"""
my_list = []
def log_process_function(log_file_path):
    my_log_file_handle = open(log_file_path, "r")
    my_log_file_content = my_log_file_handle.readlines()
    for eachline in my_log_file_content:
        if eachline.startswith("123"):
            # print("Each line is :", eachline)
            raw_string = eachline.split()
            ip = raw_string[0]
            my_list.append(ip)

    return my_list

print("Extracted Data")
print("-" * 20)
# ---------------
extracted_data = log_process_function("../log/web_server.log")
print(extracted_data)
print("#"*40, end="\n\n")
###########################