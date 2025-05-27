from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

# Open Google
browser.get("https://www.google.com")

# Check if title contains 'google'
assert 'google' in browser.title.lower()

# Find search input field
elem = browser.find_element(By.NAME, 'q')

# Type query and press Enter
elem.send_keys('openAI' + Keys.RETURN)

# Wait to see results
time.sleep(10)

# Close the browser
browser.quit()
