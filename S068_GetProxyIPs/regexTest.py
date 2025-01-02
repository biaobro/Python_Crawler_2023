# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import json

regex_IPSection = r"(?={\"ip)[\s\S]*?}"
regex_IPDetail = r"(?<={\"ip\": \")([\s\S]*?)\", \"last_check_time[\s\S]*?port\": \"([\s\S]*?)\"[\s\S]*?}"

test_str = '''const fpsList = [{"ip": "117.69.232.91", "last_check_time": "2024-03-30 09:30:03", "port": "8089", 
"speed": 270, "location": "\u6dee\u5317\u5e02"}, {"ip": "118.120.230.107", "last_check_time": "2024-03-30 08:30:06", 
"port": "41122", "speed": 204, "location": "\u5fb7\u9633\u5e02"}, {"ip": "183.165.250.112", "last_check_time": 
"2024-03-30 07:30:03", "port": "8089", "speed": 252, "location": "\u6c60\u5dde\u5e02"}, {"ip": "112.51.96.118", 
"last_check_time": "2024-03-30 06:30:03", "port": "9091", "speed": 201, "location": "\u4e09\u660e\u5e02"}, 
{"ip": "180.121.135.177", "last_check_time": "2024-03-30 05:30:03", "port": "8089", "speed": 295, "location": 
"\u5357\u901a\u5e02"}, {"ip": "101.43.76.178", "last_check_time": "2024-03-30 04:30:03", "port": "7890", 
"speed": 252, "location": "\u4e0a\u6d77\u5e02"}, {"ip": "183.166.170.136", "last_check_time": "2024-03-30 03:30:02", 
"port": "41122", "speed": 120, "location": "\u9ec4\u5c71\u5e02"}, {"ip": "180.121.133.123", "last_check_time": 
"2024-03-30 02:30:04", "port": "8089", "speed": 168, "location": "\u5357\u901a\u5e02"}, {"ip": "114.232.110.105", 
"last_check_time": "2024-03-30 01:30:03", "port": "8089", "speed": 259, "location": "\u5357\u901a\u5e02"}, 
{"ip": "180.123.193.157", "last_check_time": "2024-03-30 00:30:09", "port": "8089", "speed": 271, "location": 
"\u5f90\u5dde\u5e02"}, {"ip": "125.79.11.67", "last_check_time": "2024-03-29 23:30:03", "port": "8089", "speed": 255, 
"location": "\u6f33\u5dde\u5e02"}, {"ip": "120.196.207.10", "last_check_time": "2024-03-29 22:30:03", "port": "80", 
"speed": 183, "location": "\u6c5f\u95e8\u5e02"}];'''

# 最初没有找到能够同时提取IP地址和PORT的正则表达式
matches = re.findall(regex_IPSection, test_str, re.MULTILINE)
for match in matches:
    m = json.loads(match)
    print(m['ip'], m['port'])
