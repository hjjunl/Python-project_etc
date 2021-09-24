import subprocess
import re

sep_index = " ", "\\", '[', ']'  # index separator

def custom_split(separator, str_to_split):
    # create regular expression dynamically
    regular_exp = '|'.join(map(re.escape, separator))
    return re.split(regular_exp, str_to_split)


data_list = []

proc = subprocess.Popen(['tracert', 'google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# -h 는 최대 홉스 수 결정
# subprocess를 통해 받은 데이터
test = proc.communicate()
# 튜플형태
test = str(test[0])

# 받은 ip 주소 list ex
ip_list = ["10.141.205.254", "172.217.174.206", "10.141.7.9", \
           "10.141.7.33", "10.141.254.1", "203.248.140.1", "123.140.0.113"]
no_ip_list = []
for i in ip_list:
    if i in test:
        print("There is ip: " + i)
    else:
        no_ip_list.append(i)
        print("No ip: " + i)

for i in no_ip_list:
    print("No ip: " + i)

# 문자열 split
test = custom_split(sep_index, test)
for i in test:
    if i.count(".") == 3 or "com" in i:
        data_list.append(i)
data_list[0] = data_list[0][1:]
print(data_list)
