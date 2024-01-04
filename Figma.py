import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def Figma(inputemail):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://www.figma.com/signup')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'email')))
        emails = driver.find_element(By.NAME,'email')
        emails.clear()
        emails.send_keys(inputemail)
        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.ID, 'current-password')))
        password = driver.find_element(By.ID,'current-password')
        password.clear()
        password.send_keys('12345678',Keys.ENTER)
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'auth_form--error--Ld3sn')))
            message = driver.find_element(By.CLASS_NAME,'auth_form--error--Ld3sn')
            return message.text
        except Exception as e:
            return  "User does not exists"
    except Exception as e:
        print("Element not found",e)
    driver.quit()


if __name__ == "__main__":
    email= input("Enter a email you want to find: ")
    print(Figma(email))