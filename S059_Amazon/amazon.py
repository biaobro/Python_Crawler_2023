# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : amazon.py
@Project            : S059_Amazon
@CreateTime         : 2023/5/9 22:37
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/5/9 22:37 
@Version            : 1.0
@Description        :

1, 亚马逊网站本身并不慢，但是用 Selenium 加载需要30s 甚至更长才能完成
2, 知乎：Selenium为什么慢？那是你加载策略设置不对 ： https://zhuanlan.zhihu.com/p/453590557
3, 寻找 xpath 的技巧
    先找到1个，然后从前往后逐个删除，观察
第1个：
//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div
//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/h2/a/span/text()

全部：
//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div/div/div
//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div/div/div/div/div/div[2]/div[1]/h2/a/span/text()
"""
import random
import re

from selenium import webdriver
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import init_webdriver

folder_name = r'..\\'
file_name = r'chromedriver.exe'


class AmazonShop:
    def __init__(self):
        driver_path = init_webdriver.driver_seek(folder_name, file_name)
        if driver_path is None:
            driver_path = r'..\\'
            init_webdriver.driver_download(driver_path)

        options = webdriver.ChromeOptions()

        # 加载策略默认为 normal, 可以修改为 eager 或者 none
        # none 时会发生 找不到 ID 的情况
        # options.page_load_strategy = 'eager'

        # prefs = {"profile.managed_default_content_settings.images": 2}
        # options.add_experimental_option("prefs", prefs)
        # options.add_argument('--disable-blink-features=AutomationControlled')

        # 无头模式下 By.ID 找不到 searchbox 输入框
        # options.add_argument('--headless')
        # options.add_experimental_option('useAutomationExtension', False)
        # options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(service=ChromeService(driver_path), options=options)

    def base(self):
        # 地址必须带协议，否则报错参数不正确
        self.browser.get("https://www.amazon.cn")
        self.browser.implicitly_wait(30)
        # Selenium 会等到页面完全加载（就是页面标题不再转圈）后，才会往下执行这1句
        self.goods = input("please input the goods name: ")
        time.sleep(3)
        s = self.browser.find_element(By.ID, 'twotabsearchtextbox')
        s.send_keys(self.goods)
        s.send_keys(Keys.ENTER)
        # 上面执行完输入关键词+回车操作，就已经是在商品列表页的首页了

    def page_next(self):
        recent_url = self.browser.current_url
        i = int(input('please input page number : '))
        url = re.match('^https.*&', recent_url).group()

        # sprefix 参数随便写或者不写都没问题
        url = url + "&page={}&crid=3N8ZO9LIOL2DP&qid=1683685257&sprefix=%2Caps%2C66&ref=sr_pg_{}".format(i, i)
        print(url)
        self.browser.get(url)

    def spider(self):
        self.browser.execute_script("window.scrollBy(0,200)")
        items = {}
        num = int(input("please input the data order: "))
        a = int(num / 6)
        b = num + 1
        for i in range(a):
            self.browser.execute_script("window.scrollBy(0,1000)")

        xpa1 = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{}]/div/div/div/div/div[2]/div[2]/h2/a/span'.format(str(b))
        xpa2 = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{}]/div/div/div/div/div[2]/div[1]/h2/a/span'.format(
            str(b))
        xpa3 = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{}]/div/div/div/div/div[2]/div/div/a/span/span[2]'.format(
            str(b))
        xpa4 = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{}]/div/div/div/div/div/div/div/span[1]/span[1]'.format(
            str(b))

        try:
            title = self.browser.find_element(By.XPATH, xpa1).text
        except:
            title = self.browser.find_element(By.XPATH, xpa2).text

        price = self.browser.find_element(By.XPATH, xpa3).text

        try:
            score = self.browser.find_element(By.XPATH, xpa4).text
        except:
            score = "该产品没有评分"

        items['title'] = title
        items['price'] = price
        items['score'] = score
        print(items)

    def drop_down(self):
        for x in range(1, 10):
            j = x / 10
            js = f"document.documentElement.scrollTop = document.documentElement.scrollHeight * {j}"
            self.browser.execute_script(js)
            time.sleep(random.randint(400, 800) / 1000)

    def run(self):
        self.base()
        self.page_next()
        self.spider()

    # 类销毁时执行
    def __del__(self):
        self.browser.quit()


if __name__ == '__main__':
    ama = AmazonShop()
    ama.run()
