import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, value="cookie")

items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items if item.get_attribute("id")]


check_interval = 5
timeout = time.time() + check_interval
five_min = time.time() + 60 * 5

print("Starting Cookie Clicker bot...")

while True:
    cookie.click()


    if time.time() > timeout:

        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)


        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]


        money_text = driver.find_element(By.ID, value="money").text.replace(",", "")
        cookie_count = int(money_text)


        affordable_upgrades = {}
        for cost, upgrade_id in cookie_upgrades.items():
            if cookie_count >= cost:
                affordable_upgrades[cost] = upgrade_id

        
        if affordable_upgrades:
            highest_affordable_price = max(affordable_upgrades)
            purchase_id = affordable_upgrades[highest_affordable_price]
            driver.find_element(By.ID, value=purchase_id).click()

        
        timeout = time.time() + check_interval

    
    if time.time() > five_min:
        cps = driver.find_element(By.ID, value="cps").text
        print(f"Time is up! {cps}")
        break

driver.quit()
