import time
from selenium import webdriver

# driver_path = r'C:\Users\User\Desktop\jenkins_test\driver\chromedriver.exe'
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.ulearning.app/ulearning/index.html#/i18n')
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/header/nav/div/button").click()
time.sleep(2)
driver.find_element(By.ID,"userLoginName").send_keys('Auto_Manageadmin1')
driver.find_element(By.ID,"userPassword").send_keys('wenhua123')
time.sleep(2)
driver.quit()