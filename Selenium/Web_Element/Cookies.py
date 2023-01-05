import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class CookiesCheck:
    def demo_cookies(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        driver.implicitly_wait(5)
        # first cookies
        first_cookies = driver.get_cookies()
        print('First cookies: ',first_cookies)
        # login
        userName = driver.find_element(By.NAME,"username")
        password = driver.find_element(By.XPATH,'//input[@type="password"]')
        btnLogin = driver.find_element(By.CSS_SELECTOR,'.orangehrm-login-button')
        userName.send_keys('Admin')
        password.send_keys('admin123')
        btnLogin.click()
        time.sleep(2)
        # second cookies
        second_cookies = driver.get_cookies()
        print('This is a second:',second_cookies)
        # delete cookies
        delete_cookies = driver.delete_all_cookies()
        print('After delete cookies: ',delete_cookies)
        time.sleep(2)
        driver.refresh()


cookies_obj = CookiesCheck()
cookies_obj.demo_cookies()

