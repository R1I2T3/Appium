import time
from appium import webdriver
from typing import Any,Dict
from appium.options.common import  AppiumOptions
from appium.webdriver.common.appiumby import  AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import base64
import io
from PIL import  Image


def CallApp(number):
    cap = {
        'platformName':'Android',
        'automationName':"UIAutomator2",
        "deviceName":'Android',
        # 'appPackage':'com.callapp.contacts',
        # 'appActivity':'com.callapp.contacts.activity.contact.list.ContactsListActivity'
    }
    url='http://localhost:4473'
    driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
    try:
        app = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='CallApp')
        app.click()
        driver.implicitly_wait(5)
        try:
            searchLable=driver.find_element(by=AppiumBy.ID,value='com.callapp.contacts:id/title_background')
            searchLable.click()
            driver.implicitly_wait(5)
            try:
                searchText = driver.find_element(by=AppiumBy.ID,value='com.callapp.contacts:id/search_src_text')
                searchText.send_keys(number)
                driver.implicitly_wait(2)
                driver.press_keycode(66)
                try:
                    NameOrNumber = driver.find_element(by=AppiumBy.ID,value='com.callapp.contacts:id/nameText')
                    avatar=driver.find_element(by=AppiumBy.XPATH,value='(//android.widget.ImageView[@resource-id="com.callapp.contacts:id/contactImage"])[1]')
                    scrreenshot=avatar.screenshot_as_png
                    ss=Image.open(io.BytesIO(scrreenshot))
                    imagebytes=io.BytesIO()
                    ss.save(imagebytes,format="PNG")
                    imagebytes.seek(0)
                    encoded_image=base64.b64encode(imagebytes.getvalue()).decode("utf-8")
                    time.sleep(3)
                    info={"name":NameOrNumber.text,"encoded image":encoded_image}
                    return  info;
                except:
                   print("User not found",e)
            except Exception as e:
                print("Search field not found")
        except Exception as e:
            print("Search lable not found")
    except Exception as e:
        print("App cannot open because: ",e)
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