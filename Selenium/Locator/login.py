import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select


class Register:

    def setup(self):
        global driver
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://www.facebook.com/')
        print(driver.title)

    def allLink(self):
        link = driver.find_elements(By.TAG_NAME, 'a')
        for links in link:
            # print('Lenth of this links:', len(links.text))
            # print(links.text)
            if links.text == 'Create New Account':
                links.click()
                time.sleep(2)
                username = driver.find_element(By.NAME, 'firstname')
                lastName = driver.find_element(By.NAME, 'lastname')
                mobile = driver.find_element(By.NAME, 'reg_email__')
                password = driver.find_element(By.NAME, 'reg_passwd__')
                birth_day_date = driver.find_element(By.NAME, 'birthday_day')
                birth_day_month = driver.find_element(By.NAME, 'birthday_month')
                birth_day_year = driver.find_element(By.NAME, 'birthday_year')
                radio_box = driver.find_element(By.XPATH,
                                                '/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/label')
                singUp = driver.find_element(By.NAME, 'websubmit')
                username_enable = username.is_enabled()
                user_select = username.is_selected()

                if username_enable == True and user_select != True:
                    username.send_keys('hello')
                if lastName.is_displayed() and lastName.is_enabled():
                    lastName.send_keys('Automation')
                if mobile.is_enabled() and mobile.is_displayed():
                    mobile.send_keys('01771236578')
                if password.is_enabled() and password.is_displayed():
                    password.send_keys('123478asf')
                if birth_day_date.is_displayed() or birth_day_date.is_enabled():
                    select_day = Select(birth_day_date)
                    select_day.select_by_value('7')
                if birth_day_month.is_enabled():
                    select_month = Select(birth_day_month)
                    select_month.select_by_value('3')
                if birth_day_year.is_displayed():
                    select_year = Select(birth_day_year)
                    select_year.select_by_value('1999')
                if radio_box.is_displayed() and radio_box.is_enabled():
                    select_radio = radio_box.click()
                singUp.click()


register_obj = Register()
register_obj.setup()
register_obj.allLink()

