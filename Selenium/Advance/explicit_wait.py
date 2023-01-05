from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWait:
    def explicit_demo(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://demo.opencart.com/')
        wait = WebDriverWait(driver, 10)
        scroll = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Apple Cinema 30"')))
        driver.execute_script("arguments[0].scrollIntoView();",scroll)
        scroll.click()

explixit_obj = ExplicitWait()
explixit_obj.explicit_demo()