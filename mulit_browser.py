from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# # creating chromium driver with custom options
# op = webdriver.ChromeOptions()
# op.binary_location = "chrome-win\\chrome.exe"
# # op.add_argument("--headless")
# # op.add_argument("--no-sandbox")
# # op.add_argument("--disable-dev-sh-uage")   #only in unix like
# driver = webdriver.Chrome(executable_path="chromedriver.exe", options=op)

# # creating firefox driver, custom options are available in webdriver.FirefoxProfile
driver = webdriver.Firefox(executable_path="geckodriver.exe")

# creating an edge driver, new so less documentation
# driver = webdriver.Edge(executable_path="msedgedriver.exe")

driver.get("https://www.google.com")
print(driver.title)
driver.close()    # exits the browser if only one tab/window
