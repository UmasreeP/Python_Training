"""
Parse and print complete Head tag
"""

print("Get data from website and print")
print("-"*20)
# ---------------

import urllib.request as u

my_web_file_handle = u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")
web_content = my_web_file_handle.read()
my_web_file_handle.close()

#print(web_content)

print("#"*40, end="\n\n")
###########################

print("create Beautifulsoup class object with web_content")
print("-"*20)
# ---------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
#print(soup)

print("#"*40, end="\n\n")
###########################

print("Getting head tag data")
print("-"*20)
# ---------------

log_head_data = soup.head
print("log_head_data:", log_head_data.prettify)
print("title:", log_head_data.title.prettify)

print("#"*40, end="\n\n")
###########################
