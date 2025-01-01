# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : ctbpsp.py
@Project            : S037_Ctbpsp
@CreateTime         : 2023/3/15 23:23
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/15 23:23 
@Version            : 1.0
@Description        : None
"""
import csv
import requests
import execjs

url_web = "https://ctbpsp.com/#/"
# url_req = "https://custominfo.cebpubservice.com/cutominfoapi/platformInfo"
# url_req = 'https://custominfo.cebpubservice.com/cutominfoapi/categoryTreeQuery/categoryId/0'


def get_single_page(page, writer):
    # 最后的数字表示页码，但是页面上没展示总页数或条数，也没见有接口返回
    url_req = 'https://custominfo.cebpubservice.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/' + str(page)
    print(url_req)
    resp = requests.get(url_req)

    # resp.text 是自带引号的，解码时需要去掉
    # print(resp.text)

    ctx = execjs.compile(open('utils.js', 'r', encoding='utf-8').read())
    decrypt_data = ctx.call('decryptData', resp.text.replace('\"', ''))
    # print(decrypt_data)

    records = decrypt_data['data']['dataList']
    print(f'page {page} grab done.')

    # 写入数据，因为用了 DictWriter，所以可以直接把 字典列表写入 csv
    writer.writerows(records)

    # for idx, record in enumerate(records):
    #     print(idx, record)


if __name__ == '__main__':
    csvHeaders = ['bulletinID', 'tenderProjectName', 'noticeName', 'noticeMedia', 'bulletinTypeName', 'docGetEndTime',
                  'bidDocRefferEndTime', 'bidOpenTime', 'notieIndustriestName', 'reginProvince', 'serverPlat',
                  'tradePlat', 'dataPlat', 'regionCode', 'regionName', 'noticeSendTime', 'bulletinSource', 'noticeUrl',
                  'superviseDeptName', 'leftOpenBidDay', 'platformCode', 'platformName', 'commentCount', 'hot',
                  'viewCount', 'favCount', 'subscriptionCount', 'tenderBidder', 'tenderAgency', 'isNew', 'grade',
                  'dataSource',
                  'potentialBidderDetails', 'classifyName', 'classifyCode', 'subcription', 'similarProjectsBidInfo',
                  'fav', ]

    # newline是数据之间不加空行
    with open('data.csv', 'a', newline='', encoding='utf-8-sig') as f:
        # 提前预览列名，当下面代码写入数据时，会将其一一对应。
        writer = csv.DictWriter(f, fieldnames=csvHeaders)

        # 写入列名
        writer.writeheader()

        # 页码从1开始
        for i in range(1, 3):
            get_single_page(i, writer)
