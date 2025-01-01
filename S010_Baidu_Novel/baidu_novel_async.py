"""
# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
#File               : novel.py
#Project            : Crawler_2022
#CreateTime         : 2022/2/26 11:33
#Author             : biaobro
#Software           : PyCharm
#Last Modify Time   : 2022/2/26 11:33
#Version            : 1.0
#Description        : B站樵夫视频
"""
import asyncio
import aiohttp
import aiofiles
import requests
import json

# 直接打开这个网页，查看源代码，是看不到数据的，意味着数据是通过Ajax异步得到的
url_book = 'https://dushu.baidu.com/pc/detail?gid=4306063500'

# 获取目录的url
# url_catalog = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'

# 获取章节内容的url
# url_chapter = 'https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}'


# 1,获取目录 就1个url 不需要异步 直接用 requests
# 2,获取章节内容 是多个url 需要异步 减少等待时间
async def getCatalog(bid):
    url_catalog = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + bid + '"}'
    resp = requests.get(url_catalog)
    catalogs = resp.json()
    tasks = []
    for item in catalogs['data']['novel']['items']:
        cid = item['cid']
        ctitle = item['title']
        # print(cid, ctitle)

        # 创建任务列表
        tasks.append(asyncio.create_task(getChapter(bid, cid, ctitle)))
    await asyncio.wait(tasks)


async def getChapter(book_id, chapter_id, chapter_title):
    data_param = {
        'book_id': book_id,
        'cid': f"{book_id}|{chapter_id}",
        'need_bookinfo': 1
    }
    data_param = json.dumps(data_param)
    url_chapter = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data_param}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url_chapter) as resp:
            chapter = await resp.json() # 在这里直接拆解字典的话会报错
            async with aiofiles.open(r'data\{}.txt'.format(chapter_title), 'w', encoding='utf-8') as f:
                # 所有异步的操作 需要加 await
                # await 表示挂起，什么时候有东西了 什么时候再读
                await f.write(chapter['data']['novel']['content'])
    print(chapter_title, ' done')


if __name__ == '__main__':
    book_id = '4306063500'

    loop = asyncio.get_event_loop()
    loop.run_until_complete(getCatalog(book_id))
