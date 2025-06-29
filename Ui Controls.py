import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
time.sleep(5)
options = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
print(len(options))

for i in options:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()
        break

# Hnadle radio button
radio_buttons = driver.find_elements(By.XPATH, "//input[@class = 'radioButton']")
print(len(radio_buttons))

for radiobutton in radio_buttons:
    if radiobutton.get_attribute("value") == "radio1":
        radiobutton.click()
        assert radiobutton.is_selected()
        break

# Lets say you know that the index of the radio buttons won't change then you can use indexing to select the desired option in radio button
radio = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radio[2].click()
assert radio[2].is_selected()

# check hide and show input box
# before hiding
assert driver.find_element(By.ID, "displayed-text").is_displayed()

# after hiding it shouldn't be displayed
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

time.sleep(4)

#close browser
driver.quit()