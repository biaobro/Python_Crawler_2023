# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : soundsnap.py
@Project            : S053_SoundSnap
@CreateTime         : 2023/4/25 16:13
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/4/25 16:13
@Version            : 1.0
@Description        : None
"""
import json
import time
import requests
import re


url_web = "https://www.soundsnap.com/tags/baby_cry"
headers = {
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'referer': 'https://www.soundsnap.com/',
    'origin': 'https://www.soundsnap.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}
session = requests.Session()
session.headers.update(headers)
# 先 get 请求页面地址，收获 cookies
session.get(url_web)

url = "https://ts231.search-soundsnap.com/multi_search?x-typesense-api-key=U3NpSjF4TC9tN1ZJTnprb1hlUnFObkMrMjBzSEgxOUloQi9rSE4yTlgyVT1TTU9NeyJmaWx0ZXJfYnkiOiJwdWJsaXNoZWQ6MSAmJiB0eXBlOltcImF1ZGlvXCIsIFwibXVzaWNcIl0iLCJleGNsdWRlX2ZpZWxkcyI6ImNyZWRpdHMub3duZXJzaGlwLGNyZWRpdHMuY3JlZGl0LGNyZWRpdHMucHJvX3dyaXRlcl9pcGksY3JlZGl0cy5wdWJsaXNoaW5nX2Rlc2lnbmVlLGNyZWRpdHMucHVibGlzaGluZ19kZXNpZ25lZV9pcGksY3JlZGl0cy5kaXN0cmlidXRpb24iLCJoaWdobGlnaHRfZmllbGRzIjoidGl0bGUsIGJvZHksIHVzZXIubmFtZSwgdm9jYWIuY2F0ZWdvcnkubHZsLjAsIHZvY2FiLmNhdGVnb3J5Lmx2bC4xLCB2b2NhYi50YWcubmFtZSwgdm9jYWIucGxheWxpc3QuYXVkaW8ubmFtZSwgdm9jYWIuZ2VucmUubHZsLjAsIHZvY2FiLmdlbnJlLmx2bC4xLCB2b2NhYi5wbGF5bGlzdC5iZWF0Lm5hbWUsIHZvY2FiLnNpbWlsYXJfdG8ubmFtZSwgdm9jYWIubW9vZC5uYW1lLCB2b2NhYi5pbnN0cnVtZW50Lm5hbWUsIHZvY2FiLmF0dHJpYnV0ZS5uYW1lLCB2b2NhYi5wbGF5bGlzdC5tdXNpYy5uYW1lIn0%3D"

# payload 中包含了 page 参数
payload = {
"searches":
    [{
        "facet_by": "user.name,vocab.category.lvl.0,vocab.category.lvl.1,vocab.tag.name,libraryFacet,"
                    "audio.playTime",
        "query_by": "vocab.tag.name", "query_by_weights": "1", "q": "baby cry", "collection": "prod",
        "per_page": 15, "search_cutoff_ms": 1000, "max_facet_values": 234,
        "filter_by": "vocab.tag.name:`baby cry` && type:=audio", "page": 19,
        "sort_by": "_text_match:desc,fairness:desc"}]
}

# 然后 post 请求 ajax 地址，得到包含 音频信息的html， 注意jsons.dumps 不可少
resp = session.post(url, data=json.dumps(payload))
html = resp.text
print(html)

# 默认每个页面包含15个音频信息block
regex_document = r"document\":{[\s\S]*?\"text_match"
documents = re.findall(regex_document, html)
print(f"get {len(documents)} music documents")

# 从每个 block 中提取每个音频对应的信息，以及音频的地址
for idx, document in enumerate(documents):
    regex_bitrate = r"audio\.bitrate\":(\d+),"
    bitrate = re.findall(regex_bitrate, document)[0]

    regex_bitsPerSample = r"audio\.bitsPerSample\":(\d+),"
    bitsPerSample = re.findall(regex_bitsPerSample, document)[0]

    regex_sampleRate = r"audio\.sampleRate\":(\d+),"
    sampleRate = re.findall(regex_sampleRate, document)[0]

    regex_channel = r"audio\.channels\":\"(.*?)\""
    channel = re.findall(regex_channel, document)[0]

    regex_filepath = r"audio\.filepath\":\"(.*?)\""
    filepath = re.findall(regex_filepath, document)[0]

    filepath = filepath.split(".")[0].lower()
    if "cry" not in filepath:
        if "cries" not in filepath:
            print(f'no keyword in {filepath}, skip it')
            continue

    # 网站的原始逻辑，无论filepath 是不是 mp3，统一替换成 mp3 进行请求
    url = "https://www.soundsnap.com/play?t=e&p=" + filepath + ".mp3"
    # print(url)
    # 这个请求会返回1个302，同时在 Response Headers 中包含了跳转的地址
    resp = session.get(url, allow_redirects=False)
    url_location = resp.headers.get('location')
    print(url_location)

    # Todo: 这里会产生1个问题，session 在这个内部 for 循环内是可以共用的。内部 for 循环结束后，进入到外部 for 循环，开启下一页时， session 不能继续使用
    # 因为 url_location 的域名 和 前面不一样？

    # 这个 url_location 对应的是 attachment 下载方式，所以需要调整 header
    headers['Content-Disposition'] = 'attachment'
    resp = session.get(url_location)

    filename = filepath.split('/')[-1] + ".mp3"
    with open(filename, mode='wb') as f:
        f.write(resp.content)
        print(filename + ' has been saved.')

    time.sleep(5)
