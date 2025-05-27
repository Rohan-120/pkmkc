from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

chrome_drive_path="/usr/local/bin/chromedriver"
service = Service(executable_path=chrome_drive_path)
driver=webdriver.Chrome(service=service)

driver.get("https://www.google.com")
assert "google" in driver.title.lower()


time.sleep(5)

driver.quit()
