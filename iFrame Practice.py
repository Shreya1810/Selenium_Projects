import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

driver.execute_script("window.scrollBy(0,1000);")
time.sleep(5)
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"Courses").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys('Selenium')

time.sleep(5)
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h1").text)

#close browser
driver.quit()