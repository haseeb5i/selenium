import os
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from my_parser import get_links

county_dic = {
    "Appling": 1,
    "Atkinson":  2,
    "Bacon":  3,
    "Baker":  4,
    "Baldwin":  5,
    "Banks":  6,
    "Barrow":  7,
    "Bartow":  8,
    "Ben Hill":  9,
    "Berrien": 10,
    "Bibb": 11,
    "Bleckley": 12,
    "Gwinnett": 67
}

op = webdriver.ChromeOptions()
op.binary_location = "chrome-win\\chrome.exe"
# op.add_argument("--headless")
# op.add_argument("--no-sandbox")
# op.add_argument("--disable-dev-sh-uage")
exc_path = "drivers\\chromedriver.exe"

driver = webdriver.Chrome(exc_path, options=op)
driver.get("https://www.georgiapublicnotice.com")
assert "Georgia Public Notice" in driver.title

# getting the search box
srch = driver.find_element_by_id("ctl00_ContentPlaceHolder1_as1_txtSearch")
search_qry = "foreclosure"
# making sure our search is clear and then sending our query
srch.clear()
srch.send_keys(search_qry)
time.sleep(3)

# click on the county element to get a dropdown list
driver.find_element_by_id("ctl00_ContentPlaceHolder1_as1_divCounty").click()
# get the county name and number and make its xml path
county = "Gwinnett"  # TODO take this from user
county_num = str(county_dic.get(county))
county_xml_path = f"//ul[@id='ctl00_ContentPlaceHolder1_as1_lstCounty']/li[{county_num}]/label[1]"
print(county_xml_path)
# finally, select that county
driver.find_element_by_xpath(county_xml_path).click()
time.sleep(3)

# find the date rage element in the form to get a dropdown list
driver.find_element_by_id("ctl00_ContentPlaceHolder1_as1_divDateRange").click()
# find element to select the method "in the last x day(s)"
driver.find_element_by_id(
    "ctl00_ContentPlaceHolder1_as1_rbLastNumDays").click()
# Give the number of days to limit our search and find the element
num_last_days = 2   # TODO take this from user
date_setter = driver.find_element_by_id(
    "ctl00_ContentPlaceHolder1_as1_txtLastNumDays")
# clean the box, input our number and hit enter
date_setter.clear()
date_setter.send_keys(str(num_last_days))
time.sleep(5)
date_setter.send_keys(Keys.RETURN)

# finally get page source and close our webdriver
html = driver.page_source
# driver.delete_cookie("ASP.NET_SessionId")
# my_cookie = {
#     "domain"   : 'www.georgiapublicnotice.com',
#     "httpOnly" : True,
#     "name"     : 'ASP.NET_SessionId',
#     "path"     : '/',
#     "sameSite" : 'None',
#     "secure"   : True,
#     "value"    : "v2qybuhqy5l4z1l1jfwgi5yh"
# }
# driver.add_cookie(my_cookie)
cookies = driver.get_cookies()
print(cookies)
print(type(cookies))

# # get our links and save them to a file
# links = get_links(html)

# base_url = "https://www.georgiapublicnotice.com/"
# with open("search_result.txt", "w") as f:
#     for link in links:
#         f.write(base_url + link + "\n")
