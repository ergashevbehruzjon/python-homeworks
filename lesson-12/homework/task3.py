from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

def scrape_laptops():
    driver = webdriver.Chrome()

    driver.get("https://www.demoblaze.com/")

    laptops_section = driver.find_element(By.LINK_TEXT, "Laptops")
    laptops_section.click()
    time.sleep(2)

    laptops = []
    next_button = driver.find_element(By.ID, "next2")
    next_button.click()
    time.sleep(2)

    laptop_cards = driver.find_elements(By.CLASS_NAME, "card-block")
    for card in laptop_cards:
        name = card.find_element(By.CLASS_NAME, "card-title").text.strip()
        price = card.find_element(By.TAG_NAME, "h5").text.strip()
        description = card.find_element(By.CLASS_NAME, "card-text").text.strip()
        laptops.append({"name": name,"price": price,"description": description})

    driver.quit()
    return laptops

laptops = scrape_laptops()
with open("laptops.json", "w") as file:
    json.dump(laptops, file, indent=4)
print(f"Scraped {len(laptops)} laptops and saved to laptops.json")