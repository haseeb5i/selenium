import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# creating chromium driver with custom options
op = webdriver.ChromeOptions()
op.binary_location = "chrome-win\\chrome.exe"
# op.add_argument("--headless")
# op.add_argument("--no-sandbox")
# op.add_argument("--disable-dev-sh-uage")   #only in unix like
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=op)

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)    # title of the page
print(driver.current_url)   # current url of the windows
# find an element on the webpage
driver.find_element(
    by=By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()

time.sleep(5)

# only closes focused tab/window
driver.close()
# quite the browser
driver.quit()
