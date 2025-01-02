# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : spots.py
@Project            : S061_GaoDe
@CreateTime         : 2023/5/10 12:55
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/5/10 12:55 
@Version            : 1.0
@Description        : None
"""
import requests

cookies = {
    'guid': '535e-7a64-bec2-0289',
    'cna': '6RHiHO8a31kCAd9HLX6MNVY8',
    'xlly_s': '1',
    '_uab_collina': '168369457412578830656993',
    'tfstk': 'c37hBb1SPM-QTSaRC9TQRE7kVxYhZVZeda7N77xMUIFlvHbNivmZ0eETspebL01..',
    'l': 'fBNaDS0nNu80_FgvBO5aPurza77tnIRb8sPzaNbMiIEGa6YFgFZzqNC_IPUezdtjgTCAMeKrtWFbsdHpJszdgsFuuNPhhKC1CxJT48EBs',
    'isg': 'BLa2zVeozlpfeLo-c-XpUnzhB-y41_oRPlgAXSCfJRk0Y1f9iWepIXhVfz8PS_Ip',
}

headers = {
    'authority': 'ditu.amap.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'amapuuid': '1dc47a86-b2aa-4bfa-a845-319b8aa254bd',
    'bx-ua': '225!lrSjKpzWooizL6exiieog+mX3eDS1onm2nsqJbutV0yWt4hFMcK5XWS0Cr6m/ACc6YD8Drak+i7lN0OFFFu7CaIc1wnFRtCb303rhMD9OiViyozlb34djxf/oLnjDUHofeG92C3OeyKcIZECJU4KjcI4+cn04mBGsx6Ruo0dDMXhfidCbU4KjcI40J36DGJTx4MOukaKD6X4BidlbUSScPE3b4D840mIpBeLuN6kXAgj1ZgeD0luMAmnyqa+e3/+1bfWQE0dDMX4fidlbUSKjxI3oLiRM3l6Jl3oxD0NSPgcOtKVdk3kA5vngnRUbkyRQMlPpalObrOcGK+3dv3YA7JD4VuhVNN884D8OC9R47EMvNZ00f3kcBv9JeSthOFj6YWOfp4R/XzCGIm3KDDNw8Ihn9oiVZv284eCvaTNH22qfdKF+NCYYAF04bYDgOLO6YaPvD6lbsPju+s93ESqqJ8yecDZVvXuBwqGpoa74gzYvkXgZkT66Jktbxi+4FXABP6vQE0dDM5hfodCgaQdjxf4oLZwilgnOk6n9TcLmO0mUya7ExbbXjv1BJFm1H74VeU8QVy3YHKHiBStMZumJrRNsOuex/0QoePOs+/zw6aQS83W/FQb8+sMoR9nBlAXE3w1uhvWJp4tcOpZIjBGFG0j75/PxFJ1Bq72GxfHmVe1acjj+dVF2SpTWeIXRLt8Ev5NjdYycE8eKiBtQcXESJnawdWgU99qLARuUkmc3l1UE1N5qaiNIewGTKbupPq8HR+akvSPkG+0zDT25RGGDTp0PiCDw4go2vbF9g1dou+pehJf40/unxbh6ulzZjEeobUTu8YzJHvnUWIYnMSGPF7LVNk0qJYs52doek5+wibWeVPlBTIGrTHecPxT9LX9G3yX27i+jGha+MjNv+eXTBVA5oEkkkxY8gwYOYn5lQn00LbC3GY3aZ4+5PUX6XXokttkC8O7l7iwfGYSoAgVKw6lqGTaXL21gu4iGoHf+uboUSdVkfG10hIMaV32TZkxbkqETo9iPGBW3H3oH0kuVH6ROalKge+U+is2Dz+zpHwtXhFH4SIi7tqb6hOG8VhRKZzAn9mBq4x+CVnZoSdTWHhS/n+OCvdxphMdtAGEhZ1Q7Xl1skYR5b7OWpWicVPVWJT76nZLcOawOuPj3CTlLC5+hc4vmhKiW4KCdHVkz5gkbs9wzDgJ',
    'bx-umidtoken': 'GAD8E406A841840DB2A31BE167F45AF9648C9CF7347C90CEBC8',
    'bx-v': '2.2.3',
    'cache-control': 'no-cache',
    # 'cookie': 'guid=535e-7a64-bec2-0289; cna=6RHiHO8a31kCAd9HLX6MNVY8; xlly_s=1; _uab_collina=168369457412578830656993; tfstk=c37hBb1SPM-QTSaRC9TQRE7kVxYhZVZeda7N77xMUIFlvHbNivmZ0eETspebL01..; l=fBNaDS0nNu80_FgvBO5aPurza77tnIRb8sPzaNbMiIEGa6YFgFZzqNC_IPUezdtjgTCAMeKrtWFbsdHpJszdgsFuuNPhhKC1CxJT48EBs; isg=BLa2zVeozlpfeLo-c-XpUnzhB-y41_oRPlgAXSCfJRk0Y1f9iWepIXhVfz8PS_Ip',
    'pragma': 'no-cache',
    'referer': 'https://ditu.amap.com/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'x-csrf-token': 'null',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'query_type': 'TQUERY',
    'pagesize': '20',
    'pagenum': '1',
    'qii': 'true',
    'cluster_state': '5',
    'need_utd': 'true',
    'utd_sceneid': '1000',
    'div': 'PC1000',
    'addr_poi_merge': 'true',
    'is_classify': 'true',
    'zoom': '8.96',
    'city': '110000',
    'geoobj': '115.369101|39.30516|118.342498|40.563815',
    '_src': 'around',
    'keywords': '景点',
}

resp = requests.get('https://ditu.amap.com/service/poiInfo', params=params, cookies=cookies, headers=headers)
# print(resp.text)

spots = resp.json()['data']['poi_list']

for spot in spots:
    print(spot)

