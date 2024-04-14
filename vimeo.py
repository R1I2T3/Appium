import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
def vimeo():
    service = Service()
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = 10
    try:
        driver.get('https://vimeo.com/log_in')
        try:
            WebDriverWait(driver, wait).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email_login"]')))
            login_email = driver.find_element(By.XPATH, '//*[@id="email_login"]')
            login_email.send_keys('john@gmail.com')
            login_password = driver.find_element(By.XPATH, '//*[@id="password_login"]')
            login_password.send_keys('John_doe')
            login_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/section/section[5]/form/section[2]/button')
            login_button.click()
            try:
                WebDriverWait(driver, wait).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[5]/div/div[2]/div[1]/div/form/div/div[2]/div/div/select')))
                change_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[5]/div/div[2]/div[1]/div/form/div/div[2]/div/div/select')
                select = Select(change_field)
                select.select_by_value('Vimeo')
                search_field = driver.find_element(By.XPATH, '//*[@id="topnav-search"]')
                search_field.send_keys('Ritesh Jha')
                WebDriverWait(driver,wait).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="topnav-search_search_form"]/div[2]/div/div/div')))
                search_label = driver.find_element(By.XPATH, '//*[@id="topnav-search_search_form"]/div[2]/div/div/div')
                search_label.click()
                time.sleep(100)
            except Exception as e:
                print("Search box not found",e)
        except Exception as e:
            print("Login button not found")
    except Exception as e:
        print("Failed to opem website")
    finally:
        driver.close()
        driver.quit()

vimeo()