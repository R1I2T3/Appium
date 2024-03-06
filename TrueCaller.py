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

def TrueCaller(phoneNumber):
    cap = {
            'platformName':'Android',
            'automationName':"UIAutomator2",
            "deviceName":'Android',
            # 'appPackage':'com.truecaller',
            # 'appActivity':'com.truecaller.ui.Trueca9892878956llerInit'
    }
    url='http://localhost:4473'

        # Initializing driver and opening of app
    driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
    wait = WebDriverWait(driver, 10)
    try:
        app=driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Truecaller')
        app.click()
        # Finding of search lable with xpath
        try:
            driver.implicitly_wait(10)
            searchLabel = driver.find_element(by=AppiumBy.XPATH,value='//android.view.ViewGroup[@resource-id="com.truecaller:id/main_header_view"]/android.view.ViewGroup')
            searchLabel.click()
            # finding of search field and sending keys
            try:
                searchText=wait.until(EC.element_to_be_clickable(driver.find_element(by=AppiumBy.ID,value='com.truecaller:id/search_field')))
                searchText.send_keys(phoneNumber)
                try:
                    searchIcon= wait.until(EC.element_to_be_clickable(driver.find_element(by=AppiumBy.ID,value='com.truecaller:id/callToAction')))
                    searchIcon.click()
                    # scrapping name and avatar image and encodeing them
                    try:
                        name=wait.until(EC.element_to_be_clickable(driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@resource-id="com.truecaller:id/nameOrNumber"]')))
                        provider = driver.find_element(by=AppiumBy.ID,value='com.truecaller:id/numberDetails')
                        avatar=driver.find_element(by=AppiumBy.ID,value='com.truecaller:id/avatar')
                        scrreenshot=avatar.screenshot_as_png
                        ss=Image.open(io.BytesIO(scrreenshot))
                        imagebytes=io.BytesIO()
                        ss.save(imagebytes,format="PNG")
                        imagebytes.seek(0)
                        encoded_image=base64.b64encode(imagebytes.getvalue()).decode("utf-8")
                        time.sleep(3)
                        info={"name":name.text,"provider":provider.text,"encoded image":encoded_image}
                        return info
                    except Exception as e:
                         print("User exists but then some error occured",e)
                except Exception as e:
                    print("User not found")
            except Exception as e:
                print("Search field not found")
        except Exception as e:
            print("Search lable is not found")
    except Exception as e:
        print("App cannot open")
    finally:
            driver.terminate_app('com.truecaller')
            driver.quit()

if __name__ == "__main__":
    # Get user input for the 10-digit number
    user_input = input("Enter a 10-digit number: ")

    if not user_input.isdigit() or len(user_input) != 10:
        print("Invalid input. Please enter a valid 10-digit number.")
    else:
        result = TrueCaller(user_input)
        print(result)