# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : referer.py
@Project            : Crawler_2022
@CreateTime         : 2022/2/28 22:44
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2022/2/28 22:44
@Version            : 1.0
@Description        : B站樵夫视频
    # 重点
    1，在视频播放页面，F12 Elements 代码中是可以找到 <video> 标签的，也有对应视频地址，复制到新窗口也能播放
    2，但是在页面源代码中，没有 <video> 标签，说明这个 <video> 标签以及内容，是通过JS动态生成的
    3，切换到 Network - Fetch/XHR , 可以看到如图的请求过程
    4，请求中必须包含 Referer，网站做了防盗链

"""
import requests

urlPage = 'https://www.pearvideo.com/video_1752635'
countId = urlPage.split('_')[1]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Referer': urlPage
}

# 获取video 的是个 xhr 请求
# mrd 是个随机变化的数字
urlVideoStatus = 'https://www.pearvideo.com/videoStatus.jsp?contId={}&mrd=0.2216788115654671'.format(countId)
respVideoStatus = requests.get(urlVideoStatus, headers=headers)

# 从返回信息中得到视频信息 并拼接出地址
videoStatus = respVideoStatus.json()
systemTime = videoStatus['systemTime']
videoSrcUrl = videoStatus['videoInfo']['videos']['srcUrl']
videoSrcUrl = videoSrcUrl.replace(systemTime, f'cont-{countId}')
print(systemTime, videoSrcUrl)

# 请求视频url 地址，content 对应 b 写入方式
with open(r'data\{}.mp4'.format(countId), 'wb') as f:
    f.write(requests.get(videoSrcUrl).content)
