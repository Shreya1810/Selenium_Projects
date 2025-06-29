import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Click Here").click()

# Grab all the windows opened using
windowsopened = driver.window_handles
# after the above click it'll open a new window (child window)
# It'll work when we'll seitch the window
driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)

driver.close()

driver.switch_to.window(windowsopened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)



