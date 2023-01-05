from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

class AddToCart:
    def demoadd_product(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://www.daraz.com.bd/')
        driver.implicitly_wait(5)
        mens_fashion = driver.find_element(By.XPATH,'//*[@id="Level_1_Category_No4"]/a/span')
        watches = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/ul/ul[4]/li[1]/a/span')
        sports = driver.find_element(By.XPATH,'//*[@id="J_3442298940"]/div/ul/ul[4]/li[7]/ul/li[4]/a/span')
        action = ActionChains(driver)
        action.move_to_element(mens_fashion).pause(2).move_to_element(watches).pause(2).click(sports).pause(2).release().perform()

addcart_obj = AddToCart()
addcart_obj.demoadd_product()