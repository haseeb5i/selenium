"""
Interfacing selenium with different browsers using their webdrivers.
- Controlling chromium with chorme webdriver
- Controlling firefox using geckodriver
- Controlling ms edge witg msedgedriver
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# creating chromium driver with custom options
op = webdriver.ChromeOptions()
op.binary_location = "chrome-win\\chrome.exe"
# op.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path="drivers\\chromedriver.exe", options=op)

driver.get("https://www.google.com")
print(driver.title)
driver.close()    # exits the browser if only one tab/window

# # creating firefox driver, custom options are available in webdriver.FirefoxProfile
driver = webdriver.Firefox(executable_path="drivers\\geckodriver.exe")

driver.get("https://www.google.com")
print(driver.title)
driver.close()    # exits the browser if only one tab/window

# creating an edge driver, new so less documentation
driver = webdriver.Edge(executable_path="drivers\\msedgedriver.exe")

driver.get("https://www.google.com")
print(driver.title)
driver.close()    # exits the browser if only one tab/window
