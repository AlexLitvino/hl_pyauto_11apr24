import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_path = ""  # TODO: put path to webdriver
driver = Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demo.guru99.com/popup.php")

initial_screen_id = driver.current_window_handle
print(initial_screen_id)
print(driver.window_handles)

click_here = driver.find_element(By.LINK_TEXT, 'Click Here')
click_here.click()

print(initial_screen_id)
print(driver.window_handles)

another_window_id = list(set(driver.window_handles) - set([initial_screen_id]))[0]
print(another_window_id)

driver.switch_to.window(another_window_id)

button2window = driver.find_element(By.NAME, 'btnLogin')
print(button2window.is_displayed())

driver.switch_to.window(initial_screen_id)
click_here = driver.find_element(By.LINK_TEXT, 'Click Here')
print(click_here.is_displayed())

time.sleep(2)
driver.quit()
