import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def iepf(firstName, lastName):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get('https://iepf.gov.in/IEPFWebProject/services.html')
        wait=10
        WebDriverWait(driver, wait).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="jsn-pos-left"]/div/div/div[2]/div/div/ul[1]/li/a')))
        unClaimedLink = driver.find_element(By.XPATH, '//*[@id="jsn-pos-left"]/div/div/div[2]/div/div/ul[1]/li/a')
        unClaimedLink.click()
        try:
            # WebDriverWait(driver, wait).until(EC.number_of_windows_to_be(2))
            driver.implicitly_wait(4)
            new_tab_handle = driver.window_handles[-1]
            driver.switch_to.window(new_tab_handle)
            firstNameInputField = driver.find_element(By.XPATH, '//*[@id="DataBlock1"]/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/input')
            firstNameInputField.send_keys(firstName)
            lastNameInputField = driver.find_element(By.XPATH, '//*[@id="DataBlock1"]/tbody/tr[3]/td[2]/table/tbody/tr/td[3]/input')
            lastNameInputField.send_keys(lastName)
            searchButton = driver.find_element(By.XPATH, '//*[@id="DataBlock1"]/tbody/tr[7]/td/table/tbody/tr/td[2]/input')
            searchButton.click()
            try:
                data = []
                WebDriverWait(driver,wait).until(EC.visibility_of_element_located((By.ID, 'tableId')))
                table_element = driver.find_element(By.ID, "tableId")
                rows = table_element.find_elements(By.TAG_NAME, "tr")
                row_header = table_element.find_elements(By.TAG_NAME,'th')
                for row in rows:
                    row_data = {}
                    cells = row.find_elements(By.TAG_NAME, "td")
                    headers = []
                    for header in row_header:
                        headers.append(header.text.strip())
                    for i, cell in enumerate(cells):
                        cell_text = cell.text.strip()
                        row_data[headers[i]] = cell_text
                    data.append(row_data)
                return data[1:]
            except Exception as e:
                print("No one found with that data")
        except Exception as e:
            print("Input field not found")
    except Exception as e:
        print("Website failed to load")
    finally:
        driver.close()
        driver.quit()

fullName = input("Enter full Name")
name = fullName.split()
data=iepf(name[0], name[1])
print(data)
