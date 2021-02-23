import time
import platform

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


def init_webdriver():
    op = webdriver.ChromeOptions()
    op.add_argument("--headless")
    if platform.system() == "Linux":
        driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    elif platform.system() == "Windows":
        driver = webdriver.Chrome(executable_path="drivers\\chromedriver.exe")
    return driver

def login(driver: webdriver.Chrome, uname="kellie@inginim.com", passwd="Smecen123"):
    wait = WebDriverWait(driver, 30)
    # login and wait for the page to load
    driver.get("https://staging.smecen.com")
    uname_loc = (By.ID, "username")
    elm_uname = wait.until(EC.presence_of_element_located(uname_loc))
    elm_uname.send_keys(uname)
    driver.find_element_by_id("password").send_keys(passwd)
    driver.find_element_by_name("login").click()
    time.sleep(2)   # maybe we don't need this

def get_company_ERP(driver: webdriver.Chrome, c_name="AUTOMATION01"):
    # this method first searh for company name and then reaches
    # the target page in same fashion as a manual user would

    # wait = WebDriverWait(driver, 30)
    # driver.find_element_by_id("searchItem").send_keys(c_name)
    # company_card_loc = (By.CLASS_NAME, "dasboard-card")
    # elm_company_cards = wait.until(EC.presence_of_all_elements_located(company_card_loc))
    # for elm in elm_company_cards:
    #     card_title = elm.find_element_by_class_name("card-title").get_text()
    #     if card_title == c_name: 
    #         elm.find_element_by_link_text("Go to ERP").click()

    # driver.switch_to_window(driver.window_handles[1])

    # employee_xpath = "/html/body/div[3]/div[2]/div[1]/a[6]"
    # elm_employee = wait.until(EC.presence_of_element_located((By.XPATH, employee_xpath)))
    # elm_employee.click()

    # get to the target page directly    
    driver.get(f"https://{c_name.lower()}.c1.staging.smecen.com/web#home")
    driver.get(f"https://{c_name.lower()}.c1.staging.smecen.com/web#min=1&limit=80&view_type=list&model=hr.employee&menu_id=108&action=131")

def create_record(driver: webdriver.Chrome, data):
    """
    create and save one record at a time
    data = one row of pandas frame, containg fields to fill the form
    """
    wait = WebDriverWait(driver, 30)

    create_btn_loc = (By.CSS_SELECTOR, "button[accesskey='c']")
    elm_create_btn = wait.until(EC.presence_of_element_located(create_btn_loc))
    elm_create_btn.click()

    # employee name
    emp_name_loc = (By.ID, "o_field_input_4")
    elm_emp_name = wait.until(EC.presence_of_element_located(emp_name_loc))
    elm_emp_name.send_keys(data["emp_name"])

    def fill_field(method, loc, text="", press_enter=False):
        elem = driver.find_element(method, loc)
        ac = ActionChains(driver)
        ac.move_to_element(elem).click()
        ac.send_keys(text)
        if press_enter:
            ac.send_keys(Keys.ENTER)
        ac.perform()
    
    # EMPLOYMENT INFORMATION 
    fill_field(By.ID, "o_field_input_14", text=data["work_mobile"])
    fill_field(By.ID, "o_field_input_15", text=data["work_location"]) 
    fill_field(By.ID, "o_field_input_16", text=data["work_email"])
    # employment date
    elm_emp_join_cal = driver.find_element(By.NAME, "date_of_join")
    elm_emp_join_cal.click()
    elm_emp_join_cal.clear()
    elm_emp_join_cal.send_keys(data["emp_join_date"] + Keys.ENTER)

    # PERSONAL INFORMATION 
    pesnal_info_xpath = "/html/body/div[3]/div[2]/div[2]/div/div/div[2]/div/div[6]/ul/li[3]/a"
    driver.find_element_by_xpath(pesnal_info_xpath).click() 
    time.sleep(1)
    fill_field(By.ID, "o_field_input_49", text=data["bank_acc_holder"])

    # HR Settings
    hr_settings_xpath = "/html/body/div[3]/div[2]/div[2]/div/div/div[2]/div/div[6]/ul/li[6]/a"
    driver.find_element_by_xpath(hr_settings_xpath).click()
    time.sleep(1)

    # save the record
    driver.find_element(By.CSS_SELECTOR, "button[accesskey='s']").click()


def main():
    driver = init_webdriver()
    employes_data = pd.read_csv("employes_data.csv")
    login(driver)
    get_company_ERP(driver)
    create_record(driver, data=employes_data)


if __name__ == "__main__":
    main()