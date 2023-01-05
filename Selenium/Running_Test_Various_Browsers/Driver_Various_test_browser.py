import time
from selenium import webdriver


class VariousBrowserTest:
    global driver

    def chromeTest(self):
        driver = webdriver.Chrome(executable_path='G:\\SQA\driver\\chrome\\chromedriver.exe')
        driver.maximize_window()
        driver.get('https://www.google.com/')
        time.sleep(2)
        print(driver.title)
        driver.close()

    def firefoxTest(self):
        driver = webdriver.Firefox(executable_path='G:\\SQA\\driver\\Firefox\\geckodriver.exe')
        driver.maximize_window()
        driver.get('https://www.apple.com/')
        time.sleep(2)
        print(driver.current_url)
        driver.close()

    def edgeTest(self):
        driver = webdriver.Edge('G:\\SQA\\driver\\Edge\\msedgedriver.exe')
        driver.maximize_window()
        driver.get('https://www.facebook.com/')
        time.sleep(2)
        print(driver.get_cookies())
        driver.close()


varioustest = VariousBrowserTest()
varioustest.chromeTest()
varioustest.firefoxTest()
varioustest.edgeTest()
