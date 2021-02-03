import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# creating chromium driver with custom options
op = webdriver.ChromeOptions()
op.binary_location = "chrome-win\\chrome.exe"
# op.add_argument("--headless")
# op.add_argument("--no-sandbox")
# op.add_argument("--disable-dev-sh-uage")   #only in unix like
driver = webdriver.Chrome(
    executable_path="drivers\\chromedriver.exe", options=op)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
time.sleep(2)

print(driver.title)         # title of the page
print(driver.current_url)   # current url of the windows
html = driver.page_source   # gives unrendered page html
driver.maximize_window()    # does what it says
driver.minimize_window()    # does what it says
driver.refresh()            # does what it says
driver.save_screenshot("temp\\screenshot.png")  # takes screenshot of the page


# find an element on the webpage, in the end css is used (classes are usually same for related elements)
# other available methods are by_name, by_id, by_css_selector etc.
# find element returns WebElement object, which can be interacted with

elem_frst_name = driver.find_element(
    by=By.CSS_SELECTOR, value="#RESULT_TextField-1")
elem_last_name = driver.find_element(by=By.ID, value="RESULT_TextField-2")
elem_gender_btn = driver.find_element_by_id("RESULT_RadioButton-7_0")
elem_avb_day_btn = driver.find_element_by_id("RESULT_CheckBox-8_5")

# we can check status of the elemenet using on of the following
# is_displayed()    - can check display status on any element
# is_enabled()      - can check enable status on any element
# is_selected()     - can check selected status on checkboxes and radio button elements
print("First name box displayed", elem_frst_name.is_displayed())
print("Last name box enabled", elem_last_name.is_enabled())
print("Gender radio button selected status: ", elem_gender_btn.is_selected())

# we can interact with elements
# clear()       - clears an input text box
# send_keys()   - send keystrokes to interactable input boxes
# click()       - click the element if clickable
elem_frst_name.clear()
elem_frst_name.send_keys("Raven")
elem_last_name.clear()
elem_last_name.send_keys("Redstain")
# regular click will throw an error as two radio buttons are connected
driver.execute_script("arguments[0].click();", elem_gender_btn)
# webdriver.ActionChains(driver).move_to_element(elem_gender_btn).click(elem_gender_btn).perform()
driver.execute_script("arguments[0].click();", elem_avb_day_btn)
time.sleep(3)

# working with dropdowns, we can select one option from a dropdown menu
# we can capture an option, and count how many options are present
elem_time_dropdown = driver.find_element_by_id("RESULT_RadioButton-9")
slctd_time_dropdown = Select(elem_time_dropdown)
# some methods to select option from the dropdown
slctd_time_dropdown.select_by_visible_text("Morning")
# slctd_time_dropdown.select_by_index(2)    # index start form 0
# lctd_time_dropdown.select_by_value("Radio-2")  # value is option attribute

# check all the available options in selected dropdown
# text of captured options, as these are webelement.WebElement objects, so
print([op.text for op in slctd_time_dropdown.options])

# we can go to a new link in the current tab/window
driver.get("https://www.google.com/")

# once we have some histroy, we can navigte
driver.back()      # to go back a page
time.sleep(2)
driver.forward()    # go forward a page
time.sleep(2)

# only closes focused tab/window
# driver.close()

# quite the browser
driver.quit()
