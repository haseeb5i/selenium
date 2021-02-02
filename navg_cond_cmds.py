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

# first url we visit
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)    # title of the page

# second url we visit
driver.get("https://www.pavantestingtools.com/")
print(driver.title)    # title of the page

# go back a page
# ? do we neeed time.sleep()
time.sleep(3)
driver.back()
print(driver.title)    # title of the page

# go forward a page
time.sleep(3)
driver.forward()
print(driver.title)    # title of the page

##################################################
# is_displayed()    - can check display status on any element
# is_enabled()      - can check enable status on any element
# is_selected()     - can check selected status on checkboxes and radio button elements

driver.get("http://demo.automationtesting.in/Index.html")
elem_reg_btn = driver.find_element(by=By.CSS_SELECTOR, value="#enterimg")
elem_signup = driver.find_element(by=By.CSS_SELECTOR, value="#email")
# true if element is displayed, false otherwise
print(elem_reg_btn.is_displayed())
# true if element is enabled, false otherwise
print(elem_reg_btn.is_enabled())

##########################################################
# send_keys()   - send keystrokes to element which accepts them
# click()       - click the element if clickable
elem_signup.send_keys("ravenredstain@outlook.com")
time.sleep(3)
elem_reg_btn.click()

# quite the browser
driver.quit()
