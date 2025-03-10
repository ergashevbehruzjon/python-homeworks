from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://example.com")

print("Title: ", driver.title)

import time
time.sleep(5)

driver.quit()