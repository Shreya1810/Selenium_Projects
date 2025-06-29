import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/loginpagePractise/')
driver.maximize_window()

#click on blinking text
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
time.sleep(2)
#focus on child window
windowsopened = driver.window_handles
driver.switch_to.window(windowsopened[1])

message = driver.find_element(By.CSS_SELECTOR, ".red").text
var = message.split("at")[1].strip().split(" ")[0]
driver.close()

time.sleep(5)
driver.switch_to.window(windowsopened[0])
#enter id and password and click on sign in
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(var)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys(var)

driver.find_element(By.CSS_SELECTOR,"#usertype").click()
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR,".alert-danger").text)
#close browser
driver.quit()