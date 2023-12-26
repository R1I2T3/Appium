import time
from appium import webdriver
from typing import Any,Dict
from appium.options.common import  AppiumOptions
from appium.webdriver.common.appiumby import  AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import base64
import io
from PIL import  Image

def ShowCaller(number):
    try:
        cap = {
            'platformName':'Android',
            'automationName':"UIAutomator2",
            "deviceName":'Android',
            # 'appPackage':'com.allinone.callerid',
            # 'appActivity':'com.allinone.callerid.mvc.controller.MainActivity'
        }
        url='http://localhost:4473'
        # Initializing driver and oprning of app
        driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
        # Opening of app.
        app = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Showcaller')
        app.click()
        driver.implicitly_wait(5)
        #initial buttons
        driver.find_element(by=AppiumBy.ID,value='com.allinone.callerid:id/flayout_btn').click()
        driver.implicitly_wait(3)
        driver.find_element(by=AppiumBy.XPATH,value='//android.widget.FrameLayout[@resource-id="com.allinone.callerid:id/flayout_btn"]').click()
        driver.implicitly_wait(5)
        btn=driver.find_element(by=AppiumBy.XPATH,value='//android.widget.FrameLayout[@resource-id="com.allinone.callerid:id/flayout_btn"]')
        btn.click()
        try:
            # search lable
            searchLabel = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='search')
            searchLabel.click()
            driver.implicitly_wait(10)
            try:
                # changing region
                change_country= driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Switch country code')
                change_country.click()
                downMenu =driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='down')
                downMenu.click()
                searchCountry=driver.find_element(by=AppiumBy.ID,value='com.allinone.callerid:id/et_search_country')
                searchCountry.send_keys('india')
                driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='search')
                driver.find_element(by=AppiumBy.ID,value='com.allinone.callerid:id/ripple_bg').click()
                try:
                #    Searching text.
                   searchText=driver.find_element(by=AppiumBy.ID,value='com.allinone.callerid:id/input_number')
                   searchText.send_keys(number)
                   driver.press_keycode(66)
                   driver.implicitly_wait(5)
                   try:
                    # scrapping data.
                      name=driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@resource-id="com.allinone.callerid:id/result_type"]')
                      location=driver.find_element(by=AppiumBy.ID,value='com.allinone.callerid:id/result_location')
                      avatar=driver.find_element(by=AppiumBy.ID,value='com.allinone.callerid:id/result_photo_view')
                      scrreenshot=avatar.screenshot_as_png
                      ss=Image.open(io.BytesIO(scrreenshot))
                      imagebytes=io.BytesIO()
                      ss.save(imagebytes,format="PNG")
                      imagebytes.seek(0)
                      encoded_image=base64.b64encode(imagebytes.getvalue()).decode("utf-8")
                      driver.implicitly_wait(5)
                      info={"name":name.text,"location":location.text,"encoded image":encoded_image}
                   except Exception as e:
                       print("Some error happend: ",e)
                except Exception as e:
                    print("There is error in sending keys")
            except Exception as e:
                print("Search field not found",e)
        except Exception as e:
            print("Search lable is not found")
    except Exception as e:
        print("Can't open app because: ",e)
    driver.terminate_app('com.allinone.callerid')
    driver.quit()
    return  info
if __name__ == "__main__":
    # Get user input for the 10-digit number
    user_input = input("Enter a 10-digit number: ")
    country_Code='0'
    if not user_input.isdigit() or len(user_input) != 10:
        print("Invalid input. Please enter a valid 10-digit number.")
    else:
        number =country_Code+ user_input[:5] + " " + user_input[5:]
        result=ShowCaller(number)
        print(result)