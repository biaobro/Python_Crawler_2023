# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : clean_system_cache.py
@Project            : Crawler_2023
@CreateTime         : 2023/1/27 17:20
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/1/27 17:20 
@Version            : 1.0
@Description        : None
"""
from appium import webdriver
from selenium.webdriver.common.by import By

settings_desired_caps_bs = {
    "platformName": "Android",
    "appium:platformVersion": "7.1.1",
    "appium:deviceName": "OnePlus 5",
    "appium:appPackage": "com.bluestacks.settings",
    "appium:appActivity": ".SettingsActivity",
    "appium:noReset": False
}

server = 'http://localhost:4723/wd/hub'

# 先清除系统级别缓存：设置 - 存储 - 应用 - 哔哩哔哩HD - 清除缓存
driver = webdriver.Remote(server, settings_desired_caps_bs)

driver.implicitly_wait(10)
driver.find_element(By.ID, "com.bluestacks.settings:id/storage_settings").click()

driver.implicitly_wait(20)
menus = driver.find_elements(By.ID, "android:id/title")
for menu in menus:
    if menu.get_attribute("text") == '应用':
        menu.click()
        break

driver.implicitly_wait(30)
menus = driver.find_elements(By.ID, "android:id/title")
for menu in menus:
    if menu.get_attribute("text") == '哔哩哔哩HD':
        menu.click()
        break

driver.implicitly_wait(30)
buttons = driver.find_elements(By.ID, "com.android.settings:id/button")
for button in buttons:
    if button.get_attribute("text") == '清除缓存' and button.get_attribute("enabled"):
        button.click()

driver.quit()