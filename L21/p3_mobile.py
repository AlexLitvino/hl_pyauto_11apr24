import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_path = ""  # TODO: put path to webdriver

options = ChromeOptions()
mobile_emulation = {"deviceName": "Nexus 5"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = Chrome(service=Service(driver_path), options=options)


driver.get('http://google.com')
query_input = driver.find_element(By.NAME, 'q')
query_input.send_keys('Croatia')
time.sleep(3)

driver.quit()
