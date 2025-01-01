# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : bilibili_appium.py
@Project            : Scrapy
@CreateTime         : 2023/1/25 17:11
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/25 17:11 
@Version            : 1.0
@Description        : None
@20230127 尝试增加系统级别的应用缓存，以及应用内部缓存，但成效不大。目前看下来最大的限制还是IP
"""
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# [application][device]
# [device][application]
# 开启模拟器，adb 连接
# 进入模拟器 开启app
# 进入adb shell，运行 dumpsys activity | grep mFocusedActivity
# 在雷电模拟器 安卓9上的命令是 dumpsys activity | grep mResumedActivity
# 得到appPackage及appActivity
bilibili_desired_caps_nox = {
    "platformName": "Android",
    "appium:platformVersion": "7.1.2",
    "appium:deviceName": "SM-G9810",
    "appium:appPackage": "tv.danmaku.bilibilihd",
    "appium:appActivity": "tv.danmaku.bili.MainActivityV2",
    "appium:noReset": False
}

bilibili_desired_caps_bs = {
    "platformName": "Android",
    "appium:platformVersion": "7.1.1",
    "appium:deviceName": "OnePlus 5",
    "appium:appPackage": "tv.danmaku.bilibilihd",
    "appium:appActivity": "tv.danmaku.bili.MainActivityV2",
    "appium:noReset": False
}

bilibili_desired_caps_ld = {
    "platformName": "Android",
    "appium:platformVersion": "9",
    "appium:deviceName": "HD1910",
    "appium:appPackage": "tv.danmaku.bili",
    "appium:appActivity": ".MainActivityV2",
    "appium:noReset": False
}

server = 'http://localhost:4723/wd/hub'
driver = None
count = 1
while count < 200:
    try:
        # 不同版本app 上的组件id 不同，如平板版本 和 手机版本
        driver = webdriver.Remote(server, bilibili_desired_caps_bs)

        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        print(width, height)

        # 协议告知页面，这里点击按钮 【同意并知晓】
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "tv.danmaku.bilibilihd:id/agree").click()

        # driver.find_element(By.ID, "tv.danmaku.bili:id/agree").click()

        # 进入视频列表页，定位到左上角输入框，点击进入搜索页面
        driver.implicitly_wait(200)
        driver.find_element(By.ID, "tv.danmaku.bilibilihd:id/expand_search").click()

        # driver.find_element(By.ID, "tv.danmaku.bili:id/search_text").click()

        # 等待20s 如果出现【未成年人】告知弹窗，无脑发送【回车】
        # while WebDriverWait(driver, 20, 1).until_not(expected_conditions.alert_is_present()):
        driver.implicitly_wait(20)
        driver.press_keycode(AndroidKey.ENTER)

        # 搜索页面定位输入框，并输入内容，然后敲【回车】
        driver.implicitly_wait(20)
        driver.find_element(By.ID, "tv.danmaku.bilibilihd:id/search_src_text").send_keys("The Infographics Show - 大隐隐于市，那些隐藏在日常用品中的致命武器")

        # driver.find_element(By.ID, "tv.danmaku.bili:id/search_src_text").send_keys("爬虫攻守道 - 你敢信么，B站还能这样玩")
        driver.press_keycode(AndroidKey.ENTER)
        print('get into play page')

        # 等待加载搜索结果
        driver.implicitly_wait(20)

        # 测试：默认不下拉的话，只有第1行4个能够完整展示，所以这里会获取到 4个视频的上传者信息
        # upusers = driver.find_elements(By.ID, "tv.danmaku.bilibilihd:id/upuser")
        # # upusers = driver.find_elements(By.ID, "tv.danmaku.bili:id/upuser")
        # for upuser in upusers:
        #     print(upuser.get_attribute('text'))

        # 从搜索结果中找到每个视频对应的封面，然后点击第1个
        covers = driver.find_elements(By.ID, "tv.danmaku.bilibilihd:id/cover")

        # covers = driver.find_elements(By.ID, "tv.danmaku.bili:id/cover")
        if len(covers) > 0:
            covers[0].click()

        # inner_loop = 1
        # while inner_loop < 3:
        #     # 点击 【点赞】 按钮
        #     driver.implicitly_wait(20)
        #     driver.find_element(By.ID, "tv.danmaku.bilibilihd:id/recommend_icon").click()
        #     # driver.find_element(By.ID, "tv.danmaku.bili:id/recommend_icon").click()
        #
        #     # 等待，然后返回上个页面 —— 搜索结果页
        #     driver.implicitly_wait(20)
        #     driver.press_keycode(AndroidKey.ESCAPE)
        #
        #     # 继续进入
        #     covers = driver.find_elements(By.ID, "tv.danmaku.bilibilihd:id/cover")
        #
        #     # covers = driver.find_elements(By.ID, "tv.danmaku.bili:id/cover")
        #     if len(covers) > 0:
        #         covers[0].click()
        #
        #     time.sleep(20)
        #     inner_loop = inner_loop + 1
        time.sleep(10)

        views = driver.find_element(By.ID, "tv.danmaku.bilibilihd:id/views").get_attribute('text')
        # views = driver.find_element(By.ID, "tv.danmaku.bili:id/views").get_attribute('text')
        print('views : ', views)

    except Exception as e:
        print('exception')
    finally:
        print(count)
        driver.quit()
        count = count + 1
