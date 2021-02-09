# -*- coding: utf-8 -*-
import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions

from html_table_parser import HTMLTableParser


def login(driver, user_name="yixun1", passwd="a121212"):
    while True:
        try:
            # get the login page
            driver.get("http://dt.data1688.com/login")
            # let's login first
            driver.find_element_by_id("userName").send_keys(user_name)
            driver.find_element_by_id(
                "password").send_keys(passwd + Keys.ENTER)
            time.sleep(2)
            break
        except exceptions.NoSuchElementException:
            print("failed loading login page, refreshing")
            driver.refresh()
            time.sleep(3)
        except exceptions.TimeoutException:
            # sometimes page loading takes too much time
            print("failed loading login page due to timeout, refreshing")
            driver.refresh()
            time.sleep(3)


def get_database_page(driver):
    # get the transactions results page
    # TODO: Clean this
    try:
        srch_xpath = "span > span.ant-input-search > input"
        driver.find_element_by_css_selector(
            srch_xpath)
        time.sleep(5)
        driver.get("http://dt.data1688.com/overseas/global")
    except exceptions.NoSuchElementException:
        # just move manually there
        time.sleep(5)
        print("failed, getting the search page")
        driver.get("http://dt.data1688.com/overseas/global")
        time.sleep(3)


def make_filtered_search(driver, start_date="2021-01-01", end_date="2021-01-01", origin="china"):
    wait = WebDriverWait(driver, 10)
    cal_start_date_xpath = "//*[@id='DATE']/span/input[1]"
    while True:
        try:
            elem_cal_start_date = wait.until(
                EC.presence_of_element_located((By.XPATH, cal_start_date_xpath)))
            driver.execute_script("arguments[0].click();", elem_cal_start_date)
            time.sleep(1)
            break
        except exceptions.TimeoutException:
            print("failed, reloading search page")
            driver.refresh()
            time.sleep(2)
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    # set the date range
    ac = ActionChains(driver)
    ac.move_to_element(elem_cal_start_date).click()
    ac.send_keys(Keys.ARROW_UP + 4*Keys.DELETE + str(start_date.year))
    ac.send_keys(Keys.ARROW_RIGHT + 2*Keys.DELETE + "01")
    ac.send_keys(Keys.ARROW_RIGHT + 2*Keys.DELETE + "01")
    ac.send_keys(Keys.TAB)
    ac.send_keys(Keys.ARROW_UP + 4*Keys.DELETE + str(end_date.year))
    ac.send_keys(Keys.ARROW_RIGHT + 2*Keys.DELETE + "01")
    ac.send_keys(Keys.ARROW_RIGHT + 2*Keys.DELETE + "01")
    ac.send_keys(Keys.ARROW_RIGHT + 2*Keys.DELETE + str(start_date.month))
    ac.send_keys(Keys.ENTER)
    ac.perform()
    print("time set")
    time.sleep(2)
    # select origin country
    origin_country = origin
    driver.find_element_by_id("ORIGIN_COUNTRY_TC").send_keys(origin_country)
    time.sleep(1)
    # select destination region
    all_region_btn_xpath = "//*[@id='root']/div/div[3]/div[1]/div/div/div/div/div[3]/label/span[1]/input"
    elem_all_region_btn = driver.find_element_by_xpath(all_region_btn_xpath)
    if elem_all_region_btn.is_selected():
        elem_all_region_btn.click()
        time.sleep(0.5)
    asia_region_btn_xpath = "//*[@id='root']/div/div[3]/div[1]/div/div/div/div/div[3]/div/label[4]/span[1]/input"
    driver.find_element_by_xpath(asia_region_btn_xpath).click()
    time.sleep(1)
    # submit the filter/srch query
    driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(1)


def increase_product_count(driver):
    # increase the item count per page
    row_per_page_xpath = "//*[@id='root']/div/div[3]/div[3]/div[2]/div/div[3]/div[1]/div[3]/div/div/ul/li[11]/div[1]"
    try:
        ac = ActionChains(driver)
        elem_increase_count = driver.find_element_by_xpath(row_per_page_xpath)
        ac.move_to_element(elem_increase_count).click()
        ac.send_keys(2*Keys.ARROW_DOWN + Keys.ENTER)
        ac.perform()
        driver.execute_script("window.scrollTo(0, 0)")
        return 40
    except exceptions.NoSuchElementException:
        print("failed yet again")
        return 20


