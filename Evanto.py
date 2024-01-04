import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def Evanto(email):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://elements.envato.com/sign-up')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'firstName')))
        first_Name = driver.find_element(By.ID,'firstName')
        first_Name.clear()
        first_Name.send_keys('abcd')
        last_Name = driver.find_element(By.ID,'lastName')
        last_Name.clear()
        last_Name.send_keys('abcd')
        emails = driver.find_element(By.ID,'email')
        emails.clear()
        emails.send_keys(email)
        password = driver.find_element(By.ID,value='password')
        password.clear()
        password.send_keys('abcdabcd')
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div[2]/div/div/div/div/form/div[2]/div[3]')))
            message = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/main/div/div/div/div[2]/div/div/div/div/form/div[2]/div[3]')
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
    message=Evanto(email)
    print(message)