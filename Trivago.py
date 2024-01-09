import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def Trivago(email):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://auth.trivago.com/en-IN')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))
        emails = driver.find_element(By.XPATH,'//*[@id="email"]')
        emails.clear()
        emails.send_keys(email,Keys.ENTER)
        try:
            time.sleep(4) # there is element with similar xpath on previos page that 's why sleep method is used
            WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/section/div/div/main/div/div[1]/h1')))
            message = driver.find_element(By.XPATH,value='//*[@id="__next"]/section/div/div/main/div/div[1]/h1')
            if message.text == 'Create a password for your new account':
                return 'user does not exists'
            else:
                return  "User exists"
        except Exception as e:
            return  e
    except Exception as e:
        print("Can't find element because",e)
    finally:
        driver.close()
        driver.quit()
if __name__ == "__main__":
    email= input("Enter a email you want to find: ")
    message=Trivago(email)
    print(message)