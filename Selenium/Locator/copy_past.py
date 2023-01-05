import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class Register:

    def setup(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://www.facebook.com/')
        print(driver.title)
        user_name = driver.find_element(By.ID,'email')
        user_name.send_keys('asdf@gmal.com')
        act = ActionChains(driver)
        act.key_down(keys.Keys.CONTROL).send_keys('a').key_up(keys.Keys.CONTROL).perform()
        act.key_down(keys.Keys.CONTROL).send_keys('c').key_up(keys.Keys.CONTROL).perform()
        act.send_keys(keys.Keys.TAB).perform()
        act.key_down(keys.Keys.CONTROL).send_keys('v').key_up(keys.Keys.CONTROL).perform()
        act.send_keys(keys.Keys.ENTER).perform()



reg_obj = Register()
reg_obj.setup()