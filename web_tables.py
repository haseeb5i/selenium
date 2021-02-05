import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# creating chromium driver with custom options
op = webdriver.ChromeOptions()
op.binary_location = "chrome-win\\chrome.exe"
# op.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path="drivers\\chromedriver.exe", options=op)

#### web tables ####
driver.get('http://test-sites.octoparse.com/?page_id=192')

# we can read data from tables on webpage to an array
# first get all the rows and columns number in a particular table, so that we can
# iterate over the table using xpaths to get all the values
rows = driver.find_elements(By.XPATH, '//table/tbody/tr')
print('number of rows', len(rows))
cols = driver.find_elements(By.XPATH, '//table/tbody/tr[1]/th')
print('number of columns', len(cols))

for i in range(2, len(rows) + 1):
    for j in range(1, len(cols) + 1):
        value = driver.find_element(
            By.XPATH, f'//table/tbody/tr[{i}]/td[{j}]').text
        print(value, end='   ')
    print()


#### Scrolling ####
