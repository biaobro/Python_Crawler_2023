## 思路

- 找到接口

![interface](F:\Python\BB-Crawler-2023\S029_EnData\markdown\interface.png)

- 查看Initiator，找到请求发起

![request init](F:\Python\BB-Crawler-2023\S029_EnData\markdown\request init.png)

- 找到请求的返回处理

![response process](F:\Python\BB-Crawler-2023\S029_EnData\markdown\response process.png)

- 处理方法，关联代码太多，可以考虑把整个 webDES.min.js 代码拷贝。JS 代码中有判断 navigator 属性（userAgent)，以决定返回值，所以本地执行的话需要补齐 navigator
