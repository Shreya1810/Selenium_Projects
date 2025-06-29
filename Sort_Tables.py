import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
veggie_list =[]
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
driver.maximize_window()

# click on column header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

# store the veggie_list
lst = driver.find_elements(By.XPATH,"//tr/td[1]")
for i in lst:
    veggie_list.append(i.text)
originalBrowserSortedlist = veggie_list.copy()
# sort this list
veggie_list.sort()
print(f"Original sorted list via column header : {originalBrowserSortedlist}")
print(f"After applying sort function : {veggie_list}")
# assert -> compare whether sorted list == veggie_list
assert  originalBrowserSortedlist == veggie_list


time.sleep(5)

#close browser
driver.quit()