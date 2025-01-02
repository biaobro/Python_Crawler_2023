# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : match_19_requests_fiddler.py
@Project            : S044_YuanRenXue
@CreateTime         : 2023/4/14 13:12
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/14 13:12 
@Version            : 1.0
@Description        : 使用这个方案时，需要开启Fiddler
"""
import requests

cookies = {
    'qpfccr': 'true',
    'sessionid': '4gjc34du341pmcs3lmvljedgpbmgd69k',
    'Hm_lvt_9bcbda9cbf86757998a2339a0437208e': '1681345200,1681375667,1681441168,1681443685',
    'Hm_lvt_c99546cf032aaa5a679230de9a95c7db': '1681375648,1681441135,1681443099,1681446750',
    'Hm_lpvt_c99546cf032aaa5a679230de9a95c7db': '1681446750',
    'no-alert3': 'true',
}

headers = {
    'authority': 'match.yuanrenxue.cn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'qpfccr=true; sessionid=4gjc34du341pmcs3lmvljedgpbmgd69k; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1681345200,1681375667,1681441168,1681443685; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1681375648,1681441135,1681443099,1681446750; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1681446750; no-alert3=true',
    'pragma': 'no-cache',
    'referer': 'https://match.yuanrenxue.cn/match/19',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.get('https://match.yuanrenxue.cn/api/match/19', headers=headers, verify=False)
print(response.text)



