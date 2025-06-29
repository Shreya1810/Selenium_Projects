from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
time.sleep(3)

# handle dynamic dropdown
driver.find_element(By.ID, "autosuggest").send_keys('ind')
time.sleep(5)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

print(len(countries))
# loop through dropdown options which are visible and compare and click on that text
for country in countries:
    if country.text == "India":
        country.click()
        break

#print(driver.find_element(By.ID, "autosuggest").text) --> .text will not give output when the text is changed by our script dynamically it'll only work if we want to retrieve data from already present text in websites
assert driver.find_element(By.ID, "autosuggest").get_attribute("value")  == "India"

#Close the browser
driver.quit()