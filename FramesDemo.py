import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://the-internet.herokuapp.com/iframe')
driver.maximize_window()

# not able to iframe editbox as it is not accessible
#driver.switch_to.frame("mce_0_ifr")
#driver.find_element(By.ID,"tinymce").clear()
#driver.find_element(By.ID,"tinymce").send_keys('I am on frame')
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)