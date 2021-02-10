from selenium import webdriver
from selenium.webdriver.common.keys import Keys

op = webdriver.ChromeOptions()
op.binary_location = "chrome-win\\chrome.exe"
driver = webdriver.Chrome("drivers\\chromedriver.exe", options=op)
driver.maximize_window()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

#### scroll by pixel value ####
# driver.execute_script("window.scrollBy(0, 1000)")

#### scroll to an element ####
# NOTE: Action chain's move_to_element or webelement.some_action also move us to the certain eleemnt
pak_flag_xpath = "/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/table[2]/tbody/tr[35]/td[2]"
elem_pak_flag = driver.find_element_by_xpath(pak_flag_xpath)
driver.execute_script("arguments[0].scrollIntoView()", elem_pak_flag)

#### sctoll to the end of page ####
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
