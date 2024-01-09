import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def Booking(email):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://account.booking.com/sign-in?op_token=EgVvYXV0aCL6AgoUdk8xS2Jsazd4WDl0VW4yY3BaTFMSCWF1dGhvcml6ZRo1aHR0cHM6Ly9zZWN1cmUuYm9va2luZy5jb20vbG9naW4uaHRtbD9vcD1vYXV0aF9yZXR1cm4qmQJVck1CLXZJX2E0WGc5VmNNYUpLdVZKQWZlUWJnSk5FYlF3THdMMm9HTE9QZmZFMjJJNUZSMnBuUjBCZThmVGVBTXlDOTdCVWVxM0VQU2pzX0pCNHQ5QktsVTduc3RTdFloZ05tb09ybjlZYlZseXEzbEZJUThlV24zdVNCdlF3d1RXUEFpUDdGa3dvdkxHT1BJVXZzRmR4aU90bHZVNmNPTnd5ZXVXOG1oelJ1S1lHMl9JWUZwcU92Vy1FWlZ5LVlYTWIyWmxNSWdTM2xZNUdnWDNYTWtKSi1scVRsOWljNEtFaFRuOENid29taVFMRTg0RzQ9KmV5SnBaQ0k2SW5SeVlYWmxiR3hsY2w5b1pXRmtaWElpZlE9PUIEY29kZSoxCI7IEjCdwteyy-AmOgBCAFihpdusBpIBEHRyYXZlbGxlcl9oZWFkZXKaAQVpbmRleA')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'username')))
        emails = driver.find_element(By.ID,'username')
        emails.clear()
        emails.send_keys(email,Keys.ENTER)
        try:
            WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID, 'password')))
            message = driver.find_element(By.ID,value='password')
            return 'User exists'
        except Exception as e:
            return  "User  does not exists"
    except Exception as e:
        print("Can't find element because",e)
    finally:
        driver.close()
        driver.quit()
if __name__ == "__main__":
    email= input("Enter a email you want to find: ")
    message=Booking(email)
    print(message)