"""
Using regular expression, pull below information

Seconds     Http Method     HTTP/Version        Status Code         m/c type
23          GET             1.0                 200                 Macintosh
23          GET             1.0                 200                 Macintosh
23          GET             1.0                 200                 Macintosh
23          GET             1.0                 200                 Macintosh
23          GET             1.0                 200                 Macintosh
23          GET             1.0                 200                 Macintosh
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

print("Extract Seconds, Http, Version, type, etc.,")
print("-"*20)
# ---------------

import re

for each_line in log_file_content:

    #match_result = re.search(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[A-Za-z]{3}/\d{4}):\d{2}:(\d{2}):\d{2}.*', each_line)
    # OR
    match_result1 = re.search(r':\d{2}:(\d{2}):\d{2}.*]', each_line) #23 seconds
    match_result = re.search(r':\d{2}:(\d{2}):\d{2}.*].*"([A-Z]{3}).*/[a-z]{4}/([a-z0-9.]{})', each_line)
    if match_result is not None:
        seconds = match_result.group(1)
        Http_Method = match_result.group(2)
        HTTP_Version = match_result.group(3)
        Status_Code = match_result.group(1)
        mc_type = match_result.group(1)
        print("seconds:", seconds, end="\n")
        print("http_method:", Http_Method, end="\n")
        print("http_version:", HTTP_Version, end="\n")


print("#"*40, end="\n\n")
###########################
