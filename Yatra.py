import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Yatra(email):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-input"]')))
            input_field = driver.find_element(By.XPATH, '//*[@id="login-input"]')
            input_field.clear()
            input_field.send_keys(email, Keys.ENTER)
            try:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-password"]')))
                password = driver.find_element(By.XPATH, value='//*[@id="login-password"]')
                return 'user exists'
            except Exception as e:
                   return "User does not exists"
        except Exception as e:
                print("Can't find element because", e)
    except Exception as e:
            print("Failed to open website")
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    email = input("Enter your email: ")
    message = Yatra(email)
    print(message)
