import time

from selenium import webdriver
from selenium.webdriver import ActionChains


# using chromedriver
# op = webdriver.ChromeOptions()
# custom_prefs = {
#     "download.default_directory": "C:\\Users\\GhosT\\Downloads\\Video",
# }
# op.add_experimental_option("prefs", custom_prefs)
# driver = webdriver.Chrome("drivers\\chromedriver.exe", options=op)


# using geckodriver
# to disable download popup window in firefox
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                  "text/plain, application/pdf")
fp.set_preference("browesr.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "C:\\Users\\GhosT\\Downloads\\Video")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)
driver = webdriver.Firefox(
    firefox_profile=fp, executable_path="drivers\\geckodriver.exe")

# #### file upload ####
# if our target element is inside a form tag, switch to it
# driver.switch_to_frame(0)   # there is only frame, so switching by index

# driver.get("http://demo.automationtesting.in/FileUpload.html")

# # uploading files to the browser, input file path and use forward slashes
# file_path = "C://Users/GhosT/Downloads/stuff/output21.csv"
# driver.find_element_by_xpath(
#     "//*[@id='input-4']").send_keys(file_path)

#### download file ####
driver.get("http://demo.automationtesting.in/FileDownload.html")

# download a text file
driver.find_element_by_id("textbox").send_keys(
    "a useful text downloaded from selenium")   # put some text in the box
driver.find_element_by_id("createTxt").click()  # generate the text file
# download the text file
driver.find_element_by_id("link-to-download").click()

# download a pdf file
driver.find_element_by_id("pdfbox").send_keys(
    "a useful pdf downloaded from selenium")   # put some text for pdf in the box
driver.find_element_by_id("createPdf").click()  # generate the pdf file
# download the pdf file
driver.find_element_by_id("pdf-link-to-download").click()
