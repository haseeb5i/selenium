import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

op = webdriver.ChromeOptions()
op.binary_location = "chrome-win\\chrome.exe"

driver = webdriver.Chrome(
    executable_path="drivers\\chromedriver.exe", options=op)
driver.maximize_window()

# wait command helps us in automation sync, balance between code execuation and page response
# implicit wait, this is applicable for all the elements on the pagek
driver.get("https://www.expedia.com/")
assert "Expedia" in driver.title
driver.implicitly_wait(5)   # wait 5 secs after making get request

# Explicit wait, applicable to certain elements and based on conditions
driver.find_element(
    by=By.CSS_SELECTOR,
    value="li.uitk-tab-icon-text:nth-child(2)").click()   # click the flight button

driver.find_element(
    By.CSS_SELECTOR,
    "[data-testid='location-field-leg1-origin-container'").click()
elem_orgin = driver.find_element(
    By.CSS_SELECTOR,
    "input#location-field-leg1-origin")
elem_orgin.send_keys("SFO" + Keys.RETURN)   # filling leaving from field

driver.find_element(
    By.CSS_SELECTOR,
    "[data-testid='location-field-leg1-destination-container'").click()
elem_dest = driver.find_element(
    By.CSS_SELECTOR,
    "input#location-field-leg1-destination")
elem_dest.send_keys("NYC")  # filling out going to from field
elem_dest.send_keys(Keys.RETURN)

driver.find_element(
    By.CSS_SELECTOR, "button[data-testid='submit-button']").click()

# wait for our element to appear after above action
wait = WebDriverWait(driver, 10)

ua_airline_element_loc = (By.CSS_SELECTOR, "input#preferred-airline-UA")
# once the condition becomes true, element is returned
ua_airline_element = wait.until(
    EC.presence_of_element_located(ua_airline_element_loc))
ua_airline_element.click()


# wait for some moments and close the window
time.sleep(3)
driver.quit()
