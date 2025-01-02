
- 这个案例完全没有思路，如果不看别人的解法，1万年也搞不出来。因为属于全新的知识点。
- 特点在于服务端对Python Request库发出的请求做了识别并过滤，所以 Request拿不到数据
- 参考1：[python爬虫 - 猿人学第十九题突破ja3指纹验证](https://blog.csdn.net/Y_morph/article/details/121893114)
- 参考2：[为什么随机 IP、随机 UA 也逃不掉被反爬虫的命运](https://mp.weixin.qq.com/s/Qx7PjnBgrTR30oCurU6CGw)
- 参考3：[SSL 指纹识别和绕过](https://ares-x.com/2021/04/18/SSL-%E6%8C%87%E7%BA%B9%E8%AF%86%E5%88%AB%E5%92%8C%E7%BB%95%E8%BF%87)
- 参考方案3里给了4个解决办法
  - 第1个是将请求地址设置为ip地址，然后在header的host字段配置域名
  - 第2个是使用代理，如 Fiddler，发起请求时制定代理服务器为 Fiddler 的地址，让代理来做TLS 握手
  - 第3个是放弃requests库（本质是对urllib3的1个封装），改用不使用 urllib 的http request. 也是我们最后实际采用的方案：aiohttp. 另外也测试了 httpx，发现无效
  - 第4个是魔改requests，修改ssl_.py 中定义加密套件部分，就会导致 finger print 和 原本的 requests 不一样，从而避开服务端限制
- 第2个方案配置proxy 的代码
```python
import requests
proxies = {
'http': 'http://127.0.0.1:8080',
'https': 'http://127.0.0.1:8080'
}
rsp=requests.get(url,proxies=proxies)
```