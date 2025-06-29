from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
time.sleep(5)

# <a> inside anchor tag is a link text "forgot password?" </a>
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form//div[1]/input").send_keys("demo@gmail.com")
#driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")

#driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text() = 'Save New Password']").click()
time.sleep(5)

#close browser
driver.quit()