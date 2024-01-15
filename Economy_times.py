import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def EconmyTimes(email):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://economictimes.indiatimes.com/login.cms')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lg_login_option"]/form/div/div[5]/span')))
        signin_option=driver.find_element(By.XPATH,'//*[@id="lg_login_option"]/form/div/div[5]/span')
        time.sleep(1)
        signin_option.click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="input_email"]')))
        input_field = driver.find_element(By.XPATH,'//*[@id="input_email"]')
        input_field.clear()
        input_field.send_keys(email,Keys.ENTER)
        try:
            WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lg_password"]/form/div[1]/input')))
            password= driver.find_element(By.XPATH,value='//*[@id="lg_password"]/form/div[1]/input')
            return 'user  exists'
        except Exception as e:
            return  "User does not exists"
    except Exception as e:
        print("Can't find element because",e)
    finally:
        driver.close()
        driver.quit()
if __name__ == "__main__":
    input_field= input("Enter a email or phone number you want to find: ")
    message=EconmyTimes(input_field)
    print(message)