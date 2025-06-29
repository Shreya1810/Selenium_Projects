import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

name = "Shreya"

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
time.sleep(5)
# selected id using css_selector
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()

# Switch from driver to alert mode
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
# check whether given name  is presernt in alert pop message
assert name in alert_text

# To click on ok button on alert pop up
alert.accept()
# to click on cancel button -> alert.dismiss()
# check whether given name  is presernt in alert pop message

# close browser
driver.quit()