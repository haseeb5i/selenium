import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("drivers\\chromedriver.exe")

# # action_chains api supports most of the actions performed by the user
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element_by_id("txtUsername").send_keys("Admin")
# time.sleep(2)
# driver.find_element_by_id("txtPassword").send_keys("admin123")

# driver.find_element_by_id("btnLogin").click()

# elem_admin_menu = driver.find_element_by_id("menu_admin_viewAdminModule")
# elem_usrmgnt = driver.find_element_by_id("menu_admin_UserManagement")
# elem_usrmgnt_users = driver.find_element_by_id("menu_admin_viewSystemUsers")

# # mouse hover action
# ac = ActionChains(driver)
# ac.move_to_element(elem_admin_menu).move_to_element(elem_usrmgnt).pause(3)
# ac.move_to_element(elem_usrmgnt_users).click().perform()

# # double click action
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()

# elem_dble_click_cpy = driver.find_element_by_xpath(
#     "//*[@id='HTML10']/div[1]/button")
# ac = ActionChains(driver)
# ac.double_click(elem_dble_click_cpy).perform()

# # right click/context menu click
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# elem_rght_btn = driver.find_element_by_xpath(
#     "/html/body/div/section/div/div/div/p/span")

# ac = ActionChains(driver)
# ac.context_click(elem_rght_btn).perform()

# drag and drop actions
driver.get(
    "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

ac = ActionChains(driver)

# identify source and target element first
elem_src_box_1 = driver.find_element_by_id("box6")
elem_trgt_box_1 = driver.find_element_by_id("box106")
ac.drag_and_drop(elem_src_box_1, elem_trgt_box_1).perform()
time.sleep(2)

elem_src_box_2 = driver.find_element_by_id("box3")
elem_trgt_box_2 = driver.find_element_by_id("box103")
ac.drag_and_drop(elem_src_box_2, elem_trgt_box_2).perform()
