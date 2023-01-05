
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class Demo:

    def setup(self):
        global driver
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://www.startech.com.bd/amd-ryzen-5-5600-processor')
        print(driver.title)







demo_obj= Demo()
demo_obj.setup()

