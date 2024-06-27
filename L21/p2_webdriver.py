from time import sleep

from selenium.webdriver import Chrome, Keys, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = ""  # TODO: put path to webdriver

chrome_options = ChromeOptions()
chrome_options.add_argument('--headless=new')

driver = Chrome(service=Service(driver_path), options=chrome_options)
#driver.implicitly_wait(time_to_wait=3)

wait = WebDriverWait(driver, 3)

driver.get("https://google.com")

text_field = driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]')
text_field.send_keys("Croatia")
#text_field.send_keys("Ukraine")
#sleep(1)
#text_field.clear()
# for _ in range(5):
#     text_field.send_keys(Keys.BACKSPACE)
#     sleep(0.2)

#sleep(2)
# wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@role="listbox"]/li[1]')))
# hint = driver.find_element(By.XPATH, '//ul[@role="listbox"]/li[1]')

hint = wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[@role="listbox"]/li[1]')))
hint.click()

wait.until(EC.visibility_of_element_located((By.XPATH, '//span/a/h3')))

headers = driver.find_elements(By.XPATH, '//span/a/h3')
#import pdb; pdb.set_trace()
# for header in headers:
#     print(header.text)

# text_field = driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]')
#
# print(text_field.get_attribute("value"))
# print(text_field.get_attribute("autocomplete"))
# print(text_field.get_property("value"))
# print(text_field.get_property("autocomplete"))

wiki_link = driver.find_element(By.XPATH, '(//div/span/a/h3)[1]')
wiki_link.click()
# driver.back()
# driver.refresh()
# driver.forward()

# print(driver.title)
# print(driver.current_url)
# print(driver.page_source[:100])
print(driver.name)

flag = driver.find_element(By.XPATH, '//a[@title="Flag of Croatia"]/img')
flag.screenshot('flag.png')

driver.save_screenshot('page.png')

sleep(2)
driver.quit()
