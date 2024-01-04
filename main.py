import threading
import time

from appium import webdriver
from typing import Any,Dict
from appium.options.common import  AppiumOptions
from appium.webdriver.common.appiumby import  AppiumBy
import asyncio
def setting(cap,url):
    driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
    try:
        app = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Settings')
        app.click()
        driver.implicitly_wait(5)
        try:
            time.sleep(10)
            print("setting app is opening")
            battery = driver.find_element(by=AppiumBy.XPATH,value='(//android.widget.LinearLayout[@resource-id="com.android.settings:id/dashboard_tile"])[4]/android.widget.LinearLayout')
            battery.click()
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)

def message(cap,url):
    driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
    try:
        app = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Messaging')
        app.click()
        driver.implicitly_wait(5)
        time.sleep(10)
        try:
            print("message app is opening")
            new = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Start new conversation')
            new.click()
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)

def concurrently():
    cap1 = {
    'platformName':'Android',
    'automationName':"UIAutomator2",
    "appium:udid":'emulator-5554',
    }
    url1='http://localhost:4474'
    cap2 = {
        'platformName':'Android',
        'automationName':"UIAutomator2",
        "appium:udid":'emulator-5556',
    }
    url2='http://localhost:4473'
    thread1 = threading.Thread(target=setting(cap1,url1))
    thread2= threading.Thread(target=message(cap2,url2))
    thread1.start()
    thread2.start()

concurrently()