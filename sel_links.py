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

######### links #########
# driver.get("https://duckduckgo.com/?t=ffab&q=scrapy+image+pipelines&ia=web")

# # find all the links on a webpage
# links = driver.find_elements(by=By.TAG_NAME, value='a')
# print('Total number of links found: ', len(links))

# # find links with specific link text and click
# driver.find_element(By.LINK_TEXT, 'DuckDuckGo').click()

# # find links with specific link text using substring of text and click
# driver.back()
# driver.find_element(By.PARTIAL_LINK_TEXT, 'scrapy').click()

######## alerts  #######
# driver.get('https://testautomationpractice.blogspot.com/')
# # open the alert using a button on the webpage
# # we can't perofrm actions on alert window as it is not a webelement
# # first switch to the alert window and then accept the alert or cancel it
# driver.find_element(
#     By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button').click()
# time.sleep(5)
# driver.switch_to_alert().accept()

# driver.find_element(
#     By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button').click()
# time.sleep(5)
# driver.switch_to_alert().dismiss()

######## working with frames ######
# a frame is essentially a seperate window on a webpage, with its own scroll bar if scrollable
# so we can not directly interact with elements in different frames, without switching to a specific frame first
# driver.get(
#     "https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# # switch_to.frame(name|id|index)    - a driver method to switch between frames using different methods
# driver.switch_to.frame('packageListFrame')
# # now we can normally interact with elements in this frame
# driver.find_element(By.LINK_TEXT, 'org.openqa.selenium.chrome').click()
# time.sleep(3)
# driver.back()

# # now we cannot directly jump to another frame, we first need to go back to main frame
# # and from there we can switch to some other frame, there is once convience method for that
# # instead of manually remembering the default window
# driver.switch_to.default_content()

# driver.switch_to.frame("packageFrame")
# driver.find_element(By.LINK_TEXT, 'Alert').click()
# time.sleep(3)

####### multiple tabs/windows ######
# first window and tab are same, second every widow has a handle that can be used
# to switch to that window, we can perform actions only in current window
driver.get('http://demo.automationtesting.in/Windows.html')
# show the handle of our current focused window
print('current window handle', driver.current_window_handle)
time.sleep(3)

# show the handles of all windows in our browser, firstly let's open a new window
driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()
print('all handles', driver.window_handles)

# so once we obtained the window handle, we can switch to it and can fetch like a new page or perform other action
print("current window title:", driver.title)

sec_window_handle = driver.window_handles[1]
driver.switch_to.window(sec_window_handle)
print("switched to second window:", driver.title)
# closes only focued window
driver.close()
