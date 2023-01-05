import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
path = "G:\\SQA\\Automation\\DataDriven\\Data1.xlsx"
rows = XLUtils.getRowCount(path, "Sheet1")
for r in range(2, rows+1):
    userName = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element(By.NAME, "username").send_keys(userName)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button").click()

    expected_text = "Dashboard"

    if expected_text == "Dashboard":
        print("Test is passed..")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test pass")
    else:
        print('Tesed Failed..')
        XLUtils.writeData(path, "Sheet1", r, 3, "Tested failed")

    driver.find_element(By.CSS_SELECTOR, "img[alt='client brand banner']").click()
