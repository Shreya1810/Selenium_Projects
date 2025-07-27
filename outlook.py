from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import os


#Path to excel file
excel_path = os.path.abspath("C:/Users/SinhaShreya/Downloads/B2B_Stage_Regression_22May 2025.xlsx")

# Start browser
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://outlook.office.com/mail/")
driver.maximize_window()

# email id
time.sleep(10)
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("s1003897@thyssenkrupp-materials.com")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

#Password
time.sleep(5)
driver.find_element(By.NAME, "passwd").send_keys("Automation@2025")
driver.find_element(By.ID,"idSIButton9").click()

#Click on new mail
time.sleep(10)
driver.find_element(By.XPATH,"//button[@aria-label='New mail']").click()

#Fill 'To' Field
time.sleep(5)
driver.find_element(By.XPATH,"//div[@aria-label='To']").send_keys('shreya.sinha@thyssenkrupp-materials.com')

#Fill CC filed
driver.find_element(By.XPATH,"//div[@aria-label='Cc']").send_keys('bilwa.pelapkar@thyssenkrupp-materials.com')

# Fill Subject line
driver.find_element(By.XPATH,"//input[@aria-label='Subject']").send_keys('Testing outlook automation via selenium')

#Fill email body
body_frame = driver.find_element(By.XPATH,"//div[contains(@aria-label, 'Message body')]")
body_frame.click()
body_frame.send_keys("Hello team,\n\nPlease find attached automation report.\n\nRegards,\nShreya Sinha")

#Attach file
attach_button = driver.find_element(By.XPATH,"//button[@aria-label='Attach file']")
attach_button.click()
time.sleep(5)

#upload from computer
upload_file = driver.find_element(By.XPATH,"//button[@name = 'Browse this computer']")
upload_file.click()
time.sleep(10)

# Use PyAutoGUI to interact with OS dialog
pyautogui.write(excel_path)
pyautogui.press('enter')

time.sleep(5)

# click on send key
driver.find_element(By.XPATH,"//button[@aria-label ='Send']").click()
time.sleep(5)

#logout
driver.find_element(By.XPATH, "//button[@aria-label='Account manager for tkM IND Thane Test CoE']").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Sign out").click()
time.sleep(5)

#close browser
driver.quit()