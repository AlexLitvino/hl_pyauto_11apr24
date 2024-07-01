from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By


driver_path = ""  # TODO: put path to webdriver
driver = Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://demo.guru99.com/test/radio.html')

# radio_button_1 = driver.find_element(By.ID, 'vfb-7-1')
# radio_button_2 = driver.find_element(By.ID, 'vfb-7-2')
#
# print("=== Before selection ===")
# print(f"1 displayed {radio_button_1.is_displayed()}")
# print(f"1 enabled {radio_button_1.is_enabled()}")
# print(f"1 selected {radio_button_1.is_selected()}")
# print()
# print(f"2 displayed {radio_button_2.is_displayed()}")
# print(f"2 enabled {radio_button_2.is_enabled()}")
# print(f"2 selected {radio_button_2.is_selected()}")
# print()
#
# radio_button_2.click()
# print("=== After 2 clicked ===")
# print(f"1 displayed {radio_button_1.is_displayed()}")
# print(f"1 enabled {radio_button_1.is_enabled()}")
# print(f"1 selected {radio_button_1.is_selected()}")
# print()
# print(f"2 displayed {radio_button_2.is_displayed()}")
# print(f"2 enabled {radio_button_2.is_enabled()}")
# print(f"2 selected {radio_button_2.is_selected()}")
# print()
#
# time.sleep(1)
# print("=== After 1 clicked ===")
# radio_button_1.click()
# print(f"1 displayed {radio_button_1.is_displayed()}")
# print(f"1 enabled {radio_button_1.is_enabled()}")
# print(f"1 selected {radio_button_1.is_selected()}")
# print()
# print(f"2 displayed {radio_button_2.is_displayed()}")
# print(f"2 enabled {radio_button_2.is_enabled()}")
# print(f"2 selected {radio_button_2.is_selected()}")

# ######################################################################################################################

check_box1 = driver.find_element(By.ID, 'vfb-6-0')
check_box3 = driver.find_element(By.ID, 'vfb-6-2')

print("=== Before selection ===")
print(f"1 displayed {check_box1.is_displayed()}")
print(f"1 enabled {check_box1.is_enabled()}")
print(f"1 selected {check_box1.is_selected()}")
print()
print(f"2 displayed {check_box3.is_displayed()}")
print(f"2 enabled {check_box3.is_enabled()}")
print(f"2 selected {check_box3.is_selected()}")
print()

time.sleep(2)
check_box1.click()
check_box3.click()

print("=== After click ===")
print(f"1 displayed {check_box1.is_displayed()}")
print(f"1 enabled {check_box1.is_enabled()}")
print(f"1 selected {check_box1.is_selected()}")
print()
print(f"2 displayed {check_box3.is_displayed()}")
print(f"2 enabled {check_box3.is_enabled()}")
print(f"2 selected {check_box3.is_selected()}")

time.sleep(2)
check_box3.click()
time.sleep(1)

driver.quit()
