## 

## 思路

### 第1步：对 getData 的返回进行解密

- 在进入 JS 代码前，要先对接口参数、名称、header、返回建立起初步印象
- 然后以 getData 作为关键字进行搜索，就发现了 layout.js 代码中，这个看起来像是执行 post 请求的部分，上面几行非常明显是 post 提交的 payload，还有下面的 response,status 的判断

- 在这里打上断点，发现在 _0x5c879 的位置，从 layout.js 跳到 app.js

![image-20230309152056694](F:\Python\BB-Crawler-2023\S025_ZZZMH\markdown\layout.png)

- app.js 这里的代码页很明显，就是在处理 getData 返回的 result 信息。给每个函数都打上断点

![image-20230309152143632](F:\Python\BB-Crawler-2023\S025_ZZZMH\markdown\app.png)

- 这里是 getData 接口的 response

![image-20230309152307065](F:\Python\BB-Crawler-2023\S025_ZZZMH\markdown\XHR result.png)

- 最终经过 app.js 中这3段代码的处理，得到每张图片（1页上24张）的尺寸和id 信息

![image-20230309221639542](F:\Python\BB-Crawler-2023\S025_ZZZMH\markdown\parse string.png)

![image-20230309221639542](F:\Python\BB-Crawler-2023\S025_ZZZMH\markdown\pic info.png)

- 到这里，第1个堡垒已经被攻破。把这几段 js 代码复制出来，本地执行，发现有个报错 window['atob'] 找不到，搜索发现这个起始就是执行 base64 解码，而本地nodejs 有提供1个全局函数 atob 可以直接使用。使用getData 返回的字符串进行测试，可以得到正确的图片信息。 



### 第2步：获取 cookies

- 因为后面的大图请求中有增加cookies 参数，所以还需要找到 cookies 的来源。于是找到 cookie 最早出现的位置。 这里是向1个地址post 了3个参数，服务器端直接返回的 cookie。

![image-20230309222519502](F:\Python\BB-Crawler-2023\S025_ZZZMH\markdown\cookies.png)

- cookie 请求时提交的参数，前2个看起来就是固定字符串，第3个找了半天在 index 页面中，看起来也是固定值。那就Cookie 页不是问题了

![image-20230309223014592](F:\Python\BB-Crawler-2023\S025_ZZZMH\markdown\cookie payload.png)



![image-20230309223204319](F:\Python\BB-Crawler-2023\S025_ZZZMH\markdown\3rd parameter of cookie payload.png)

### 第3步：请求图片

- 网站提供了2种图片展示形式，
    - 1种是点击列表页上的 Thumb 图片，会在当前窗口展示这张图的大图，最开始走的就是这个路子，但是后来发现得到的图片大小和直接下载的要小很多，再看分辨率也不是前面获取到图片信息中给出的分辨率。所以就改走下载路线
    - 另1种就是点击下载按钮
- 这2种形式共同点是都会先发起1个 https://api.zzzmh.cn/bz/v3/getUrl/+图片ID+21 或者 29 的请求，21是对应展示大图，29是对应下载大图，然后服务端会返回1个302，新的地址在返回的 Response Headers 的 Location 中。**这里需要对 requests.get 增加 allow_redirects = False 的设定**。这里也能看到新的地址中包含了1个 auth_key 信息，是服务端返回的。

![image-20230309224217431](F:\Python\BB-Crawler-2023\S025_ZZZMH\markdown\redirect.png)

- 需要再进一步对这个新的地址发起请求，以获得最终的大图。如果是获取展示的大图，直接将 resp.content 写入jpg 文件即可，如果是获取下载的大图，需要在 headers 中增加参数 headers['Content-Disposition'] = 'attachment'