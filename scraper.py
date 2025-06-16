from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service()
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.olx.in/items/q-car-cover"

driver.get(url)
time.sleep(5)

titles = []
prices = []
locations = []

ads = driver.find_elements(By.CSS_SELECTOR, "li.EIR5N")
for ad in ads:
    try:
        title = ad.find_element(By.CSS_SELECTOR, "span._2tW1I").text
        price = ad.find_element(By.CSS_SELECTOR, "span._89yzn").text
        location = ad.find_element(By.CSS_SELECTOR, "span._2FcK0").text
        titles.append(title)
        prices.append(price)
        locations.append(location)
    except:
        continue

driver.quit()

df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Location": locations
})

df.to_csv("olx_car_covers.csv", index=False)
