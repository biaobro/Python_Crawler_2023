# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : lagou_selenium.py
@Project            : S016_lagou
@CreateTime         : 2023/2/7 11:48
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/7 11:48 
@Version            : 1.0
@Description        : B站樵夫视频

    # 知识点
    1，selenium webdriver

    # 思路
    1，selenium 模拟人的行为，点击按钮，输入信息等，直到找到目标

    # 目标：拉勾网
    1，https:www.lagou.com 1个有意思的地方是，在职位列表上，每个职位所在的a标签，在网页源代码里是看不到href的。
    猜测是通过页面的 mouse click 事件，动态生成
    2，selenium 的好处就是完全忽略上面这个逻辑，和人的真实操作一样，找到a标签，点击即可

    # 注意点
    1，因为是拟人操作，所以需要关注每步操作之间的延迟，否则报错
    2，抓到12页之后就会触发登录 （数字貌似和操作速度有关，即使真人操作，也会触发，但目前测到的最大数字就是12）
    3，登录页面除了输入用户名密码，还涉及到图片验证
    4，延迟5s是目前测得的最合理值，3s就很快触发登录

"""
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

import init_webdriver

# 默认下载路径 "..\.wdm\drivers\chromedriver"
# ..\\ 表示当前目录的上级目录

folder_name = r'..\\'
file_name = r'chromedriver.exe'

driver_path = init_webdriver.driver_seek(folder_name, file_name)
if driver_path is None:
    driver_path = r'..\\'
    init_webdriver.driver_download(driver_path)

options = webdriver.ChromeOptions()
# options.add_argument(r"--headless")
# options.add_argument(r"user-data-dir=data")

keyword = "python"

# 地址必须带协议，否则报错参数不正确
url = "https://www.lagou.com"
browser = webdriver.Chrome(service=ChromeService(driver_path), options=options)
browser.get(url)

# 关闭选择城市的弹窗窗口
browser.find_element(By.XPATH, '//*[@id="cboxClose"]').click()
time.sleep(1)

# 向搜索框发送内容
browser.find_element(By.XPATH, '//*[@id="search_input"]').send_keys(keyword, Keys.ENTER)
time.sleep(1)

# 找到每条职位所在div 的class，得到职位列表
div_list = browser.find_elements(By.CLASS_NAME, 'p-top__1F7CL')
for div, count in zip(div_list, range(len(div_list))):
    # 找到a标签，点击
    div.find_element(By.TAG_NAME, 'a').click()
    time.sleep(5)

    # 切换到新开的窗口上，否则 browser 还是指向列表页，而非详情页
    browser.switch_to.window(browser.window_handles[-1])
    time.sleep(1)

    # 下拉滚动条到底部
    # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # ActionChains(browser).key_down(Keys.DOWN).perform()

    job_detail = browser.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text
    f = open(f"data/{keyword}_%03d.txt" % count, mode='w', encoding='utf-8')
    f.write(job_detail)
    f.close()

    # 关闭这个详情页
    browser.close()
    time.sleep(1)

    # 切换回列表页
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(1)

    break

browser.quit()


if __name__ == '__main__':
    pass
