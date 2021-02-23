# -*- coding: utf-8 -*-
import time
import logging
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


def init_logger():
    # create a logger, create handler with configs, add to logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # creating some handlers
    log_file = "data_crawler.log"
    fh = logging.FileHandler(filename=log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def login(driver, user_name="yixun1", passwd="a212121"):
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


def make_filtered_search(driver, srch_term="", start_date="2018-01-01", end_date="2018-02-01", origin="", dest="", hs_code=""):
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

    # select dest country
    driver.find_element_by_id("DEST_COUNTRY_TC").send_keys(dest)
    time.sleep(1)

    # input hs code
    driver.find_element_by_id("HS_CODE").send_keys(hs_code)
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


def fetch_a_page(driver, page_number=1):
    elem_jumper = driver.find_element_by_css_selector(
        ".ant-pagination-options-quick-jumper input")
    ac = ActionChains(driver)
    ac.move_to_element(elem_jumper).click()
    ac.send_keys(str(page_number) + Keys.ENTER)
    ac.perform()
    # wait for the new page to load and then release
    wait = WebDriverWait(driver, 20)
    active_page_btn_selector = f"ul > li.ant-pagination-item-active[title='{page_number}']"
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, active_page_btn_selector)))


def parse_data(driver):
    html = driver.find_element_by_tag_name(
        "html").get_attribute("innerHTML")
    p = HTMLTableParser()
    p.feed(html)
    # print("parsed_data_invoked")
    with open("data.csv", "a+", encoding="utf-8", newline='') as csvf:
        csv_writer = csv.writer(csvf)
        csv_writer.writerows(p.tables[0])


def init_webdriver(exec_path="", headless_mode=False):
    op = webdriver.ChromeOptions()
    if headless_mode:
        op.add_argument("--headless")
        op.add_argument("--no-sandbox")
    prefs = {"profile.managed_default_content_settings.images": 2}
    op.add_experimental_option("prefs", prefs)
    if exec_path == "":
        driver = webdriver.Chrome(options=op)
    else:
        driver = webdriver.Chrome(exec_path, options=op)

    return driver


def get_arguments():
    import argparse

    args = argparse.ArgumentParser(
        description="Simple selenium script for gathering trade data")
    args.add_argument("--start_date", "-sd", default="2018-01-01",
                      help="Specify the start date for the filter in format yyyy-mm-dd")
    args.add_argument("--end_date", "-ed", default="2018-02-01",
                      help="Specify the end date for the filter in format yyyy-mm-dd")
    args.add_argument("--keywords", "-k", default="",
                      help="Specify any keywords, note use double quotes if more than one e.g., \"bolt steel\"")
    args.add_argument("--origin_country", "-c", default="",
                      help="Specify the origin country for the filter")
    args.add_argument("--dest_country", "-d", default="",
                      help="Specify the destination country for the filter")
    args.add_argument("--hs_code", "-hs", default="",
                      help="Specify the HS code of the product for the filter")
    args.add_argument("--start_page", "-sp", default=1, type=int,
                      help="Specify the start page for scraping")
    args.add_argument("--end_page", "-ep", default=5, type=int,
                      help="Specify the end page for scraping")
    arguments = args.parse_args()

    assert arguments.start_page <= arguments.end_page, "Start page must be smaller than end page"

    return arguments


def main():

    # driver = init_webdriver("drivers\\chromedriver.exe")
    driver = init_webdriver(headless_mode=True)
    logger = init_logger()
    # parameters to set
    args = get_arguments()
    keywords = args.keywords
    s_date = args.start_date
    e_date = args.end_date
    origin_count = args.origin_country
    dest_count = args.dest_country
    hs_code = args.hs_code

    # wait for javascript loadings, time can be changed
    wait = WebDriverWait(driver, 20)

    login(driver)
    logger.debug("Login is succesful!")
    # filter the search results
    make_filtered_search(driver, srch_term=keywords, start_date=s_date,
                         end_date=e_date, origin=origin_count, dest=dest_count, hs_code=hs_code)
    wait.until(EC.invisibility_of_element_located(
        (By.CSS_SELECTOR, ".ant-spin-blur")))
    # first page appears after the search btn submit, so wait for it
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "ul > li.ant-pagination-item-active[title='1']")))
    # increase product count from 20 to 40
    increase_product_count(driver)

    S_PAGE = args.start_page
    E_PAGE = args.end_page
    counter = S_PAGE
    TRY_LIMIT = 5
    try_counter = 0

    logger.debug(
        f"params:  -sd {s_date} -ed {e_date} -sp {S_PAGE} -ep {E_PAGE} -c {origin_count} -k {keywords} -d {dest_count} -hs {hs_code}")

    while counter <= E_PAGE:
        try:
            fetch_a_page(driver, counter)
            # getting data rom current page
            parse_data(driver)
            print(f"page {counter}/{E_PAGE} is done, moving to next")
            logger.debug(f"page {counter}/{E_PAGE} is done, moving to next")
            counter += 1
            # resets the try couter after every successful run
            try_counter = 0
        except exceptions.TimeoutException:
            if try_counter < TRY_LIMIT:
                logger.warning(
                    f"Timeout exception caught, resetting the page and retrying at page {counter}")
                # slow down and resets the whole setup
                time.sleep(5)
                driver.get("http://dt.data1688.com/overseas/global")
                wait.until(EC.invisibility_of_element_located(
                    (By.CSS_SELECTOR, ".ant-spin-blur")))
                make_filtered_search(driver, srch_term=keywords, start_date=s_date,
                                     end_date=e_date, origin=origin_count, dest=dest_count, hs_code=hs_code)
                # first page appears after the search btn submit, so wait for it
                wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "ul > li.ant-pagination-item-active[title='1']")))
                # increase product count from 20 to 40
                increase_product_count(driver)
                try_counter += 1
            else:
                logger.error(
                    "Max retries reached (reloaded page 5 times), no response from website, exiting")
                break
        except Exception as _:
            logger.error("Someother exception ocurred", exc_info=True)
            break

    print("crawled all pages, now quitting")
    logger.debug("crawled all pages, now quitting")
    driver.quit()


if __name__ == "__main__":
    # python data_crawler.py -sp 3 -ep 5 -sd 2020-03-02 -ed 2021-01-01 -c china -k "bolt"
    main()
