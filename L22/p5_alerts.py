import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_path = ""  # TODO: put path to webdriver
driver = Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demo.guru99.com/test/delete_customer.php")

submit_button = driver.find_element(By.NAME, 'submit')
submit_button.click()
time.sleep(2)
submit_alert = driver.switch_to.alert
print(submit_alert.text)
submit_alert.dismiss()
time.sleep(2)
submit_button.click()
submit_alert.accept()
time.sleep(2)
print(submit_alert.text)
submit_alert.accept()

time.sleep(2)
driver.quit()
