import time

from  selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def adobe(email):
    service = Service(executable_path='chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get('https://auth.services.adobe.com/en_US/deeplink.html?deeplink=ssofirst&callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2FSunbreakWebUI1%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Faccount.adobe.com%252F%2523old_hash%253D%2526from_ims%253Dtrue%253Fclient_id%253DSunbreakWebUI1%2526api%253Dauthorize%2526scope%253DAdobeID%252Copenid%252Cacct_mgmt_api%252Cgnav%252Cread_countries_regions%252Csocial.link%252Cunlink_social_account%252Cadditional_info.address.mail_to%252Cclient.scopes.read%252Cpublisher.read%252Cadditional_info.account_type%252Cadditional_info.roles%252Cadditional_info.social%252Cadditional_info.screen_name%252Cadditional_info.optionalAgreements%252Cadditional_info.secondary_email%252Cadditional_info.secondary_email_verified%252Cadditional_info.phonetic_name%252Cadditional_info.dob%252Cupdate_profile.all%252Csecurity_profile.read%252Csecurity_profile.update%252Cadmin_manage_user_consent%252Cadmin_slo%252Cpiip_write%252Cmps%252Clast_password_update%252Cupdate_email%252Cfirefly_api%252Cpasskey_read%252Cpasskey_write%252Caccount_cluster.read%252Caccount_cluster.update%252Cadditional_info.authenticatingAccount%2526reauth%253Dtrue%26state%3D%257B%2522jslibver%2522%253A%2522v2-v0.31.0-2-g1e8a8a8%2522%252C%2522nonce%2522%253A%25224046977657338535%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=SunbreakWebUI1&scope=AdobeID%2Copenid%2Cacct_mgmt_api%2Cgnav%2Cread_countries_regions%2Csocial.link%2Cunlink_social_account%2Cadditional_info.address.mail_to%2Cclient.scopes.read%2Cpublisher.read%2Cadditional_info.account_type%2Cadditional_info.roles%2Cadditional_info.social%2Cadditional_info.screen_name%2Cadditional_info.optionalAgreements%2Cadditional_info.secondary_email%2Cadditional_info.secondary_email_verified%2Cadditional_info.phonetic_name%2Cadditional_info.dob%2Cupdate_profile.all%2Csecurity_profile.read%2Csecurity_profile.update%2Cadmin_manage_user_consent%2Cadmin_slo%2Cpiip_write%2Cmps%2Clast_password_update%2Cupdate_email%2Cfirefly_api%2Cpasskey_read%2Cpasskey_write%2Caccount_cluster.read%2Caccount_cluster.update%2Cadditional_info.authenticatingAccount%2Creauthenticated&state=%7B%22jslibver%22%3A%22v2-v0.31.0-2-g1e8a8a8%22%2C%22nonce%22%3A%224046977657338535%22%7D&relay=ca995e8b-5d4d-44e2-8421-1b46be127159&locale=en_US&flow_type=token&idp_flow_type=login&reauthenticate=force&s_p=google%2Cfacebook%2Capple&response_type=token&code_challenge_method=plain&redirect_uri=https%3A%2F%2Faccount.adobe.com%2F%23old_hash%3D%26from_ims%3Dtrue%3Fclient_id%3DSunbreakWebUI1%26api%3Dauthorize%26scope%3DAdobeID%2Copenid%2Cacct_mgmt_api%2Cgnav%2Cread_countries_regions%2Csocial.link%2Cunlink_social_account%2Cadditional_info.address.mail_to%2Cclient.scopes.read%2Cpublisher.read%2Cadditional_info.account_type%2Cadditional_info.roles%2Cadditional_info.social%2Cadditional_info.screen_name%2Cadditional_info.optionalAgreements%2Cadditional_info.secondary_email%2Cadditional_info.secondary_email_verified%2Cadditional_info.phonetic_name%2Cadditional_info.dob%2Cupdate_profile.all%2Csecurity_profile.read%2Csecurity_profile.update%2Cadmin_manage_user_consent%2Cadmin_slo%2Cpiip_write%2Cmps%2Clast_password_update%2Cupdate_email%2Cfirefly_api%2Cpasskey_read%2Cpasskey_write%2Caccount_cluster.read%2Caccount_cluster.update%2Cadditional_info.authenticatingAccount%26reauth%3Dtrue&use_ms_for_expiry=true#/')
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME, 'username')))
        emails = driver.find_element(By.NAME,'username')
        emails.clear()
        emails.send_keys(email,Keys.ENTER)
        try:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="EmailForm"]/section[1]/label')))
            message = driver.find_element(By.XPATH,value='//*[@id="EmailForm"]/section[1]/label')
            return message.text
        except Exception as e:
            return  "User  exists"
    except Exception as e:
        print("Can't find element because",e)
    finally:
        driver.close()
        driver.quit()
if __name__ == "__main__":
    email= input("Enter a email you want to find: ")
    message=adobe(email)
    print(message)