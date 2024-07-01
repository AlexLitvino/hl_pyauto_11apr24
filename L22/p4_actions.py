import time

from selenium.webdriver import Chrome, Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = ""  # TODO: put path to webdriver
driver = Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://en.wikipedia.org/wiki/Croatia")

action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

time.sleep(2)
driver.quit()
