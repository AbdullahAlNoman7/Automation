import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class Locator:

    def setUp(self):
        global driver
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('https://www.apple.com/')

    def serach(self):
        search = driver.find_element(By.XPATH, '//*[@id="ac-gn-link-search"]')
        search.click()
        search_item = driver.find_element(By.ID, 'ac-gn-searchform-input')
        search_item.send_keys('Mobile')
        clk_search = driver.find_element(By.ID, 'ac-gn-searchform-submit')
        clk_search.click()
        time.sleep(2)
    def scrollToFifa(self):
        fifa = driver.find_element(By.LINK_TEXT,'FIFA Mobile: FIFA World Cup™')
        driver.execute_script("arguments[0].scrollIntoView();",fifa)
        fifa.click()
        time.sleep(2)



locator_obj = Locator()
locator_obj.setUp()
locator_obj.serach()
locator_obj.scrollToFifa()
