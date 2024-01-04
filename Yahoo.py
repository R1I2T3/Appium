import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def Yahoo(email):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://login.yahoo.com/account/create?intl=in&specId=usernameregsimplified&done=https%3A%2F%2Fwww.yahoo.com')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'usernamereg-firstName')))
        first_Name = driver.find_element(By.ID,'usernamereg-firstName')
        first_Name.clear()
        first_Name.send_keys('abcd')
        last_Name = driver.find_element(By.ID,'usernamereg-lastName')
        last_Name.clear()
        last_Name.send_keys('abcd')
        birth_Date = driver.find_element(By.ID,'usernamereg-birthYear')
        birth_Date.send_keys('2000')
        emails = driver.find_element(By.NAME,'email')
        emails.clear()
        emails.send_keys(email,Keys.ENTER)
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'reg-error-email')))
            message = driver.find_element(By.ID,value='reg-error-email')
            return message.text
        except Exception as e:
            return  "User  does not exists"
    except Exception as e:
        print("Can't find element because",e)
    finally:
        driver.close()
        driver.quit()
if __name__ == "__main__":
    email= input("Enter a email you want to find: ")
    message=Yahoo(email)
    print(message)