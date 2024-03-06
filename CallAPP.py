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


def CallApp(number):
    cap = {
        'platformName':'Android',
        'automationName':"UIAutomator2",
        "deviceName":'Android',
        "appium:ignoreHiddenApiPolicyError": "true",
        "appium:udid":'emulator-5554',
    }
    url='http://localhost:4473'
    driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
    wait = WebDriverWait(driver, 10)
    try:
        app = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='CallApp')
        app.click()
        driver.implicitly_wait(3)
        try:
            searchLable=wait.until(EC.element_to_be_clickable(driver.find_element(by=AppiumBy.ID,value='com.callapp.contacts:id/title_background')))
            searchLable.click()
            try:
                searchText = wait.until(EC.element_to_be_clickable(driver.find_element(by=AppiumBy.ID,value='com.callapp.contacts:id/search_src_text')))
                searchText.send_keys(number)
                try:
                   try:
                       personPreviouslySearched = driver.find_element(by=AppiumBy.XPATH,value='(//android.widget.ImageView[@resource-id="com.callapp.contacts:id/contactImage"])[2]')
                       personPreviouslySearched.click()
                   except:
                       searchIcon = wait.until(EC.element_to_be_clickable(driver.find_element(by=AppiumBy.XPATH,value='(//android.widget.ImageView[@resource-id="com.callapp.contacts:id/buttonIcon"])[1]')))
                       searchIcon.click()
                   name=driver.find_element(by=AppiumBy.ID,value='com.callapp.contacts:id/nameText')
                   location=driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@resource-id="com.callapp.contacts:id/item_title" and @text="India"]')
                   provider = driver.find_element(by=AppiumBy.ID,value='com.callapp.contacts:id/item_subtitle')
                   avatar=wait.until(EC.element_to_be_clickable(driver.find_element(by=AppiumBy.XPATH,value='(//android.widget.ImageView[@resource-id="com.callapp.contacts:id/contactImage"])[1]')))
                   scrreenshot=avatar.screenshot_as_png
                   ss=Image.open(io.BytesIO(scrreenshot))
                   imagebytes=io.BytesIO()
                   ss.save(imagebytes,format="PNG")
                   imagebytes.seek(0)
                   encoded_image=base64.b64encode(imagebytes.getvalue()).decode("utf-8")
                   driver.implicitly_wait(5)
                   info={"name":name.text,"location":location.text,"provider":provider.text,"encoded image":encoded_image}
                   return  info
                except:
                   print("Person with following phone number not found")
            except Exception as e:
                print("Search field not found",e)
        except Exception as e:
            print("Search lable not found",e)
    except Exception as e:
        print("Element not found within the specified timeout.",e)
    finally:
            driver.terminate_app('com.callapp.contacts')
            driver.quit()


if __name__ == "__main__":
    # Get user input for the 10-digit number
    user_input = input("Enter a 10-digit number: ")
    country_Code='+91'
    if not user_input.isdigit() or len(user_input) != 10:
        print("Invalid input. Please enter a valid 10-digit number.")
    else:
        number =country_Code+ user_input
        result=CallApp(number)
        print(result)
        # print(result)