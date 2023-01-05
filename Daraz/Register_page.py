from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

class RegisterDemo:
    def register_demo(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://www.daraz.com.bd/')
        # driver.switch_to.alert.dismiss()
        click_singUp = driver.find_element(By.LINK_TEXT,'SIGNUP / LOGIN')
        # driver.switch_to.alert.dismiss()
        click_singUp.click()
        click_register = driver.find_element(By.LINK_TEXT,'Register')
        click_register.click()
        number = driver.find_element(By.CSS_SELECTOR,'.mod-login-input-phone [type]')
        get_sms = driver.find_element(By.CSS_SELECTOR,'.btn_slide.nc_iconfont')
        number.send_keys('0124567864')
        xoffset = 0
        yoffset = 500
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(get_sms,xoffset,yoffset).pause(1).release().perform()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,'.baxia-dialog-close').click()




register_obj = RegisterDemo()
register_obj.register_demo()