# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : producer_consumer.py
@Project            : S021_csres
@CreateTime         : 2023/2/25 10:15
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/25 10:15 
@Version            : 1.0
@Description        : None
"""
import queue
import csres
import time
import random
import threading


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = csres.craw(url)
        html_queue.put(html)
        print(threading.current_thread().name, f"craw {url}",
              "url_queue.size = ", url_queue.qsize())
        time.sleep(random.randint(1, 2))
        if url_queue.empty():
            break


def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        results = csres.parse(html)
        for result in results:
            fout.write(str(result))
        # 因为parse 返回的是字符串，所以这里的len(results) 是字符串长度
        # 实际每个页面共40条数据
        print(threading.current_thread().name, "results.size", len(results),
              "html_queue.size = ", html_queue.qsize())
        time.sleep(random.randint(1, 2))
        if html_queue.empty():
            break


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()

    for url in csres.urls:
        url_queue.put(url)

    for idx in range(3):
        tc = threading.Thread(target=do_craw, args=(url_queue, html_queue),
                              name=f"craw{idx}")
        tc.start()

    fout = open("data.txt", "w", encoding='utf-8')
    for idx in range(5):
        tp = threading.Thread(target=do_parse, args=(html_queue, fout),
                              name=f"parse{idx}")
        tp.start()
