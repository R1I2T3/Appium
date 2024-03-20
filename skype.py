import time
from appium import webdriver
from typing import Any,Dict
from appium.options.common import  AppiumOptions
from appium.webdriver.common.appiumby import  AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import io
from PIL import  Image

def Skype():
    cap = {
        'platformName':'Android',
        'automationName':"UIAutomator2",
        "deviceName":'Android',
        "appium:ignoreHiddenApiPolicyError": "true",
        "appium:udid":'emulator-5554',
    }
    url='http://localhost:4473'
    try:
        driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
        wait = WebDriverWait(driver, 10)
        app = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Skype')
        app.click()
        time.sleep(20)
    except Exception as e:
        print("Failed to open app")
    finally:
        driver.terminate_app('com.skype.raider')
        driver.quit()

Skype()