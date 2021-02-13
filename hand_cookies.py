import logging
from selenium import webdriver

# driver = webdriver.Chrome(executable_path="drivers\\chromedriver.exe")

# # cookie store information in key-value pairs, info about
# # current session, user interaction with the site etc.
# # a cookie will have a name and some values as a dict

# #### capture all cookies from browser ####
# driver.get("https://www.amazon.in/")
# cookies = driver.get_cookies()
# print("all cookies", len(cookies))
# print(cookies)

# #### adding new cookie to the browser ####
# new_cookie = {
#     'name': 'my_cookie',
#     'value': '12345'
# }
# driver.add_cookie(new_cookie)
# cookies = driver.get_cookies()
# print("all cookies", len(cookies))
# print(cookies)

# #### deleting a cookie using its name ####
# driver.delete_cookie('my_cookie')
# cookies = driver.get_cookies()
# print("all cookies", len(cookies))

# #### deleting all the cookies ####
# driver.delete_all_cookies()
# cookies = driver.get_cookies()
# print("all cookies", len(cookies))

#### logging ####
logger = logging.getLogger()

s_handler = logging.StreamHandler()
f_handler = logging.FileHandler('test.log')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s: %(message)s',
    handlers=[s_handler, f_handler]
)

logger.debug("some debug log")
logger.info("some info log")
logger.warning("some warning log")
logger.error("some error log")

# a better method, create handler, specify loggin level and format for these
# handlers, get a logger and add these handlers
