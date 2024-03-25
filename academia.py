import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def academia(emailInput):
    service = Service('chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get('https://www.academia.edu/signup')
        wait = 10
        try:
            WebDriverWait(driver,wait).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user_first_name"]')))
            firstName = driver.find_element(By.XPATH, '//*[@id="user_first_name"]')
            firstName.send_keys("Tony")
            LastName = driver.find_element(By.XPATH , '//*[@id="user_last_name"]')
            LastName.send_keys("Stark")
            email = driver.find_element(By.XPATH,'//*[@id="user_email"]')
            email.send_keys(emailInput)
            password = driver.find_element(By.XPATH,'//*[@id="user_password"]')
            password.send_keys("Tony@1234")
            signUpButton = driver.find_element(By.XPATH,'//*[@id="register_button"]')
            signUpButton.click()
            try:
                WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="content"]/div[1]/div/div/div/div/div[4]/form/div[1]/div[3]/div/div')))
                info = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div/div/div/div/div[4]/form/div[1]/div[3]/div/div')
                return info.text
            except Exception as e:
                return "Email is not in use"
        except Exception as e:
            print("Failed to find input field")
    except Exception as e:
        print("Website failed to open", e)
    finally:
        driver.close()
        driver.quit()


email= input("Enter your email: ")
data= academia(email)
print(data)