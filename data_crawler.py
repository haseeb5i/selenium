# -*- coding: utf-8 -*-
import time
import csv
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions

from html_table_parser import HTMLTableParser


def login(driver, user_name="", passwd=""):
    TRY_AGAIN = True
    try_counter = 0
    tries_allowed = 2
    while TRY_AGAIN:
        try:
            # get the login page
            driver.get("http://dt.data1688.com/login")
            time.sleep(1)

            # let's login first
            driver.find_element_by_id("userName").send_keys(user_name)
            driver.find_element_by_id(
                "password").send_keys(passwd + Keys.ENTER)

            # wait for it to log us in
            wait = WebDriverWait(driver, 15)
            srch_selector = "span > span.ant-input-search > input"
            srch_loc = (By.CSS_SELECTOR, srch_selector)
            wait.until(EC.presence_of_element_located(srch_loc))

            # once the search box appears, move the search page
            driver.get("http://dt.data1688.com/overseas/global")
            time.sleep(2)
            break

        except exceptions.NoSuchElementException:
            print("failed loading login page, refreshing")
            try_counter += 1
            driver.refresh()
            time.sleep(3)
            if try_counter > tries_allowed:
                print("failed getting the login page, max tries reached")
                sys.exit(1)

        except exceptions.TimeoutException:
            # sometimes page loading takes too much time
            print("failed loading login page due to timeout, refreshing")
            try_counter += 1
            driver.refresh()
            time.sleep(3)
            if try_counter > tries_allowed:
                print("failed getting the login page, max tries reached")
                sys.exit(1)


def make_filtered_search(driver, srch_term="", start_date="2021-01-01", end_date="2021-01-01", origin="china"):
    wait = WebDriverWait(driver, 15)
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

    # set the date range
    ac = ActionChains(driver)
    ac.move_to_element(elem_cal_start_date).click()
    ac.send_keys(Keys.ARROW_UP + 4*Keys.DELETE + start_date[:4])
    ac.send_keys(Keys.ARROW_RIGHT + 2*Keys.DELETE + start_date[5:7])
    ac.send_keys(Keys.ARROW_RIGHT + 2*Keys.DELETE + start_date[8:])
    ac.send_keys(Keys.TAB)
    ac.send_keys(Keys.ARROW_UP + 4*Keys.DELETE + end_date[:4])
    ac.send_keys(Keys.ARROW_RIGHT + 2*Keys.DELETE + end_date[5:7])
    ac.send_keys(Keys.ARROW_RIGHT + 2*Keys.DELETE + end_date[8:])
    ac.click().perform()
    time.sleep(2)

    # make search, if srch term is not empty
    if not srch_term == "":
        driver.find_element_by_id("GOODS_DESC").send_keys(srch_term)
        time.sleep(1)

    # select origin country
    driver.find_element_by_id("ORIGIN_COUNTRY_TC").send_keys(origin)
    time.sleep(1)

    # submit the filter/srch query
    driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(1)


def increase_product_count(driver):
    # increase the item count per page
    wait = WebDriverWait(driver, 15)
    elem_increase_count = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[title='20 条/页']")))
    # although we don't need to wait above
    ac = ActionChains(driver)
    ac.move_to_element(elem_increase_count).click()
    ac.send_keys(2*Keys.ARROW_DOWN + Keys.ENTER)
    ac.perform()
    # after performing the action, wait untill product count changes from 20 to 40
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[title='40 条/页']")))


def parse_data(driver):
    html = driver.find_element_by_tag_name(
        "html").get_attribute("innerHTML")
    p = HTMLTableParser()
    p.feed(html)
    # print("parsed_data_invoked")
    with open("data.csv", "a+", encoding="utf-8", newline='') as csvf:
        csv_writer = csv.writer(csvf)
        csv_writer.writerows(p.tables[0])


def main():
    # get the chromedriver with proper options
    op = webdriver.ChromeOptions()
    # uncomment this to run in headless mode (without any dislplay)
    # op.add_argument("--headless")
    prefs = {"profile.managed_default_content_settings.images": 2}
    op.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("drivers\\chromedriver.exe", options=op)

    # parameters to set
    # NOTE: provide start and end data in this format, yyyy-mm-dd
    keywords = "steel"
    s_date = "2018-01-01"
    e_date = "2018-01-01"
    origin_count = "china"

    login(driver)
    make_filtered_search(driver, srch_term=keywords, start_date=s_date,
                         end_date=e_date, origin=origin_count)

    # wait for javascript loadings, time can be changed
    wait = WebDriverWait(driver, 20)

    # first page appears after the search btn submit, so wait for it
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "ul > li.ant-pagination-item-active[title='1']")))
    increase_product_count(driver)

    PAGES = 5
    for i in range(1, PAGES + 1):
        # moving to a specific page nubmer and waiting for it to load
        driver.find_element_by_link_text(f"{i}").click()
        active_page_btn_selector = f"ul > li.ant-pagination-item-active[title='{i}']"
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, active_page_btn_selector)))
        # getting data from current page
        parse_data(driver)
        print(f"page {i}/{PAGES} is done, moving to next")

    print("crawled all pages, now quitting")
    driver.quit()


if __name__ == "__main__":
    main()
