import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

# Expected list of items
expected_list = ['Cucumber - 1 Kg' ,'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actual_list = []
driver = webdriver.Chrome()

# each line of code will wait for 5 secs max to search for the data if not found
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# using .classname for css_selector
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys('ber')
time.sleep(2)

results = driver.find_elements(By.XPATH,"//div[@class = 'products']/div")
count = len(results)
print(count)
assert count > 0
# iterate through each product found related to text 'ber' and click on add to cart button for those products
for result in results:
    actual_list.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()
assert expected_list == actual_list

# click on cart button
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
# click on proceed to checkout button
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# sum validations
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum += int(price.text)

print(sum)

total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == total_amount

# enter promo code and click on apply coupon button
#driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys('rahulshettyacademy')
# or we can use css_selector in order to input promocode using class

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Explicit wait -> we can keep globally implicit wait for all the steps but for the individual step where we know it takes sometime to load there we have to put explicit wait
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
#check message after applying promo code..
code_info = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(code_info)
assert code_info == "Code applied ..!"

# Amount after discount will always less than total amount
total_after_discount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert total_amount > total_after_discount

# close browser
driver.quit()
