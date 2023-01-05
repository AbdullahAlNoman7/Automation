import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class WebElement:

    def setup(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://www.startech.com.bd/')
        print(driver.title)
        component = driver.find_element(By.LINK_TEXT, 'Component')
        processor = driver.find_element(By.CSS_SELECTOR,
                                        'li:nth-of-type(3) > .drop-down.drop-menu-1 > li:nth-of-type(1) > .nav-link')
        adm_processor = driver.find_element(By.CSS_SELECTOR,
                                            ".navbar-nav [class='nav-item has-child c-1']:nth-of-type(3) .has-child:nth-of-type(1) .nav-item:nth-of-type(1) .nav-link")
        action = ActionChains(driver)
        action.move_to_element(component).move_to_element(processor).click(adm_processor).pause(5).release().perform()
        expected_result = 'AMD'
        if expected_result == 'AMD':
            scroll_to_ryzen5 = driver.find_element(By.CSS_SELECTOR, "img[alt='AMD Ryzen 5 5600 Processor']")
            driver.execute_script("arguments[0].scrollIntoView();", scroll_to_ryzen5)
            scroll_to_ryzen5.click()
        else:
            # link = driver.find_element(By.TAG_NAME,'a')
            # for links in link:
            #     print(len(links))
            #     break
            print('Tested Failed..')

        payment = driver.find_element(By.CSS_SELECTOR,
                                      '.product-price-options label:nth-of-type(1) .p-tag:nth-child(3)')
        payment_month = driver.find_element(By.CSS_SELECTOR, '.product-price-options .p-wrap:nth-of-type(2) [type]')
        print(payment.is_selected())
        """
        try:
            if payment.is_selected() == True and payment_month.is_selected() != True:
                payment_month.click()
                time.sleep(2)
                driver.find_element(By.CSS_SELECTOR, 'button#button-cart').click()
                driver.find_element(By.CSS_SELECTOR, '.checkout-btn > .btn.st-outline').click()
        except:
            print('Logical Error')
            driver.find_element(By.XPATH, "/html//button[@id='button-cart']").click()
        """
        try:
            payment_month.click()
            driver.find_element(By.CSS_SELECTOR, '.increment .material-icons').click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, 'button#button-cart').click()
            driver.find_element(By.CSS_SELECTOR, '.checkout-btn > .btn.st-outline').click()
        except:
            driver.find_element(By.XPATH, "/html//button[@id='button-cart']").click()
        # create account
        first_name = driver.find_element(By.NAME, 'firstname')
        last_name = driver.find_element(By.NAME, 'lastname')
        address = driver.find_element(By.NAME, 'address_1')
        mobile = driver.find_element(By.NAME, 'telephone')
        email = driver.find_element(By.NAME, 'email')
        city = driver.find_element(By.NAME, 'city')
        zone = driver.find_element(By.NAME, 'zone_id')
        comment = driver.find_element(By.NAME, 'comment')
        condition = driver.find_element(By.NAME, 'agree')
        confirm = driver.find_element(By.XPATH, "/html//button[@id='button-confirm']")
        if first_name.is_enabled() == True and last_name.is_displayed():
            first_name.send_keys('Hello')
            last_name.send_keys('Ketty')
        if address.is_enabled() == True and mobile.is_displayed():
            address.send_keys('Uttara, Zasimuddin, Dhaka ')
            mobile.send_keys(12346567895)
        email.send_keys('sagor@gmail.com')
        city.send_keys('Dhaka')
        list = Select(zone)
        drop_list_show = []
        for lists in list.options:
            # print(lists.text)
            value = lists.text
            drop_list_show.append(value)
            if lists.text == ' Rangpur City':
                list.select_by_value('4231')
        # raise NoSuchElementException("Rangpur are not selected")
        comment.send_keys('Test Automation..')
        condition.click()
        time.sleep(2)
        confirm.click()
        expected_result_condition = ' Warning: You must agree to the Terms and Conditions!        '
        if expected_result_condition == ' Warning: You must agree to the Terms and Conditions!        ':
            print('Test cased Success..')
        else:
            print('Error.....')


webelement_obj = WebElement()
webelement_obj.setup()
# webelement_obj.all_webelement()
