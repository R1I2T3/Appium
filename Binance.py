import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def Binance(email):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://accounts.binance.com/en/login')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME, 'username')))
        input_field = driver.find_element(By.NAME,'username')
        input_field.clear()
        input_field.send_keys(email,Keys.ENTER)
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME, 'password')))
            password= driver.find_element(By.NAME,value='password')
            return 'user exists'
        except Exception as e:
            return  "User does not exists"
    except Exception as e:
        print("Can't find element because",e)
    finally:
        driver.close()
        driver.quit()
if __name__ == "__main__":
    input_field= input("Enter a email or phone number you want to find: ")
    message=Binance(input_field)
    print(message)