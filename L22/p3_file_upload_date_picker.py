import os
import time

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_path = ""  # TODO: put path to webdriver
driver = Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# # Uploading file
# driver.get('https://www.imgonline.com.ua/eng/combine-two-images-into-one.php')
#
# upload_file = driver.find_element(By.XPATH, "//input[@name='uploadfile']")
# image_path = r'flags.png'
# upload_file.send_keys(os.path.abspath(image_path))

# ######################################################################################################################
# Datepicker

driver.get('https://demo.guru99.com/test/')
date_picker = driver.find_element(By.XPATH, "//input[@name='bdaytime']")
date_picker.send_keys('11012023')
date_picker.send_keys(Keys.TAB)
date_picker.send_keys('0914PM')

# submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
# submit_button.click()

form = driver.find_element(By.XPATH, "//form[@name='bdate']")
form.submit()

time.sleep(3)
driver.quit()
