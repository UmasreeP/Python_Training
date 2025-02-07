"""
Develop a class called 'LogProcessClass'
with below methods

1. get_all_ips method
2. get_all_records method
3. to_txt method
4. to_json method

Example: We are planning use class like this

l1 = LogProcessClass(r"../log/webserver.log")
ips_list = l1.get_all_ips()
print("ips_list:", ips_list) # [ip, ip, ip, ip]
all_records_list = l1.get_all_records()
print("all_records_list:", all_records_list) # [(ip, dt, url),(ip, dt, url),]
l1.to_txt("myreport.txt") # -> this should write to file
l1.to_json("myreport.json") # -> this should write to file

"""

class LogProcessClass:


    def get_all_ips(self, log_file_path):
        my_list = []
        my_log_file_handle = open(log_file_path, "r")
        my_log_file_content = my_log_file_handle.readlines()
        for eachline in my_log_file_content:
            if eachline.startswith("123"):
                # print("Each line is :", eachline)
                raw_string = eachline.split()
                ip = raw_string[0]
                my_list.append(ip)
        return my_list
    def get_all_records(self, log_file_path):
        my_list1 = []
        my_log_file_handle = open(log_file_path, "r")
        my_log_file_content = my_log_file_handle.readlines()
        for eachline in my_log_file_content:
            if eachline.startswith("123"):
                # print("Each line is :", eachline)
                raw_string = eachline.split()
                ip = raw_string[0]
                dt_start_index = eachline.find("[") + 1
                dt_end_index = eachline.find(":")
                dt = eachline[dt_start_index:dt_end_index]
                raw_url = raw_string[10]
                url = raw_url[1:-2]
                tuple_list = (ip, dt, url)
                my_list1.append(tuple_list)
        return my_list1
    def to_json(self, filename):
        my_json_file_handle = open(filename, 'w')
        import json
        json.dump(ips_list, my_json_file_handle)  # write to json file
        print("JSON updated, please check")
        my_json_file_handle.close()
    def to_txt(self, filename):
        my_out_file_handle = open(filename, "w")
        # print(all_records_list, sep="\t", file=my_out_file_handle)
        for item in all_records_list:
            my_out_file_handle.writelines(str(item)+"\n")
        print("Text file Updated, Please check")
        my_out_file_handle.close()

l1 = LogProcessClass()
ips_list = l1.get_all_ips("../log/web_server.log")
all_records_list = l1.get_all_records("../log/web_server.log")
print(ips_list, all_records_list)
l1.to_txt("myreport.txt") # -> this should write to file
l1.to_json("myreport.json") # -> this should write to file



