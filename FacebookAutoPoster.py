from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

#Set chrome options
chrome_options = Options()
prefs = {
    "profile.default_content_setting_values.notifications":2, #1-Allow , 2-Block
    "profile.default_content_setting_values.geolocation":2,
    "profile.default_content_setting_values.media_stream_camera":2,
    "profile.default_content_setting_values.media_stream_mic":2
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.facebook.com/')
driver.maximize_window()
time.sleep(5)

#Enter email
email_element = driver.find_element(By.XPATH, "//input[@id = 'email']").send_keys('sinhashreyaa18@gmail.com')
#Enter password
password_element  = driver.find_element(By.XPATH, "//input[@id='pass']").send_keys('Demoaccount@123')

driver.find_element(By.NAME, "login").click()
time.sleep(5)
#click on home
home_element = driver.find_element(By.XPATH, "//span[@class= 'x1n2onr6']").click()
time.sleep(5)

#click on post
post_element = driver.find_element(By.XPATH, "//div[@class = 'xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe']").click()
time.sleep(5)

#Write a post
text_element = driver.find_element(By.XPATH, "//div[@class = 'xzsf02u x1a2a7pz x1n2onr6 x14wi4xw x9f619 x1lliihq x5yr21d xh8yej3 notranslate']").send_keys('Hi there!')
time.sleep(5)

#click on post button
post_button = driver.find_element(By.XPATH, "//div[@aria-label='Post']")
post_button.click()

time.sleep(10)

print("Post submitted successfully!")
time.sleep(5)
#close browser
driver.quit()