import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def UnoCoin(input):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://unocoin.com/in/home?type=login')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div[2]/label/div/div[1]/div/input')))
        input_field = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div[2]/label/div/div[1]/div/input')
        input_field.clear()
        input_field.send_keys(input)
        password = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div[3]/label/div/div/div[1]/input')
        password.send_keys('12345678',Keys.ENTER)
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div[2]/label/div/div[2]')))
            message= driver.find_element(By.XPATH,value='//*[@id="__next"]/div/div[2]/div/div[2]/div/div[2]/label/div/div[2]')
            return 'user does not exists'
        except Exception as e:
            return  "User exists"
    except Exception as e:
        print("Can't find element because",e)
    finally:
        driver.close()
        driver.quit()
if __name__ == "__main__":
    input_field= input("Enter a email or phone number you want to find: ")
    message=UnoCoin(input_field)
    print(message)