import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def spotify(email):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://www.spotify.com/in-en/signup')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'username')))
        emails = driver.find_element(By.ID,'username')
        emails.clear()
        emails.send_keys(email,Keys.ENTER)
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/main/main/section/div/div/form/div/div/div/div/div[2]/div[1]/span/span')))
            message = driver.find_element(By.XPATH,value='//*[@id="__next"]/main/main/section/div/div/form/div/div/div/div/div[2]/div[1]/span/span')
            return message.text
        except Exception as e:
            return  "User does not exists"
    except Exception as e:
        print("Can't find element because",e)
    finally:
        driver.close()
        driver.quit()
if __name__ == "__main__":
    email= input("Enter a email you want to find: ")
    message=spotify(email)
    print(message)