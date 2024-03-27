import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import io
from PIL import  Image
def Skype(email):
    service = Service('chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get("https://web.skype.com/")
        wait=10
        try:
            WebDriverWait(driver,wait).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="i0116"]')))
            signin_email = driver.find_element(By.XPATH,'//*[@id="i0116"]')
            signin_email.send_keys('riteshjha082@gmail.com')
            signin_email_next_button = driver.find_element(By.XPATH,'//*[@id="idSIButton9"]')
            signin_email_next_button.click()
            WebDriverWait(driver, wait).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i0118"]')))
            singin_password = driver.find_element(By.XPATH,'//*[@id="i0118"]')
            singin_password.send_keys('Rit_20_04@/')
            signin_password_next_button = driver.find_element(By.XPATH,'//*[@id="idSIButton9"]')
            signin_password_next_button.click()
            try:
                WebDriverWait(driver, wait).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="declineButton"]')))
                stay_signedin_button = driver.find_element(By.XPATH,'//*[@id="declineButton"]')
                stay_signedin_button.click()
            except Exception as e:
                   print("It was done previously")
            try:
                WebDriverWait(driver,wait).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[3]/button')))
                condition_accept_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[3]/button')
                condition_accept_button.click()
                search_field = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div[2]')
                search_field.click()
                try:
                    WebDriverWait(driver,wait).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/input')))
                    input_field = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/input')
                    input_field.send_keys(email)
                    try:
                        WebDriverWait(driver,wait).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div')))
                        name = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div')
                        live_cid = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div/div[2]/div')
                        image = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[3]/div/div/div/div[1]/div[1]/div')
                        scrreenshot=image.screenshot_as_png
                        ss=Image.open(io.BytesIO(scrreenshot))
                        imagebytes=io.BytesIO()
                        ss.save(imagebytes,format="PNG")
                        imagebytes.seek(0)
                        encoded_image=base64.b64encode(imagebytes.getvalue()).decode("utf-8")
                        return {"name": name.text, "live_cid": live_cid.text,"image":encoded_image}
                    except Exception as e:
                        return "User with that email not found"
                except Exception as e:
                    print("Input field not found")
            except Exception as e:
                print("Input label not found")
        except Exception as e:
            print("Sign in failed")
    except Exception as e:
        print("failed to open website")
    finally:
        driver.close()
        driver.quit()

email = input("Enter email you want to search: ")
info=Skype(email)
print(info)