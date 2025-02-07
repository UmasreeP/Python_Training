"""
From the given string below,
extract
IP
DATE
URL

Expected Output in list of tuples:
------------
[
('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
]
------------
"""

print("Input Data:")
print("-"*20)
# ---------------

input_data = """
First lets look at a fragment of log file....

fcrawler.looksmart.com - - [26/Apr/2000:00:00:12 -0400] "GET /contacts.html HTTP/1.0" 200 4595 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"
fcrawler.looksmart.com - - [26/Apr/2000:00:17:19 -0400] "GET /news/news.html HTTP/1.0" 200 16716 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"

ppp931.on.bellglobal.com - - [26/Apr/2000:00:16:12 -0400] "GET /download/windows/asctab31.zip HTTP/1.0" 200 1540096 "http://www.htmlgoodies.com/downloads/freeware/webdevelopment/15.html" "Mozilla/4.7 [en]C-SYMPA  (Win95; U)"

123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:47 -0400] "GET /asctortf/ HTTP/1.0" 200 8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&width=4&font=digital&noshow HTTP/1.0" 200 36 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

(Note, I've added some space for clarity, and changed the IP number to 123.123.123.123 to protect the privacy of the actual visitor)

The fragment shown represents three visitors to my web site
"""

print(input_data)

print("#"*40, end="\n\n")
###########################


print("List of lines")
print("-"*20)
# ---------------

list_of_lines = input_data.splitlines() # no need to provide \n
print(list_of_lines)

print("#"*40, end="\n\n")
###########################

print("Extract IP and DATE")
print("-"*20)
# ---------------
# expected output=[(ip,dt,url),(ip,dt,url),(ip,dt,url),]
output_list = []
for each_line in list_of_lines:
    if each_line.startswith("123"):
        sp = each_line.split()
        ip = sp[0]
        dt = each_line[each_line.index("[") + 1: each_line.index(":")]
        raw_url = sp[10]
        url = raw_url[1:-1]
        each_line_tuple = (ip, dt, url)
        output_list.append(each_line_tuple)

print(output_list)

print("#"*40, end="\n\n")
###########################

print("writing to 'log_report.json'")
print("-"*20)
# ---------------

my_json_file_handle = open('log_report.json', 'w')
# new file 'log_report.json' will be created

import json
json.dump(output_list, my_json_file_handle) # write to json file

my_json_file_handle.close()

print("""
'log_report.json' file created,
Please check
""")
print("#"*40, end="\n\n")
###########################

print("Reading 'log_report.json'")
print("-"*20)
# ---------------

my_json_file_handle = open('log_report.json', 'r')
# mode=r -> read

import json
json_file_content = json.load(my_json_file_handle)

my_json_file_handle.close()

print("json_file_content:", json_file_content, end="\n\n")
print("type of json_file_content:", type(json_file_content), end="\n\n")

print("#"*40, end="\n\n")
###########################