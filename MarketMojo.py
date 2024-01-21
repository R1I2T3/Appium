import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def MarketMojo(email):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://www.marketsmojo.com/mojofeed/login')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mm-apage-section"]/div/app-login/section/div/div/div/div[2]/div/div[2]/form/div[1]/input')))
        input_field = driver.find_element(By.XPATH,'//*[@id="mm-apage-section"]/div/app-login/section/div/div/div/div[2]/div/div[2]/form/div[1]/input')
        input_field.clear()
        input_field.send_keys(email)
        password= driver.find_element(By.XPATH,value='//*[@id="exampleInputPassword1"]')
        password.clear()
        password.send_keys(12345,Keys.ENTER)
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="emailHelp"]')))
            message= driver.find_element(By.XPATH,value='//*[@id="emailHelp"]')
            return message.text
        except Exception as e:
            return  "some error taken place"
    except Exception as e:
        print("Can't find element because",e)
    finally:
        driver.close()
        driver.quit()
if __name__ == "__main__":
    input_field= input("Enter a email or phone number you want to find: ")
    message=MarketMojo(input_field)
    if message == 'Oops! The password you are entering seems to be wrong':
        print("user exists")
    else:
        print('user does not exists')