def mutate_dom(driver, product_count=20):

    # NOTE: there are still some bugs
    wait = WebDriverWait(driver, 10)
    product_table_xpath = "//*[@id='root']/div/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[3]/div/div/div/div/div/table/tbody"
    no_of_products = product_count
    product_counter = 1

    while product_counter <= no_of_products:
        try:
            product_detail_xpath = product_table_xpath + \
                f"/tr[{product_counter}]/td[5]/span/span/a"
            elem_product_detail = wait.until(
                EC.presence_of_element_located((By.XPATH, product_detail_xpath)))
            # click here to mutate the dom
            driver.execute_script("arguments[0].click();", elem_product_detail)
            time.sleep(0.5)
            # only increment if reached here
            product_counter += 1
            # wait for the close button and close it
            # close_btn_xpath = f"/html/body/div[{product_counter+2}]/div/div[2]/div/div[2]/button"
            # elem_close_btn = wait.until(EC.element_to_be_clickable(
            #     (By.XPATH, close_btn_xpath)))
            # elem_close_btn.click()
        except exceptions.TimeoutException:
            print("failed loading the product detail page, retrying")
        #     # needs to scroll down
        #     if elem_close_btn.is_displayed():
        #         print("closing agin")
        #         elem_close_btn.click()
        # except exceptions.NoSuchElementException:
        #     # page needs to scroll to find the elemenets
        #     print("failed to find the elemenet, scrolling down")
        #     driver.execute_script(f"window.scrollTo(0, {scroll_height})")
        #     scroll_height += 300
        # except exceptions.ElementClickInterceptedException:
        #     # maybe the product page is not closed properly
        #     print("click intercepted error")
        #     if elem_close_btn.is_displayed():
        #         print("closing agin")
        #         elem_close_btn.click()

    time.sleep(3)
    product_counter = no_of_products + 2

    while product_counter >= 3:
        close_btn_xpath = f"/html/body/div[{product_counter}]/div/div[2]/div/div[2]/button"
        elem_close_btn = wait.until(
            EC.presence_of_element_located((By.XPATH, close_btn_xpath)))
        ActionChains(driver).move_to_element(elem_close_btn).click().perform()
        time.sleep(0.5)
        product_counter -= 1


def parse_data(driver):

    html = driver.find_element_by_tag_name(
        "html").get_attribute("innerHTML")
    p = HTMLTableParser()
    # html is of type str
    p.feed(html)

    # at every seventh index new detail_table starts and first sub_table is empty
    table_idxs = [i for i, t in enumerate(p.tables) if len(t) == 0]

    transactions_info = []
    for i, idx in enumerate(table_idxs):
        transactions_info.append([])
        for l in range(1, 7):
            flat_list = [item for sub_list in p.tables[idx+l]
                         for item in sub_list]
            transactions_info[i].append(flat_list)

    with open("data.txt", "w", encoding="utf-8") as wt:
        for trans in transactions_info:
            for sub_table in trans:
                sub_table_str = ' '.join(sub_table)
                wt.write(sub_table_str+"\n")
            wt.write("\n")


def get_next_page(driver):
    # move to next page
    next_page_selector = "ul.ant-pagination > li[title='下一页'] > a"
    elem_next_page = driver.find_element_by_css_selector(next_page_selector)
    ActionChains(driver).move_to_element(elem_next_page).click().perform()
    print("visting next page")
    time.sleep(3)


def main():
    op = webdriver.ChromeOptions()
    # op.binary_location = "chrome-win\\chrome.exe"
    # op.add_argument("--headless")
    prefs = {"profile.managed_default_content_settings.images": 2}
    op.add_experimental_option("prefs", prefs)
    #driver = webdriver.Chrome("drivers\\chromedriver.exe", options=op)
    driver = webdriver.Chrome(options=op)
    
    login(driver)
    get_database_page(driver)
    make_filtered_search(driver)
    product_count = increase_product_count(driver)
    mutate_dom(driver, product_count=product_count)
    parse_data(driver)
    get_next_page(driver)


if __name__ == "__main__":
    main()
