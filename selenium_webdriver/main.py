from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Home")

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, "a-price-fraction")

# print(f"Price: {price_dollar.text}.{price_cent.text} dollars")


# search_bar = driver.find_element(By.NAME, value="q")

# print(search_bar)


# bug_link = driver.find_element(By.XPATH , value="//*[@id='site-map']/div[2]/div/ul/li[3]/a")

# print(bug_link.text)

article_count = driver.find_element(By.CSS_SELECTOR , value="#articlecount a")
article_count.click()






driver.quit()
# driver.close()