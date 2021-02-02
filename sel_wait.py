import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.binary_location = "chrome-win\\chrome.exe"

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=op)

# wait command helps us in automation sync, balance between code execuation and page response
# implicit wait, this is applicable for all the elements on the pagek
# driver.get("http://demo.automationtesting.in/Register.html")
# assert "Register" in driver.title
# driver.implicitly_wait(5)   # wait 5 secs after making get request

# Explicit wait, applicable to certain elements and based on conditions
driver.get("https://www.expedia.com/")
driver.find_element(
    by=By.CSS_SELECTOR,
    value="li.uitk-tab-icon-text:nth-child(2)").click()   # click the flight button

driver.find_element(
    By.CSS_SELECTOR,
    "[data-testid='location-field-leg1-origin-container'").click()
elem_orgin = driver.find_element(
    By.CSS_SELECTOR,
    "[data-stid='location-field-leg1-origin-dialog-input'")
elem_orgin.send_keys("SFO")
elem_orgin.send_keys(Keys.RETURN)  # filling leaving from field


driver.find_element(
    By.CSS_SELECTOR,
    "[data-testid='location-field-leg1-destination-container'").click()
elem_dest = driver.find_element(
    By.CSS_SELECTOR,
    "[data-stid='location-field-leg1-destination-dialog-input'")
elem_dest.send_keys("NYC")
elem_dest.send_keys(Keys.RETURN)  # filling out going to from field

driver.find_element(
    By.CSS_SELECTOR, "button[data-testid='submit-button']").click()
