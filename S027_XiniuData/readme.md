# 逆向思路

- 这个案例的关键点是请求表单payload加密 和 返回体加密
- 请求头

![XHR request payload](F:\Python\BB-Crawler-2023\S027_XiniuData\markdown\XHR request payload.png)

- 先纵览 Initiator，有2个 js 文件，在 industry-newest.js 中扫到了接口名称，而且是被 fetch，应该就是从这里发起请求。打上断点，然后调试。在这里构造了 a 变量，包含 sort,start,limit

![XHR request start](F:\Python\BB-Crawler-2023\S027_XiniuData\markdown\XHR request start.png)

- 代码来到了 common.js，在这里生成了加密的 payload 和 sig，内部添加默认参数是 sort，start，limit，start 应该是已经加载的数量，limit 就是本次请求数量

![XHR payload encrypt](F:\Python\BB-Crawler-2023\S027_XiniuData\markdown\XHR payload encrypt.png)



- 代码会一直往下执行，然后发现一大串字符被解密，

![XHR result parse](F:\Python\BB-Crawler-2023\S027_XiniuData\markdown\XHR result parse.png)



- 顺带研究了下 payload 是受哪里控制的，看起来是每请求1次，this.state 就会相应增加

![params](F:\Python\BB-Crawler-2023\S027_XiniuData\markdown\params.png)



- 最后遇到1个问题，请求得到的字符串，直接放到 JS 代码里是能够成功解析的，但是通过 execjs.call(函数，参数) 传过去就一直报错：UnicodeEncodeError: ‘gbk‘ codec can‘t encode character —— 最后借鉴了这位网友的[方案](https://blog.csdn.net/BraveMrJ/article/details/124131064)，修改了库文件 C:\Program Files\Python310\Lib\subprocess.py，将 encoding=None 改为 encoding='utf-8' 
- 可以确认的是，和 JS 代码里后补的 中文注释没关系，应该是因为解码后的内容中包含中文导致的

![response](F:\Python\BB-Crawler-2023\S027_XiniuData\markdown\response.png)