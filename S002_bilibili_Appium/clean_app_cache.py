# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : clean_app_cache.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/27 17:22
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/27 17:22 
@Version            : 1.0
@Description        : None
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

bilibili_desired_caps_bs = {
    "platformName": "Android",
    "appium:platformVersion": "7.1.1",
    "appium:deviceName": "OnePlus 5",
    "appium:appPackage": "tv.danmaku.bilibilihd",
    "appium:appActivity": "tv.danmaku.bili.MainActivityV2",
    "appium:noReset": False
}

server = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(server, bilibili_desired_caps_bs)

# 进入【我的】Tab
tabs = driver.find_elements(By.ID, "tv.danmaku.bilibilihd:id/tab_text")
for tab in tabs:
    if tab.get_attribute('text') == '我的':
        print('get into "我的"')
        tab.click()
        break

# 清空历史记录，应该先判断，如果没有历史记录，就不执行
histories = driver.find_elements(By.ID, "tv.danmaku.bilibilihd:id/cover")
if len(histories) > 0:
    print('history records > 0, start to clean.')
    # 先找到右上角 【管理】按钮
    driver.implicitly_wait(20)
    driver.find_element(By.ID, "tv.danmaku.bilibilihd:id/edit").click()

    # 再找到【全选】按钮
    driver.implicitly_wait(20)
    driver.find_element(By.ID, "tv.danmaku.bilibilihd:id/select_all").click()

    # 最后找到 【删除】按钮
    driver.implicitly_wait(20)
    driver.find_element(By.ID, "tv.danmaku.bilibilihd:id/text_delete_history").click()

    # 最后是弹窗确认 【删除】
    driver.implicitly_wait(20)
    driver.find_element(By.ID, "tv.danmaku.bilibilihd:id/common_dialog_nagetive_btn").click()

# 清除缓存
# 从左侧菜单栏找到 【设置】，该菜单在底部，需要以【更多服务】为基准，先下拉 scroll
print('start to clean cache')
menus = driver.find_elements(By.ID, "tv.danmaku.bilibilihd:id/title")
for menu in menus:
    if menu.get_attribute('text') == '更多服务':
        actions = TouchAction(driver)
        actions.long_press(menu).move_to(None, 0, 100).release().perform()
        break

# 从左侧菜单栏找到 【设置】
driver.implicitly_wait(20)
menus = driver.find_elements(By.ID, "tv.danmaku.bilibilihd:id/title")
for menu in menus:
    if menu.get_attribute('text') == '设置':
        menu.click()
        break

# 从右侧菜单栏找到 【清理存储空间】
driver.implicitly_wait(60)
menus = driver.find_elements(By.ID, "android:id/title")
for menu in menus:
    print(menu.get_attribute('text'))
    if menu.get_attribute('text') == '清理存储空间':
        menu.click()
        break

# 这个页面上就1个菜单
driver.implicitly_wait(60)
menus = driver.find_elements(By.ID, "android:id/title")
for menu in menus:
    if menu.get_attribute('text') == '清空本地图片缓存':
        menu.click()
        break

# 回到首页
driver.implicitly_wait(60)
tabs = driver.find_elements(By.ID, "tv.danmaku.bilibilihd:id/tab_text")
for tab in tabs:
    if tab.get_attribute('text') == '首页':
        print('get into "首页"')
        tab.click()
        break