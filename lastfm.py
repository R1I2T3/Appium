import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def LastFM(email):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://www.last.fm/join')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME, 'email')))
        input_field = driver.find_element(By.NAME,'email')
        input_field.clear()
        input_field.send_keys(email,Keys.ENTER)
        try:
            WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mantle_skin"]/div[2]/div/div[2]/form/div[2]/div/div[2]/div/p')))
            message= driver.find_element(By.XPATH,value='//*[@id="mantle_skin"]/div[2]/div/div[2]/form/div[2]/div/div[2]/div/p')
            return message.text
        except Exception as e:
            return  "message not found"
    except Exception as e:
        print("Can't find element because",e)
    finally:
        driver.close()
        driver.quit()
if __name__ == "__main__":
    input_field= input("Enter a email or phone number you want to find: ")
    message=LastFM(input_field)
    if message =='Looking good!':
        print("User does not exists")
    else:
        print("User exists")