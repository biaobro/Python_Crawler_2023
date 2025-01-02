# 利用第三方库 webdriver_manager 自动下载 driver

- 业务代码："ChromeDriverManager().install()"  —— 这行代码会初始化 DriverManager ，并执行 install 方法，在执行 install 方法过程中，会通过执行对应系统下的脚本，来获取 Chrome 浏览器的版本
- webdriver_manager 的库文件 "C:\Program Files\Python310\Lib\site-packages\webdriver_manager\core\utils.py" 中，第263 和 第279 行，原先都是 stream.communicate()[0].decode() —— 但这会抛出1个异常：'str' object has no attribute 'decode'
- 经过 Debug 发现， stream.communicate()[0] 得到的浏览器版本，"113.0.5672.93\n" 已经是字符串形式，而字符串是不能被 decode 的。
- 所以这里直接修改了库文件，在 decode 函数前加了 encode() 函数，代码就能正常运行了
- 4月底就遇到这个问题了，直到5月中才静下心来，逐步调试追踪到真正触发报错的代码位置 —— 但是在之前代码都是正常运行的，猜测是浏览器自动升级导致返回信息发生变化？没有再对浏览器做版本回退确认

![](F:\Python\BB-Crawler-2023\S060_Selenium\markdown\1.png)