# 解题思路

- 这题也是，自己研究最多追到 JS 代码，就走不下去了。最后还是参考前人的[文章](https://blog.csdn.net/Ig_thehao/article/details/125432643) 搞出来。



## 解法1：追代码

- JS 代码追踪 Payload 赋值位置

![](F:\Python\BB-Crawler-2023\S044_YuanRenXue\20\screenshot\1.png)



- JS 代码追踪 Sign 函数，调用的 wasm 代码。这里记录 var55 和 var56 的值

![](F:\Python\BB-Crawler-2023\S044_YuanRenXue\20\screenshot\2.png)



- 回到 JS 代码，选中 getStringFromWasm0(r0, r1) 部分，可以看到最终的 sign 已经生成。此时在 console 端口中输入 getStringFromWasm0(1114192， 31) —— 1114192和31 是 var55 和 var56 的值，1个代表内存地址，1个代表偏移量，表示从这个地址取这个长度的字符 —— 可以看到后面加了1串固定的字符串，也就是传说中的 md5 的盐？

![](F:\Python\BB-Crawler-2023\S044_YuanRenXue\20\screenshot\3.png)

- 这道题的难点在于 wasm 代码



## 解法2：JSRPC

- JSRPC 之前看过不得其法，今天实验1把。原理是在浏览器控制台新建一个[WebScoket](https://so.csdn.net/so/search?q=WebScoket&spm=1001.2101.3001.7020)客户端链接到服务器通信，调用服务器的接口，服务器会发送信息给客户端，客户端接收到要执行的方法，执行完js代码后，把获得想要的内容发回给服务器，服务器接收到后再显示出来。
- [GitHub 项目地址](https://github.com/jxhczhl/JsRpc#jsrpc-hliang)
- [参考文章](https://blog.csdn.net/qq_43308242/article/details/123132695)
    - 需要准备2个东西，1个是项目中 **resources** 中的JS 代码，1个是作者编译好的exe文件
    - 第1步，运行 exe 文件，建议在文件夹中右键选择在终端中打开，然后从命令行唤起
    - 第2步，进入浏览器 Console，输入JS代码
    - 第3步，运行Python 代码