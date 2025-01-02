import datetime
import queue
import re
import requests
import threading
import time

Proxy_89 = 'https://www.89ip.cn/index_{}.html'
Proxy_KDL = 'https://www.kuaidaili.com/free/inha/{}'

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/123.0.0.0 Safari/537.36'
}

fileName = str(datetime.datetime.now()).replace(' ', '-').replace(':', '-').split('.')[0] + '_IPs.txt'
timeName = str(datetime.datetime.now()).split('.')[0]
q = queue.Queue()


def getContent(url, headerParam):
    try:
        res = requests.get(url, headers=headerParam, timeout=5).content.decode()
        if res is not None:
            return res
        else:
            return None
    except:
        return None


def getProxyIP():
    for i in range(1, 2):
        # 89ip 的IP数据是直接在渲染后的html标签中返回的
        con = getContent(Proxy_89.format(i), header)
        if con is not None:
            ips = [':'.join(x) for x in
                   re.findall('<td>\n\t\t\t(\d.*?)\t\t</td>\n\t\t<td>\n\t\t\t(\d.*?)\t\t</td>', con)]
            # print(ips)
            for ip in ips:
                q.put(ip)

        # 快代理 的IP信息是保存在JS代码里，页面需要执行JS代码，才会展示IP信息。所以需要从JS代码中提取
        con = getContent(Proxy_KDL.format(i), header)
        if con is not None:
            # print(con)
            ips = [':'.join(x) for x in re.findall('(?<={\"ip\": \")([\s\S]*?)\", \"last_check_time[\s\S]*?port\": \"([\s\S]*?)\"[\s\S]*?}', con)]
            # print(ips)
            for ip in ips:
                q.put(ip)


def checkProxyIP():
    url = "https://www.baidu.com"
    while not q.empty():
        ip = q.get_nowait()
        proxy = {'http': str(ip)}
        res = requests.get(url, headers=header, timeout=5, proxies=proxy)
        if res.status_code == 200 and '百度一下' in res.content.decode():
            print('[{}] found free IP {}'.format(timeName, ip))
            with open(fileName, 'a+') as f:
                f.write(ip + '\n')


if __name__ == '__main__':
    print('available proxy ip check ...')
    threading.Thread(target=getProxyIP).start()
    time.sleep(2)
    for i in range(3):
        threading.Thread(target=checkProxyIP).start()
